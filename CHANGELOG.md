# CHANGELOG HAOS_CC Plugin

## v0.2.0 — 2026-05-28 (HAOS-PADG Absorption)

### Adicionadas (TIER S — sem reservas)
- `token-optimizer` — analisa JSONL transcripts, identifica top-10 turns mais caros, otimiza cache. **Ganho financeiro direto**.
- `obsidian-bases` — cria/edita `.base` Obsidian (views, filters, formulas, table/cards/list/map)
- `obsidian-cli` — interacao com vault via CLI oficial
- `obsidian-markdown` — cria/edita `.md` Obsidian-flavored (wikilinks, callouts, embeds, properties)
- `obsidian-organizer` — reformata notas, gera Dashboard, cria novos temas
- `incorporador` — meta-skill que analisa sistemas externos, identifica gaps, produz plano de merge
- `json-canvas` — cria/edita `.canvas` Obsidian (mind maps, flowcharts)

### Adicionadas (TIER A — adaptacao leve)
- `vibe-designer` — diretor de criacao Lovable autonomo (Landing/Institucional/E-commerce)
- `lovable-publisher` — recebe prompt, publica no Lovable via MCP, retorna URL
- `page-analyst` — Playwright + visao para analise visual de sites (referencia / auditoria)
- `feedback-interpreter` — traduz feedback vago de cliente em prompt Lovable estruturado

### Substituida
- `skill-creator` — versao pro do HAOS-PADG (pesquisa web obrigatoria, ZIP de entrega).
  Backup do antigo em `skills/_skill-creator-old-backup/`.

### Pendentes adaptacao PT-BR (22 skills em `skills-pending-translation/`)
copywriting, copy-editing, competitor-profiling, customer-research, ai-seo,
community-marketing, ad-creative, ads, cro, ab-testing, marketing-ideas,
design-taste-frontend, product-marketing, churn-prevention, emails, launch,
lead-magnets, cold-email, marketing-psychology, content-strategy, analytics, schema.

Cada uma precisa: PT-BR + trocar Stripe/Klaviyo/Apollo/TCPA por Yampi/Mautic/Evolution/LGPD
+ adaptar 4 marcas (HAU/SIM/Edson/Editora). `product-marketing` precisa 4 versoes (uma por marca).

### Integracao obsidian-logger (HAOS-PADG)
- Instalado em `/root/.claude/obsidian-logger/` no Hetzner
- 4 arquivos: hook.py (patched cross-platform), worker.py 708 linhas, sync-pending.py, themes.json customizado (20 temas HAOS)
- Hook SessionEnd adicionado no `~/.claude/settings.json` (multi-hook safe)
- Modo degraded: roda sem ANTHROPIC_API_KEY (sem resumo Haiku, mantem captura de requests/files/skills/commands)

### Skills DESCARTADAS (duplicacao, paths Paulo, irrelevante)
chefe (duplica nosso main), brand-guidelines (Anthropic), paywalls (SaaS US),
sms (regulacao US), nomear-agente (Pixel Agents), session-logger.py (legacy),
hooks/session_*.py (duplicam nossos), ofiscal (conflita com claude-hud, postergado).

### Total skills ativas: 30 (era 19 + 7 TIER S + 4 TIER A = 30)
### Skills pendentes: 22

---

## v0.1.0 — 2026-05-24 (Initial release)
Plugin publicado: 29 agents + 45 commands + 19 skills + hooks + manual PDF.
