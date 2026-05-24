# Instalação — HAOS_CC

Guia passo-a-passo para Windows (primário), com notas pra macOS/Linux. Tempo estimado: **5-10 minutos**.

---

## Pré-requisitos

| Item | Versão mínima | Como verificar | Como instalar |
|---|---|---|---|
| **Claude Code** | 2.1.x ou superior | `claude --version` | [claude.com/claude-code](https://claude.com/claude-code) |
| **Python 3** | 3.10+ | `py -3 --version` (Windows) ou `python3 --version` | Windows: `winget install Python.Python.3.12` · macOS: `brew install python@3.12` · Linux: `apt install python3` |
| **Git** (opcional, só se for editar) | 2.x | `git --version` | `winget install Git.Git` ou [git-scm.com](https://git-scm.com) |

> **Importante:** o Claude Code precisa estar instalado como **CLI/desktop**. A Console web (console.anthropic.com) NÃO suporta plugins.

---

## Instalação

### Opção A — Via marketplace community (recomendado, quando publicado)

```bash
# 1. Adicione o marketplace community (se ainda não tiver)
claude plugin marketplace add anthropics/claude-plugins-community

# 2. Instale o HAOS
claude plugin install haos@claude-community

# 3. Verifique
claude plugin list
# Deve listar: haos@claude-community  Version: 0.1.0  Status: enabled
```

### Opção B — Via marketplace local (pra testar antes de publicar, ou usar fork)

```bash
# 1. Clone (ou baixe o ZIP) do repo
git clone https://github.com/simtransforma/HAOS_CC.git
cd HAOS_CC

# 2. Adicione como marketplace local (use o caminho absoluto da pasta)
claude plugin marketplace add "C:\caminho\completo\HAOS_CC"

# 3. Instale
claude plugin install haos@hau-solucoes-digitais

# 4. Verifique
claude plugin list
```

### Opção C — Sessão temporária (sem instalar globalmente)

Útil só pra **testar uma vez** sem persistir:

```powershell
# Numa pasta de trabalho qualquer
claude --plugin-dir "C:\caminho\completo\HAOS_CC"
```

O plugin fica ativo só nessa sessão.

---

## Primeira execução — Setup Wizard

Depois de instalar, abra o Claude Code no diretório do seu projeto:

```bash
cd C:\seus-projetos\meu-projeto
claude
```

Aí dentro:

```
/haos:setup
```

O wizard faz **4 perguntas-chave** (~2 min) e gera:
- `CLAUDE.md` no seu projeto (instruções personalizadas)
- `bootstrap.md` em `~/.claude/projects/{encoded}/memory/` (perfil persistente)

Você pode aceitar os defaults com Enter em tudo se quiser começar rápido — sempre dá pra reconfigurar depois.

---

## Verificação

Após o setup, confirme que tudo funciona:

```
/haos:menu
```

Deve aparecer o menu principal com 8 departamentos, operação e agentes.

```
/haos:agentes
```

Deve listar os 29 agentes agrupados.

Se ambos funcionarem, **plugin está operacional**. ✅

---

## Update

Quando uma nova versão sair:

```bash
claude plugin update haos
```

Se você instalou via marketplace local (Opção B), atualize o marketplace primeiro:

```bash
claude plugin marketplace update hau-solucoes-digitais
claude plugin update haos
```

---

## Uninstall

```bash
claude plugin uninstall haos
```

A memória persistente em `~/.claude/projects/{encoded}/memory/` **NÃO** é apagada automaticamente. Pra limpar manualmente:

```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.claude\projects\{encoded-do-seu-projeto}\memory"
```

---

## Notas de plataforma

### Windows
- Use **PowerShell** ou **Windows Terminal** — não `cmd.exe` (problemas com aspas em paths com espaços/acentos)
- O Python launcher `py -3` é preferido sobre `python3` (mais robusto no Windows)
- Paths com acentos (ex: "Soluções") funcionam, mas sempre coloque em **aspas duplas**

### macOS / Linux
- Use `python3` no lugar de `py -3` se preferir; o plugin funciona com ambos
- Path típico: `~/.claude/projects/{encoded}/memory/`
- O encoding de paths funciona igual ao Windows (espaços → `-`, etc)

---

## Verificar saúde da instalação

```bash
# 1. Plugin instalado e enabled?
claude plugin list

# 2. Inventário (commands, agents, skills, hooks)
claude plugin details haos

# 3. Manifesto válido?
claude plugin validate "C:\caminho\HAOS_CC"
```

Se tiver qualquer erro, vá pra [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

---

## Próximos passos

- Manual de uso completo: [USER_GUIDE.md](USER_GUIDE.md)
- Conhecer os 29 agentes: [AGENTS_GUIDE.md](AGENTS_GUIDE.md)
- Pipeline Rito V2 (marketing): [RITO_V2.md](RITO_V2.md)
- Exemplos práticos: [EXAMPLES.md](EXAMPLES.md)
