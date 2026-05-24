"""
HAOS Hook: SessionStart
Injeta memória persistente do projeto + sessões recentes + estado de Rito ativo
como contexto adicional no início de cada sessão Claude Code.

Funciona em qualquer projeto: descobre o memory dir dinamicamente a partir do
cwd da sessão (sem paths hardcoded).
"""
import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path


def encode_project_dir(cwd: str) -> str:
    """Replica o esquema de encoding do Claude Code para nomear pastas de projeto."""
    s = cwd.replace(":", "-").replace("\\", "-").replace("/", "-").replace(" ", "-")
    s = re.sub(r"[^\x00-\x7F]", "-", s)
    return s


def find_memory_dir(cwd: str) -> Path:
    """Resolve o memory dir do projeto baseado no cwd. Cria se não existir."""
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

    parts = []
    parts.append("=== HAOS — Memória do Projeto (SessionStart) ===")
    parts.append(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    # 1. MEMORY.md (índice de memórias do projeto)
    idx = memory_dir / "MEMORY.md"
    if idx.exists():
        parts.append("\n--- MEMORY INDEX ---")
        parts.append(idx.read_text(encoding="utf-8")[:2000])

    # 2. Sessões recentes (últimos 3 dias, máx 5)
    sessions_dir = memory_dir / "sessions"
    if sessions_dir.exists():
        cutoff = datetime.now() - timedelta(days=3)
        recent = []
        for f in sorted(sessions_dir.glob("*.md"), reverse=True):
            try:
                file_date = datetime.strptime(f.stem[:10], "%Y-%m-%d")
                if file_date >= cutoff:
                    recent.append(f)
            except (ValueError, IndexError):
                continue
        if recent:
            parts.append("\n--- SESSÕES RECENTES ---")
            for sf in recent[:5]:
                parts.append(f"\n[{sf.stem}]")
                parts.append(sf.read_text(encoding="utf-8")[:800])

    # 3. Rito v2 ativo (se houver)
    rito = memory_dir / "rito_state.json"
    if rito.exists():
        try:
            state = json.loads(rito.read_text(encoding="utf-8"))
            if state.get("status") == "active":
                parts.append("\n--- RITO V2 ATIVO ---")
                parts.append(f"Fase atual: {state.get('current_phase', '?')}")
                parts.append(f"Briefing: {str(state.get('briefing', 'N/A'))[:400]}")
        except Exception:
            pass

    # 4. Bootstrap opcional (perfil/preferências do usuário, se foi configurado via /haos:setup)
    bootstrap = memory_dir / "bootstrap.md"
    if bootstrap.exists():
        content = bootstrap.read_text(encoding="utf-8")
        if content.startswith("---"):
            split = content.split("---", 2)
            if len(split) >= 3:
                content = split[2].strip()
        parts.append("\n--- BOOTSTRAP (Perfil + Contexto do Projeto) ---")
        parts.append(content[:3000])

    parts.append("\n=== FIM ===")

    full = "\n".join(parts)
    if len(full) > 9000:
        full = full[:9000] + "\n... [truncado]"

    out = {
        "continue": True,
        "suppressOutput": False,
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": full,
        },
    }
    sys.stdout.buffer.write(json.dumps(out, ensure_ascii=False).encode("utf-8"))
    sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
