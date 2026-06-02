# CHANGELOG HAOS_CC Plugin

## v0.5.0 — 2026-06-02 (Meta/Stape API skill)

### Adicionada (1 skill — haos-meta-stape-api)
+haos-meta-stape-api skill (Meta Graph/Marketing + Stape sGTM, read-only audit).
Skill operacional para acesso Meta Graph/Marketing API, system-user tokens do
Business Manager, auditoria read-only de ad accounts, diagnóstico Pixel/CAPI,
acesso Stape API e containers sGTM, sem expor segredos. Origem: máquina local do
Gian (Xtreme3), adaptada para portabilidade entre os runtimes HAOS. Total de
skills: 58 → **59** (após `haos-google-ads-gtm-api`, que entrou no mesmo dia).

- `haos-meta-stape-api` — Meta Graph `v21.0`, variáveis de token por BM
  (`META_TOKEN_BM01..BM13`, só NOMES), `META_APP_ID`/`META_APP_SECRET`,
  Stape `STAPE_API_KEY` + header `X-AUTH-TOKEN`, base `https://api.app.stape.io`,
  container Edson Burger (`efznyhks`). Specialist Routing: `dev-backend`,
  `tracking-engineer`, `traffic-master`, `media-buyer`, `compliance-officer`.

### Portabilidade (adaptação para runtimes Linux)
- Caminho do `MASTER.env` agora runtime-aware: Windows local (Xtreme3) vs
  Hetzner (`/opt/secrets/.env`) vs Paulo sandbox (broker de secrets, sem ler
  MASTER direto).
- Bootstrap `C:\Projetos\Codex_HAOS-Xtreme3` e seção Scripts `.ps1` marcados
  explicitamente como "ambiente local Windows (Xtreme3) apenas — não disponível
  nos runtimes Linux". Nenhum script Linux equivalente inventado.
- Guardrails (read-only, nunca expor segredo), findings e known-environment
  preservados intactos.

### Distribuição (8 destinos / runtimes HAOS)
Local (repo canônico) · /opt/HAOS_CC (canônica, via git pull) · Codex
`/opt/openclaw/codex-data/skills/` · Hermes `/root/.hermes/skills/` · OpenClaw
(via `sync-haos-skills-openclaw.sh`) · Claude Code Hetzner `/root/.claude/skills/`
· Paperclip `/paperclip/.claude/skills/` · Paulo sandbox
`/home/paulo/.claude/skills/`. Sem colisão de nomes (skill nova).

## v0.4.0 — 2026-05-31 (TikTok skills)

### Adicionadas (5 skills TikTok — Shop / Ads / Creative / BI / Tracking)
Conhecimento operacional TikTok 2026 com foco Brasil + EUA. Origem: company-skills
do runtime Paperclip (Hetzner), adaptadas ao padrão HAOS_CC (frontmatter `metadata`
com version/autor/marca; wikilinks Obsidian `[[...]]` convertidos para links relativos
`references/sources.md` e refs cruzadas em **bold**, compatíveis com Claude Code).
Cada skill traz `SKILL.md` + `references/sources.md`. Total de skills: 52 → **57**.

- `tiktok-shop-fundamentals` — seller setup (US/UK/BR/MX), fulfillment (FBT/FBM/Affiliate), take-rate real, catalog, affiliate, LIVE Shopping, Shop Ads (GMV Max), Open API, compliance.
- `tiktok-ads-fundamentals` — Ads Manager 2026, hierarquia Campaign/AdGroup/Ad, objetivos, bidding (Max Delivery/Cost Cap/VBO), targeting, Marketing API, SKAN 4.0, Spark Ads, política BR.
- `tiktok-creative-playbook` — anatomia 3s/hook/body/CTA, hooks PT-BR, frameworks (AIDA/PAS/BAB), UGC/creators BR, testing matrix 3-2-2, kill rules, compliance CONAR+ANVISA.
- `tiktok-bi-metrics` — KPIs e fórmulas (CPM/CPC/ROAS/MER/Hook Rate/GMV/AOV/LTV), Marketing API Reporting, Shop Open API, ETL/schemas star, SQL, MTA/MMM.
- `tiktok-tracking-setup` — Pixel + Events API CAPI, dedupe via event_id, EMQ 8+, ttclid/_ttp, server-side (Stape/GTM Server), partner integrations, LGPD/ANPD/consent.

### Distribuição (5 runtimes HAOS)
Mesmo SKILL.md replicado nos 5 runtimes (formato idêntico entre Claude Code / Codex /
Hermes — verificado byte-a-byte). OpenClaw recebe via `sync-haos-skills-openclaw.sh`
(tar para o container, sem restart). Sem colisão de nomes em nenhum destino.

## v0.3.0 — 2026-05-28 (TIER B PT-BR — conclusão da absorção HAOS-PADG)

### Adicionadas (TIER B — 22 skills marketing adaptadas PT-BR + marca HAOS)
Skills traduzidas pra PT-BR com stack/marca HAOS (Stripe→Yampi, Klaviyo→Mautic+Evolution,
Apollo→manual BR, TCPA→LGPD, SMS→WhatsApp; 4 marcas HAU/EdsonBurger/SIM/Editora; autor Gian;
GTM-K5DPXJTV padrão). Total de skills: 30 → **52**.

- `product-marketing` (fundação de contexto de marca) · `copywriting` · `copy-editing` · `cro`
- `ab-testing` · `analytics` · `schema` · `ai-seo` · `ads` · `ad-creative` · `emails`
- `cold-email` · `churn-prevention` · `community-marketing` · `competitor-profiling`
- `customer-research` · `content-strategy` · `marketing-ideas` · `marketing-psychology`
- `lead-magnets` · `launch` · `design-taste-frontend` (corpo de código mantido EN, language-agnostic)

### Limpeza
- `_skill-creator-old-backup` movido de `skills/` para `.archive/` (não era pra carregar como skill).

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
