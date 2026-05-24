# Rito V2 — Pipeline Serializado de 13 Fases

> **Documentação de referência.** Para detalhes de cada agente envolvido, ver `AGENTS_GUIDE.md`. Para instalação do plugin, ver `INSTALLATION.md`.

---

## 1. O que é o Rito V2

O **Rito V2** é o pipeline serializado de governança que o HAOS_CC aplica a projetos de **marketing e lançamento de grande escopo**. Ele decompõe uma demanda complexa em **13 fases sequenciais**, cada uma com agentes designados, inputs e outputs explícitos, e um **gate bloqueante** que precisa ser aprovado antes de avançar.

A premissa é simples: lançamentos falham por execução desordenada, não por falta de talento. Saltar diagnóstico vira copy genérica. Saltar tracking vira mídia cega. Saltar QA vira incêndio. O Rito V2 força a ordem certa, com governança humana nos pontos onde dinheiro, reputação ou conformidade estão em jogo.

Estado é persistido em `rito_state.json` no diretório da sessão. Pode-se pausar a qualquer momento e retomar dias depois sem perda de contexto.

---

## 2. Quando usar vs quando NÃO usar

| Cenário | Usar Rito V2? | Por quê |
|---|---|---|
| Lançamento de produto novo (perpétuo ou evento) | ✅ Sim | Pipeline completo necessário |
| Campanha de aquisição com budget >R$ 10k | ✅ Sim | Risco financeiro exige governança |
| Reposicionamento de marca / nova linha | ✅ Sim | Estratégia → criação → ativação cross-departamental |
| Otimização de funil existente com 5+ alavancas | ✅ Sim | Decomposição WBS evita atropelo |
| Trocar a copy de um ad | ❌ Não | Chamar `copy-specialist` direto |
| Subir uma campanha de retargeting já planejada | ❌ Não | Chamar `media-buyer` direto |
| Sprint técnico de software/infra | ❌ Não | Usar os agentes técnicos diretamente (`dev-backend`, `devops`, `dev-frontend`) |
| Auditoria de tracking | ❌ Não | Chamar `tracking-engineer` direto |
| Publicar 3 posts da semana | ❌ Não | Chamar `sm-social` direto |
| Bug fix / pequena melhoria | ❌ Não | Roteamento direto |

**Regra prática:** se a demanda envolve **3+ departamentos** e **gasto/risco material**, é Rito V2. Caso contrário, roteamento direto.

---

## 3. Princípios do Rito

### 3.1. Gates bloqueantes
Cada fase termina num gate. **Nenhuma fase avança sem o gate da anterior aprovado com evidência.** Não existe "avança que depois corrijo". Não existe atalho.

### 3.2. Governança humana em pontos críticos
- **Fase 1 (Intake):** confirmação do usuário sobre o briefing — obrigatória.
- **Fase 3 (Estratégia):** aprovação do `@conselho` (estrategista-chefe + cmo + diretor-criativo).
- **Fase 7 (Funil):** validação end-to-end antes de mídia.
- **Fase 10 (QA & Compliance):** aprovação dupla (`qa-reviewer` + `compliance-officer`).
- **Fase 11 (Deploy):** ⚠️ OK explícito do usuário (gasta dinheiro).

### 3.3. Estado persistente em `rito_state.json`
A cada gate, o `main` grava o estado: fase atual, agentes envolvidos, outputs gerados, decisões tomadas, próximos passos. Permite `abortar rito` e `retomar rito` sem perda.

### 3.4. Uma fase por vez
Não há paralelismo entre fases. Dentro de uma fase pode haver paralelismo entre agentes — fases são serializadas, agentes dentro de fase podem ser paralelizados pelo `main`.

### 3.5. Fase 1 nunca é pulada
Mesmo se o usuário pedir, mesmo sob "urgência". A Fase 1 é o que separa orquestração de adivinhação.

---

## 4. As 13 fases — detalhe

### Fase 1 — Intake & Validação

| Item | Detalhe |
|---|---|
| **Agentes** | `main` + `project-manager` |
| **Inputs** | Briefing inicial do usuário (texto livre) |
| **Outputs** | Briefing validado em `.md`: objetivo, KPIs, escopo, restrições, prazo, critério de pronto |
| **Gate** | Briefing validado E confirmado pelo usuário (resposta explícita) |
| **Tempo típico** | 1-3 horas (depende da clareza inicial) |
| **Pitfalls** | Aceitar briefing vago "para não incomodar"; pular para Fase 2 sem confirmação; perguntas genéricas em vez de específicas (errado: "pode dar mais detalhes?"; certo: "qual o budget máximo de mídia paga para o lançamento?") |

Checklist de saída:
- [ ] Objetivo mensurável definido (faturamento, leads, clientes)
- [ ] KPIs primários e secundários nomeados
- [ ] Budget total + alocação inicial por bloco
- [ ] Janela de tempo + marcos não-negociáveis
- [ ] Restrições explícitas (compliance, plataforma, marca)
- [ ] Usuário respondeu "confirmado" ou equivalente

---

### Fase 2 — Pesquisa & Diagnóstico

| Item | Detalhe |
|---|---|
| **Agentes** | `pesquisador`, `data-analyst`, `cmo` |
| **Inputs** | Briefing validado (F1) + acesso a dados históricos + plataformas |
| **Outputs** | Diagnóstico em `.md`: snapshot de mercado, análise competitiva, performance histórica, hipóteses iniciais |
| **Gate** | Diagnóstico com **dados reais documentados** (fonte + data + métrica) |
| **Tempo típico** | 1-3 dias |
| **Pitfalls** | Pular pesquisa porque "já conhecemos o mercado"; inventar números; análise puramente competitiva sem olhar dados próprios |

Checklist:
- [ ] Concorrentes diretos e indiretos mapeados com evidência
- [ ] Performance histórica do próprio negócio (ROAS, CAC, LTV, conversão)
- [ ] Hipóteses iniciais com critério de validação
- [ ] Gargalos identificados e ranqueados

---

### Fase 3 — Estratégia & Posicionamento

| Item | Detalhe |
|---|---|
| **Agentes** | `estrategista-chefe`, `cmo`, `diretor-criativo` |
| **Inputs** | Diagnóstico (F2) |
| **Outputs** | Documento de estratégia: posicionamento, alvo, ângulo central, oferta, ascensão, prova social, métrica-mestre |
| **Gate** | **Estratégia aprovada pelo @conselho** (3 votos com fundamentação) |
| **Tempo típico** | 1-2 dias |
| **Pitfalls** | Pular voto de algum membro do conselho; aprovar estratégia "boa o suficiente" para evitar conflito; posicionamento genérico tipo "ajudamos pessoas a transformar a vida"; sem hipótese falsificável |

Checklist:
- [ ] Posicionamento em 1 frase com diferenciação real
- [ ] Persona específica (não "público em geral")
- [ ] Ângulo central da campanha + 2 ângulos secundários para teste
- [ ] Métrica-mestre + critério de sucesso
- [ ] Riscos top 3 com mitigação
- [ ] Atas do conselho com posições individuais

---

### Fase 4 — Planejamento Tático

| Item | Detalhe |
|---|---|
| **Agentes** | `project-manager`, `traffic-master`, `funnel-architect` |
| **Inputs** | Estratégia aprovada (F3) |
| **Outputs** | WBS + cronograma + backlog priorizado + RACI + plano de mídia em `.md` |
| **Gate** | WBS + cronograma aprovados pelo usuário |
| **Tempo típico** | 4-8 horas |
| **Pitfalls** | Cronograma sem dependências mapeadas; backlog sem priorização; alocação de tempo otimista demais; esquecer buffer para QA |

Checklist:
- [ ] WBS com decomposição até nível tarefa atribuível
- [ ] Cronograma com marcos e caminho crítico
- [ ] Plano de mídia com público/budget/KPI por canal
- [ ] Plano de funil (jornada esboçada)
- [ ] Buffer de QA e compliance previsto
- [ ] RACI definido por entregável

---

### Fase 5 — Copywriting & Mensagens

| Item | Detalhe |
|---|---|
| **Agentes** | `copy-specialist`, `email-marketer`, `crm-specialist` |
| **Inputs** | Estratégia (F3) + plano (F4) + brand guidelines |
| **Outputs** | Copy de ads (headlines, primários, descrições), VSL, sequência de e-mail, scripts de mensageria, copy de LP |
| **Gate** | **Copies aprovadas pelo `diretor-criativo` E pelo `compliance-officer`** |
| **Tempo típico** | 2-5 dias |
| **Pitfalls** | Pular variações A/B; aprovar internamente claims sensíveis sem compliance; copy genérica desligada do ângulo de F3; entregar sem flag de compliance |

Checklist:
- [ ] Cada peça tem ≥2 variações A/B com hipótese
- [ ] Flag de compliance em cada peça (`LIMPO` ou revisado)
- [ ] Aprovação `diretor-criativo` por escrito (P0/P1 resolvidos)
- [ ] Aprovação `compliance-officer` por escrito
- [ ] Copy de LP, ads, e-mail e mensageria coerentes entre si

---

### Fase 6 — Design & Criativos

| Item | Detalhe |
|---|---|
| **Agentes** | `designer`, `videomaker`, `content-strategist` |
| **Inputs** | Copies aprovadas (F5) + brand guidelines |
| **Outputs** | Banners de ads, carrosséis, thumbnails, Reels, VSL editado, cortes derivados, social cards |
| **Gate** | **Criativos aprovados pelo `diretor-criativo`** (checklist 10 dimensões) |
| **Tempo típico** | 3-7 dias |
| **Pitfalls** | Entregar sem variações por formato; legenda de vídeo faltando (videomaker DEVE entregar legendas sincronizadas em 100% das peças); design desconectado da copy; thumbnail só decorativo sem hook |

Checklist:
- [ ] Variações por canal (feed/stories/reels/YouTube/etc.)
- [ ] Legendas sincronizadas em 100% dos vídeos
- [ ] Contraste WCAG AA + fonte ≥18pt em texto principal
- [ ] Mobile-first verificado
- [ ] Aprovação por escrito do `diretor-criativo`
- [ ] Anti-AI-slop checklist aplicado

---

### Fase 7 — Funil & Automação

| Item | Detalhe |
|---|---|
| **Agentes** | `funnel-architect`, `automation-engineer`, `dev-frontend`, `dev-backend` |
| **Inputs** | Estratégia (F3) + copies (F5) + criativos (F6) |
| **Outputs** | LPs/checkout no ar, automações configuradas, integrações testadas, webhooks funcionando, e-mails programados |
| **Gate** | **Funil testado end-to-end** (lead simulado percorre todos os pontos) |
| **Tempo típico** | 5-10 dias |
| **Pitfalls** | Subir LP sem otimização de CWV; webhooks sem idempotência; automações sem fallback; pular teste end-to-end por "tempo curto"; thank-you page sem evento de conversão configurado |

Checklist:
- [ ] LP/checkout em produção (URL estável)
- [ ] Core Web Vitals dentro de limites
- [ ] Automações com retry/idempotência
- [ ] Lead de teste passou por todos os pontos: ad → LP → conversão → e-mail → CRM
- [ ] Integrações com pixel/CAPI prontas (mas não validadas ainda — isso é Fase 9)

---

### Fase 8 — Tráfego & Mídia

| Item | Detalhe |
|---|---|
| **Agentes** | `traffic-master`, `media-buyer`, `tracking-engineer` |
| **Inputs** | Funil testado (F7) + plano de mídia (F4) + criativos (F6) |
| **Outputs** | Campanhas **CONFIGURADAS** nas plataformas (estrutura, públicos, criativos carregados, budgets definidos) |
| **Gate** | **Campanhas configuradas — NÃO ativadas.** Ativação é Fase 11. |
| **Tempo típico** | 1-2 dias |
| **Pitfalls** | Ativar por engano (sempre deixar em `OFF` ou `PAUSADO`); públicos sem exclusões; criativos sem nomes padronizados que prejudicam relatório; sem green light de tracking |

Checklist:
- [ ] Estrutura de campanhas/conjuntos/ads padronizada
- [ ] Públicos com exclusões (clientes, conversores, lookalikes)
- [ ] Criativos com naming convention consistente
- [ ] Budgets diários definidos
- [ ] Status: PAUSADO (não ativar antes da Fase 11)

---

### Fase 9 — Tracking & Dados

| Item | Detalhe |
|---|---|
| **Agentes** | `tracking-engineer`, `bi-engineer`, `data-analyst` |
| **Inputs** | Funil em produção (F7) + campanhas configuradas (F8) |
| **Outputs** | Eventos validados (pixel, CAPI, GA4, GTM), UTMs padronizadas, dashboard pronto, alertas configurados |
| **Gate** | **Pipeline de dados funcional** — green light explícito do `tracking-engineer` |
| **Tempo típico** | 1-3 dias |
| **Pitfalls** | Confiar em "deve estar funcionando"; pular teste de cada evento via console/diagnóstico; UTM com case inconsistente; sem CAPI configurado (iOS 14.5+ exige); dashboard sem filtro de UTM |

Checklist:
- [ ] Cada evento validado por teste real (event ID, valor, parâmetros)
- [ ] CAPI ativo onde aplicável
- [ ] UTMs documentadas e aplicadas
- [ ] Dashboard mostra dados do teste
- [ ] Alertas de drop de evento configurados
- [ ] Green light por escrito do `tracking-engineer`

---

### Fase 10 — QA & Compliance

| Item | Detalhe |
|---|---|
| **Agentes** | `qa-reviewer`, `compliance-officer`, `project-manager` |
| **Inputs** | Tudo de F5 a F9 |
| **Outputs** | Parecer QA + parecer Compliance + checklist final de go-live |
| **Gate** | **AMBOS aprovados.** Se qualquer um pede ajuste, volta para a fase responsável e retorna. |
| **Tempo típico** | 4-12 horas |
| **Pitfalls** | Tratar como formalidade e aprovar sem revisar; ignorar `AJUSTES` por pressão de prazo; aprovar com pendências P0 abertas; não atualizar runbook após correção |

Checklist:
- [ ] QA: todos os pontos do funil testados + tracking validado + criativos no ar conferem
- [ ] Compliance: claims revisados, políticas de plataforma respeitadas, LGPD em conformidade
- [ ] Lista de pendências = zero P0/P1
- [ ] Plano de rollback documentado
- [ ] Runbook de operação atualizado

---

### Fase 11 — Deploy & Ativação ⚠️ ALERTA ESPECIAL

| Item | Detalhe |
|---|---|
| **Agentes** | `devops`, `media-buyer`, `sm-social` |
| **Inputs** | Tudo aprovado em F10 + **OK explícito do usuário** |
| **Outputs** | Campanhas ATIVAS, deploys aplicados, posts agendados publicando, automações ligadas |
| **Gate** | Ativação confirmada com smoke-test e primeiros eventos chegando |
| **Tempo típico** | 1-4 horas |
| **Pitfalls** | Ativar sem OK explícito por escrito; ativar fora de janela combinada; ativar tudo de uma vez sem ramp-up; não monitorar primeira hora |

**⚠️ Esta é a única fase do Rito V2 em que dinheiro real começa a ser gasto e ações irreversíveis acontecem (impressões compradas, leads recebem e-mail real, posts vão ao ar).**

Protocolo obrigatório antes da ativação:
1. `main` apresenta resumo final: o que será ativado, custo estimado primeiras 24h, plano de rollback, responsável por monitorar.
2. Usuário responde explicitamente com `OK ATIVAR` ou equivalente inequívoco.
3. `media-buyer` ativa primeiro conjunto/campanha (ramp-up — não tudo de uma vez).
4. `tracking-engineer` confirma chegada dos primeiros eventos.
5. `main` reporta status nas primeiras 1h, 4h e 24h.

Sem OK explícito, ativação **não acontece** — mesmo que F10 esteja perfeita.

---

### Fase 12 — Monitoramento & Otimização

| Item | Detalhe |
|---|---|
| **Agentes** | `media-buyer`, `data-analyst`, `traffic-master`, `cmo` |
| **Inputs** | Campanhas ativas + dados do dashboard |
| **Outputs** | Relatório de performance (diário inicial, depois semanal) + decisões de otimização (pausa/scaling/ajuste) |
| **Gate** | Relatório de performance documentado a cada ciclo |
| **Tempo típico** | Duração da campanha (contínuo) |
| **Pitfalls** | Otimizar com janela curta demais (decisão em <100 conversões); pausar criativo bom por aversão à perda; escalar mais de 30% do budget livre sem validação de ROI; ignorar alertas de tracking |

Checklist por ciclo:
- [ ] Métricas vs KPI (verde/amarelo/vermelho)
- [ ] Top 3 alavancas de otimização aplicadas
- [ ] Hipóteses validadas/invalidadas registradas
- [ ] Próximas ações endereçadas

---

### Fase 13 — Debrief & Aprendizados

| Item | Detalhe |
|---|---|
| **Agentes** | `cmo`, `project-manager`, `main` |
| **Inputs** | Resultado completo da campanha |
| **Outputs** | Pós-mortem em `.md`: o que funcionou, o que não funcionou, hipóteses validadas, ajustes para próximo ciclo, atualização de memória |
| **Gate** | Retrospectiva documentada + memória atualizada |
| **Tempo típico** | 2-4 horas |
| **Pitfalls** | Pular debrief porque "campanha foi bem"; debrief só com narrativa, sem números; não atualizar memória — perde aprendizado; culpar agente em vez de processo |

Checklist:
- [ ] Resumo executivo (3 parágrafos: contexto, resultado, próximo)
- [ ] Métricas finais vs metas
- [ ] O que funcionou (manter)
- [ ] O que não funcionou (mudar)
- [ ] Hipóteses validadas/invalidadas com evidência
- [ ] Memória do projeto atualizada para próximas execuções

---

## 5. Como iniciar um Rito V2

Comando único:

```
/haos:main #
```

Seguido do briefing detalhado. Prefixo `#` ativa o Rito V2; sem prefixo, vira modo Concierge.

Exemplo:

```
/haos:main # Quero lançar o curso XYZ em setembro. Budget de R$ 80k de mídia,
meta de 200 vendas a R$ 1.997. Funil atual: webinar perpétuo convertendo 1,2%.
Tenho lista de 18k leads aquecidos. Preciso ir ao ar dia 15/09.
```

`main` recebe, classifica como Rito V2, e **começa sempre na Fase 1** — não pula para "ok, vamos atacar".

---

## 6. Como pausar, retomar, abortar

| Comando | Efeito |
|---|---|
| `abortar rito` | Salva `rito_state.json`, encerra sessão, mantém artefatos gerados |
| `retomar rito` | Lê `rito_state.json`, mostra resumo do estado, retoma da próxima fase pendente |
| `status rito` | Mostra fase atual, gates aprovados, pendências |
| `voltar fase N` | Reabre fase anterior (gates posteriores invalidados — exige justificativa) |

Estado salvo inclui: fase atual, decisões aprovadas, agentes envolvidos, outputs em disco, próximos passos, pendências.

---

## 7. Checkpoints expandidos

Três fases têm checkpoint reforçado — não basta o gate normal, exige confirmação humana explícita:

### Checkpoint pós-Fase 3 (Estratégia)
Antes de gastar tempo de equipe em F4-F10, usuário valida estratégia. Se mudou de ideia, agora é hora — depois é desperdício.

### Checkpoint pós-Fase 7 (Funil)
Antes de configurar mídia, usuário valida que jornada do lead está como queria. Mudança aqui ainda é barata; depois exige refação cara.

### Checkpoint pós-Fase 10 (QA & Compliance)
Antes da Fase 11 (ativação), usuário recebe pacote final consolidado: criativos, mídia, funil, tracking, riscos conhecidos. Última chance antes de gasto real.

Cada checkpoint produz `.md` resumido para revisão rápida e exige resposta explícita do usuário antes de prosseguir.

---

## 8. Fase 11 — ALERTA ESPECIAL: Deploy & Ativação

A Fase 11 é tratada de forma diferente por uma razão simples: é a única em que **dinheiro sai da conta e ações se tornam irreversíveis**.

Regras inflexíveis:

1. **OK explícito por escrito do usuário** — não inferir, não assumir, não interpretar silêncio como aprovação.
2. **Ramp-up obrigatório** — ativar primeiro um conjunto piloto (10-20% do budget), validar que tracking chega, escalar gradualmente.
3. **Monitoramento ativo na primeira hora, 4h, 24h** — relatórios obrigatórios.
4. **Rollback pronto** — comando ou procedimento documentado para pausar tudo em <5min.
5. **Janela de ativação combinada** — não ativar fora da janela acordada (final de semana, madrugada, datas sensíveis).

Se o usuário não responder o OK em até X horas, o `main` reporta `BLOQUEADO` e mantém tudo pausado. Não há ativação por timeout.

---

## 9. Pós-rito — debrief, aprendizados, memória

Após Fase 13:

1. **Atualizar memória do projeto** — registrar aprendizados na memória persistente do HAOS (`memory/` no diretório do projeto).
2. **Atualizar brand guidelines** se houve aprovação de novo padrão (responsável: `diretor-criativo`).
3. **Atualizar playbook de mídia** com novas alavancas validadas (responsável: `traffic-master`).
4. **Documentar bugs/limitações** encontrados nas ferramentas (responsável: `devops`/`automation-engineer`).
5. **Arquivar ativos** em estrutura padronizada para reaproveitamento.
6. **Fechar `rito_state.json`** com status final e link para o debrief.

A próxima execução começa com mais conhecimento — esse é o ROI composto do HAOS_CC.

---

## 10. Resumo executivo do pipeline

| Fase | Nome | Agentes | Gate | Bloqueia? |
|---|---|---|---|---|
| 1 | Intake & Validação | main, project-manager | Briefing validado pelo usuário | ✅ |
| 2 | Pesquisa & Diagnóstico | pesquisador, data-analyst, cmo | Dados reais documentados | ✅ |
| 3 | Estratégia & Posicionamento | estrategista-chefe, cmo, diretor-criativo | Aprovação do @conselho | ✅ |
| 4 | Planejamento Tático | project-manager, traffic-master, funnel-architect | WBS + cronograma aprovados | ✅ |
| 5 | Copywriting | copy-specialist, email-marketer, crm-specialist | Aprovação diretor-criativo + compliance | ✅ |
| 6 | Design | designer, videomaker, content-strategist | Aprovação diretor-criativo | ✅ |
| 7 | Funil & Automação | funnel-architect, automation-engineer, dev-frontend, dev-backend | Funil testado end-to-end | ✅ |
| 8 | Tráfego | traffic-master, media-buyer, tracking-engineer | Campanhas CONFIGURADAS (não ativas) | ✅ |
| 9 | Tracking | tracking-engineer, bi-engineer, data-analyst | Pipeline de dados funcional | ✅ |
| 10 | QA & Compliance | qa-reviewer, compliance-officer, project-manager | AMBOS aprovados | ✅ |
| 11 | **Deploy & Ativação** | devops, media-buyer, sm-social | ⚠️ **OK explícito do usuário** | ✅ |
| 12 | Monitoramento | media-buyer, data-analyst, traffic-master, cmo | Relatório de performance por ciclo | ✅ |
| 13 | Debrief & Aprendizados | cmo, project-manager, main | Retrospectiva + memória atualizada | ✅ |

Toda fase tem gate. Toda gate é bloqueante. Toda decisão crítica passa pelo usuário. Isso é o Rito V2.
