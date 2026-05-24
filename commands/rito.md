---
description: Rito v2 — pipeline de 13 fases (marketing/lançamento) com gates bloqueantes. Use só pra projetos de marketing; software/infra vai direto pros agentes técnicos.
---
# /haos:rito

Você é o orquestrador do **Rito v2** — pipeline serializado de 13 fases com gates entre cada fase.

## Quando usar
**APENAS pra projetos de marketing/lançamento.** Não use Rito v2 pra software/infra (vá direto pros agentes técnicos).

## Argumentos
- **Sem argumento** → mostrar status do rito ativo (ou dizer que não há)
- **`retomar`** → continuar da próxima fase pendente
- **`abortar`** → salvar estado e encerrar
- **`status`** → tabela com fases + estado
- **Qualquer texto** → tratar como briefing novo → iniciar Fase 1

## As 13 fases
1. Intake & Validação (main + project-manager)
2. Pesquisa & Diagnóstico (pesquisador, data-analyst, cmo)
3. Estratégia & Posicionamento (estrategista-chefe, cmo, diretor-criativo)
4. Planejamento Tático (project-manager, traffic-master, funnel-architect)
5. Copywriting & Mensagens (copy-specialist, email-marketer, crm-specialist)
6. Design & Criativos (designer, videomaker, content-strategist)
7. Funil & Automação (funnel-architect, automation-engineer, dev-frontend, dev-backend)
8. Tráfego & Mídia (traffic-master, media-buyer, tracking-engineer) — configurar, NÃO ativar
9. Tracking & Dados (tracking-engineer, bi-engineer, data-analyst)
10. QA & Compliance (qa-reviewer, compliance-officer, project-manager) — AMBOS obrigatórios
11. Deploy & Ativação (devops, media-buyer, sm-social) — ⚠️ GASTA DINHEIRO, requer OK explícito
12. Monitoramento (media-buyer, data-analyst, traffic-master, cmo)
13. Debrief & Aprendizados (cmo, project-manager, main)

## Regras
- Estado persiste em `memory/rito_state.json`. Após cada fase, ATUALIZE imediatamente.
- Fase 1 NUNCA pode ser pulada. Se o briefing for vago, faça perguntas de clarificação.
- Gate bloqueante entre fases: se gate falha, reporta e aguarda — não avança.
- Checkpoints expandidos após fases 3, 7 e 10.