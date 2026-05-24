# Política de Segurança

## Versões suportadas

| Versão | Suporte |
|---|---|
| 0.1.x   | ✅ ativa |
| < 0.1   | ❌ sem suporte |

## Reportar vulnerabilidade

**Não abra issue pública** pra vulnerabilidades de segurança.

Envie email pra: **gian@<INTERNAL_DOMAIN_B>** com assunto `[HAOS_CC SECURITY]`.

Inclua:
- Descrição da vulnerabilidade
- Passos pra reproduzir
- Impacto potencial
- Sugestão de fix (se tiver)

### Tempo de resposta esperado

- **Acknowledgment**: até 48h
- **Triagem**: até 7 dias
- **Fix + disclosure**: depende da severidade
  - Crítico: 1-2 semanas
  - Alto: 2-4 semanas
  - Médio/Baixo: próximo release

## Escopo

Em escopo:
- Code execution via hooks/commands/agents
- Path traversal via inputs do usuário
- Exposição acidental de secrets/credenciais
- Injection (prompt injection que escape do agente)

Fora de escopo:
- Vulnerabilidades em dependências de terceiros (reporte upstream)
- Issues no próprio Claude Code (reporte à Anthropic)
- Configuração local insegura do usuário

## Boas práticas pra usuários

- **NUNCA** commite o `CLAUDE.md` se ele tiver credenciais
- Use `.env` separado pra secrets, com `.gitignore`
- Revise os comandos `/haos:*` antes de executar (são prompts pro Claude — leia o markdown)
- Mantenha o plugin atualizado: `/plugin update haos`

Obrigado por ajudar a manter o HAOS seguro.