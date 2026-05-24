---
description: Mega-Brain — gestão de conhecimento, pipeline de 8 fases, DNA cognitivo, Conclave
---
# /haos:mb — Mega-Brain

Sistema de gestão de conhecimento e cognição do HAOS.

## Subcomandos
| Comando | Função |
|---|---|
| `mb:briefing` | Status operacional do sistema de conhecimento |
| `mb:ingest [url]` | Ingerir material (YouTube, PDF, texto) |
| `mb:scan` | Listar materiais no inbox |
| `mb:process` | Processar inbox pelo pipeline de 8 fases |
| `mb:extract-dna [pessoa]` | Extrair DNA Cognitivo (5 camadas) |
| `mb:ask [agente] [pergunta]` | Consultar agente com DNA aplicado |
| `mb:conclave [decisão]` | Conselho estratégico (Crítico + Advogado do Diabo + Sintetizador) |
| `mb:dossier [pessoa]` | Gerar dossiê completo |

## Pipeline de 8 fases
Chunking → Resolução de Entidades → Extração de Insights → Classificação → Síntese Narrativa → Compilação de Dossiê → Geração de Playbook → Indexação

## DNA Cognitivo (5 camadas)
L1 Filosofias · L2 Modelos Mentais · L3 **Heurísticas** (prioridade) · L4 Frameworks · L5 Metodologias

## Conclave (decisões de alto risco)
4 fases: Debate (paralelo) → Crítico (score 0-100) → Advogado do Diabo → Sintetizador. Se confiança < 60% → escalar pro usuário com Opção A vs B.

Interprete o input do usuário e roteie pro subcomando correto, ou execute direto se a intenção for clara.