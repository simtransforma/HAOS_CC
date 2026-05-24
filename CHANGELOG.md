# Changelog

Todas as mudanças notáveis deste projeto serão documentadas aqui.
Formato: [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/). Versionamento: [SemVer](https://semver.org/lang/pt-BR/).

## [0.1.0] — 2026-05-24

### Adicionado
- `plugin.json` (manifesto Claude Code Plugin) e estrutura `.claude-plugin/`
- **44 slash commands** no namespace `/haos:*`:
  - 7 operação (`menu`, `base`, `rito`, `mb`, `emergencia`, `agentes`, `departamentos`, `setup`)
  - 8 departamentos (`conselho`, `criativo`, `trafego`, `dados`, `funnel`, `produto`, `orquestracao`, `seguranca`)
  - 29 agentes individuais (`cmo`, `dev-backend`, `copy-specialist`, etc)
- **29 subagents nativos** em `agents/` — cada um com identidade, framework, princípios, regras "nunca"
- **19 skills** em `skills/` (design, dev, marketing, conteúdo, prompt eng, pentest, meta)
- **3 hooks Python** (`SessionStart`, `Stop`, `PostCompact`) — memória persistente, sem paths hardcoded
- **/haos:setup wizard** — entrevista 4 etapas, gera `CLAUDE.md` + `bootstrap.md` personalizados
- Documentação: README, CHANGELOG, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY
- Templates `.github/` (issue, PR)

### Notas
- Versão inicial pública; ainda não publicada em marketplace.
- Logo HAU oficial vai ser adicionada em v0.2.0.
- Testado primariamente em Windows; Linux/macOS validação em andamento.