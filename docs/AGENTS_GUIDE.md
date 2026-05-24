# HAOS_CC — Guia de Referência dos 29 Agentes

> **Documentação de referência.** Para tutorial introdutório, ver `README.md`. Para o pipeline serializado de marketing/lançamento, ver `RITO_V2.md`.

---

## Como ler este guia

Cada agente está descrito num bloco compacto com cinco campos:

- **Departamento + slash command + tools:** roteamento e capacidades técnicas do sub-agente.
- **Quando usar:** cenários típicos de invocação — gatilhos concretos, não slogans.
- **Quando NÃO usar:** limites do agente. Lista o agente correto para o caso adjacente.
- **Brief que ele exige:** as perguntas obrigatórias antes de qualquer entrega. Se o usuário não fornecer, o agente devolve `BLOQUEADO` listando o que falta.
- **Output esperado:** formato da entrega — tabela, doc `.md`, plano, código, parecer, etc.

Todos os 29 agentes obedecem o **padrão transversal** descrito ao final deste documento: BRIEF OBRIGATÓRIO, RETORNO ESTRUTURADO (`CONCLUÍDO` / `BLOQUEADO` / `REVISÃO`) e regras `NUNCA` comuns.

### Tabela-resumo dos 8 departamentos

| # | Departamento | Slash | Função | Agentes |
|---|---|---|---|---|
| 1 | **@orquestracao** | `/haos:main`, `/haos:concierge`, `/haos:project-manager`, `/haos:qa-reviewer` | Classifica, roteia, sequencia, valida e fecha gates | main, concierge, project-manager, qa-reviewer |
| 2 | **@conselho** | `/haos:estrategista-chefe`, `/haos:cmo`, `/haos:diretor-criativo` | Decisões macro com voto de peso | estrategista-chefe, cmo, diretor-criativo |
| 3 | **@criativo** | `/haos:copy-specialist`, `/haos:content-strategist`, `/haos:designer`, `/haos:videomaker`, `/haos:sm-social` | Conteúdo, copy, design, vídeo, gestão social | 5 agentes |
| 4 | **@trafego** | `/haos:traffic-master`, `/haos:media-buyer`, `/haos:tracking-engineer` | Estratégia de mídia, execução tática, rastreamento | 3 agentes |
| 5 | **@dados** | `/haos:data-analyst`, `/haos:bi-engineer`, `/haos:pesquisador` | Análise, infra de BI, inteligência competitiva | 3 agentes |
| 6 | **@funnel** | `/haos:funnel-architect`, `/haos:automation-engineer`, `/haos:crm-specialist`, `/haos:email-marketer` | Jornada, automações, CRM e e-mail | 4 agentes |
| 7 | **@produto** | `/haos:product-manager`, `/haos:ux-researcher`, `/haos:dev-frontend`, `/haos:dev-backend` | Discovery, UX, engenharia de produto | 4 agentes |
| 8 | **@seguranca** | `/haos:compliance-officer`, `/haos:devops`, `/haos:chuck-norris` | Compliance regulatório, infra/ops, segurança ofensiva | 3 agentes |

Total: 29 agentes (main+concierge contam como entry-points do sistema; os demais 27 são especialistas).

---

## 1. @orquestracao — Roteamento, governança e gate de qualidade

### main — Orquestrador Principal
**Departamento:** @orquestracao · **Slash command:** `/haos:main` · **Tools:** Read, Grep, Glob, Bash, Agent, WebFetch

**Quando usar:**
- Entry point absoluto de toda demanda multi-agente.
- Demandas com prefixo `#` (ativa Rito V2 — pipeline de 13 fases).
- Quando 3+ subsistemas independentes precisam ser executados em paralelo.
- Consolidação de outputs de múltiplos especialistas antes de entregar ao usuário.

**Quando NÃO usar:**
- Tarefa única e clara para um especialista (chamar `/haos:<agente>` direto).
- Pergunta de "para quem falo sobre X?" (usar `concierge`).
- Execução de tarefa especializada — `main` orquestra, não executa.

**Brief que ele exige:**
- Mensagem completa do usuário (sem truncagem).
- Modo de operação (Concierge / Rito / Direto / Broadcast / Emergência).
- Sessão e histórico imediato relevantes.
- Nível de permissão e contexto do projeto.

**Output esperado:**
- Plano de roteamento + delegações com briefing completo a cada sub-agente + consolidação final formatada. Status sempre `CONCLUÍDO`, `BLOQUEADO` ou `REVISÃO`.

---

### concierge — Roteador e Recepcionista
**Departamento:** @orquestracao · **Slash command:** `/haos:concierge` · **Tools:** Read, Grep, Glob

**Quando usar:**
- Mensagem chegou sem destino explícito e não está claro quem deve atender.
- Usuário pergunta "para quem falo sobre X?".
- Triagem de mensagens vagas que precisam ser classificadas antes de roteamento.

**Quando NÃO usar:**
- Tarefa já tem agente claro (delegar direto).
- Orquestração de pipeline (chamar `main`).
- Decisões estratégicas — apenas classifica intenção.

**Brief que ele exige:**
- Texto integral da mensagem original.
- Contexto mínimo do projeto (qual marca/produto/cliente).
- Urgência percebida.

**Output esperado:**
- Classificação curta: agente alvo + 1-2 linhas de contexto reenviado ao agente. Não produz entregas de conteúdo.

---

### project-manager — Dono do Plano Tático
**Departamento:** @orquestracao · **Slash command:** `/haos:project-manager` · **Tools:** Read, Grep, Glob, Bash, Write, Edit

**Quando usar:**
- Planejar escopo e decompor em WBS.
- Sequenciar dependências, montar kanban.
- Monitorar progresso com evidência, gerir bloqueios.
- Escalonar no tempo certo (não cedo demais nem tarde).
- Fase 4 do Rito V2 (Planejamento Tático).

**Quando NÃO usar:**
- Decisão estratégica de portfólio (chamar `estrategista-chefe`).
- Decisão de gasto/canal (chamar `traffic-master` ou `cmo`).
- Tarefas operacionais individuais — PM coordena, não executa.

**Brief que ele exige:**
- Objetivo do projeto + critério de pronto.
- Prazo e marcos não-negociáveis.
- Recursos disponíveis (agentes, budget, ferramentas).
- Restrições conhecidas (datas mortas, dependências externas).

**Output esperado:**
- WBS + cronograma + RACI + lista de bloqueios + status report periódico em `.md`.

---

### qa-reviewer — Gate de Aprovação
**Departamento:** @orquestracao · **Slash command:** `/haos:qa-reviewer` · **Tools:** Read, Grep, Glob, Bash, WebFetch

**Quando usar:**
- ANTES de publicar/deployar qualquer artefato: copy, design, código, campanha, automação, e-mail.
- Fase 10 do Rito V2 (QA & Compliance) — junto com `compliance-officer`.
- Quando precisa de parecer formal externo ao autor.

**Quando NÃO usar:**
- Para escrever ou consertar o artefato (devolve `AJUSTES`, não executa correção).
- Para validação subjetiva sem critério — exige checklist objetivo.

**Brief que ele exige:**
- Artefato concreto a revisar (arquivo, link, URL, código).
- Critérios de aceitação aplicáveis (técnicos, marca, conformidade).
- Quem é o autor (para devolução com endereço correto).

**Output esperado:**
- Parecer formal: `APROVADO` / `AJUSTES` (lista numerada de correções) / `REPROVADO` (com justificativa e refação).

---

## 2. @conselho — Decisões macro com voto de peso

### estrategista-chefe — Estrategista Macro de Negócios
**Departamento:** @conselho · **Slash command:** `/haos:estrategista-chefe` · **Tools:** Read, Grep, Glob, Bash, WebFetch, Agent

**Quando usar:**
- Definição/revisão de posicionamento.
- Análise de cenários (otimista/base/risco) para decisões de impacto.
- Planejamento trimestral, priorização de portfólio.
- Análise competitiva, avaliação de fit de novo produto, decisão de expansão de mercado.
- Fase 3 do Rito V2 (Estratégia & Posicionamento).

**Quando NÃO usar:**
- Otimização tática de campanha em curso (chamar `cmo` ou `traffic-master`).
- Análise de dados sem ângulo estratégico (chamar `data-analyst`).
- Criação de copy/criativo (chamar criativo).

**Brief que ele exige:**
- Objetivo da demanda — qual pergunta estratégica precisa ser respondida?
- Dados de performance recentes (30-90 dias) por produto e canal.
- Contexto competitivo e movimentações de mercado relevantes.
- Restrições (budget, prazo, capacidade).
- Modo: PLANEJAMENTO_TRIMESTRAL / REVISAO_ESTRATEGIA / ANALISE_COMPETITIVA / EXPANSAO_MERCADO.

**Output esperado:**
- Recomendação com matriz de cenários, hipóteses falsificáveis, alternativas, riscos top 2-3 com mitigação, ações 30/60/90 dias com responsável e métrica.

---

### diretor-criativo — Direção Criativa de Marca
**Departamento:** @conselho · **Slash command:** `/haos:diretor-criativo` · **Tools:** Read, Grep, Glob, Bash, WebFetch, Agent

**Quando usar:**
- Conceituação de campanha (definição do conceito central).
- Aprovação/veto de material criativo (10 dimensões de critique).
- Definição/atualização de brand guidelines (tom, paleta, tipografia).
- Direção de produção criativa cross-agentes.
- Fase 5/6 do Rito V2.

**Quando NÃO usar:**
- Execução de design ou copy (papel é dirigir e aprovar, não executar).
- Decisão de mídia/canal (chamar `traffic-master`).
- Compliance regulatório (chamar `compliance-officer`).

**Brief que ele exige:**
- Objetivo do projeto (tráfego, conversão, autoridade, retenção?).
- Canal de destino (feed, Stories, Reels, ad, email, LP?).
- Público específico (frio, base quente, recompra?).
- Produto/tema.
- Restrições (prazo, plataforma).

**Output esperado:**
- `APROVADO` (com nota) / `REVISÃO` (P0-P3 com critério violado + correção) / `VETADO` (com justificativa de marca). Briefings de produção para designer/copy/videomaker quando concebe campanha.

---

### cmo — Chief Marketing Officer Virtual
**Departamento:** @conselho · **Slash command:** `/haos:cmo` · **Tools:** Read, Grep, Glob, Bash, WebFetch, Agent

**Quando usar:**
- Diagnóstico de funil ponta-a-ponta com sinais OK/Atenção/Crítico.
- Análise de ROI/ROAS/CPA/LTV e plano de otimização.
- Crítica de criativos com lente de performance.
- Posição estratégica no `@conselho` para decisão pendente.
- Debrief de lançamento (pós-mortem).

**Quando NÃO usar:**
- Definição de posicionamento macro (chamar `estrategista-chefe`).
- Execução tática de mídia (chamar `media-buyer`).
- Análise sem dados de performance disponíveis — devolve `BLOQUEADO`.

**Brief que ele exige:**
- Tipo de sessão (Funil & ROI / Criativos / Comercial / Conselho / Debrief).
- Período de análise (ontem, 7d, 30d, ciclo).
- Canais e dados disponíveis.
- Arquivos concretos (CSV, planilha, dashboard) por nome e função.
- Objetivo da sessão.

**Output esperado:**
- Tabela de diagnóstico por etapa do funil + hipóteses ranqueadas + top 5 ações priorizadas (canal/etapa/métrica/risco) + posição formal quando em modo Conselho.

---

## 3. @criativo — Conteúdo, copy, design, vídeo, social

### copy-specialist — Copywriter de Conversão
**Departamento:** @criativo · **Slash command:** `/haos:copy-specialist` · **Tools:** Read, Grep, Glob, Bash, WebFetch

**Quando usar:**
- Headlines de ads, VSLs, sequências de e-mail, scripts de mensageria.
- Copy de landing page, carrosséis, anúncios em qualquer formato.
- Sempre que precisar de variações A/B (entrega obrigatória).
- Fase 5 do Rito V2.

**Quando NÃO usar:**
- Conteúdo orgânico de atração/nutrição (chamar `content-strategist`).
- Decisão de canal/budget para a copy (chamar `traffic-master`).
- Aprovação final do material (chamar `diretor-criativo` + `compliance-officer`).

**Brief que ele exige:**
- Produto, objetivo da peça, estágio do funil (topo/meio/fundo).
- Canal/formato (ad, LP, email, VSL, carrossel).
- Avatar ativo e momento de dor específico.
- Oferta, CTA, preço/condição.
- Referências aprovadas e restrições (compliance, plataforma).

**Output esperado:**
- Arquivo `.md` com versão principal + ≥1 variação A/B + hipótese de teste + flag de compliance (`LIMPO` ou `COMPLIANCE_REQUIRED`). Para ads: mínimo 3 headlines + 2 textos primários.

---

### content-strategist — Estrategista de Conteúdo Orgânico
**Departamento:** @criativo · **Slash command:** `/haos:content-strategist` · **Tools:** Read, Grep, Glob, Bash, WebFetch

**Quando usar:**
- Construir audiência qualificada sem depender 100% de tráfego pago.
- Calendário editorial mensal cross-platform.
- Briefings de conteúdo (Reels, YouTube, blog SEO).
- Estratégia de reaproveitamento (long-form → short-form).
- Análise de performance orgânica.

**Quando NÃO usar:**
- Copy de conversão (chamar `copy-specialist` — content faz atração, copy faz conversão).
- Pauta de campanha paga (chamar `traffic-master`).
- Execução de publicação (chamar `sm-social`).

**Brief que ele exige:**
- Modo: CALENDARIO_MENSAL / MAQUINA_DE_REELS / YOUTUBE_STRATEGY / SEO_BLOG / REAPROVEITAMENTO.
- Plataformas ativas + cadência atual.
- Audiência-alvo e dores prioritárias.
- Métricas orgânicas atuais (alcance, salvamento, watch-time).
- Pilares de conteúdo já validados.

**Output esperado:**
- Calendário em tabela (data / canal / formato / hook / CTA) + briefings individuais por peça + plano de derivativos.

---

### designer — Designer Gráfico e Diretor de Arte
**Departamento:** @criativo · **Slash command:** `/haos:designer` · **Tools:** Read, Grep, Glob, Bash, Write, WebFetch

**Quando usar:**
- Carrosséis, banners de ad, thumbnails, cards de feed, stories.
- Material impresso.
- Aplicação visual de brand guidelines em peças novas.
- Modos: CARROSSEL / BANNER_ADS / THUMBNAIL / MATERIAL_IMPRESSO / SOCIAL_CARD.

**Quando NÃO usar:**
- Conceito de campanha (chamar `diretor-criativo`).
- Vídeo/animação (chamar `videomaker`).
- Sem brand guidelines disponíveis — devolve `BLOQUEADO`.

**Brief que ele exige:**
- Brand guidelines vigentes (paleta, tipografia, logo).
- Canal + specs técnicas (formato, dimensões, peso).
- Copy/texto final aprovado.
- Mood/referências de aprovação prévia.

**Output esperado:**
- Especificação visual + entrega seguindo regras: fonte ≥18pt para texto principal, contraste WCAG AA, mobile-first, anti-AI-slop checklist aplicado.

---

### videomaker — Produtor e Editor de Vídeo
**Departamento:** @criativo · **Slash command:** `/haos:videomaker` · **Tools:** Read, Grep, Glob, Bash, Write, WebFetch

**Quando usar:**
- Reels, vídeos YouTube longos, TikTok, VSL, cortes derivados.
- Storyboard de vídeo (pré-produção).
- Edição com obsessão pelos primeiros 3 segundos.
- Modos: REELS / YOUTUBE / VSL / TIKTOK / CORTES / STORYBOARD.

**Quando NÃO usar:**
- Sem roteiro/copy aprovado — devolve `BLOQUEADO`.
- Sem hook definido — devolve `BLOQUEADO` ao copy.
- Design estático puro (chamar `designer`).

**Brief que ele exige:**
- Roteiro com timecodes ou estrutura narrativa.
- Plataforma de destino + duração-alvo.
- Material bruto disponível (captação, b-roll, trilhas).
- Estilo de edição de referência.

**Output esperado:**
- Vídeo final ou edit-list anotado + **legendas sincronizadas obrigatórias** (100% das entregas) + thumbnail proposto + cortes derivados.

---

### sm-social — Gestor de Redes Sociais
**Departamento:** @criativo · **Slash command:** `/haos:sm-social` · **Tools:** Read, Grep, Glob, Bash, WebFetch

**Quando usar:**
- Execução do calendário editorial (publicação efetiva).
- Gestão de comunidade (comentários, DMs).
- Métricas semanais por plataforma.
- Coordenação com criativo (peças) e tráfego (impulsionamento orgânico→pago).
- Protocolo de crise de reputação.

**Quando NÃO usar:**
- Definir o que postar (chamar `content-strategist`).
- Criar a peça (chamar `designer` / `copy-specialist` / `videomaker`).
- Decisão estratégica de canal (chamar `cmo`).

**Brief que ele exige:**
- Calendário editorial aprovado da semana/mês.
- Peças finais aprovadas (qa-reviewer + diretor-criativo).
- Protocolo de respostas (FAQ, tom, escalonamento).
- Credenciais/acesso às plataformas.

**Output esperado:**
- Publicações no horário + log semanal (alcance, engajamento, salvamentos, DMs) + alertas de crise + sugestões ao content-strategist.

---

## 4. @trafego — Mídia paga, execução e rastreamento

### traffic-master — Estrategista-Chefe de Tráfego Pago
**Departamento:** @trafego · **Slash command:** `/haos:traffic-master` · **Tools:** Read, Grep, Glob, Bash, WebFetch, Agent

**Quando usar:**
- Planos de mídia: perpétuo, lançamento, expansão de canal, retargeting, crise.
- Briefing ao `media-buyer` (público, budget, KPIs).
- Debrief de ciclo de mídia.
- Orquestrar `media-buyer`, `tracking-engineer`, `data-analyst`.
- Fase 8 do Rito V2.

**Quando NÃO usar:**
- Setup operacional de campanha (delegar ao `media-buyer`).
- Definir copy/criativo (chamar `@criativo`).
- Validar tracking (chamar `tracking-engineer`).

**Brief que ele exige:**
- Objetivo de mídia (faturamento, leads, awareness, retargeting).
- Budget total + distribuição inicial.
- Janela temporal + marcos.
- Plataformas elegíveis e restrições.
- Histórico de campanhas recentes.

**Output esperado:**
- Plano de mídia em `.md`: público(s), budget por canal/etapa, KPIs primários e secundários, calendário, critérios de scaling/corte, debrief template.

---

### media-buyer — Executor Tático de Mídia Paga
**Departamento:** @trafego · **Slash command:** `/haos:media-buyer` · **Tools:** Read, Grep, Glob, Bash, WebFetch, Agent

**Quando usar:**
- Setup de campanha (estrutura, públicos, criativos).
- Otimização diária, ajustes de budget, lances.
- Teste A/B operacional.
- Scaling de campanhas validadas.
- Protocolo de crise em campanhas ativas.
- Fase 11 do Rito V2 — execução do GO.

**Quando NÃO usar:**
- Definir estratégia ou KPIs (chamar `traffic-master`).
- Subir campanha sem `tracking-engineer` ter dado green light de tracking.
- Decidir gasto novo sem plano aprovado.

**Brief que ele exige:**
- Plano de mídia aprovado pelo `traffic-master`.
- Criativos finais aprovados.
- Públicos definidos + exclusões.
- Green light de tracking.
- Budget aprovado + limite diário/semanal.

**Output esperado:**
- Campanhas no ar (ou prontas para ativar) + log diário de otimizações + alertas de divergência vs KPI + relatório de fim-de-ciclo.

---

### tracking-engineer — Engenheiro de Rastreamento
**Departamento:** @trafego · **Slash command:** `/haos:tracking-engineer` · **Tools:** Read, Grep, Glob, Bash, WebFetch

**Quando usar:**
- Auditoria de tracking (pixels, eventos, CAPI).
- Setup/configuração de GTM, GA4, pixels de plataforma.
- Geração de UTMs padronizadas.
- Validação pré-go-live (green light obrigatório antes de qualquer campanha).
- Debugging de eventos.
- Fase 9 do Rito V2.

**Quando NÃO usar:**
- Análise de dados de performance (chamar `data-analyst`).
- Construção de dashboard (chamar `bi-engineer`).
- Sem acesso técnico à plataforma — devolve `BLOQUEADO`.

**Brief que ele exige:**
- Stack atual (GTM container ID, GA4 property, pixels ativos).
- Eventos a rastrear + valores monetários.
- URLs das LPs / checkout / thank-you.
- Plataformas de ads em uso (FB, Google, TikTok, etc.).

**Output esperado:**
- Documento de tracking: mapa de eventos, parâmetros, UTMs padronizadas, testes de validação + parecer `GREEN LIGHT` ou `BLOQUEADO` para subir mídia.

---

## 5. @dados — Análise, BI e inteligência competitiva

### data-analyst — Analista de Dados de Performance
**Departamento:** @dados · **Slash command:** `/haos:data-analyst` · **Tools:** Read, Grep, Glob, Bash, WebFetch, Agent

**Quando usar:**
- Diagnóstico diário/semanal de performance.
- Análise de funil (LP → Lead → Conversão → Venda) com pontos de fuga.
- Deep dive em questão específica.
- Debrief de lançamento.
- Validação de qualidade de dados entre fontes (cross-check).

**Quando NÃO usar:**
- Construir pipeline ETL (chamar `bi-engineer`).
- Inteligência competitiva (chamar `pesquisador`).
- Recomendação estratégica macro (chamar `cmo` ou `estrategista-chefe`).

**Brief que ele exige:**
- Pergunta concreta a responder.
- Período de análise + fontes disponíveis.
- Métricas-alvo (ROAS, CAC, LTV, taxa de conversão por etapa).
- Benchmarks históricos para comparação.

**Output esperado:**
- Relatório em `.md` com dados → padrões → hipóteses → **recomendação concreta** (entrega sempre termina com ação sugerida).

---

### bi-engineer — Engenheiro de BI
**Departamento:** @dados · **Slash command:** `/haos:bi-engineer` · **Tools:** Read, Grep, Glob, Bash

**Quando usar:**
- Projetar/manter pipelines ETL.
- Modelar tabelas (star schema, snowflake).
- Construir dashboards.
- Automatizar relatórios.
- Integrar nova fonte de dados (API de plataforma de ads, checkout, CRM).

**Quando NÃO usar:**
- Análise interpretativa dos dados (chamar `data-analyst`).
- Tracking front-end (chamar `tracking-engineer`).
- Decisão de produto sobre métrica (chamar `product-manager`).

**Brief que ele exige:**
- Fontes a integrar + credenciais/acessos.
- Granularidade necessária + retenção.
- Casos de uso downstream (dashboard, análise, automação).
- Restrições de infra/orçamento de armazenamento.

**Output esperado:**
- Schema documentado + scripts ETL + dashboard funcional + runbook de manutenção.

---

### pesquisador — Pesquisador de Mercado e Inteligência Competitiva
**Departamento:** @dados · **Slash command:** `/haos:pesquisador` · **Tools:** Read, Grep, Glob, Bash, WebFetch

**Quando usar:**
- Análise de concorrentes (criativos, copy, oferta, posicionamento).
- Monitoramento de tendências de mercado.
- Benchmarks setoriais.
- Pesquisa de público-alvo (linguagem, dores, desejos).
- Monitoramento regulatório.
- Fase 2 do Rito V2.

**Quando NÃO usar:**
- Análise dos próprios dados internos (chamar `data-analyst`).
- Conceituação de campanha a partir da pesquisa (chamar `diretor-criativo`).

**Brief que ele exige:**
- Pergunta de pesquisa concreta.
- Concorrentes/segmento a investigar.
- Fontes elegíveis (web, redes, relatórios, comunidades).
- Profundidade vs prazo.

**Output esperado:**
- Documento em `.md` com **fonte + data + citação verificável** em toda afirmação + implicações concretas para decisão. Zero alucinação.

---

## 6. @funnel — Jornada, automação, CRM, e-mail

### funnel-architect — Arquiteto de Funis
**Departamento:** @funnel · **Slash command:** `/haos:funnel-architect` · **Tools:** Read, Grep, Glob, Bash, WebFetch, Agent

**Quando usar:**
- Desenhar jornada do cliente ponta-a-ponta (anúncio → conversão → pós-venda).
- Sistema de tags e segmentação.
- Especificação de funis perpétuos / lançamento / pós-venda / reativação.
- Handoff técnico para `automation-engineer`.
- Fase 7 do Rito V2.

**Quando NÃO usar:**
- Implementação técnica das automações (chamar `automation-engineer`).
- Copy dos e-mails do funil (chamar `email-marketer` ou `copy-specialist`).
- Decisão de oferta (chamar `cmo`).

**Brief que ele exige:**
- Tipo de funil (perpétuo, lançamento, evento, recuperação).
- Oferta principal + ascensão + downsell.
- Canais de entrada (mídia, orgânico, indicação).
- Stack atual (CRM, ESP, automação).
- Mapas de jornada existentes.

**Output esperado:**
- Diagrama em `.md` ou Mermaid: nós, condicionais, gatilhos, tags por etapa, integração com sistemas + spec técnica para automação.

---

### automation-engineer — Engenheiro de Automações
**Departamento:** @funnel · **Slash command:** `/haos:automation-engineer` · **Tools:** Read, Grep, Glob, Bash, Edit, Write, WebFetch

**Quando usar:**
- Implementar workflows em n8n / Zapier / Make.
- Webhooks e integrações entre plataformas (CRM, e-mail, mensageria, checkout).
- Debugging de fluxos quebrados.
- Aplicar padrões de resiliência e idempotência.

**Quando NÃO usar:**
- Desenhar a jornada (chamar `funnel-architect`).
- Backend de aplicação (chamar `dev-backend`).
- Sem spec técnica de funil — devolve `BLOQUEADO`.

**Brief que ele exige:**
- Spec do `funnel-architect` ou diagrama equivalente.
- Acessos/credenciais às ferramentas.
- Volume esperado + SLA.
- Casos de falha conhecidos + comportamento esperado.

**Output esperado:**
- Workflows em produção + documentação de cada nó + logs/alertas + testes de idempotência documentados.

---

### crm-specialist — Especialista em CRM e Vendas por Mensageria
**Departamento:** @funnel · **Slash command:** `/haos:crm-specialist` · **Tools:** Read, Grep, Glob, Bash, WebFetch, Agent

**Quando usar:**
- Gestão de pipeline comercial.
- Cadências de follow-up.
- Scripts de abordagem e tratamento de objeção.
- Qualificação de leads.
- Recuperação de inativos.
- Higiene da base.

**Quando NÃO usar:**
- E-mail marketing em volume (chamar `email-marketer`).
- Estratégia macro de comercial (chamar `cmo`).
- Automação técnica da cadência (chamar `automation-engineer`).

**Brief que ele exige:**
- CRM em uso + acesso.
- Definição de lead qualificado (BANT, MEDDIC, ou critério próprio).
- Histórico de conversão por etapa.
- Volume de pipeline atual.
- Scripts já validados.

**Output esperado:**
- Pipeline configurado + cadência de follow-up em tabela + scripts por objeção + playbook de recuperação + relatório de saúde da base.

---

### email-marketer — Especialista em E-mail Marketing
**Departamento:** @funnel · **Slash command:** `/haos:email-marketer` · **Tools:** Read, Grep, Glob, Bash, WebFetch, Agent

**Quando usar:**
- Sequências: welcome, nutrição, lançamento, reativação, transacional.
- Segmentação avançada.
- Testes A/B (assunto, CTA, horário).
- Auditoria de deliverability (SPF, DKIM, DMARC, BIMI).
- Limpeza de lista.

**Quando NÃO usar:**
- Mensageria 1:1 / WhatsApp comercial (chamar `crm-specialist`).
- Copy isolada fora de sequência (chamar `copy-specialist`).
- Spec da jornada do funil (chamar `funnel-architect`).

**Brief que ele exige:**
- ESP em uso + reputação atual.
- Lista (tamanho, segmentos, engajamento médio).
- Objetivo da sequência + janela.
- Oferta + CTA.
- Histórico de open/click/conversão.

**Output esperado:**
- Sequência completa em `.md`: assunto A/B + preheader + corpo + CTA + P.S. + horário sugerido + checklist de deliverability.

---

## 7. @produto — Discovery, UX, engenharia

### product-manager — Gerente de Produto Digital
**Departamento:** @produto · **Slash command:** `/haos:product-manager` · **Tools:** Read, Grep, Glob, Bash, WebFetch, Agent

**Quando usar:**
- Discovery de problema/oportunidade.
- Escrita de PRDs.
- Priorização de roadmap (RICE, MoSCoW, WSJF).
- Análise de métricas de produto (ativação, retenção, NPS).
- Planejamento de lançamento de feature/produto.

**Quando NÃO usar:**
- Estratégia macro de negócio (chamar `estrategista-chefe`).
- Pesquisa de usabilidade (chamar `ux-researcher`).
- Implementação técnica (chamar `dev-frontend`/`dev-backend`).

**Brief que ele exige:**
- Problema/oportunidade que motiva.
- Métricas atuais + métrica-alvo.
- Restrições técnicas e de tempo.
- Stakeholders e critérios de sucesso.

**Output esperado:**
- PRD em `.md`: contexto, problema, métricas, escopo, hipóteses, roadmap RICE + plano de lançamento.

---

### ux-researcher — Pesquisador de UX
**Departamento:** @produto · **Slash command:** `/haos:ux-researcher` · **Tools:** Read, Grep, Glob, Bash, WebFetch, Agent

**Quando usar:**
- Testes de usabilidade.
- Análises heurísticas (Nielsen).
- Auditorias de acessibilidade WCAG 2.1/2.2 AA.
- Mapeamento de jornada.
- Benchmarks competitivos de UX.
- Recomendações priorizadas para dev/design.

**Quando NÃO usar:**
- Pesquisa de mercado/concorrência comercial (chamar `pesquisador`).
- Decisão de roadmap de produto (chamar `product-manager`).

**Brief que ele exige:**
- Artefato a avaliar (URL, fluxo, protótipo).
- Persona/perfil de usuário-alvo.
- Hipóteses a investigar.
- Nível de profundidade (heurística rápida vs teste com usuários).

**Output esperado:**
- Relatório com achados ranqueados por severidade (crítico/alto/médio/baixo) + recomendações com endereço (dev/design) + checklist WCAG quando aplicável.

---

### dev-frontend — Desenvolvedor Frontend
**Departamento:** @produto · **Slash command:** `/haos:dev-frontend` · **Tools:** Read, Grep, Glob, Bash, Edit, Write, WebFetch

**Quando usar:**
- Construir landing pages, checkouts customizados.
- Componentes de plataforma.
- Otimização de Core Web Vitals (LCP, INP, CLS).
- Implementação de tracking (pixels, GTM, CAPI).
- Auditoria de acessibilidade no código.

**Quando NÃO usar:**
- APIs e backend (chamar `dev-backend`).
- Spec de tracking (chamar `tracking-engineer` antes de implementar).
- Design visual (chamar `designer`).

**Brief que ele exige:**
- Specs visuais + brand guidelines.
- Spec de tracking aprovado.
- Stack escolhida + restrições.
- Critérios de performance e acessibilidade.

**Output esperado:**
- Código em produção + testes + Lighthouse score + checklist WCAG AA + PR documentado.

---

### dev-backend — Desenvolvedor Backend
**Departamento:** @produto · **Slash command:** `/haos:dev-backend` · **Tools:** Read, Grep, Glob, Bash, Edit, Write, WebFetch

**Quando usar:**
- Endpoints REST/GraphQL.
- Integrações com APIs externas.
- Handlers de webhook.
- Migrações de dados.
- Otimização de performance backend.
- Hardening de segurança backend.

**Quando NÃO usar:**
- UI/Frontend (chamar `dev-frontend`).
- Workflow visual em n8n/Zapier (chamar `automation-engineer`).
- Infra de servidor/deploy (chamar `devops`).

**Brief que ele exige:**
- Requisitos funcionais + contrato de API.
- SLA esperado + volume.
- Stack + ambiente.
- Modelo de dados + regras de negócio.
- Threat model conhecido.

**Output esperado:**
- Código + testes (unit/integração) + documentação OpenAPI/contrato + checklist de segurança (OWASP top 10) + PR.

---

## 8. @seguranca — Compliance, infra/ops, segurança

### compliance-officer — Oficial de Compliance
**Departamento:** @seguranca · **Slash command:** `/haos:compliance-officer` · **Tools:** Read, Grep, Glob, Bash, WebFetch, Write

**Quando usar:**
- Revisar ads, páginas de venda, contratos, termos, e-mails antes de publicar.
- Auditorias de privacidade (LGPD/GDPR), defesa do consumidor.
- Validar políticas de plataforma (Meta, Google, TikTok ads policies).
- Material sensível: saúde, finanças, claims de resultado.
- Fase 10 do Rito V2 — junto com `qa-reviewer` (AMBOS aprovam).

**Quando NÃO usar:**
- Validação técnica de software (chamar `qa-reviewer`).
- Segurança de infraestrutura (chamar `chuck-norris` ou `devops`).

**Brief que ele exige:**
- Artefato concreto a revisar.
- Plataformas de destino + jurisdição.
- Tipo de claim (saúde, financeiro, comum).
- Histórico de bloqueios prévios.

**Output esperado:**
- Parecer formal: `APROVADO` / `AJUSTES` (lista numerada com fundamentação legal/regulatória) / `VETADO` (com risco e refação) + log para auditoria.

---

### devops — Engenheiro de Infraestrutura e Operações
**Departamento:** @seguranca · **Slash command:** `/haos:devops` · **Tools:** Read, Grep, Glob, Bash, Edit, Write

**Quando usar:**
- Deploys e rollbacks.
- Troubleshooting de produção.
- Configuração de containers, reverse proxy, CDN, WAF.
- Gestão de secrets.
- Backups e disaster recovery.
- Scaling e monitoramento.
- Resposta a incidentes de infra.
- Fase 11 do Rito V2 (deploy técnico).

**Quando NÃO usar:**
- Código de aplicação (chamar `dev-backend` ou `dev-frontend`).
- Auditoria de segurança ofensiva (chamar `chuck-norris`).
- Conformidade regulatória (chamar `compliance-officer`).

**Brief que ele exige:**
- Ambiente alvo + acessos.
- Mudança proposta + plano de rollback.
- Janela de manutenção.
- SLA e impacto esperado.

**Output esperado:**
- Mudança aplicada + log de comandos + verificação pós-deploy + atualização de runbook.

---

### chuck-norris — Guarda-Costa Digital (Audit-Only)
**Departamento:** @seguranca · **Slash command:** `/haos:chuck-norris` · **Tools:** Read, Grep, Glob, Bash, WebFetch

**Quando usar:**
- Auditoria de servidores e containers.
- Hardening (CIS, baseline).
- Vetting de skills/plugins externos antes de instalar.
- Revisão OWASP de código exposto.
- Análise de logs suspeitos.
- Gestão de WAF/firewall.
- Resposta a incidente e investigação forense.

**Quando NÃO usar:**
- Escrever código de aplicação (audit-only).
- Aplicar fix em produção (recomenda; `devops` aplica).
- Compliance regulatório (chamar `compliance-officer`).

**Brief que ele exige:**
- Alvo da auditoria (host, container, repo, skill).
- Nível de profundidade (rápida vs forense).
- Janela de execução + acessos read-only.
- Histórico de incidentes prévios.

**Output esperado:**
- Relatório com achados priorizados (crítico/alto/médio/baixo) + evidências + recomendações de fix endereçadas a `devops`/`dev-backend` + score de postura.

---

## Padrões transversais — válidos para os 29 agentes

Todos os agentes do HAOS_CC obedecem aos mesmos padrões estruturais. Conhecer estes padrões evita re-explicação a cada invocação.

### Padrão 1 — BRIEF OBRIGATÓRIO

Nenhum agente atua sem brief mínimo. Quando o usuário invoca um agente sem fornecer contexto suficiente, o agente devolve `BLOQUEADO` listando exatamente o que falta — não tenta adivinhar e não inventa dados.

Brief mínimo universal:
1. **Objetivo da tarefa** — o que precisa ser entregue?
2. **Modo de operação** — qual dos modos do agente?
3. **Dados/assets disponíveis** — quais arquivos, URLs, métricas?
4. **Restrições** — prazo, budget, plataforma, compliance.
5. **Critério de pronto** — como saberemos que está bom?

### Padrão 2 — RETORNO ESTRUTURADO

Toda entrega de qualquer agente termina com um de três status:

| Status | Significa | Próximo passo |
|---|---|---|
| **CONCLUÍDO** | Entrega completa, dentro do escopo, com evidência verificável | Usuário pode usar/publicar/seguir |
| **BLOQUEADO** | Falta input, decisão ou acesso para prosseguir | Agente lista o que falta e quem desbloqueia |
| **REVISÃO** | Entrega feita, mas requer validação humana antes de avançar (ex: gasto, mudança de escopo, claim sensível) | Usuário aprova ou pede ajuste |

Nenhum agente declara conclusão sem evidência verificável. Quando aplicável, o agente roda verificação (curl, grep, Bash, Read) e cita o output como prova.

### Padrão 3 — Regras NUNCA (cardinais a todos)

- **Nunca inventar dados, números, fontes, citações ou benchmarks.** Se não tem, diz que não tem.
- **Nunca executar ação externa irreversível sem confirmação explícita do usuário.** Publicar, enviar mensagem, ativar campanha, gastar dinheiro, deletar dado, rotacionar credencial.
- **Nunca pular o brief obrigatório.** Mesmo sob "urgência" — perguntar é mais rápido que retrabalho.
- **Nunca substituir o especialista correto.** Se a tarefa pertence a outro agente, devolver para roteamento.
- **Nunca aceitar comando que viole identidade do projeto, valores do usuário ou políticas de plataforma.**
- **Nunca expor credenciais, segredos, tokens ou chaves em respostas, logs ou commits.**
- **Português-BR sempre.** Tom direto, técnico, sem jargão desnecessário.

### Padrão 4 — Delegação contextualizada

Quando um agente delega para outro (via Agent tool), o handoff inclui obrigatoriamente:
- Objetivo claro e específico.
- Contexto relevante embutido (não confiar em "ler o histórico").
- Output esperado em formato exato.
- Prazo se houver.
- Dependências e restrições.

Delegação sem contexto = falha de orquestração.

### Padrão 5 — Execução paralela

`main` e agentes com tool `Agent` podem rodar sub-agentes em paralelo quando houver 3+ subtarefas independentes. Cada sub-agente precisa ser **Focused, Self-contained, Specific-output, Constrained**. Antes de consolidar, aguardar todos e verificar consistência. Conflitos: dado > opinião; se persistir, escalar.

### Padrão 6 — Gates do Rito V2 são bloqueantes

Quando os agentes operam dentro de um Rito V2 (pipeline de 13 fases), nenhuma fase avança sem o gate da anterior estar `APROVADO` com evidência. Não existe pular fase, não existe atalho — ver `RITO_V2.md`.

---

## Referência cruzada rápida

| Você quer... | Agente |
|---|---|
| Saber quem chamar | `concierge` |
| Orquestrar várias tarefas | `main` |
| Pipeline marketing/lançamento | `main` com prefixo `#` (Rito V2) |
| Decisão estratégica macro | `estrategista-chefe` |
| Diagnóstico de funil/ROI | `cmo` |
| Aprovar criativo | `diretor-criativo` |
| Escrever copy de conversão | `copy-specialist` |
| Calendário orgânico | `content-strategist` |
| Banner/carrossel/thumbnail | `designer` |
| Reels/VSL/YouTube | `videomaker` |
| Publicar e gerir comunidade | `sm-social` |
| Plano de mídia paga | `traffic-master` |
| Subir/otimizar campanha | `media-buyer` |
| Tracking/pixels/UTMs | `tracking-engineer` |
| Análise de performance | `data-analyst` |
| Dashboard/ETL | `bi-engineer` |
| Pesquisa de mercado/concorrência | `pesquisador` |
| Desenhar funil | `funnel-architect` |
| Automatizar workflow | `automation-engineer` |
| CRM e mensageria | `crm-specialist` |
| Sequência de e-mail | `email-marketer` |
| PRD/roadmap | `product-manager` |
| Usabilidade/WCAG | `ux-researcher` |
| LP/checkout/CWV | `dev-frontend` |
| API/webhook/integração | `dev-backend` |
| Plano e cronograma | `project-manager` |
| Aprovar antes de publicar | `qa-reviewer` |
| Compliance regulatório | `compliance-officer` |
| Deploy/infra/incidente | `devops` |
| Auditoria de segurança | `chuck-norris` |
