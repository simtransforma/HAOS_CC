# Contribuindo para o HAOS

Obrigado pelo interesse! O HAOS é um framework open-source MIT mantido por [HAU Soluções Digitais](https://hausolucoes.com.br).

## Setup local

\`\`\`bash
# Clone
git clone https://github.com/simtransforma/HAOS_CC.git
cd HAOS_CC

# Teste localmente (sem instalar via marketplace)
claude --plugin-dir ./

# Após mudanças
/reload-plugins
\`\`\`

## Tipos de contribuição

| Tipo | Onde |
|---|---|
| **Bug** | Abra uma issue com label `bug` |
| **Novo agente** | PR em `agents/{nome}.md` seguindo o padrão (frontmatter `description` + `tools` + corpo com NORTE/BRIEF/FRAMEWORK/RETORNO/NUNCA) |
| **Nova skill** | PR em `skills/{nome}/SKILL.md` (frontmatter + corpo técnico) |
| **Novo slash command** | PR em `commands/{nome}.md` (frontmatter `description` + corpo com instruções pro Claude) |
| **Tradução** | PR adaptando README/agents/skills para outro idioma |
| **Doc** | PRs em README, este CONTRIBUTING, ou docs/ |

## Padrões

### Agentes
- **PT-BR** (consistência com a squad atual)
- Frontmatter mínimo: `description` + `tools`
- Estrutura: NORTE (5-6 princípios) → BRIEF OBRIGATÓRIO → FRAMEWORK FIXO (4-6 fases) → RETORNO ESTRUTURADO → NUNCA
- 80-180 linhas (denso, não verboso)

### Commands
- Frontmatter: `description` clara (quando invocar)
- Corpo: instruções diretas pro Claude executar
- Tom: técnico, direto

### Skills
- Frontmatter: `name` + `description`
- Conteúdo técnico independente de marca/empresa específica
- Se for skill de terceiro, manter créditos upstream

## Code of Conduct

Veja [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). TL;DR: seja respeitoso, profissional, construtivo.

## Workflow

1. Fork → branch `feat/algo` ou `fix/algo`
2. Mudanças com commits descritivos
3. Teste localmente (`--plugin-dir`)
4. PR pro `main` com:
   - **Descrição** do que muda e por quê
   - **Screenshots/exemplos** se UI/UX
   - **Checklist** se for novo agente/skill/command (segue padrão? PT-BR? sem dados pessoais?)
5. Review por mantenedores

## Sanitização (obrigatório)

**Nunca commite:**
- Credenciais (`.env`, `MASTER.env`, chaves)
- Paths absolutos do seu sistema (use `\` ou `\C:\Users\gians`)
- Dados de clientes/projetos confidenciais
- Marcas/empresas específicas em agents/skills genéricos

O `.gitignore` ajuda mas é sua responsabilidade revisar antes do push.

## Dúvidas

Abra uma [discussion](https://github.com/simtransforma/HAOS_CC/discussions) ou issue com label `question`.