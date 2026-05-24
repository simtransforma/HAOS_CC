"""
HAOS Hook: Stop (fim de resposta do Claude)
Salva registro da sessão na memória persistente do projeto.
Funciona em qualquer projeto: descobre memory dir dinamicamente.
"""
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path


def encode_project_dir(cwd: str) -> str:
    s = cwd.replace(":", "-").replace("\\", "-").replace("/", "-").replace(" ", "-")
    s = re.sub(r"[^\x00-\x7F]", "-", s)
    return s


def find_memory_dir(cwd: str) -> Path:
    base = Path.home() / ".claude" / "projects"
    memory = base / encode_project_dir(cwd) / "memory"
    memory.mkdir(parents=True, exist_ok=True)
    return memory


def main():
    try:
        stdin_data = sys.stdin.read()
        hook_input = json.loads(stdin_data) if stdin_data.strip() else {}
    except Exception:
        hook_input = {}

    cwd = hook_input.get("cwd") or str(Path.cwd())
    memory_dir = find_memory_dir(cwd)

    sessions_dir = memory_dir / "sessions"
    sessions_dir.mkdir(exist_ok=True)

    now = datetime.now()
    session_file = sessions_dir / f"{now.strftime('%Y-%m-%d_%H-%M')}.md"

    session_id = hook_input.get("session_id", "unknown")
    transcript_path = hook_input.get("transcript_path", "")

    entry = [
        f"# Sessão {now.strftime('%Y-%m-%d %H:%M')}",
        f"- **Session ID:** {session_id}",
        f"- **Diretório:** {cwd}",
        f"- **Timestamp:** {now.isoformat()}",
    ]

    if transcript_path and os.path.exists(transcript_path):
        entry.append(f"- **Transcript:** {transcript_path}")
        try:
            with open(transcript_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines[-20:]:
                    try:
                        msg = json.loads(line)
                        if msg.get("role") == "assistant" and isinstance(msg.get("content"), str):
                            snippet = msg["content"][:300]
                            entry.append(f"\n## Última resposta (snippet)")
                            entry.append(f"```\n{snippet}\n```")
                            break
                    except Exception:
                        continue
        except Exception:
            pass

    entry.append("")
    session_file.write_text("\n".join(entry), encoding="utf-8")

    # Limpar sessões antigas (manter últimos 30 dias)
    cutoff = datetime.now().timestamp() - (30 * 86400)
    for old in sessions_dir.glob("*.md"):
        try:
            if old.stat().st_mtime < cutoff:
                old.unlink()
        except Exception:
            continue

    sys.stdout.buffer.write(json.dumps({"continue": True, "suppressOutput": True}).encode("utf-8"))
    sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
