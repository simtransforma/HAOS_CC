---
name: prd-brainstorm
description: Brainstorming interativo e geração estruturada de PRD para novos projetos. Use ao iniciar um novo produto, feature, MVP ou POC e precisar de um Product Requirements Document construído via discovery guiado (problem framing, JTBD, Opportunity Solution Tree, assumption mapping, pesquisa de tech stack).
---

# PRD Brainstorm Skill

## Objetivo
Conduzir um processo de brainstorming estruturado e interativo para product discovery, resultando em um PRD (Product Requirements Document) completo que serve como input para a skill `sprint-context-generator`.

## Referências Importantes
- [Técnicas de Brainstorming](./references/brainstorm-techniques.md) — OST, JTBD, Assumption Mapping
- [Template do PRD](./references/prd-template.md) — Estrutura completa do documento
- [Tech Stack Guide](./references/tech-stack-guide.md) — Matriz de decisão de tecnologias

---

## WORKFLOW DE 5 FASES

### FASE 1: Discovery Inicial

**Objetivo:** Entender o problema fundamental e o contexto do projeto.

Fazer as perguntas a seguir **uma de cada vez**, aguardando confirmação:

#### Q1: Problema
```
Qual problema você quer resolver?

Descreva a dor ou necessidade que motivou essa ideia. Seja específico:
- O que está acontecendo hoje que não funciona bem?
- Qual o impacto desse problema?
- Com que frequência ele ocorre?
```

**Após a resposta:** Resumir o problema em 1-2 frases e pedir confirmação.

#### Q2: Usuários
```
Quem são os usuários afetados por esse problema?

Considere:
- Perfil demográfico (idade, profissão, localização)
- Nível técnico
- Frequência esperada de uso
- Outros produtos que usam hoje
```

**Após a resposta:** Criar uma persona resumida e confirmar.

#### Q3: Tipo de Projeto
```
Que tipo de projeto é esse?

[ ] Novo produto — Criar algo do zero
[ ] Nova feature — Adicionar funcionalidade a produto existente
[ ] Melhoria — Otimizar algo que já existe
[ ] Migração — Reescrever/modernizar sistema legado
[ ] Prova de conceito — Validar viabilidade técnica
```

**Após a resposta:** Confirmar as implicações do tipo escolhido.

#### Q4: Ideias Iniciais
```
Quais ideias de solução você já considerou?

Mesmo ideias parciais ou vagas são úteis. Compartilhe:
- Funcionalidades imaginadas
- Referências de produtos similares
- Abordagens técnicas consideradas
```

**Após a resposta:** Listar as ideias e confirmar o entendimento.

---

### FASE 2: Brainstorming Estruturado

**Objetivo:** Aprofundar o discovery usando técnicas profissionais de product discovery.

Aplicar as 3 técnicas abaixo interativamente:

#### 2.1 Opportunity Solution Tree (OST)

```
Vamos construir uma Opportunity Tree:

1. BUSINESS OUTCOME
   Qual resultado mensurável você quer atingir?
   Ex: "Aumentar retenção em 20%" ou "Reduzir tempo de onboarding para 5min"

2. OPPORTUNITIES
   Quais problemas/necessidades de usuários, se resolvidos, levariam a esse outcome?
   (Listar 3-5 oportunidades)

3. SOLUTIONS
   Para cada oportunidade, quais soluções podemos testar?
   (2-3 soluções por oportunidade)
```

**Visualizar o resultado:**
```
                    [OUTCOME]
                        |
        ┌───────────────┼───────────────┐
        |               |               |
  [Oportunidade 1] [Oportunidade 2] [Oportunidade 3]
        |               |               |
    ┌───┴───┐       ┌───┴───┐       ┌───┴───┐
[Sol A] [Sol B]  [Sol C] [Sol D]  [Sol E] [Sol F]
```

Confirmar a árvore antes de prosseguir.

#### 2.2 Jobs To Be Done (JTBD)

```
Agora vamos identificar os "Jobs" que os usuários precisam realizar.

Complete as sentenças no formato:

"Quando [SITUAÇÃO/CONTEXTO],
 eu quero [AÇÃO/CAPACIDADE],
 para que [RESULTADO DESEJADO]."

Identifique jobs em 3 categorias:

FUNCIONAL (tarefas práticas):
- "Quando _______, eu quero _______, para que _______."

EMOCIONAL (como querem se sentir):
- "Quando _______, eu quero _______, para que _______."

SOCIAL (como querem ser percebidos):
- "Quando _______, eu quero _______, para que _______."
```

Documentar pelo menos 2 jobs por categoria.

#### 2.3 Assumption Mapping

```
Toda solução é baseada em premissas. Vamos mapeá-las:

Liste suas premissas em 3 categorias:

VALOR (o usuário quer isso?)
- Premissa 1: _______
- Premissa 2: _______

USABILIDADE (o usuário consegue usar?)
- Premissa 1: _______
- Premissa 2: _______

VIABILIDADE (conseguimos construir?)
- Premissa 1: _______
- Premissa 2: _______
```

**Priorização (matriz 2x2):**
```
              ALTO IMPACTO
                   |
    Testar    |    Testar
    Depois    |    Primeiro
              |
 BAIXA ───────┼─────────── ALTA
 INCERTEZA    |    INCERTEZA
              |
    Assumir   |    Monitorar
    OK        |    de Perto
              |
              BAIXO IMPACTO
```

Classificar cada premissa e identificar as que precisam ser testadas primeiro.

---

### FASE 3: Pesquisa de Tecnologia

**OBRIGATÓRIO: Usar WebSearch para pesquisar stacks atuais.**

```javascript
// Buscas obrigatórias:
WebSearch("[tipo de projeto] tech stack 2024 2025")
WebSearch("[framework/linguagem considerado] vs alternativas 2025")
WebSearch("[tipo de projeto] MVP best practices")
```

#### Apresentar 2 Opções Comparativas:

**OPÇÃO A: MVP Simples**
- Foco: Validação rápida, baixo custo
- Critérios: Menor curva de aprendizado, deploy rápido, pivot fácil
- Stack exemplo: [baseado na pesquisa]

**OPÇÃO B: Stack Robusta**
- Foco: Escalabilidade, longo prazo
- Critérios: Performance, manutenibilidade, ecossistema maduro
- Stack exemplo: [baseado na pesquisa]

**Tabela Comparativa:**
```
| Critério          | Opção A (MVP)    | Opção B (Robusta) |
|-------------------|------------------|-------------------|
| Time to MVP       | X semanas        | Y semanas         |
| Custo inicial     | $                | $$                |
| Escalabilidade    | Limitada         | Alta              |
| Curva aprendizado | Baixa            | Média/Alta        |
| Comunidade        | [Tamanho]        | [Tamanho]         |
```

**Recomendação:** Baseado no contexto do projeto (tipo, timeline, time), recomendar uma opção com justificativa.

Pedir confirmação do usuário sobre a stack escolhida.

---

### FASE 4: Consolidação

**Objetivo:** Criar um resumo completo antes de gerar o PRD.

```
📋 RESUMO DO PROJETO

PROBLEMA:
[Resumo do problema em 2-3 frases]

SOLUÇÃO:
[Descrição da solução proposta]

USUÁRIOS:
[Persona principal]

OUTCOME ESPERADO:
[Métrica principal de sucesso]

JOBS PRINCIPAIS:
1. [Job funcional mais importante]
2. [Job emocional mais importante]

PREMISSAS CRÍTICAS:
1. [Premissa de maior risco]
2. [Segunda premissa crítica]

TECH STACK ESCOLHIDA:
[Stack selecionada com justificativa]

ESCOPO DO MVP:
- Inclui: [features essenciais]
- Exclui: [features pra depois]
```

**Confirmação obrigatória:**
```
Esse resumo está correto e completo?
Quer ajustar algo antes de gerar o PRD final?
```

---

### FASE 5: Geração do PRD

**Após confirmação, gerar o arquivo `prd.md`.**

Usar o template em [references/prd-template.md](./references/prd-template.md).

#### Localização do Arquivo:
- Se existe pasta do projeto: `[projeto]/docs/prd.md`
- Senão: criar na raiz como `prd.md`

#### Seções Obrigatórias:
1. Metadata (projeto, versão, data, status)
2. Overview (problema, solução, objetivo)
3. Contexto (background, usuários, métricas)
4. Premissas (valor, viabilidade, riscos)
5. Escopo (in/out of scope, futuro)
6. User Stories (formato padrão + critérios)
7. Stack Técnica (escolha + alternativas)
8. Métricas de Sucesso (KPIs mensuráveis)
9. Dependências & Bloqueios
10. Timeline Estimada
11. Próximos Passos

#### Validação:
Rodar o script de validação:
```bash
node scripts/validate-prd.js prd.md
```

#### Finalização:
```
✅ PRD gerado com sucesso: [caminho do arquivo]

📌 PRÓXIMO PASSO:
Rodar /sprint-context-generator pra criar o contexto técnico do sprint.

O sprint-context-generator vai:
- Importar automaticamente informações do PRD
- Pular perguntas já respondidas
- Focar em detalhes técnicos (arquitetura, APIs, testes)
```

---

## REGRAS IMPORTANTES

### Interatividade
- **NUNCA** pular fases ou perguntas
- **SEMPRE** aguardar confirmação antes de avançar
- **SEMPRE** resumir o entendimento após cada resposta
- Se o usuário parece confuso, oferecer exemplos

### Pesquisa
- **OBRIGATÓRIO** usar WebSearch na Fase 3
- Citar fontes ao recomendar tecnologias
- Apresentar dados atuais (2024-2025)

### Qualidade do PRD
- User Stories devem seguir formato padrão
- Métricas devem ser mensuráveis (números específicos)
- Escopo deve ser claramente definido
- Tech stack deve ter justificativa

### Integração
- O PRD deve ser compatível com o sprint-context-generator
- Manter consistência de nomenclatura
- Incluir seção explícita de "Próximos Passos"

---

## EXEMPLOS DE INTERAÇÃO

### Exemplo: Início de Sessão
```
Usuário: /prd-brainstorm

Claude: 🧠 **PRD Brainstorm Iniciado**

Vou te guiar por um processo de discovery estruturado pra criar
um PRD completo. São 5 fases:

1. Discovery Inicial — Entender o problema
2. Brainstorming — Técnicas de product discovery
3. Pesquisa Técnica — Definir stack ideal
4. Consolidação — Validar entendimento
5. Geração do PRD — Documento final

Bora começar?

**FASE 1: Discovery Inicial**

Qual problema você quer resolver?

Descreva a dor ou necessidade que motivou essa ideia...
```

### Exemplo: Transição de Fase
```
Claude: Excelente! Entendi que o problema é [resumo].

Está correto? (sim/não/ajustar)

Usuário: sim

Claude: Perfeito! Próxima pergunta:

Quem são os usuários afetados por esse problema?...
```

---

## TROUBLESHOOTING

### Usuário muito vago
Oferecer exemplos concretos e perguntar qual está mais próximo da ideia.

### Usuário quer pular fases
Explicar o valor de cada fase. Se insistir, documentar no PRD que a fase foi pulada e os riscos.

### Escopo muito grande
Sugerir dividir em múltiplos PRDs ou priorizar features pro MVP.

### Alta incerteza técnica
Recomendar uma fase de spike/prova de conceito antes do desenvolvimento.

---

## CHANGELOG

- v1.0.0: Versão inicial com workflow de 5 fases
