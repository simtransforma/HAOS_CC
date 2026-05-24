<div align="center">

<!-- TODO: substituir por logo HAU real em docs/assets/hau-logo.png -->
# 🧠 HAOS

### HAU Autonomous Operations Squad — Framework Multi-Agente para Claude Code

**Squad autônoma de 29 agentes IA orquestrados em 8 departamentos, com 44 slash commands, memória persistente, backup automático e governança humana em pontos críticos.**

*by [**HAU Soluções Digitais**](https://<INTERNAL_DOMAIN_B>) 🇧🇷*

[![Plugin Claude Code](https://img.shields.io/badge/claude--code-plugin-blue?logo=anthropic)](https://claude.com/claude-code)
[![Version](https://img.shields.io/badge/version-0.1.0-blue)](CHANGELOG.md)
[![Agents](https://img.shields.io/badge/agentes-29-green)](#-agentes-29)
[![Commands](https://img.shields.io/badge/commands-44-orange)](#-comandos-44)
[![Skills](https://img.shields.io/badge/skills-19-purple)](#-skills-19)
[![Departments](https://img.shields.io/badge/departamentos-8-yellow)](#-departamentos-8)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

</div>

---

## ✨ O que é o HAOS?

**HAOS (HAU Autonomous Operations Squad)** é um framework completo para [Claude Code](https://claude.com/claude-code) que transforma seu terminal numa **squad inteira operada por IA** — 29 agentes especializados, 8 departamentos, pipelines de governança, memória persistente entre sessões e gates humanos antes de ações irreversíveis.

**Não são chatbots.** Os agentes executam — geram código, copy, análises, planos, campanhas. Param e pedem aprovação quando vão publicar, gastar ou enviar algo.

### Por que isso importa?

- **Especialização real** — cada agente tem identidade, framework e regras "nunca". Não é "um modelo genérico fazendo tudo"
- **Governança incorporada** — gates humanos em pontos críticos (publicar, gastar, deploy)
- **Memória eterna** — hooks SessionStart/Stop/PostCompact preservam contexto entre sessões
- **Plug-and-play** — instala como plugin Claude Code oficial, namespace `/haos:*`
- **Open-source (MIT)** — você pode forkar, adaptar, contribuir

---

## 🚀 Quick Start

### Pré-requisitos
- [Claude Code](https://claude.com/claude-code) instalado
- Python 3.10+ (Windows: instale via `winget install Python.Python.3.12`)
- Sistema operacional: **Windows 10+**, macOS, Linux (testado primariamente em Windows)

### Instalação (3 comandos)

```bash
# 1. Adicione o marketplace community (se ainda não tiver)
/plugin marketplace add anthropics/claude-plugins-community

# 2. Instale o HAOS
/plugin install haos@claude-community

# 3. Configure (entrevista de 2 min)
/haos:setup
```

Pronto. O `/haos:setup` faz 4 perguntas-chave, gera seu `CLAUDE.md` personalizado e seu perfil persistente. Depois disso:

```bash
/haos:menu        # menu principal
/haos:agentes     # lista os 29 agentes
/haos:departamentos   # lista os 8 departamentos
```

Ou simplesmente descreva sua demanda em linguagem natural — o agente `main` classifica e roteia automaticamente.

---

## 📚 Documentação detalhada

| Doc | Quando ler |
|---|---|
| **[docs/INSTALLATION.md](docs/INSTALLATION.md)** | Setup passo-a-passo Windows/Mac/Linux + verificação |
| **[docs/USER_GUIDE.md](docs/USER_GUIDE.md)** | Manual completo: 5 modos de operação, fluxos, melhores práticas |
| **[docs/AGENTS_GUIDE.md](docs/AGENTS_GUIDE.md)** | Deep-dive dos 29 agentes (quando usar cada, brief que pedem, output) |
| **[docs/RITO_V2.md](docs/RITO_V2.md)** | Pipeline de 13 fases pra marketing/lançamento (gates + checkpoints) |
| **[docs/EXAMPLES.md](docs/EXAMPLES.md)** | 6 cenários práticos com input + comando + resposta esperada |
| **[docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)** | Problemas comuns e soluções |
| **[docs/00-Index.md](docs/00-Index.md)** | Índice geral da pasta docs |

---

## 🏗️ Arquitetura

```
┌───────────────────────────────────────────────────────────────┐
│                       HAOS v0.1.0                              │
│                HAU Autonomous Operations Squad                  │
├───────────────────────────────────────────────────────────────┤
│                                                                 │
│  ENTRADA                                                        │
│  ├─ /haos:setup          → wizard de configuração inicial      │
│  ├─ /haos:menu           → menu interativo                     │
│  ├─ /haos:rito [briefing]→ Rito v2 (pipeline de 13 fases)      │
│  ├─ /haos:{agente}       → delegação direta (29 opções)        │
│  ├─ /haos:{depto}        → broadcast pro departamento (8)      │
│  └─ Texto livre          → Concierge (classificação automática)│
│                                                                 │
│  DEPARTAMENTOS                                                  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │@conselho │ │@criativo │ │ @trafego │ │  @dados  │          │
│  │ 4 agents │ │ 5 agents │ │ 3 agents │ │ 3 agents │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│  ┌──────────┐ ┌────────────┐ ┌─────────────────┐ ┌─────────┐  │
│  │ @funnel  │ │  @produto  │ │ @orquestracao   │ │@seguranca│ │
│  │ 4 agents │ │  4 agents  │ │   4 agents      │ │ 2 agents│  │
│  └──────────┘ └────────────┘ └─────────────────┘ └─────────┘  │
│                                                                 │
│  HOOKS (memória persistente)                                    │
│  ├─ SessionStart → carrega MEMORY.md + sessões recentes        │
│  ├─ Stop         → salva sessão                                │
│  └─ PostCompact  → reinjecta contexto após compactação         │
│                                                                 │
└───────────────────────────────────────────────────────────────┘
```

---

## 🏢 Departamentos (8)

| Departamento | Entry-point | Agentes | Foco |
|---|---|:-:|---|
| `/haos:conselho` | estrategista-chefe | 4 | Estratégia, decisões críticas, conflitos |
| `/haos:criativo` | copy-specialist | 5 | Copy, design, vídeo, conteúdo, social |
| `/haos:trafego` | traffic-master | 3 | Mídia paga, tracking |
| `/haos:dados` | data-analyst | 3 | Análise, BI, pesquisa |
| `/haos:funnel` | funnel-architect | 4 | Funis, automação, CRM, email |
| `/haos:produto` | product-manager | 4 | PM, UX, dev frontend/backend |
| `/haos:orquestracao` | qa-reviewer | 4 | QA, PM, compliance, devops |
| `/haos:seguranca` | chuck-norris | 2 | Security, concierge externo |

---

## 🤖 Agentes (29)

Cada agente tem identidade, framework de fases, princípios "norte", regras "nunca" e formato de retorno estruturado (CONCLUÍDO / BLOQUEADO / REVISÃO).

<details>
<summary><b>@conselho (4)</b></summary>

- **main** — orquestrador principal (classifica, roteia, consolida)
- **estrategista-chefe** — estratégia macro, posicionamento de longo prazo
- **diretor-criativo** — direção criativa, poder de veto, assina visual
- **cmo** — Chief Marketing Officer (ROI, funis, decisões comerciais)
</details>

<details>
<summary><b>@criativo (5)</b></summary>

- **copy-specialist** — copywriting persuasivo, gatilhos mentais
- **content-strategist** — estratégia de conteúdo, calendário editorial
- **designer** — design visual, identidade, layouts
- **videomaker** — roteiro, storyboard, produção de vídeo
- **sm-social** — social media management
</details>

<details>
<summary><b>@trafego (3)</b></summary>

- **traffic-master** — estratégia de tráfego pago, audiences
- **media-buyer** — operação tática, ajustes diários
- **tracking-engineer** — pixels, eventos, CAPI, GTM
</details>

<details>
<summary><b>@dados (3)</b></summary>

- **data-analyst** — análise quantitativa, queries, dashboards
- **bi-engineer** — pipeline de dados, ETL, BI
- **pesquisador** — pesquisa de mercado, concorrência, validação
</details>

<details>
<summary><b>@funnel (4)</b></summary>

- **funnel-architect** — arquitetura de funis ponta a ponta
- **automation-engineer** — automações, integrações
- **crm-specialist** — operação de CRM, segmentação
- **email-marketer** — sequências, broadcasts, deliverability
</details>

<details>
<summary><b>@produto (4)</b></summary>

- **product-manager** — roadmap, priorização, métricas
- **ux-researcher** — pesquisa UX, WCAG, journey mapping
- **dev-frontend** — React/Next/Vue, performance, acessibilidade
- **dev-backend** — APIs, banco, autenticação, integrações
</details>

<details>
<summary><b>@orquestracao (4)</b></summary>

- **qa-reviewer** — QA, testes, validação pré-deploy
- **project-manager** — WBS, cronograma, tracking, riscos
- **compliance-officer** — compliance regulatório, políticas
- **devops** — infra, deploy, CI/CD, monitoring
</details>

<details>
<summary><b>@seguranca (2)</b></summary>

- **chuck-norris** — security, audit, threat modeling
- **concierge** — entry-point para visitantes/externos
</details>

---

## ⚡ Comandos (44)

### Operação (7)
| Comando | Função |
|---|---|
| `/haos:setup` | Wizard de configuração inicial (4 etapas) |
| `/haos:menu` | Menu interativo principal |
| `/haos:base` | Visão geral do sistema |
| `/haos:agentes` | Lista os 29 agentes |
| `/haos:departamentos` | Lista os 8 departamentos |
| `/haos:rito` | Pipeline Rito v2 (13 fases — só marketing/lançamento) |
| `/haos:mb` | Mega-Brain (gestão de conhecimento) |
| `/haos:emergencia` | Modo emergência (convoca @conselho) |

### Departamentos (8)
`/haos:conselho` · `/haos:criativo` · `/haos:trafego` · `/haos:dados` · `/haos:funnel` · `/haos:produto` · `/haos:orquestracao` · `/haos:seguranca`

### Agentes (29)
Todos os 29 agentes disponíveis como `/haos:{nome}` — ex: `/haos:cmo`, `/haos:dev-backend`, `/haos:copy-specialist`, `/haos:chuck-norris`.

---

## 📚 Skills (19)

Skills carregadas sob demanda quando relevantes ao contexto:

| Categoria | Skills |
|---|---|
| **Design & UX** | `design-principles`, `mobile-responsiveness` |
| **Desenvolvimento** | `software-engineer`, `software-architecture`, `fullstack-dev` |
| **Marketing** | `marketing-expert`, `seo-optimizer` |
| **Conteúdo** | `landing-page-prd-architect`, `prd-brainstorm`, `youtube-content-generator`, `hero-visual-prompt-generator`, `sprint-context-generator` |
| **Pesquisa & Engenharia de Prompt** | `last30days-skill`, `lisa-prompt-engineering`, `ralph-prompt-builder` |
| **Meta (skills sobre skills)** | `skill-creator`, `skill-auditor-v2`, `long-running-agent` |
| **Pentest** | `ffuf-skill` |

---

## 🎯 Rito v2 — Pipeline de 13 Fases

Quando o projeto é **marketing/lançamento** com risco/escopo grande, use o Rito v2 — pipeline serializado com gate bloqueante entre cada fase:

1. Intake & Validação · 2. Pesquisa & Diagnóstico · 3. Estratégia & Posicionamento · 4. Planejamento Tático · 5. Copywriting · 6. Design · 7. Funil & Automação · 8. Tráfego (configurar, NÃO ativar) · 9. Tracking · 10. QA & Compliance · 11. **Deploy & Ativação (⚠️ gasta dinheiro — pede OK)** · 12. Monitoramento · 13. Debrief

**Não use Rito v2 pra software/infra** — vá direto pros agentes técnicos.

```bash
/haos:rito "lançamento do produto X em 30 dias, foco em conversão de leads existentes"
```

---

## 🧠 Memória persistente (hooks automáticos)

3 hooks Python que mantêm seu contexto eterno entre sessões:

| Hook | Quando dispara | O que faz |
|---|---|---|
| `SessionStart` | Início de cada sessão | Carrega `MEMORY.md` + sessões recentes + Rito ativo + bootstrap |
| `Stop` | Fim de cada resposta | Salva registro da sessão em `memory/sessions/` |
| `PostCompact` | Após compactação do contexto | Reinjecta `MEMORY.md` + Rito + pendências |

Memória vive em `~/.claude/projects/{seu-projeto}/memory/` — descoberta dinamicamente pelo `cwd` (não há paths hardcoded).

---

## 📁 Estrutura do plugin

```
HAOS_CC/
├── .claude-plugin/plugin.json    # manifesto Claude Code
├── commands/                      # 44 slash commands /haos:*
├── agents/                        # 29 subagents nativos
├── hooks/
│   ├── hooks.json                 # declara SessionStart, Stop, PostCompact
│   ├── session_start.py
│   ├── session_end.py
│   └── post_compact.py
├── skills/                        # 19 skills (cada uma em sua subpasta)
├── .github/                       # ISSUE templates, PR template, workflows
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE                        # MIT
└── .gitignore                     # strict — sem secrets, .env
```

---

## 🛠️ Configuração avançada

### Reconfigurar
A qualquer momento, rode `/haos:setup` de novo — ele detecta config existente e pergunta se sobrescreve.

### Editar manualmente
Após o setup, edite livremente:
- `{seu-projeto}/CLAUDE.md` — instruções específicas do projeto
- `~/.claude/projects/{encoded}/memory/bootstrap.md` — seu perfil persistente
- `~/.claude/projects/{encoded}/memory/MEMORY.md` — índice de memórias do projeto

### Adicionar novos agentes
Crie um arquivo em `~/.claude/agents/{nome}.md` seguindo o formato dos agents do HAOS (frontmatter `description` + `tools` + corpo com identidade/framework). Claude Code carrega automaticamente.

---

## 🤝 Contribuindo

PRs bem-vindos! Veja [CONTRIBUTING.md](CONTRIBUTING.md) pra setup local, padrões de código, e como propor novos agentes/skills/commands.

**Reportou bug? Tem ideia?** Abra uma [issue](https://github.com/simtransforma/HAOS_CC/issues).

**Security:** se achou vulnerabilidade, veja [SECURITY.md](SECURITY.md) pra reporte responsável.

---

## 🗺️ Roadmap

- [x] **v0.1.0** — Release inicial (44 commands, 29 agents, 19 skills, 3 hooks)
- [ ] **v0.2.0** — Logo HAU oficial + screenshots + vídeo demo
- [ ] **v0.3.0** — Setup wizard em modo TUI (interactive prompts além de AskUserQuestion)
- [ ] **v0.4.0** — Integração MCP para Bitwarden/secrets vault
- [ ] **v0.5.0** — Skills marketplace customizado HAU
- [ ] **v1.0.0** — Produção: testes E2E em 5+ projetos diversos, performance baseline

Veja [CHANGELOG.md](CHANGELOG.md) pra histórico de versões.

---

## 📜 Licença

[MIT](LICENSE) © 2026 [HAU Soluções Digitais](https://<INTERNAL_DOMAIN_B>)

---

## 🙏 Créditos

- **Criado por** [Gian Marco Menegussi Scaglianti](https://github.com/simtransforma) / [HAU Soluções Digitais](https://<INTERNAL_DOMAIN_B>) 🇧🇷
- **Inspiração arquitetural**: [claude-mem](https://github.com/thedotmack/claude-mem) (pattern de plugin Claude Code)
- **Skills de terceiros incluídas**: `skill-auditor-v2` (M. Abidi / AgxntSix), `skill-creator` (Anthropic), `sprint-context-generator` (Script7), `ffuf-skill` (community)
- **Stack base**: [Claude Code](https://claude.com/claude-code) (Anthropic)

---

<div align="center">

**Construído com 🤖 por agentes, para agentes.**

[Documentação](#-quick-start) · [Comandos](#-comandos-44) · [Issues](https://github.com/simtransforma/HAOS_CC/issues) · [Contribuindo](CONTRIBUTING.md)

</div>
