---
name: haos-google-ads-gtm-api
description: Use when working on HAOS/SIM/Edson Burger Google Ads API or Google Tag Manager API access, MCC setup, API Center developer token, OAuth scopes, MASTER.env variables, read-only Ads/GTM audits, account suspension diagnostics, or Google Ads/GTM credential validation without exposing secrets.
---

# HAOS Google Ads/GTM API

Use this skill for Google Ads API and GTM API work in the HAOS/SIM/Edson
Burger environment.

## Guardrails

- Load HAOS bootstrap from `C:\Projetos\Codex_HAOS-Xtreme3` before acting.
- Never print, quote, mask, commit, or store secrets in memory: developer token,
  client secret, refresh token, access token, cookies, passwords.
- Use `MASTER.env` only as a source/sink for secrets:
  `C:\Users\gians\OneDrive\Documentos\Projetos\Agencia HAU - Soluções Digitais\HAO IA Operation System\_secrets\MASTER.env`
- Keep Google Ads/GTM operations read-only unless Gian gives explicit OK for
  the exact external change.
- Never use MCC/API access to bypass a Google Ads suspension.
- Do not activate campaigns, budgets, ads, bids, billing, audiences, tags, or
  publishes during access/audit work.

## Known Accounts

- MCC: `552-214-6221` / `5522146221`, `Sociedade Internacional do Mindset - MCC`, auth user `simtranforma@gmail.com`.
- Ads client: `282-397-2901`, `Sociedade Internacional do Mindset`, status observed `ENABLED`.
- Ads client: `640-403-7852`, `SOCIEDADE INTERNACIONAL DO MINDSET`, status observed `SUSPENDED`.
- GTM containers expected:
  - `GTM-T4MGXKFT` - Edson Buger | Server
  - `GTM-N3J6H8QK` - Edson Buger | Server | Backup
  - `GTM-K5DPXJTV` - Edson Burger | Web
  - `GTM-KV2XK8QW` - Yampi mapeamento

## Scripts

Run from `C:\Projetos\Codex_HAOS-Xtreme3`.

```powershell
.\scripts\audit-google-master-env.ps1
.\scripts\probe-google-oauth-scopes.ps1
.\scripts\probe-google-ads-readonly-access.ps1
.\scripts\probe-google-ads-readonly-access.ps1 -ProbeCustomerIds '5522146221,2823972901,6404037852'
.\scripts\probe-gtm-readonly-access.ps1
```

To save a Google Ads developer token without printing it:

```powershell
.\scripts\save-google-ads-api-token-from-clipboard.ps1 -LoginCustomerId '5522146221' -TokenFromClipboard
```

If extracting through a temporary file, delete the temporary file immediately;
the script supports `-TokenFile` and removes that file after reading.

## Workflow

1. Confirm bootstrap and `claude-mem` health if available.
2. Run `audit-google-master-env.ps1`; it must show presence only, never values.
3. Run `probe-google-oauth-scopes.ps1`; require `adwords` and `tagmanager.readonly`.
4. If `GOOGLE_ADS_DEVELOPER_TOKEN` is missing, use Google Ads MCC API Center.
5. API Center fields used successfully:
   - API contact: monitored email such as `gian@<INTERNAL_DOMAIN_B>`
   - Company: `Sociedade Internacional do Mindset`
   - URL: `https://<INTERNAL_DOMAIN_A>`
   - Company type: `Anunciante`
   - Intended use: internal read-only reporting/audit for own Google Ads accounts, no campaign/ad/budget/bid/user/billing mutations.
6. Save token only into `MASTER.env`.
7. Set `GOOGLE_ADS_LOGIN_CUSTOMER_ID` to MCC ID without hyphens: `5522146221`.
8. Run Ads and GTM probes.
9. Record conclusions without secrets.

## Troubleshooting

- If Google Ads UI says API Center is only for manager accounts, select the MCC
  `552-214-6221`.
- If Chrome automation hits `chrome://extensions` policy, stop. Ask Gian to
  pause/allowlist the ad blocker manually for `ads.google.com`.
- If Ads API `listAccessibleCustomers` lists an account but GAQL via MCC returns
  `USER_PERMISSION_DENIED`, try the read-only direct route. This happened with
  `6404037852`; direct access confirmed `SUSPENDED`.
- If a web OAuth client redirects to `tarefas.<INTERNAL_DOMAIN_A>` with
  `state_parse_error`, use the desktop OAuth client and localhost listener
  instead of the web client callback.
- If a token appears in a tool output accidentally, do not repeat it, summarize
  only that a secret was handled and rotate if Gian requests.
