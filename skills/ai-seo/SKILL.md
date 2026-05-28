---
name: ai-seo
description: "Use quando o usuário quiser otimizar conteúdo para buscadores de IA, ser citado por LLMs ou aparecer em respostas geradas por IA. Use também quando ele mencionar 'AI SEO', 'AEO', 'GEO', 'LLMO', 'answer engine optimization', 'generative engine optimization', 'otimização para LLM', 'AI Overviews', 'otimizar para ChatGPT', 'otimizar para Perplexity', 'citações de IA', 'visibilidade em IA', 'busca zero-click', 'como apareço nas respostas de IA', 'menções em LLM' ou 'otimizar para Claude/Gemini'. Use sempre que alguém quiser que o conteúdo seja citado pelos assistentes e buscadores de IA. Para SEO técnico e on-page tradicional, veja seo-optimizer. Para dados estruturados, veja schema."
metadata:
  version: 2.0.1
  autor: Gian Marco Menegussi Scaglianti
  marca: HAOS / HAU Soluções Digitais
---

# AI SEO (HAOS)

Você é especialista em otimização para busca por IA — a prática de tornar o conteúdo descobrível, extraível e citável por sistemas de IA como Google AI Overviews, ChatGPT, Perplexity, Claude, Gemini e Copilot. Seu objetivo é ajudar o usuário a ser citado como fonte nas respostas geradas por IA.

> **Janela 2026 (HAOS).** Estar citável por IA é uma vantagem atual. Toda página pública tem GTM `GTM-K5DPXJTV`. Para conteúdo em PT-BR no Brasil, vale tudo abaixo — só ajuste exemplos de fontes terceiras (Reddit/Quora → também comunidades BR, YouTube, portais).

## Antes de Começar

**Verifique o contexto de marketing de produto primeiro:**
Se `.agents/product-marketing.md` existir (ou `.claude/product-marketing.md`, ou o legado `product-marketing-context.md`), leia antes de perguntar.

Reúna este contexto (pergunte se não tiver):

### 1. Visibilidade Atual em IA
- Você sabe se sua marca aparece em respostas de IA hoje?
- Já checou ChatGPT, Perplexity ou Google AI Overviews para suas consultas-chave?
- Que consultas importam mais pro negócio?

### 2. Conteúdo & Domínio
- Que tipo de conteúdo você produz? (Blog, docs, comparações, páginas de produto)
- Qual sua autoridade de domínio / força de SEO tradicional?
- Você tem dados estruturados (schema markup)?

### 3. Metas
- Ser citado como fonte nas respostas de IA?
- Aparecer no Google AI Overviews para consultas específicas?
- Competir com marcas que já são citadas?
- Otimizar conteúdo existente ou criar conteúdo novo otimizado para IA?

### 4. Cenário Competitivo
- Quem são os principais concorrentes nos resultados de IA?
- Eles são citados onde você não é?

---

## Como Funciona a Busca por IA

### O Cenário

| Plataforma | Como funciona | Seleção de fontes |
|------------|---------------|-------------------|
| **Google AI Overviews** | Resume as páginas mais bem ranqueadas | Forte correlação com rankings tradicionais |
| **ChatGPT (com busca)** | Busca na web, cita fontes | Faixa mais ampla, não só top-ranqueadas |
| **Perplexity** | Sempre cita fontes com links | Favorece conteúdo autoritativo, recente, bem estruturado |
| **Gemini** | Assistente de IA do Google | Índice do Google + Knowledge Graph |
| **Copilot** | Busca de IA do Bing | Índice Bing + fontes autoritativas |
| **Claude** | Brave Search (quando ativado) | Dados de treino + resultados Brave |

Para um mergulho em como cada plataforma seleciona fontes e o que otimizar por plataforma, veja [references/platform-ranking-factors.md](references/platform-ranking-factors.md).

### Diferença-Chave do SEO Tradicional

SEO tradicional te coloca ranqueado. AI SEO te faz **citado**.

Na busca tradicional, você precisa ranquear na página 1. Na busca por IA, uma página bem estruturada pode ser citada mesmo ranqueando na página 2 ou 3 — os sistemas de IA escolhem fontes por qualidade, estrutura e relevância, não só pela posição.

**Estatísticas críticas:**
- AI Overviews aparecem em ~45% das buscas do Google
- AI Overviews reduzem cliques para sites em até 58%
- Marcas têm 6,5x mais chance de serem citadas via fontes de terceiros do que pelo próprio domínio
- Conteúdo otimizado é citado 3x mais que o não otimizado
- Estatísticas e citações elevam a visibilidade em 40%+

### Posição Oficial do Google vs. Realidade Multiplataforma

Importante ler uma vez antes de qualquer coisa.

**Posição do Google** ([guia de otimização para IA](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)):
> "As melhores práticas de SEO continuam relevantes porque nossos recursos de IA generativa na Busca são enraizados nos sistemas centrais de ranking e qualidade."

O Google diz explicitamente:
- **Nenhuma marcação ou arquivo especial é necessário** para AI Overviews ou AI Mode
- **Não fatie o conteúdo para IA** — escreva para pessoas, organize com headings e parágrafos normais
- **Não escreva conteúdo separado para IA** — isso arrisca a política de spam "scaled content abuse"
- **Conteúdo útil, confiável e centrado em pessoas** vence — mesmos padrões E-E-A-T da Busca
- **Sem relatório específico de IA no Search Console** — use métricas padrão de SEO

**Outros buscadores de IA (ChatGPT, Claude, Perplexity, Copilot) se comportam diferente:**
- Recompensam ativamente estrutura extraível — trechos, FAQs, tabelas de comparação, blocos de definição
- Leem `llms.txt`, páginas de preço estruturadas e arquivos legíveis por máquina quando presentes
- Citam fontes de terceiros (Reddit, Wikipedia, sites de avaliação) mais do que páginas top-ranqueadas

**O que isso significa:**
- Os padrões estruturais desta skill (blocos de resposta de 40-60 palavras, FAQ schema, tabelas de comparação) ajudam materialmente os **buscadores de IA não-Google**. E não prejudicam o Google — é só boa organização de conteúdo.
- Para Google AI Overviews / AI Mode: otimize para pessoas e Busca central, ponto. E-E-A-T forte, informação original, HTML semântico, indexabilidade limpa.
- Para ChatGPT/Claude/Perplexity: adicione a estrutura extraível + llms.txt + arquivos legíveis por máquina.

Na dúvida, "escreva para pessoas, organize para clareza" — satisfaz os dois lados.

### Query Fan-Out (Busca de IA do Google)

Os recursos de IA do Google não respondem só a consulta digitada — geram **consultas concorrentes relacionadas** nos bastidores e recuperam resultados de cada uma.

**Implicações:**
- Mirar uma página por palavra-chave é menos eficaz. Cubra o **cluster temático completo** para ser recuperável nas variantes do fan-out.
- Intenção de cauda longa importa menos que autoridade temática — a IA entende sinônimos e equivalência semântica.
- Uma página que responde abrangentemente um tema-pai (com sub-perguntas cobertas) é recuperada mais que páginas estreitas por consulta.

**Ação**: ao planejar conteúdo, faça brainstorm das 5-10 consultas relacionadas que a IA provavelmente vai gerar e garanta que seu conteúdo (ou seu site no todo) as cobre.

---

## Auditoria de Visibilidade em IA

Antes de otimizar, avalie sua presença atual.

### Passo 1: Cheque as Respostas de IA para suas Consultas-Chave

Teste 10-20 das suas consultas mais importantes nas plataformas:

| Consulta | Google AI Overview | ChatGPT | Perplexity | Você citado? | Concorrentes citados? |
|----------|:------------------:|:-------:|:----------:|:------------:|:---------------------:|
| [consulta 1] | Sim/Não | Sim/Não | Sim/Não | Sim/Não | [quem] |

**Tipos de consulta a testar:**
- "O que é [sua categoria de produto]?"
- "Melhor [categoria] para [caso de uso]"
- "[Sua marca] vs [concorrente]"
- "Como [problema que seu produto resolve]"
- "[Sua categoria] preço"

### Passo 2: Analise Padrões de Citação

Quando os concorrentes são citados e você não, examine: estrutura do conteúdo (mais extraível?), sinais de autoridade (mais citações, estatísticas, citações de especialistas?), frescor (atualizado mais recentemente?), schema markup, presença em terceiros (Wikipedia, Reddit, sites de avaliação).

### Passo 3: Checagem de Extratibilidade

Para cada página prioritária, verifique:

| Checagem | Passa/Falha |
|----------|-------------|
| Definição clara no primeiro parágrafo? | |
| Blocos de resposta autocontidos (funcionam sem contexto ao redor)? | |
| Estatísticas com fonte citada? | |
| Tabelas de comparação para consultas "[X] vs [Y]"? | |
| Seção de FAQ com perguntas em linguagem natural? | |
| Schema markup (FAQ, HowTo, Article, Product)? | |
| Atribuição de especialista (nome do autor, credenciais)? | |
| Atualizado recentemente (nos últimos 6 meses)? | |
| Estrutura de heading bate com padrões de consulta? | |
| Bots de IA permitidos no robots.txt? | |

### Passo 4: Checagem de Acesso de Bots de IA

Verifique se seu robots.txt permite os crawlers de IA. Cada plataforma tem seu bot, e bloqueá-lo significa que ela não pode citar você:

- **GPTBot** e **ChatGPT-User** — OpenAI (ChatGPT)
- **PerplexityBot** — Perplexity
- **ClaudeBot** e **anthropic-ai** — Anthropic (Claude)
- **Google-Extended** — Google Gemini e AI Overviews
- **Bingbot** — Microsoft Copilot (via Bing)

Procure regras `Disallow` no robots.txt mirando qualquer um desses. Se estiverem bloqueados, é uma decisão de negócio: bloquear evita treino de IA no seu conteúdo, mas também evita citação. Um meio-termo é bloquear crawlers só de treino (como o **CCBot** do Common Crawl) enquanto permite os de busca acima.

Veja [references/platform-ranking-factors.md](references/platform-ranking-factors.md) para a configuração completa de robots.txt.

---

## Estratégia de Otimização

### Os Três Pilares

```
1. Estrutura (torne extraível)
2. Autoridade (torne citável)
3. Presença (esteja onde a IA olha)
```

### Pilar 1: Estrutura — Torne o Conteúdo Extraível

A IA extrai trechos, não páginas. Toda afirmação-chave deve funcionar como frase autônoma.

**Padrões de bloco de conteúdo:**
- **Blocos de definição** para consultas "O que é X?"
- **Blocos passo a passo** para consultas "Como fazer X"
- **Tabelas de comparação** para consultas "X vs Y"
- **Blocos de prós/contras** para consultas de avaliação
- **Blocos de FAQ** para perguntas comuns
- **Blocos de estatística** com fontes citadas

Para templates detalhados de cada tipo, veja [references/content-patterns.md](references/content-patterns.md).

**Regras estruturais:**
- Comece cada seção com uma resposta direta (não enterre)
- Mantenha os trechos de resposta-chave em 40-60 palavras (ótimo para extração)
- Use headings H2/H3 que batem com a forma como as pessoas perguntam
- Tabelas batem prosa em conteúdo comparativo
- Listas numeradas batem parágrafos em conteúdo de processo
- Cada parágrafo transmite uma ideia clara

### Pilar 2: Autoridade — Torne o Conteúdo Citável

A IA prefere fontes confiáveis. Construa credibilidade.

**A pesquisa GEO de Princeton** (KDD 2024, estudada no Perplexity.ai) ranqueou 9 métodos:

| Método | Ganho de Visibilidade | Como Aplicar |
|--------|:---------------------:|--------------|
| **Citar fontes** | +40% | Referências autoritativas com links |
| **Adicionar estatísticas** | +37% | Números específicos com fontes |
| **Adicionar citações** | +30% | Citações de especialista com nome e cargo |
| **Tom autoritativo** | +25% | Escrita com expertise demonstrada |
| **Melhorar clareza** | +20% | Simplificar conceitos complexos |
| **Termos técnicos** | +18% | Terminologia do domínio |
| **Vocabulário único** | +15% | Aumentar diversidade de palavras |
| **Otimizar fluência** | +15-30% | Melhorar legibilidade e fluxo |
| ~~Keyword stuffing~~ | **-10%** | **Prejudica ativamente a visibilidade em IA** |

**Melhor combinação:** Fluência + Estatísticas = ganho máximo. Sites de baixo ranking se beneficiam ainda mais — até 115% de aumento de visibilidade com citações.

**Estatísticas e dados** (+37-40%): números específicos com fontes, pesquisa original (não resumos), datas em todas as estatísticas.

**Atribuição de especialista** (+25-30%): autores nomeados com credenciais, citações com cargo e organização, enquadramento "segundo [fonte]", bios de autor.

**Sinais de frescor**: "Última atualização: [data]" em destaque, refresh regular (trimestral no mínimo em temas competitivos), referências ao ano atual.

**Alinhamento E-E-A-T**: experiência de primeira mão demonstrada, informação específica (não genérica), fonte e metodologia transparentes, expertise clara do autor.

### Pilar 3: Presença — Esteja Onde a IA Olha

A IA não cita só seu site — cita onde você aparece.

**Fontes de terceiros importam mais que seu próprio site:**
- Menções na Wikipedia (7,8% de todas as citações do ChatGPT)
- Discussões no Reddit (1,8% das citações do ChatGPT)
- Publicações do setor e guest posts
- Sites de avaliação (BR: Reclame Aqui, Google Reviews; B2B: G2, Capterra)
- YouTube (citado com frequência pelo Google AI Overviews)
- Quora e comunidades BR

**Ações:**
- Garanta que sua página na Wikipedia (se houver) está correta e atual
- Participe autenticamente de comunidades (Reddit, grupos BR)
- Seja destaque em compilados e artigos de comparação do setor
- Mantenha perfis atualizados em plataformas de avaliação relevantes
- Crie conteúdo de YouTube para consultas de "como fazer"

### Arquivos Legíveis por Máquina para Agentes de IA

> **Posição do Google**: não exigido para AI Overviews/AI Mode.
> **Por que incluir mesmo assim**: buscadores de IA não-Google (ChatGPT, Claude, Perplexity) e agentes autônomos de compra recompensam estrutura extraível.

Agentes de IA não só respondem — estão virando compradores. Quando um agente avalia ferramentas em nome de um usuário, precisa de informação estruturada e parseável. Se seu preço está travado em página renderizada por JS ou atrás de "fale com vendas", os agentes pulam você.

Adicione ao root do site:

**`/pricing.md` ou `/pricing.txt`** — dados de preço estruturados:

```markdown
# Preços — [Nome do Produto]

## Grátis
- Preço: R$0/mês
- Limites: 100 e-mails/mês, 1 usuário
- Recursos: Templates básicos, acesso à API

## Pro
- Preço: R$X/mês (anual) | R$Y/mês (mensal)
- Limites: 10.000 e-mails/mês, 5 usuários
- Recursos: Domínios personalizados, analytics, suporte prioritário

## Enterprise
- Preço: Sob consulta — contato@exemplo.com
- Limites: Ilimitado
- Recursos: SSO, SLA, gerente de conta dedicado
```

**Por que importa agora:** agentes comparam produtos programaticamente antes de um humano visitar; preço opaco é filtrado das jornadas mediadas por IA; um markdown simples é trivialmente parseável.

**`/llms.txt`** — arquivo de contexto para sistemas de IA (ver [llmstxt.org](https://llmstxt.org)). Se não tiver um, adicione um `llms.txt` com visão rápida do que o produto faz, pra quem é, e links para páginas-chave (incluindo preço).

### Schema Markup para IA

| Tipo de Conteúdo | Schema | Por que ajuda |
|------------------|--------|---------------|
| Artigos/Posts | `Article`, `BlogPosting` | Identificação de autor, data, tópico |
| Conteúdo how-to | `HowTo` | Extração de passos |
| FAQs | `FAQPage` | Extração direta de Q&A |
| Produtos | `Product` | Preço, recursos, avaliações |
| Comparações | `ItemList` | Dados comparativos estruturados |
| Avaliações | `Review`, `AggregateRating` | Sinais de confiança |
| Organização | `Organization` | Reconhecimento de entidade |

Conteúdo com schema adequado mostra 30-40% mais visibilidade em buscadores de IA não-Google. Para implementação, use a skill **schema**.

---

## Experiências Agênticas

Além de resumir conteúdo, agentes autônomos começam a acessar sites diretamente — clicando, lendo, comparando, até comprando em nome de usuários.

**Como os agentes acessam seu site:** renderização visual, inspeção do DOM, árvore de acessibilidade.

**O que fazer:**
- **Renderize conteúdo sem ginástica pesada de JS** — se a página fica em branco até 4 frameworks carregarem, o agente vê branco
- **HTML semântico** — `<main>`, `<nav>`, `<article>`, `<button>`, hierarquia de heading, `alt` em imagens
- **Árvore de acessibilidade limpa** — todo elemento interativo rotulado; ARIA correto
- **Seletores estáveis / layouts previsíveis**
- **Preço, specs e contato visíveis** — em página pública e indexável (é onde `/pricing.md` ajuda)

**Emergente — Universal Commerce Protocol (UCP):** protocolo futuro que dará aos agentes ganchos padronizados para comércio. Acompanhe a adoção.

Para e-commerce e negócio local, o Google destaca: Merchant Center + Google Business Profile para visibilidade de produto/serviço na busca de IA.

---

## Tipos de Conteúdo Mais Citados

| Tipo | Fatia de Citação | Por que a IA cita |
|------|:----------------:|-------------------|
| **Artigos de comparação** | ~33% | Estruturado, equilibrado, alta intenção |
| **Guias definitivos** | ~15% | Abrangente, autoritativo |
| **Pesquisa/dados originais** | ~12% | Estatísticas únicas e citáveis |
| **Listas "melhores de"** | ~10% | Estrutura clara, rica em entidades |
| **Páginas de produto** | ~10% | Detalhes específicos extraíveis |
| **Guias how-to** | ~8% | Estrutura passo a passo |
| **Opinião/análise** | ~10% | Perspectiva de especialista, citável |

**Que performam mal:** posts genéricos sem estrutura, páginas de produto rasas, conteúdo gated (IA não acessa), conteúdo sem data/autor, conteúdo só em PDF.

---

## Monitorando a Visibilidade em IA

### O que Acompanhar

| Métrica | O que mede | Como checar |
|---------|------------|-------------|
| Presença em AI Overview | AI Overviews aparecem nas suas consultas? | Checagem manual ou Semrush/Ahrefs |
| Taxa de citação da marca | Frequência de citação em IA | Ferramentas de visibilidade em IA |
| Share of AI voice | Suas citações vs. concorrentes | Peec AI, Otterly, ZipTie |
| Sentimento da citação | Como a IA descreve sua marca | Revisão manual + ferramentas |
| Atribuição de fonte | Quais páginas suas são citadas | Tráfego de referência de fontes de IA |

### DIY (Sem Ferramentas)

Checagem manual mensal:
1. Pegue suas top 20 consultas
2. Rode cada uma no ChatGPT, Perplexity e Google
3. Registre: você é citado? Quem é? Qual página?
4. Log em planilha, acompanhe mês a mês

### Expectativa do Search Console

O Google é explícito: **não há relatório específico de IA no Search Console**. AI Overviews e AI Mode usam o ranking central, então os relatórios padrão (Performance, Cobertura, Core Web Vitals) seguem sendo a medida para o Google.

---

## O Que NÃO Fazer

1. **Escrever conteúdo separado "para IA"** — arrisca a política de spam "scaled content abuse"
2. **Fatiar páginas em fragmentos isca-de-IA** — use estrutura normal de parágrafo + heading
3. **Gerar em escala para manipular ranking** — conteúdo de IA é ok *se* atende às políticas
4. **Buscar menções inautênticas** — sem fabricar citações ou spammar Reddit/Wikipedia
5. **Bloquear crawlers de IA se quiser citação** — bloquear GPTBot/PerplexityBot/ClaudeBot impede citação
6. **Esconder conteúdo principal atrás de JS que não renderiza**
7. **Pular fundamentos de E-E-A-T**

---

## AI SEO por Tipo de Conteúdo

Para orientação tática em páginas de produto, blog, comparação, documentação e local/e-commerce, veja [references/content-types.md](references/content-types.md).

---

## Erros Comuns

- **Ignorar a busca por IA** — ~45% das buscas do Google já mostram AI Overviews
- **Tratar AI SEO como separado de SEO** — bom SEO tradicional é a fundação
- **Escrever para IA, não pessoas** — se parece feito pra enganar algoritmo, não converte nem é citado
- **Sem sinais de frescor** — conteúdo sem data perde
- **Gatear todo o conteúdo** — IA não acessa gated
- **Ignorar presença em terceiros** — pode render mais citação que seu próprio blog
- **Sem dados estruturados**
- **Keyword stuffing** — reduz visibilidade em IA em 10%
- **Esconder preço atrás de "fale com vendas"/JS** — adicione `/pricing.md`
- **Bloquear bots de IA**
- **Conteúdo genérico sem dados**
- **Esquecer de monitorar**

---

## Integrações de Ferramentas (Stack HAOS)

| Ferramenta | Usar para |
|------------|-----------|
| **Brave Search** | Pesquisa de consultas e fontes (API HAOS) |
| **Google Search Console** | Performance de busca, acompanhamento de consultas |
| **GA4** | Tráfego de referência de fontes de IA |
| **Semrush/Ahrefs** | AI Overview tracking, gap de conteúdo (se disponível) |

---

## Perguntas Específicas da Tarefa

1. Quais suas top 10-20 consultas mais importantes?
2. Já checou se respostas de IA existem para elas hoje?
3. Você tem dados estruturados (schema) no site?
4. Que tipos de conteúdo você publica?
5. Concorrentes são citados onde você não é?
6. Você tem página na Wikipedia ou presença em sites de avaliação?

---

## Skills Relacionadas

- **seo-optimizer**: para SEO técnico e on-page tradicional
- **schema**: para dados estruturados que ajudam a IA a entender o conteúdo
- **content-strategy**: para planejar o que criar
- **copywriting**: para conteúdo legível por humano e extraível por IA
