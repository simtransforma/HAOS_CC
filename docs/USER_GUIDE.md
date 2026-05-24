# HAOS_CC — Manual do Usuário

> **HAOS** = HAU Autonomous Operations Squad. Um framework multi-agente para Claude Code que transforma uma instância "vazia" do Claude em um time operacional de 29 especialistas, com memória persistente, hooks automáticos e fluxos de trabalho prontos para marketing, produto, dados, tráfego e segurança.

---

## 1. Quick orientation

O HAOS não é um chatbot nem um assistente único. É um **sistema operacional de agentes** rodando dentro do Claude Code. Quando você instala o plugin, ganha:

- **29 sub-agentes especialistas** organizados em 8 departamentos (criativo, tráfego, dados, funnel, produto, orquestração, segurança e o conselho estratégico)
- **44 slash commands** (`/haos:*`) que invocam agentes, departamentos ou rituais inteiros
- **19 skills** específicas (copywriting, SEO, PRD, fullstack, segurança etc.) que os agentes ativam quando precisam
- **Hooks de memória persistente** que salvam contexto entre sessões (SessionStart, Stop, PostCompact)
- **Setup wizard** que personaliza o HAOS pra sua identidade, marca, tom e nível de autonomia

Como pensar nele: o agente `main` é o **maestro**. Você fala em linguagem natural ou usa um comando, ele classifica a demanda, roteia para o(s) especialista(s) certo(s), consolida o resultado e te entrega. Você não precisa decorar os 29 agentes — só precisa saber pedir o que quer.

---

## 2. Os 5 modos de operação

O HAOS opera em 5 modos. O modo é determinado pelo **prefixo** da sua mensagem (ou ausência dele).

| Modo | Prefixo | Quando usar |
|---|---|---|
| **CONCIERGE** | nenhum | Padrão — texto livre, deixa o `main` decidir |
| **RITO V2** | `/haos:rito` + briefing | Lançamento/campanha de marketing (13 fases) |
| **DIRETO** | `/haos:{agente}` | Você já sabe qual especialista precisa |
| **BROADCAST** | `/haos:{departamento}` | Quer o entry-point de um time |
| **EMERGÊNCIA** | `/haos:emergencia` | Algo grave — convoca o conselho |

### 2.1. CONCIERGE (padrão)

Sem prefixo. Você descreve a situação, o `main` interpreta intenção, decide se responde direto ou delega.

```
> Tô vendo queda de 30% nas vendas da última semana, não sei se é tráfego ou checkout.
```

O `main` provavelmente vai delegar pra `@cmo` + `@data-analyst` em paralelo e consolidar o diagnóstico.

### 2.2. RITO V2 (`/haos:rito`)

Pipeline serializado de **13 fases com gates bloqueantes**. UMA fase por vez, cada uma exige aprovação antes de avançar. Estado salvo a cada fase (pode pausar com `abortar rito` e voltar com `retomar rito`).

```
/haos:rito Lançamento do curso "SIM Foundations" — público mindset/desenvolvimento pessoal, 
ticket R$1.997, meta 200 vendas em 14 dias, orçamento mídia R$60k, deadline 30/Jun.
```

**Use só pra marketing/lançamento.** Software, infra e tarefas técnicas vão direto pros agentes (veja §6).

### 2.3. DIRETO (`/haos:{agente}`)

Delegação 1:1. Pula o roteamento, vai direto pro especialista.

```
/haos:copy-specialist Reescreve esse headline aplicando os 7 gatilhos do Gustavo Ferreira: 
"Aprenda inglês em 30 dias com nosso método exclusivo"
```

Agentes disponíveis: `main`, `estrategista-chefe`, `diretor-criativo`, `cmo`, `copy-specialist`, `content-strategist`, `designer`, `videomaker`, `sm-social`, `traffic-master`, `media-buyer`, `tracking-engineer`, `data-analyst`, `bi-engineer`, `pesquisador`, `funnel-architect`, `automation-engineer`, `crm-specialist`, `email-marketer`, `product-manager`, `ux-researcher`, `dev-frontend`, `dev-backend`, `qa-reviewer`, `project-manager`, `compliance-officer`, `devops`, `chuck-norris`, `concierge`.

### 2.4. BROADCAST (`/haos:{departamento}`)

Roteia pro **entry-point** do departamento. Útil quando você sabe a área mas não o agente.

| Departamento | Entry-point | Membros |
|---|---|---|
| `/haos:conselho` | estrategista-chefe | main, estrategista-chefe, diretor-criativo, cmo |
| `/haos:criativo` | copy-specialist | copy, content, designer, video, sm-social |
| `/haos:trafego` | traffic-master | traffic-master, media-buyer, tracking-engineer |
| `/haos:dados` | data-analyst | data-analyst, bi-engineer, pesquisador |
| `/haos:funnel` | funnel-architect | funnel, automation, crm, email |
| `/haos:produto` | product-manager | PM, UX, dev-front, dev-back |
| `/haos:orquestracao` | qa-reviewer | qa, PM, compliance, devops |
| `/haos:seguranca` | chuck-norris | chuck-norris, concierge |

```
/haos:dados Preciso entender churn dos últimos 90 dias. Tenho export do Stripe em CSV.
```

### 2.5. EMERGÊNCIA (`/haos:emergencia`)

Convoca o `@conselho`, suspende execução em andamento, documenta o incidente. Use quando: agente bloqueado, conflito grave entre agentes, suspeita de violação de identidade da marca, falha de segurança.

```
/haos:emergencia O dev-backend deployou em produção sem rodar o QA — site fora do ar.
```

---

## 3. Fluxo recomendado pra novo usuário

Logo depois de `/plugin install haos@hau-solucoes-digitais`:

```
1. /haos:setup       → wizard de 4 etapas (identidade, modo, estilo, permissões)
2. /haos:menu        → mostra o índice visual de comandos disponíveis  
3. Escolhe um modo   → CONCIERGE pra explorar, DIRETO pra tarefa específica
4. Executa           → pedido em PT-BR, deixa o HAOS rotear
```

### 3.1. O wizard `/haos:setup` cobre

1. **Identidade** — nome, marca(s), tom de comunicação, idioma (default PT-BR)
2. **Tipo de operação** — solo, agência, in-house, freelance (calibra nível de formalidade)
3. **Estilo** — direto/didático, verbose/conciso, com/sem emojis
4. **Permissões** — quais ações exigem OK explícito (default: publicar, gastar, deletar, deploy)

Tudo salvo em `~/.claude/projects/{encoded}/memory/user_profile.md`. Pode reabrir o wizard a qualquer hora.

### 3.2. `/haos:menu` — seu mapa visual

Lista os 44 comandos agrupados por departamento, com 1 linha de descrição cada. Use quando esquecer o nome de um agente.

---

## 4. Como delegar bem

O HAOS é tão bom quanto seu briefing. Princípios de bom prompt (vale tanto para CONCIERGE quanto DIRETO):

| Elemento | Bom exemplo | Ruim exemplo |
|---|---|---|
| **Objetivo claro** | "Quero 5 variações de headline para anúncio Meta" | "Mexe nesse anúncio aí" |
| **Dados/contexto** | "Público 35-55, mulheres, ticket R$497, dor: emagrecer pós-50" | "Pra mulher" |
| **Formato esperado** | "Markdown, tabela com headline + gancho psicológico" | (nada) |
| **Restrições** | "Máx 40 chars, sem promessa de resultado, em PT-BR" | (nada) |
| **Prazo/escopo** | "Pra publicar amanhã, só headlines (descrições depois)" | (nada) |

### Template universal

```
Objetivo: <o que você quer>
Contexto: <dados, situação, histórico relevante>
Formato: <markdown/CSV/JSON/texto corrido/etc>
Restrições: <limites, tom, compliance, marca>
Prazo: <quando>
```

Você não precisa preencher os 5 sempre — mas quanto mais preencher, menos ping-pong.

---

## 5. Gestão de memória

### 5.1. Onde fica

```
~/.claude/projects/{encoded(cwd)}/memory/
├── MEMORY.md                          ← índice mestre (sempre carregado)
├── user_profile.md                    ← seu perfil do wizard
├── project_*.md                       ← contexto por projeto/cliente
├── feedback_*.md                      ← suas regras e preferências
├── learning_*.md                      ← coisas que o HAOS aprendeu
└── reference_*.md                     ← ponteiros pra docs externas
```

`{encoded(cwd)}` = o caminho do seu projeto com `/`, `\` e `:` convertidos pra `-`. Cada projeto tem sua própria memória — abrir o Claude Code em outra pasta = outro contexto.

### 5.2. Como funciona o backup

O HAOS roda 3 hooks automáticos:

| Hook | Quando dispara | O que faz |
|---|---|---|
| **SessionStart** | Toda sessão nova | Carrega MEMORY.md + arquivos referenciados |
| **Stop** | Você fecha a sessão | Resume a conversa, atualiza/cria arquivos de memória |
| **PostCompact** | Claude comprime o contexto | Re-injeta a memória pra não perder |

Plus: você pode configurar backup externo (Obsidian, GitHub privado, OneDrive) — veja `bootstrap.md`.

### 5.3. Como inspecionar

```bash
# Listar arquivos de memória do projeto atual
ls ~/.claude/projects/$(pwd | sed 's|/|-|g')/memory/

# Ler o índice
cat ~/.claude/projects/.../memory/MEMORY.md
```

Ou simplesmente peça ao HAOS: `"me mostra o que você lembra desse projeto"`.

### 5.4. Como editar

Você pode editar qualquer `.md` direto no editor. O HAOS vai ler na próxima sessão. Use isso pra:

- Corrigir algo que ele entendeu errado
- Adicionar contexto novo que não veio na conversa
- Deletar memórias obsoletas

Ou peça: `"esquece o que você sabe sobre o projeto X"` / `"atualiza sua memória: a meta mudou pra R$500k"`.

---

## 6. Quando NÃO usar Rito V2

**Rito V2 é exclusivo para marketing/lançamento.** As 13 fases (intake → pesquisa → estratégia → planejamento → copy → design → funnel → tráfego → tracking → QA → deploy → otimização → debrief) são otimizadas pra campanhas e produtos comerciais.

### Pra essas tarefas, vá DIRETO no agente técnico

| Demanda | Comando correto |
|---|---|
| Fix de bug em React | `/haos:dev-frontend` |
| Refactor de API Node | `/haos:dev-backend` |
| Setup de CI/CD | `/haos:devops` |
| Code review | `/haos:qa-reviewer` |
| Auditoria de segurança | `/haos:chuck-norris` |
| Schema de banco | `/haos:dev-backend` |
| Performance de query SQL | `/haos:bi-engineer` |
| Análise de log de produção | `/haos:devops` |

Forçar Rito V2 numa tarefa técnica = 13 fases de overhead pra resolver algo que precisava de 1 agente e 5 minutos.

**Regra prática:** se a entrega final é **código, infra ou config**, vai direto. Se é **mensagem para o mercado** (anúncio, página, email, vídeo, post), considere Rito V2.

---

## 7. Gates humanos — o que exige seu OK

Por design, o HAOS executa **ações internas** sem pedir permissão (criar arquivos, rodar análises, escrever drafts, gerar relatórios). Mas para **ações externas irreversíveis**, ele para, mostra o plano e espera você falar "ok".

| Categoria | Exemplos | Por quê |
|---|---|---|
| **Publicar** | Post em redes, email broadcast, anúncio go-live | Marca pública |
| **Gastar** | Ativar campanha paga, comprar domínio, contratar serviço | Dinheiro real |
| **Deletar** | Remover dados, dropar tabela, deletar repo | Irreversível |
| **Deploy** | Push pra prod, mudar DNS, mudar config de produção | Risco de downtime |
| **Enviar mensagem** | Email pra cliente, WhatsApp, DM | Imagem pessoal/marca |
| **Mexer em credencial** | Rotacionar chave, mudar senha, revogar token | Pode quebrar integrações |

Você pode customizar essa lista no wizard (`/haos:setup`) ou direto em `~/.claude/projects/.../memory/user_profile.md` na seção `Permissões`.

### Como o HAOS pede OK

```
[gate humano — ação externa]
Plano: ativar campanha CBO no Meta Ads Manager
  - Conta: 564700162489469
  - Budget diário: R$2.000
  - Início: hoje 14h
  - Stop loss configurado: CPL > R$80 em 48h
Responda "ok ativar" pra prosseguir, ou ajuste os parâmetros.
```

Você sempre tem a opção de **dizer não** ou pedir ajuste antes do "ok".

---

## 8. Como customizar

O HAOS é um plugin, mas tudo que ele faz é **legível e editável**. Os 4 pontos de extensão principais:

### 8.1. CLAUDE.md do projeto

Arquivo no root do projeto (`./CLAUDE.md`). Sobrescreve qualquer comportamento default. Use pra:

- Regras específicas do projeto (ex: "todo SQL nesse repo é Postgres 15, não MySQL")
- Glossário interno (ex: "quando eu falar 'A1', é a conta do cliente X")
- Vetos absolutos (ex: "nunca sugira AWS — usamos Hetzner")

### 8.2. bootstrap.md (memória eterna)

`~/.claude/projects/.../memory/bootstrap.md` — carregado em toda sessão antes da MEMORY.md. Use pra:

- Identidade e tom permanentes
- Hooks customizados (backup pra Obsidian, push pra GitHub privado)
- Comandos de boas-vindas

### 8.3. Adicionar seus próprios slash commands

```
~/.claude/commands/meu-comando.md
```

Markdown simples com o prompt que vira o comando. Exemplo:

```markdown
---
description: Roda meu checklist diário pré-publicação
---
Antes de publicar qualquer coisa, verifica:
1. Compliance (CTA permitido, claims comprováveis)
2. Tracking (UTM correto, pixel disparando)
3. Mobile (testou em 360px?)
4. Fallback (se quebrar, qual o plano B?)
Lê o draft em $ARGUMENTS e responde com aprovação ou ajustes.
```

Vira `/meu-comando <arquivo>`.

### 8.4. Adicionar seus próprios agentes

```
~/.claude/agents/{nome-agente}.md
```

Com frontmatter YAML definindo nome, descrição, model e ferramentas permitidas. Reutilize o template de qualquer agente HAOS em `plugins/haos/agents/` como base.

### 8.5. Override de hook

Se o backup global do HAOS não te serve, edite `~/.claude/hooks/` — os 3 scripts são PowerShell legíveis (Windows) ou bash (Mac/Linux).

---

## Recursos rápidos

| O que você quer | Onde achar |
|---|---|
| Lista visual de comandos | `/haos:menu` |
| Cenários práticos | `docs/EXAMPLES.md` |
| Refazer onboarding | `/haos:setup` |
| Suspender e retomar Rito | `abortar rito` / `retomar rito` |
| Inspecionar memória | `~/.claude/projects/.../memory/` |
| Reportar bug do plugin | issues no repo público |

---

**Autor:** Gian Marco Menegussi Scaglianti — HAU Soluções Digitais
**Licença:** MIT
