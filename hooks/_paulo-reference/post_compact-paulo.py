"""
HAOS Master Hook: PostCompact
Re-injeta contexto crítico após o Claude Code compactar o histórico.
Estrutura baseada no padrão session_memory_compaction do anthropics/claude-cookbooks.
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
    parts.append(f"=== HAOS Master — Re-injeção pós-compact {datetime.now().strftime('%Y-%m-%d %H:%M')} ===")

    if memory_dir:
        # MEMORY INDEX — índice de memórias persistentes
        idx = memory_dir / "MEMORY.md"
        if idx.exists():
            parts.append("\n## Memory Index")
            parts.append(idx.read_text(encoding="utf-8")[:1500])

        # RITO V2 — estado ativo (se houver)
        rito = memory_dir / "rito_state.json"
        if rito.exists():
            try:
                state = json.loads(rito.read_text(encoding="utf-8"))
                if state.get("status") == "active":
                    parts.append("\n## Active Work (Rito V2)")
                    parts.append(f"Fase atual: {state.get('current_phase', '?')} / 13")
                    parts.append(f"Briefing: {str(state.get('briefing', 'N/A'))[:300]}")
                    if state.get("gates_passed"):
                        parts.append(f"Gates aprovados: {state['gates_passed']}")
                    if state.get("pending_action"):
                        parts.append(f"Próxima ação: {state['pending_action']}")
            except Exception:
                pass

        # PENDÊNCIAS — tarefas em aberto
        pending = memory_dir / "pending_tasks.md"
        if pending.exists():
            parts.append("\n## Pending Tasks")
            parts.append(pending.read_text(encoding="utf-8")[:600])

        # CORREÇÕES DO USUÁRIO — preferências aprendidas (preservar verbatim)
        corrections = memory_dir / "user_corrections.md"
        if corrections.exists():
            parts.append("\n## User Corrections (preserve verbatim)")
            parts.append(corrections.read_text(encoding="utf-8")[:400])

        # KEY REFERENCES — IDs, paths, valores críticos
        key_refs = memory_dir / "key_references.md"
        if key_refs.exists():
            parts.append("\n## Key References")
            parts.append(key_refs.read_text(encoding="utf-8")[:400])

    parts.append("\n=== FIM ===")
    full = "\n".join(parts)
    if len(full) > 5000:
        full = full[:5000] + "\n... [truncado]"

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
