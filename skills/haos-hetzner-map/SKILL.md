---
name: haos-hetzner-map
description: >-
  Use ANTES de qualquer tarefa no servidor Hetzner (<SERVER_IP> / ubuntu-32gb-hel1-1).
  Mapa de referencia "leia antes de agir": inventario de containers e portas (host:container),
  runtimes de IA (Claude Code, Codex, Hermes, OpenClaw, Paperclip) e onde ficam as skills de cada,
  rede e exposicao (Traefik vs Cloudflare Tunnel), dominios -> container, bancos de dados,
  paths-chave em /opt e /root, systemd timers, cron, firewall (UFW + iptables owner-match),
  backups e camadas de seguranca/sandbox. Acione quando for fazer deploy, troubleshooting,
  scaling, reconfiguracao, auditoria ou qualquer mexida no Hetzner.
metadata:
  version: "1.0"
  autor: Gian Marco Menegussi Scaglianti
  marca: HAOS
  data_varredura: "2026-06-07 (atualizado 2026-06-07 — disco)"
  fonte: varredura read-only ao vivo via SSH (estado REAL, nao de memoria)
---

# HAOS Hetzner Map (leia antes de qualquer tarefa no servidor)

> Servidor unico de producao da operacao HAU/SIM/Edson/Editora.
> Acesso SSH (curto e individual, conexao instavel):
> `ssh -i ".../_secrets/ssh/<SSH_KEY_FILE>" -o StrictHostKeyChecking=no root@<SERVER_IP> "comando"`
> Chave SSH no MASTER.env. NUNCA expor valores de secrets, so NOMES de variavel e PATHS.

---

## Host

| Item | Valor |
|---|---|
| Hostname | `ubuntu-32gb-hel1-1` |
| IP publico | `<SERVER_IP>` (provedor Hetzner, Helsinki / hel1) |
| OS | Ubuntu 24.04.4 LTS |
| Kernel | 6.8.0-106-generic |
| CPU | 8 vCPU |
| RAM | 30 GiB (≈7 GiB usados, ~23 GiB buff/cache disponiveis) |
| Swap | 4 GiB |
| Disco | `/dev/sda1` 226 GB — **78% usado, ~50 GB livres** (atencao: monitorar) |
| Uptime tipico | dezenas de dias (estavel) |

---

## Containers (Docker) — por stack

**40 containers** no total (`docker ps -a`). Apenas as portas 22/80/443 sao publicas; todo o resto e loopback (127.0.0.1) ou rede interna Docker. Networks customizadas: `network_public`, `painel-net`, `painel-net-exec`.

### Stack n8n (automacao)
| Container | Imagem | Porta | Proposito |
|---|---|---|---|
| n8n | n8nio/n8n:latest (v2.10.3) | 5678 (interno) | Orquestrador de workflows. DB = container `postgres`, database `n8n` |
| n8n-worker | n8nio/n8n:latest | 5678 (interno) | Worker de execucao de filas n8n |

### Stack Paperclip + memoria de agentes
| Container | Imagem | Porta | Proposito |
|---|---|---|---|
| paperclip | ghcr.io/paperclipai/paperclip:latest | `127.0.0.1:3100->3100` | Plataforma multi-agente (company SIM, ~33 agentes). Painel via tunnel `agencia.<INTERNAL_DOMAIN_A>` |
| agent-memory-pg | pgvector/pgvector:pg15 | 5432 (interno) | Postgres dedicado do Paperclip + **pgvector** (extensao `vector` confirmada). DB `agent_memory`, user `admin` |

### Stack OpenClaw (host process + monitor)
| Componente | Onde | Porta | Proposito |
|---|---|---|---|
| openclaw (container) | openclaw-haos:2026.5.12 | `127.0.0.1:18789` | Runtime OpenClaw HAOS (WhatsApp/agents). Healthy |
| painel/nginx interno | nginx (host) | `127.0.0.1:18790/18791` | Front do OpenClaw / hetzer panel (via tunnel) |

### Stack Painel HAOS (servidor admin)
| Container | Imagem | Porta | Proposito |
|---|---|---|---|
| painel-app | painel-haos:latest | 3000 | Painel HAOS (Host `painel.<INTERNAL_DOMAIN_A>`) |
| painel-worker | painel-haos-worker:latest | - | Worker do painel |
| painel-postgres | postgres:16-alpine | 5432 | DB do painel (databases: `postgres`, `painel`) |
| painel-redis | redis:7-alpine | 6379 | Cache/fila do painel |
| painel-docker-proxy | tecnativa/docker-socket-proxy | 2375 | Acesso controlado ao docker.sock (read) |
| painel-docker-proxy-exec | tecnativa/docker-socket-proxy | 2375 | Acesso controlado ao docker.sock (exec) |

### Stack Mautic (email marketing)
| Container | Imagem | Porta | Proposito |
|---|---|---|---|
| mautic | mautic/mautic:5-apache | 80 | Mautic (Host `mautic.<INTERNAL_DOMAIN_C>`) |
| mautic-db | mariadb:10.11 | 3306 | DB MariaDB do Mautic |

### Stack Evolution (WhatsApp API)
| Container | Imagem | Porta | Proposito |
|---|---|---|---|
| evolution | evoapicloud/evolution-api:latest | 8080 | Evolution API (Host `evo.<INTERNAL_DOMAIN_C>`) |
| evolution-manager | evoapicloud/evolution-manager:latest (v2.3.5) | 80 | UI do Evolution (Host `evo-manager.<INTERNAL_DOMAIN_C>`) |

### Stack Typebot + MinIO
| Container | Imagem | Porta | Proposito |
|---|---|---|---|
| typebot-builder | baptistearno/typebot-builder (v3.15.2) | 3000 | Builder (Host `typebot.<INTERNAL_DOMAIN_C>`) |
| typebot-viewer | baptistearno/typebot-viewer (v3.15.2) | 3000 | Viewer/chat (Host `chat.<INTERNAL_DOMAIN_C>`) |
| minio | minio/minio:latest | 9000 | Object storage S3 do Typebot (Host `storage.<INTERNAL_DOMAIN_C>`) |

### Stack HAU Tasks (gerenciador de tarefas interno)
| Container | Imagem | Porta | Proposito |
|---|---|---|---|
| hau-tasks-web | nginx:1.27-alpine | 80 | Front (Host `tarefas.<INTERNAL_DOMAIN_A>`) |
| hau-tasks-api | node:22-alpine | 8787 | API (Host + PathPrefix /api, /webhooks, /health; e `api.tarefas...`) |
| hau-tasks-notifier | node:22-alpine | - | Notificacoes/alertas |

### Stack SIM / dashboards / sites
| Container | Imagem | Porta | Proposito |
|---|---|---|---|
| sim-site | sim-site | 3000 | Site SIM staging (Host `staging-osim.<INTERNAL_DOMAIN_C>`) |
| sim-dash | sim-dash | 3000 | Dashboard SIM (Host `<SERVICE_HOST_B>`) |
| sim-dash-etl (x2: hopeful_kowalevski, elastic_greider) | sim-dash-etl | - | Jobs ETL do sim-dash (rodam via cron, ver secao ETL) |
| live-display | live-display-g369 | 3000 | Display ao vivo (Host `display.<INTERNAL_DOMAIN_C>`) |

### Stack Edsonburger / Powermind / landing pages
| Container | Imagem | Porta | Proposito |
|---|---|---|---|
| powermind-web | nginx:alpine | 80 | Powermind front (Host `powermind.<INTERNAL_DOMAIN_C>`) |
| powermind-api | node:20-alpine | 3370 | Powermind API (Host + PathPrefix /api) |
| fundadores-web | nginx:alpine | 80 | Fundadores front (Host `fundadores.<INTERNAL_DOMAIN_C>`) |
| fundadores-api | node:20-alpine | 3369 | API fundadores/protocolo (Host fundadores/protocolo + /api) |
| protocolo-web | nginx:alpine | 80 | Protocolo (Host `protocolo.<INTERNAL_DOMAIN_C>`) |
| policies-edsonburger | nginx:alpine | 80 | Politicas (Host `policies.<INTERNAL_DOMAIN_C>`) |
| flix369 | nginx:alpine | 80 | 369flix (Host `369flix.<INTERNAL_DOMAIN_A>`) |

### Stack RAG-SIM + monitoramento + infra base
| Container | Imagem | Porta | Proposito |
|---|---|---|---|
| rag-sim-api | rag-sim-api | `127.0.0.1:8766->8000` | API do RAG vetorial da marca SIM |
| wa-monitor | hau/wa-monitor:0.1.0 | 8080 | Monitor de templates WhatsApp/Meta (Host `meta.<INTERNAL_DOMAIN_C>`) |
| sandbox-paulo-otel | otel/opentelemetry-collector-contrib:0.110.0 | `127.0.0.1:4317`, `127.0.0.1:9464` | Coletor OTel da sandbox do Paulo (metricas/traces) |
| postgres | postgres:15 | 5432 | Postgres compartilhado (n8n DB `n8n`; user `admin`). Stacks legadas |
| redis | redis:7-alpine | 6379 | Redis compartilhado |
| traefik | traefik:v2.11 | **`0.0.0.0:80`, `0.0.0.0:443`** | Reverse proxy / TLS (Let's Encrypt). UNICO container com portas publicas |

> ETL sim-dash: dois containers `sim-dash-etl` aparecem como instancias de run (disparados por `/opt/sim-dash-etl/run.sh` no cron). Sao jobs, nao servico permanente.

---

## Runtimes de IA (CRITICO)

Cinco runtimes coexistem. **Dois sao CLI no host (NAO containers): Codex e Hermes.**

| Runtime | Tipo | Onde mora | Auth | Skills dir | Obs |
|---|---|---|---|---|---|
| **Claude Code (host)** | CLI host | `/usr/bin/claude` (v2.1.150), config em `/root/.claude` | OAuth Max (`/login` interativo, refresh root-only) | `/root/.claude/skills` (197 itens — superset + oficiais) | Runtime principal do root |
| **Codex** | CLI (via harness OpenClaw) | dados/auth em `/opt/openclaw/codex-data` | ChatGPT Pro (re-login conta Pro) | `/opt/openclaw/codex-data/skills` (65) | NAO ha bin em /usr/local/bin; roda dentro do harness OpenClaw |
| **Hermes** | CLI host (Python venv) | `/usr/local/bin/hermes` + projeto `/usr/local/lib/hermes-agent` (Python 3.11), config `/root/.hermes` | OpenAI SDK 2.24 (ChatGPT Pro) | `/root/.hermes/skills` (100) | v0.14.0 (2026.5.16). **NAO e container.** ~1266 commits atras de update |
| **OpenClaw** | Container | container `openclaw` (`127.0.0.1:18789`) | ver MASTER.env | `/home/node/.claude/skills` (59 no container) | WhatsApp + agents. **Cuidado com restart (ver Regras)** |
| **Paperclip** | Container | container `paperclip` (`127.0.0.1:3100`) | propria (DB `agent_memory`) | `/paperclip/.claude/skills` (1) | Company SIM, ~33 agentes. Codex auth em `/paperclip/.codex` |

### Skills — fonte da verdade e propagacao
- **Repo unico = `HAOS_CC`** (superset HAOS, ~65 skills, formato SKILL.md). `/opt/HAOS_CC` e o clone local que recebe `git pull`.
- Sync para OpenClaw/Codex: `/opt/sync-haos-skills-openclaw.sh` (roda `@reboot` e `0 4 * * *` no cron).
- Para propagar uma skill nova: commit no repo `HAOS_CC` -> `git pull` em `/opt/HAOS_CC` -> rodar o sync. NAO editar skills direto dentro dos containers (sobrescrito pelo sync).
- `/root/.claude/skills` (197) e `/root/.hermes/skills` (100) tem o superset + skills oficiais Anthropic; nao confundir contagem com o repo (65).

---

## Rede / Exposicao

### Portas publicas (0.0.0.0)
| Porta | Servico | Observacao |
|---|---|---|
| 22 | sshd | Acesso SSH (chave ed25519). Protegido por fail2ban (jail sshd) |
| 80 | traefik (docker-proxy) | Redireciona para 443 |
| 443 | traefik (docker-proxy) | TLS Let's Encrypt, entrypoint `websecure` |

Todo o resto escuta em `127.0.0.1` (loopback): paperclip 3100, openclaw 18789, nginx 18790/18791/8765, rag 8766, otel 4317/9464, broker/audit 18795, cloudflared 20241, etc.

### Dois caminhos de entrada
1. **Traefik direto** (porta 443, cert Let's Encrypt, Cloudflare como proxy/CDN na frente): a maioria dos dominios.
2. **Cloudflare Tunnel** (`cloudflared`, tunnel id `caf822cd-...`, config `/etc/cloudflared/config.yml`, service systemd `cloudflared`): 4 hostnames que apontam para loopback.

### Dominios -> como chega -> destino
**Via Traefik (Host rule -> container:porta):**
| Dominio | Container | Porta |
|---|---|---|
| n8n.<INTERNAL_DOMAIN_C> | n8n | 5678 |
| mautic.<INTERNAL_DOMAIN_C> | mautic | 80 |
| evo.<INTERNAL_DOMAIN_C> | evolution | 8080 |
| evo-manager.<INTERNAL_DOMAIN_C> | evolution-manager | 3000 |
| typebot.<INTERNAL_DOMAIN_C> | typebot-builder | 3000 |
| chat.<INTERNAL_DOMAIN_C> | typebot-viewer | 3000 |
| storage.<INTERNAL_DOMAIN_C> | minio | 9000 |
| display.<INTERNAL_DOMAIN_C> | live-display | 3000 |
| meta.<INTERNAL_DOMAIN_C> | wa-monitor | 8080 (com secure headers + HSTS) |
| powermind.<INTERNAL_DOMAIN_C> | powermind-web / -api (/api) | 80 / 3370 |
| fundadores.<INTERNAL_DOMAIN_C> | fundadores-web / -api (/api) | 80 / 3369 |
| protocolo.<INTERNAL_DOMAIN_C> | protocolo-web / fundadores-api (/api) | 80 / 3369 |
| policies.<INTERNAL_DOMAIN_C> | policies-edsonburger | 80 |
| staging-osim.<INTERNAL_DOMAIN_C> | sim-site | 3000 |
| painel.<INTERNAL_DOMAIN_A> | painel-app | 3000 |
| <SERVICE_HOST_B> | sim-dash | 3000 |
| tarefas.<INTERNAL_DOMAIN_A> | hau-tasks-web (+ -api em /api,/webhooks,/health) | 80 / 8787 |
| api.tarefas.<INTERNAL_DOMAIN_A> | hau-tasks-api | 8787 |
| 369flix.<INTERNAL_DOMAIN_A> | flix369 | 80 |

**Via Cloudflare Tunnel (cloudflared):**
| Hostname | Service interno |
|---|---|
| hetzer.<INTERNAL_DOMAIN_A> | http://localhost:18791 (nginx painel) |
| <SERVICE_HOST_D> | http://localhost:18789 (OpenClaw, noTLSVerify) |
| agencia.<INTERNAL_DOMAIN_A> | http://localhost:3100 (Paperclip) |
| paulo-audit.<INTERNAL_DOMAIN_A> | http://127.0.0.1:18795 (dashboard de auditoria do Paulo) |

> ~23 dominios mapeados (≈19 via Traefik + 4 via Tunnel).

---

## Bancos de dados

| Container | Engine | Porta (loopback/interna) | Usado por |
|---|---|---|---|
| postgres | postgres:15 (user `admin`) | 5432 | n8n (DB `n8n`); stacks legadas compartilhadas |
| agent-memory-pg | pgvector/pgvector:pg15 (user `admin`, DB `agent_memory`) | 5432 | **Paperclip + pgvector** (memoria vetorial de agentes) |
| painel-postgres | postgres:16-alpine | 5432 | Painel HAOS (databases `postgres`, `painel`) |
| painel-redis | redis:7-alpine | 6379 | Painel HAOS (cache/fila) |
| mautic-db | mariadb:10.11 | 3306 | Mautic |
| redis | redis:7-alpine | 6379 | Redis compartilhado (n8n/legado) |

> Nenhum banco exposto publicamente. Antes de qualquer restart/migracao de banco: **backup verificado primeiro** (ver Regras).

---

## Paths-chave

### /opt (servicos e infra)
| Path | Proposito |
|---|---|
| `/opt/secrets/.env` | Espelho do MASTER.env, **perm 600 root** (158 variaveis). Fonte de secrets do server |
| `/opt/HAOS_CC` | Clone do repo HAOS_CC (skills+agentes, fonte da verdade via git pull) |
| `/opt/claude-broker` | Broker de secrets: `broker.py` + shims `_broker-client` e calls (clint/evolution/mautic/openai/openrouter/yampi) — agentes chamam APIs sem ver as chaves |
| `/opt/claude-paulo` | Runtime/config do funcionario Paulo (sandbox auditado) |
| `/opt/paulo-audit-dashboard` | Dashboard de auditoria do Paulo (servido em :18795 / paulo-audit.osimtransforma) |
| `/opt/sandbox-paulo-otel` | Stack OTel da sandbox do Paulo (collector) |
| `/opt/n8n` | docker-compose do n8n |
| `/opt/backups` | Backups (subpastas: weekly, monthly, hau-tasks, sim-dash, openclaw-pre-reinstall...) |
| `/opt/haos-paperclip`, `/opt/haos-paperclip-ops`, `/opt/HAOS-Paperclip-Memory` | Operacao/ops/memoria do Paperclip (inclui snapshot semanal) |
| `/opt/sim-dash`, `/opt/sim-dash-etl` | Dashboard SIM + jobs ETL (run.sh, run-clint-tags.sh, run-pedidos.sh) |
| `/opt/sync-haos-skills-openclaw.sh` | Script de sync de skills (repo -> OpenClaw/Codex) |
| `/opt/scripts` | Scripts de manutencao: backup.sh, n8n-backup.sh, haos-security-monitor.sh, backups hau-tasks |
| `/opt/traefik` | Config do reverse proxy |
| `/opt/openclaw` | OpenClaw (data, monitor/check_openclaw.sh, selfheal.sh, codex-data, extensions) |
| `/opt/safeline` | SafeLine (WAF — presente no diretorio) |
| `/opt/obsidian-vault-hetzner` | Vault Obsidian espelhado (git pull a cada 15 min) |
| `/opt/openrouter-balance-alert` | Alerta de saldo OpenRouter (check.py diario) |
| `/opt/wa-monitor` | Monitor de templates WhatsApp/Meta |
| `/opt/rag-sim-api` | RAG vetorial da marca SIM |
| `/opt/databases`, `/opt/postgres-mcp` | DBs auxiliares / MCP de Postgres |
| Outros sites/apps | `/opt/369flix`, `/opt/powermind-experience`, `/opt/fundadores-edsonburger`, `/opt/protocolo-edsonburger`, `/opt/policies-edsonburger`, `/opt/live-display-g369`, `/opt/live-inscricoes-display`, `/opt/audience-check`, `/opt/sim-site`, `/opt/typebot`, `/opt/evolution`, `/opt/mautic`, `/opt/painel-haos`, `/opt/haos-server-panel`, `/opt/backup-asterisk` |

### /root e /home
| Path | Proposito |
|---|---|
| `/root/.claude` | Config + skills (197) do Claude Code host (OAuth Max) |
| `/root/.hermes` | Config + skills (100) do Hermes (CLI, NAO container) |
| `/usr/local/lib/hermes-agent` | Codigo do Hermes (Python venv 3.11) |
| `/usr/bin/claude`, `/usr/local/bin/hermes`, `/usr/local/bin/cloudflared` | Binarios |
| `/home/paulo` | Sandbox do funcionario Paulo; skills em `/home/paulo/.claude/skills` (2) |
| `/paperclip` | Volume do Paperclip (`.claude/skills`, `.codex` auth) |

---

## systemd (services / timers)

| Unit | Tipo | Proposito |
|---|---|---|
| cloudflared.service | service (enabled) | Tunnel Cloudflare (4 hostnames) |
| fail2ban.service | service (enabled) | Brute-force protection (jail sshd ativo) |
| claude-paulo-refresh.timer | timer | Refresh do token/login do Paulo (a cada ~30 min) |
| claude-paulo-audit.service | service (enabled) | Auditoria continua da sandbox do Paulo |
| claude-paulo-alerts.service | service (enabled) | Alertas da sandbox do Paulo (WhatsApp via Evolution) |
| paulo-audit-dashboard.service | service (enabled) | Dashboard de auditoria (:18795) |
| paulo-audit-fw.service | service (enabled) | Firewall/owner-match da sandbox do Paulo |
| claude-mem-worker.timer | timer | Worker de memoria (claude-mem) |
| sysstat-collect/summary.timer | timer | Coleta de metricas do sistema |

---

## cron (jobs agendados)

`crontab -l` (root) + `/etc/cron.d`:
| Agenda | Job | Proposito |
|---|---|---|
| `0 3 * * *` | /opt/scripts/backup.sh | Backup geral diario |
| `30 6 * * 0` | /opt/scripts/n8n-backup.sh | Backup semanal do n8n -> Google Drive |
| `* * * * *` | /opt/openclaw/selfheal.sh | Self-heal do OpenClaw (a cada minuto) |
| `*/10 * * * *` | /opt/openclaw/monitor/check_openclaw.sh | Health check do OpenClaw |
| `*/15 * * * *` | git pull obsidian-vault-hetzner | Sync do vault Obsidian |
| `*/30 * * * *` | /opt/sim-dash-etl/run.sh | ETL do dashboard SIM |
| `0 3 * * *` | /opt/sim-dash-etl/run-clint-tags.sh | ETL tags Clint |
| `15 */2 * * *` | /opt/sim-dash-etl/run-pedidos.sh | ETL pedidos |
| `*/30 * * * *` | wa-monitor check_template_status.py | Status de templates WhatsApp/Meta |
| `0 5 * * 0` | snapshot-agent-memory.sh | Snapshot semanal da memoria do Paperclip |
| `@reboot` + `0 4 * * *` | /opt/sync-haos-skills-openclaw.sh | Sync de skills |
| `0 4 / 15 4 / 30 4 1` | backups hau-tasks (db, pgdump, purge notif) | Backup e limpeza HAU Tasks |
| `0 12 * * *` | openrouter-balance-alert/check.py | Alerta de saldo OpenRouter |
| `0 3 1,6,11,...` | supabase-bigdata-keepalive.sh | Keepalive Supabase Big Data |
| `*/5 * * * *` (cron.d) | haos-security-monitor.sh | Monitor de seguranca (flock) |

---

## Firewall

### UFW (status: active)
| Porta | Acao |
|---|---|
| 22/tcp | ALLOW |
| 80/tcp | ALLOW |
| 443/tcp | ALLOW |
| 8765/tcp | DENY |
| 18790/tcp | DENY |

### iptables owner-match (sandbox do Paulo)
Regras REJECT em OUTPUT para as portas do Paulo, permitindo apenas UID 0 (root):
- `tcp dpt:9464  ! owner UID 0  -> REJECT` (metricas OTel do Paulo)
- `tcp dpt:18795 ! owner UID 0  -> REJECT` (dashboard de auditoria do Paulo)

### fail2ban
Ativo, jail `sshd` (protege a porta 22).

---

## Backups

- `/opt/backups`: subpastas `weekly`, `monthly`, `hau-tasks`, `sim-dash`, mais snapshots pre-reinstalacao (ex.: `openclaw-pre-reinstall-...`).
- Backup geral: `/opt/scripts/backup.sh` diario (03h).
- Backup n8n: `/opt/scripts/n8n-backup.sh` semanal (dom 06h30) -> Google Drive (pasta N8N). Encryption key no MASTER.env.
- Backup HAU Tasks: db + pgdump diarios; purge de notificacoes mensal.
- Snapshot memoria Paperclip: semanal (dom 05h).
- Politica documentada (memoria): manter ~15 backups diarios. DR ja testado (runbook existente).

### Estado pos-saneamento de disco (2026-06-07)
- **Retencao LOCAL do backup geral reduzida 30 -> 3 dias.** `/opt/scripts/backup.sh`
  linha 16 `RETENTION_DAYS=3` (poda automatica na linha 139 via
  `find -mtime +RETENTION_DAYS -delete`, cron diario 3h). `/opt/backups/daily` ~18G.
  **Backup completo continua indo DIARIO pro Google Drive (copia segura off-site,
  inalterado).** Causa-raiz: retencao 30 enchia ~86G.
- **Cap de log de container (`/etc/docker/daemon.json`):** `log-driver json-file` +
  `max-size 50m` / `max-file 3`. Vale para containers RECRIADOS apos reload do
  daemon. **Reload PENDENTE de proposito** (aplica naturalmente nos proximos
  deploys; NAO reiniciar o daemon Docker com ~39 containers a toa). Causa-raiz:
  Docker NAO rotaciona log por padrao (evolution chegou a 1,2G; wa-monitor 114M —
  truncados sem restart via `truncate -s 0 $(docker inspect --format '{{.LogPath}}' <ct>)`).
- **OpenClaw `/opt/openclaw/data/agents` podado 11G -> 1,7G (~9,3G).** Apagados SO
  `logs_2.sqlite*` (logs de execucao Codex, congelados desde 22/mai) + sessoes/
  sessions-archive >3 dias. **PRESERVADOS (29/29 cada):** `memories/`,
  `auth-state.json`, `auth-profiles.json`, `config.toml`, `models.json`, `SOUL.md`,
  `state_*.sqlite`. Sem restart do OpenClaw. Salvaguardas:
  `/root/openclaw-agents-config-backup-20260607.tar.gz` +
  `/root/openclaw-prune-manifest-20260607.log`.
- Resultado: disco **78% -> 42%** (90G/226G, ~77 GB liberados).

---

## Seguranca / Sandbox

- **Broker de secrets** (`/opt/claude-broker`): agentes acessam APIs (clint, evolution, mautic, openai, openrouter, yampi) via shims `*-call` SEM ver as chaves. `broker.py` central. `/opt/secrets/.env` perm 600.
- **Sandbox do Paulo** (funcionario auditado): runtime em `/opt/claude-paulo` + `/home/paulo`, managed-settings/guard, auditoria continua (`claude-paulo-audit`), alertas (`claude-paulo-alerts`) via Evolution para WhatsApp **<OWNER_PHONE>** (NAO <OWNER_PHONE>). Telemetria OTel isolada (`sandbox-paulo-otel`), firewall owner-match nas portas 9464/18795. Dashboard de auditoria em `paulo-audit.<INTERNAL_DOMAIN_A>`.
- **WAF**: SafeLine presente em `/opt/safeline`. Cloudflare na frente dos dominios proxados.
- **fail2ban** + **UFW** + iptables owner-match como camadas de rede.

---

## Regras operacionais (LEIA antes de agir)

1. **NAO reiniciar OpenClaw em sequencia.** Restart derruba a sessao WhatsApp. Self-heal (`selfheal.sh`, a cada minuto) e o monitor cuidam de recuperacao automatica. Se precisar mexer, um restart por vez e validar conexao WhatsApp antes de qualquer outro.
2. **Backup verificado ANTES de mexer** em banco, volume ou stack critica. Backup nao testado nao conta.
3. **Hermes e Codex sao CLI, NAO containers.** Hermes = host (`/usr/local/bin/hermes` + venv). Codex roda dentro do harness OpenClaw (`/opt/openclaw/codex-data`), auth ChatGPT Pro. Nao procure container para eles.
4. **Paperclip: cap `maxConcurrentRuns=1` nos agentes Claude** (anti 529 / rate-limit do Max compartilhado). Nao subir esse cap sem briefing.
5. **Tunnel e remote-managed/local config** (`/etc/cloudflared/config.yml`, tunnel `caf822cd-...`). Alterar ingress = editar o config + restart `cloudflared.service`. NAO mexer no DNS dos 4 hostnames sem coordenar.
6. **Skills: fonte unica = repo HAOS_CC.** Editar no repo -> `git pull` em `/opt/HAOS_CC` -> rodar `/opt/sync-haos-skills-openclaw.sh`. Editar dentro de container e perda garantida (sobrescrito pelo sync 04h/reboot).
7. **Secrets: so via broker ou `/opt/secrets/.env` (600).** Nunca colocar chave em codigo/compose/repo. Nunca printar valores; so NOMES.
8. **Disco em 42%** (apos saneamento 07/06; era 78%). Antes de operacoes pesadas (pull de imagem grande, dump), checar `df -h`. Pruning de imagens com cuidado (nao remover imagens em uso por containers parados que serao reusados).
8a. **Backups locais: retencao 3 dias** (`/opt/scripts/backup.sh` linha 16 `RETENTION_DAYS=3`, poda na linha 139, cron 3h). Drive diario e a copia segura off-site. NAO subir a retencao local sem briefing (foi o que enchia ~86G).
8b. **Log de container limitado a 50m x 3** via `/etc/docker/daemon.json`. **Reload do daemon esta PENDENTE de proposito** (aplica naturalmente em deploys/recriacoes). **NAO reiniciar o daemon Docker com ~39 containers a toa.** Se um log voltar a crescer, truncar pontual: `truncate -s 0 $(docker inspect --format '{{.LogPath}}' <container>)` (sem restart).
8c. **Poda de OpenClaw e SEGURA so se restrita a `logs_2.sqlite*` e sessoes/sessions-archive antigas (>3 dias).** NUNCA apagar `memories/`, `auth-state.json`, `auth-profiles.json`, `config.toml`, `models.json`, `SOUL.md`, `state_*.sqlite` em `/opt/openclaw/data/agents`. Backup + manifesto antes (ver secao Backups). Sem restart do OpenClaw.
9. **Sandbox do Paulo e auditada.** Nao desabilitar guard/audit/alerts nem as regras iptables owner-match sem aprovacao explicita + chuck-norris na call.
10. **SSH instavel: comandos curtos e individuais.** Evitar pipelines longos numa unica sessao.
11. **Login Max e root-only** (refresh). Usar `/login` interativo, nao `setup-token`.
12. **Producao e sagrada.** Mudanca em prod = rollback planejado + janela (fora de horario comercial por padrao) + registro. Staging antes de prod sempre que houver.

---

## Specialist Routing

| Demanda | Agente |
|---|---|
| Infra, deploy, containers, Docker, Traefik, tunnel, DNS, backup, scaling, troubleshooting de servidor | **@devops** (dono da infra) |
| Apps, APIs, scripts, codigo dos servicos (n8n flows custom, painel, RAG, hau-tasks, sites) | **@dev-backend** (ou @dev-frontend para UI) |
| Auditoria, seguranca, vulnerabilidades, WAF/SafeLine, revisao do broker e da sandbox do Paulo, hardening | **@chuck-norris** (sempre em par com devops em mudanca de WAF/firewall) |

> Mudanca em WAF/CDN/firewall = revisao obrigatoria com @chuck-norris. Acesso SSH novo = aprovacao @chuck-norris.
