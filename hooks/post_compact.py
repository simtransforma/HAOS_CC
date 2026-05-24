"""
HAOS Hook: PostCompact
Re-injecta contexto crítico após o Claude Code compactar o histórico.
Recarrega MEMORY.md + Rito ativo (se houver).
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path


def encode_project_dir(cwd: str) -> str:
    s = cwd.replace(":", "-").replace("\\", "-").replace("/", "-").replace(" ", "-")
    s = re.sub(r"[^\x00-\x7F]", "-", s)
    return s


def find_memory_dir(cwd: str) -> Path | None:
    """Retorna memory dir se existir (não cria — só leitura para reinjeção)."""
    base = Path.home() / ".claude" / "projects"
    memory = base / encode_project_dir(cwd) / "memory"
    return memory if memory.exists() else None


def main():
    try:
        stdin_data = sys.stdin.read()
        hook_input = json.loads(stdin_data) if stdin_data.strip() else {}
    except Exception:
        hook_input = {}

    cwd = hook_input.get("cwd") or str(Path.cwd())
    memory_dir = find_memory_dir(cwd)

    parts = []
    parts.append("=== HAOS — Re-injeção pós-compact ===")
    parts.append(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    if memory_dir:
        idx = memory_dir / "MEMORY.md"
        if idx.exists():
            parts.append("\n--- MEMORY INDEX ---")
            parts.append(idx.read_text(encoding="utf-8")[:1500])

        rito = memory_dir / "rito_state.json"
        if rito.exists():
            try:
                state = json.loads(rito.read_text(encoding="utf-8"))
                if state.get("status") == "active":
                    parts.append("\n--- RITO V2 ATIVO ---")
                    parts.append(f"Fase: {state.get('current_phase', '?')}")
                    parts.append(f"Briefing: {str(state.get('briefing', 'N/A'))[:300]}")
            except Exception:
                pass

        pending = memory_dir / "pending_tasks.md"
        if pending.exists():
            parts.append("\n--- PENDÊNCIAS ---")
            parts.append(pending.read_text(encoding="utf-8")[:800])

    parts.append("\n=== FIM ===")
    full = "\n".join(parts)
    if len(full) > 6000:
        full = full[:6000] + "\n... [truncado]"

    out = {
        "continue": True,
        "suppressOutput": False,
        "hookSpecificOutput": {
            "hookEventName": "PostCompact",
            "additionalContext": full,
        },
    }
    sys.stdout.buffer.write(json.dumps(out, ensure_ascii=False).encode("utf-8"))
    sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
