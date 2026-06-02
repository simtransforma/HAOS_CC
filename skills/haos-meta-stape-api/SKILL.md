---
name: haos-meta-stape-api
description: Use when working on HAOS/SIM/Edson Burger Meta Graph or Marketing API access, Meta Business Manager system-user tokens, ad account read-only audits, Pixel/CAPI diagnostics, Stape API access, Stape sGTM containers, server-side tracking, MASTER.env variables, or Meta/Stape credential validation without exposing secrets.
metadata:
  version: 1.0
  autor: Gian Marco Menegussi Scaglianti
  marca: HAOS
---

# HAOS Meta/Stape API

Use this skill for Meta Graph/Marketing API and Stape API work in the
HAOS/SIM/Edson Burger environment.

## Guardrails

- Never print, quote, mask, commit, or store secrets in memory: access tokens,
  app secret, Stape API key, container API key, cookies, passwords, headers.
- Use `MASTER.env` only as a source for secrets. The path is **runtime-aware**:
  - **Local Windows (Xtreme3)**:
    `C:\Users\gians\OneDrive\Documentos\Projetos\Agencia HAU - Soluções Digitais\HAO IA Operation System\_secrets\MASTER.env`
  - **Hetzner runtimes** (Codex, Hermes, Claude Code Hetzner, Paperclip,
    OpenClaw): `/opt/secrets/.env`
  - **Paulo sandbox**: does NOT read MASTER directly — secrets are served by the
    secrets broker (the skill receives access to the variables it needs without
    ever seeing the raw key values). Treat broker-provided values with the same
    no-print guardrail.
- Keep Meta/Stape operations read-only unless Gian gives explicit OK for the
  exact external change.
- Do not create, pause, activate, edit or delete campaigns, ad sets, ads,
  budgets, pixels, audiences, domains, containers, power-ups, schedules,
  billing, users, API keys or webhooks during access/audit work.
- Do not call Stape `GET /api/v2/users/api-key` unless you sanitize the response
  because it can expose API-key material.

## Specialist Routing

Reference these agents — they are the ones who consume this skill:

- `dev-backend`: OAuth/token handling, Graph/Stape API probes, script fixes.
- `tracking-engineer`: pixels, CAPI, Stape sGTM container, domains and event
  quality diagnostics.
- `traffic-master` and `media-buyer`: ad account/campaign/insights read-only
  interpretation after access is confirmed.
- `compliance-officer`: policy, LGPD, token/permission risk and change gates.

## Known Environment

- Meta Graph version validated: `v21.0`.
- Meta token variables observed in `MASTER.env`: `META_TOKEN_BM01`,
  `META_TOKEN_BM02`, `META_TOKEN_BM08`, `META_TOKEN_BM09`, `META_TOKEN_BM10`,
  `META_TOKEN_BM11`, `META_TOKEN_BM12`, `META_TOKEN_BM13`.
- Meta app variables observed: `META_APP_ID`, `META_APP_SECRET`.
- Stape token variable observed: `STAPE_API_KEY`.
- Stape auth header: `X-AUTH-TOKEN`.
- Stape base URL validated: `https://api.app.stape.io`.
- Stape container validated:
  - name: `Edson Burger`
  - identifier: `efznyhks`
  - status: `Running`
  - zone: `SA East (Brazil)`
  - domain: `api.<INTERNAL_DOMAIN_C>`, status `Ready`

## Scripts

> **Ambiente local Windows (Xtreme3) apenas — NÃO disponível nos runtimes Linux
> (Hetzner: Codex / Hermes / Claude Code / Paperclip / OpenClaw / Paulo
> sandbox).** Os scripts abaixo e o bootstrap PowerShell existem somente na
> máquina local do Gian. Não há equivalente nesses runtimes; nesses ambientes
> use chamadas Graph/Stape diretas (read-only) lendo os nomes de variável de
> `/opt/secrets/.env` (ou broker, na sandbox do Paulo).

On local Windows (Xtreme3), load HAOS bootstrap from
`C:\Projetos\Codex_HAOS-Xtreme3` before acting, then run from that directory:

```powershell
.\scripts\audit-meta-stape-master-env.ps1
.\scripts\probe-meta-readonly-access.ps1
.\scripts\probe-meta-readonly-access.ps1 -MaxAdAccounts 20
.\scripts\probe-stape-readonly-access.ps1
```

These scripts never print secrets. They return names of variables used, status
flags, account/container names, counts and sanitized errors only.

## Workflow

1. Confirm HAOS bootstrap and `claude-mem` health if available (local Windows
   only; on Linux runtimes skip the bootstrap step and go straight to probes).
2. Run `audit-meta-stape-master-env.ps1` (local Windows) or read variable
   presence from the runtime MASTER (`/opt/secrets/.env`) / broker; expect
   presence only, never values.
3. Probe Meta read-only access; validate:
   - token debug valid;
   - `ads_read` for read-only Ads/Insights;
   - `business_management` for Business/asset discovery;
   - ad accounts returned;
   - `campaigns`, `adspixels` and `insights` GETs succeed.
4. Probe Stape read-only access; validate:
   - `GET /api/v2/containers`;
   - `GET /api/v2/containers/{identifier}`;
   - `GET /api/v2/containers/{identifier}/domains`;
   - `GET /api/v2/containers/{identifier}/analytics/info`.
5. Summarize by credential variable name and operational result only.
6. If a token is valid but no ad account appears, treat as asset assignment or
   permission scope issue, not as credential failure.

## Current Findings To Remember

- `META_TOKEN_BM01`: token valid, has `ads_read`, `ads_management`,
  `business_management`; six ad accounts were readable; campaigns, pixels and
  insights GETs succeeded.
- `META_TOKEN_BM02`: token valid, has `ads_read`, `ads_management`,
  `business_management`; one ad account was readable; campaigns, pixels and
  insights GETs succeeded.
- `META_TOKEN_BM08`: token valid but missing `ads_read`; no ad accounts were
  returned.
- `META_TOKEN_BM09` to `META_TOKEN_BM13`: tokens valid and include `ads_read`,
  but no ad accounts were returned by the tested GET routes. Likely missing
  asset/ad-account assignment or no accessible account on those BMs.
- Stape access is OK for the Edson Burger sGTM container and domain.

## Troubleshooting

- If `debug_token` fails, verify `META_APP_ID` and `META_APP_SECRET` exist in
  `MASTER.env` and match the app that issued the token.
- If token is valid but account count is zero, inspect Business Manager asset
  assignment in Meta UI before changing code.
- If Stape returns 401/403, check that the API key is account-level or has
  access to the expected workspace/container.
- If Stape returns a wrapper object with `body.body`, update the parser instead
  of printing raw response.
- If any secret appears in tool output, do not repeat it. Stop, summarize the
  incident, and rotate only if Gian asks.
