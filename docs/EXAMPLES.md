# HAOS_CC — Cenários práticos

6 exemplos reais de uso do HAOS. Cada um mostra: **contexto**, **comando exato**, **o que esperar** e **próximos passos típicos**.

---

## 1. Diagnóstico rápido de funil

### Contexto

Você tem um e-commerce que vinha vendendo R$80k/mês estável. Nos últimos 14 dias a receita caiu 35% sem mudanças óbvias de campanha. Você quer um diagnóstico rápido antes de tomar decisão (cortar verba? mexer no produto? trocar criativo?).

### Comando

```
/haos:cmo Queda de 35% na receita nos últimos 14 dias. Contexto:
- Loja: nutricosméticos, ticket médio R$180
- Tráfego: Meta Ads (70%) + Google Shopping (20%) + orgânico (10%)
- Sem mudança de criativo, sem mudança de preço, sem alteração de checkout
- Stripe + Shopify, posso exportar qualquer dado
- Concorrente forte lançou promoção 50% off há 10 dias

Quero diagnóstico em 3 hipóteses ranqueadas por probabilidade + plano de validação 
de cada uma em menos de 48h. Modo A (diagnóstico rápido), não Rito V2.
```

### O que esperar

O CMO entra em **Modo A — Diagnóstico Rápido** (não dispara Rito V2). Resposta típica:

```
DIAGNÓSTICO (15 min de análise)

Hipótese 1 (60% prob): Cannibalização por concorrente em promoção
  - Sinal: timing bate (queda começou 4 dias após promo do concorrente)
  - Validação: rodar query "CTR Meta últimos 30d", se caiu = confirmado
  - Comando: /haos:traffic-master "puxa CTR/CPC/CPM por campanha últimos 30d"

Hipótese 2 (25% prob): Saturação de criativo
  - Sinal: 70% do tráfego em Meta + nenhum criativo novo há 21+ dias
  - Validação: frequência média > 3.5 = criativo saturado
  - Comando: /haos:tracking-engineer "frequência por adset últimos 14d"

Hipótese 3 (15% prob): Quebra silenciosa de tracking
  - Sinal: vendas reais podem estar OK, mas atribuição zerada
  - Validação: comparar receita Stripe vs receita Meta últimos 14d
  - Se gap > 20% = pixel quebrado

PLANO 48H
  Dia 1 manhã: validar H1 e H3 em paralelo
  Dia 1 tarde: se H1 confirmado → decisão de match price vs. diferenciação
  Dia 2: ação corretiva + monitoramento intensivo

Quer que eu delegue as 3 validações em paralelo agora?
```

### Próximos passos típicos

- Responder "sim, paralelo" → HAOS dispara 3 sub-agentes simultaneamente
- Em ~10 min você tem os 3 outputs consolidados
- CMO recomenda ação (provavelmente: contra-oferta + criativo novo + auditoria de pixel)
- Se decisão envolver > R$10k → CMO sugere abrir Conclave (skill mega-brain)

---

## 2. Crítica de um criativo de anúncio

### Contexto

Sua equipe criou um anúncio Meta para campanha de lead gen B2B. Antes de subir, você quer uma crítica honesta — o que pode estar falhando antes de gastar verba testando.

### Comando

```
/haos:diretor-criativo Avalia esse criativo em 10 dimensões antes de eu subir:

[IMAGEM]: foto de homem 40+ de terno olhando laptop, fundo escritório, 
sorriso confiante, overlay "+R$50k/mês"

HEADLINE: "Descubra o método que está transformando contadores em CFOs digitais"

PRIMARY TEXT:
"Você ainda fatura por hora? Enquanto isso, contadores que dominam o método CFO Digital 
faturam R$50k+/mês entregando o que o cliente realmente quer: previsibilidade financeira.

Vagas limitadas para a próxima turma. Clique e descubra se você se qualifica."

CTA: "Saiba Mais"
PÚBLICO: contadores, BR, 30-55, renda média-alta
OBJETIVO: lead pra webinar (ticket back-end R$3k)
```

### O que esperar

Crítica estruturada nas 10 dimensões padrão do `diretor-criativo`:

```
AVALIAÇÃO (score 0-10 por dimensão)

1. PROMESSA (8/10) — Clara, específica (R$50k), mas overlay numérico pode 
   trigger compliance Meta. Risco de reprovação.

2. PÚBLICO-MENSAGEM FIT (9/10) — Linguagem ressoa com dor real do contador.

3. STOPPER VISUAL (5/10) — Imagem genérica "homem de terno" — 1000+ anúncios 
   parecidos. Não para o scroll.

4. GANCHO DE COPY (7/10) — "Você ainda fatura por hora?" é forte. Mantém.

5. PROVA (3/10) — ZERO prova social. Quantos contadores? Quem? Depoimento?
   Caso real? Risco de soar "promessa vazia".

6. ESPECIFICIDADE (6/10) — "Método CFO Digital" precisa de 1 linha do que é.

7. URGÊNCIA (4/10) — "Vagas limitadas" é fraco/genérico. Quantas? Até quando?

8. CTA (4/10) — "Saiba Mais" é o CTA mais fraco do Meta. Trocar.

9. COMPLIANCE (5/10) — "R$50k/mês" sem disclaimer = risco de reprovação 
   + risco CVM se virar tema.

10. DIFERENCIAL (3/10) — Nada nesse anúncio diz por que VOCÊ e não os outros 
    50 cursos de contador-CFO. Falta posicionamento.

SCORE GERAL: 5.4/10 — NÃO recomendo subir como está

TOP 3 AJUSTES (ordem de impacto):
  1. Trocar imagem por algo específico (print de dashboard real, antes/depois 
     anonimizado, foto da turma anterior)
  2. Adicionar prova: "+127 contadores formados" ou depoimento de 1 linha
  3. CTA "Quero entrar na próxima turma" + remover overlay numérico

Quer que eu delegue ao copy-specialist pra reescrever, ou prefere ajustar você?
```

### Próximos passos típicos

- Aceitar os ajustes e delegar reescrita: `/haos:copy-specialist [colar crítica + pedir reescrita]`
- OU pedir variações A/B: `/haos:copy-specialist 5 variações aplicando os 3 ajustes do diretor`
- Depois de novo criativo: pode pedir 2ª passada pro diretor-criativo (sem score, só go/no-go)

---

## 3. Sprint técnico curto — fix de bug em React

### Contexto

Você descobriu um bug: o formulário de checkout no app React perde o estado quando o usuário troca de aba e volta. Quer um fix rápido, não um lançamento.

### Comando

```
/haos:dev-frontend Bug: formulário de checkout perde estado ao trocar de aba.

Stack: React 18, Next.js 14 (App Router), Zustand pra state, sem persist configurado
Repo: ./apps/checkout/
Componente afetado: components/CheckoutForm.tsx
Reprodução: preenche os campos → troca de aba → espera 30s → volta → campos vazios
Esperado: estado preservado por pelo menos 30 min

Investiga causa-raiz, propõe fix mínimo, implementa, roda os testes existentes.
NÃO precisa abrir Rito V2 — isso é fix técnico.
```

### O que esperar

```
INVESTIGAÇÃO

Causa-raiz identificada (3 min):
  - Zustand store em components/CheckoutForm.tsx linha 23 não tem middleware persist
  - Browser dispara cleanup de tabs inativas após ~30s em mobile
  - Estado mora só em memória → perdido no remount

FIX PROPOSTO (1 arquivo, 8 linhas)

Adicionar middleware `persist` do Zustand com storage = sessionStorage 
(preserva no tab atual, limpa ao fechar — adequado pra checkout).

Diff:
- import { create } from 'zustand'
+ import { create } from 'zustand'
+ import { persist, createJSONStorage } from 'zustand/middleware'

- export const useCheckoutStore = create<CheckoutState>((set) => ({
+ export const useCheckoutStore = create<CheckoutState>()(
+   persist(
+     (set) => ({
        ...campos...
-     }))
+     }),
+     { name: 'checkout-form', storage: createJSONStorage(() => sessionStorage) }
+   )
+ )

EXECUTADO:
  ✓ Implementado em components/CheckoutForm.tsx
  ✓ pnpm test checkout — 14/14 passing
  ✓ pnpm typecheck — sem erros
  ✓ Validado manualmente: preenchi → troquei aba 2min → voltei → estado OK

RISCOS:
  - sessionStorage tem limite ~5MB (não é problema pra form de checkout)
  - Dados sensíveis (CPF, cartão): confirma se OK persistir em sessionStorage 
    ou se prefere só campos não-sensíveis (posso filtrar com partialize)

Quer que eu commite ou prefere revisar antes?
```

### Próximos passos típicos

- Revisar diff → aprovar commit → `git commit -m "fix: persist checkout form state across tab switches"`
- Se quiser ser mais conservador: pedir versão com `partialize` excluindo dados sensíveis
- Se for crítico: rodar `/haos:qa-reviewer` pra segunda opinião antes de mergear

---

## 4. Lançamento completo de produto — uso correto do Rito V2

### Contexto

Você vai lançar um produto novo (curso digital) em 60 dias. Não é "ajustar campanha" — é construir do zero: posicionamento, copy, página, funnel, tráfego, tracking, ativação, monitoramento. Esse é o uso canônico de Rito V2.

### Comando

```
/haos:rito Lançamento: "Mindset Foundations" — curso digital de 8 semanas.

CONTEXTO:
- Marca: Mindset Co (substitua pela sua marca/empresa)
- Público: profissionais 30-50 em transição de carreira ou empreendedores early-stage
- Dor central: "sei o que fazer mas não executo / autosabotagem"
- Ticket: R$1.997 à vista ou 12x R$197
- Capacidade: 500 alunos por turma
- Meta: 300 vendas em 14 dias de cart-open (R$599k de receita)
- Orçamento mídia: R$90k (15% do faturamento meta)
- Deadline: cart-open em 60 dias (15/Set), pré-launch nos 30 dias anteriores
- Diferencial: metodologia proprietária "Espiral Cognitiva" + comunidade ativa

JÁ EXISTE:
- Marca, logo, identidade visual
- Lista de email com 12k contatos quentes
- 3 lançamentos anteriores (CR médio 1.8%, ticket médio R$1.4k)

PRECISA SER FEITO DO ZERO:
- Posicionamento da nova oferta
- Copy de página + emails + anúncios
- Página de vendas
- Funnel de captura + nurturing
- Configuração de tráfego e tracking
- Plano de ativação
```

### O que esperar

O HAOS abre o Rito V2 e **começa OBRIGATORIAMENTE pela Fase 1** (Intake & Validação):

```
RITO V2 ABERTO — Lançamento "Mindset Foundations"

═══ FASE 1/13 — INTAKE & VALIDAÇÃO ═══

Antes de avançar, preciso validar o briefing. Detectei 4 gaps:

1. SEGMENTAÇÃO DENTRO DO PÚBLICO
   "Profissionais 30-50 em transição OU empreendedores" são 2 personas distintas.
   Pergunta: é 1 oferta pra 2 públicos (risco de mensagem fraca) ou vamos 
   escolher 1 persona primária e usar a 2ª como secundária?

2. MECANISMO ÚNICO
   "Espiral Cognitiva" — preciso de 1 parágrafo do que é, pra construir 
   posicionamento. Sem isso, a oferta vira "mais um curso de mindset".

3. PROVA DOS LANÇAMENTOS ANTERIORES
   CR 1.8% + ticket R$1.4k → 3 lançamentos. Quero ver: público desses lançamentos, 
   canais que funcionaram, principais objeções captadas.

4. CAPACIDADE OPERACIONAL
   300 vendas em 14 dias = 21 vendas/dia. Time de suporte tem capacidade pra 
   onboarding desse volume? Plataforma aguenta?

Por favor responde os 4 antes de avançar pra Fase 2 (Pesquisa & Diagnóstico).
Posso prosseguir com assumptions, mas marcaria como "gap aprovado pelo usuário".
```

### Próximos passos típicos

- Você responde os 4 gaps (ou autoriza assumptions)
- HAOS valida → **gate de Fase 1 fecha** → abre Fase 2 (Pesquisa & Diagnóstico)
- Em Fase 2 dispara `pesquisador` + `data-analyst` + `cmo` em paralelo
- Após cada fase: relatório, gate, sua aprovação, próxima fase
- Fase 11 (Deploy/Ativação) **exige OK explícito** — é onde começa a gastar
- Pode pausar a qualquer momento: `abortar rito`. Retomar: `retomar rito`
- Ao final (Fase 13): debrief com aprendizados arquivados na memória

**Tempo total esperado:** 7-15 dias de calendário (dependendo da agilidade das aprovações), distribuídos entre trabalho de agente (rápido) e revisão humana (gate-dependent).

---

## 5. Pesquisa de mercado pra entrar num nicho

### Contexto

Você está avaliando entrar num nicho novo (educação financeira pra mulheres 50+). Quer competitive intelligence antes de investir tempo construindo qualquer coisa.

### Comando

```
/haos:pesquisador Pesquisa de entrada de mercado: educação financeira para mulheres 50+ no Brasil.

QUERO MAPEAR:
1. Tamanho do mercado (TAM/SAM/SOM aproximado)
2. Top 10 players (cursos, canais, influencers) — quem domina, quanto faturam, 
   modelo de negócio, posicionamento
3. Dores não atendidas (analisar reviews 1-3 estrelas, comentários YouTube, threads Reddit/X)
4. Vocabulário do público (palavras que ELAS usam — não as que o mercado usa)
5. Gaps de oferta (o que ninguém tá fazendo bem)

FONTES PERMITIDAS:
- YouTube (transcripts + comentários)
- Reddit BR + comunidades no Facebook
- Amazon BR (reviews de livros do tema)
- Google Trends últimos 24m
- Páginas de venda dos top players

FORMATO ENTREGA:
- Markdown estruturado, máx 4 páginas
- Tabela comparativa dos 10 players
- Top 5 dores priorizadas
- Recomendação: vale entrar / não vale / entrar com diferencial X

PRAZO: assíncrono, qualidade > velocidade
```

### O que esperar

O `pesquisador` ativa as skills `last30days` e relacionadas. Resposta típica em ~10-20 min de processamento:

```
PESQUISA — Educação Financeira Mulheres 50+ BR

EXEC SUMMARY (TL;DR)
Mercado em crescimento (+34% buscas YoY), mas dominado por 3 players com 
proposta genérica. Gap claro: ninguém endereça especificamente a interseção 
"viuvez/divórcio tardio + zero histórico de gestão financeira". 
Recomendação: ENTRAR com posicionamento de nicho ("Refazendo as contas aos 50+").

1. TAMANHO (estimativa)
   - TAM: ~14M mulheres BR 50+ com renda própria
   - SAM (interessadas em educação financeira): ~3.2M (23% baseado em pesquisas Anbima)
   - SOM realista ano 1 (0.1% do SAM): 3.200 alunas

2. TOP 10 PLAYERS
   [tabela com nome / canal principal / posicionamento / ticket estimado / 
    pontos fortes / pontos fracos]

3. DORES NÃO ATENDIDAS (priorizadas)
   - D1: "Meu marido sempre cuidou disso, agora estou perdida" (viuvez/divórcio)
   - D2: "Tenho vergonha de perguntar coisas básicas" (autoestima financeira)
   - D3: "Conteúdo é todo jovem demais ou empresarial demais" (gap etário)
   - D4: "Não confio em homem novo me ensinando sobre dinheiro" (afinidade)
   - D5: "Quero algo simples, não quero virar trader" (anti-complexidade)

4. VOCABULÁRIO REAL (top 20 termos com frequência)
   "começar do zero", "depois dos 50", "tarde demais", "aposentadoria pequena", 
   "filhos adultos", "casa quitada", ... 

5. GAPS DE OFERTA
   - Ninguém entrega: comunidade só de mulheres 50+ + linguagem afetiva + 
     conteúdo específico de transição de vida
   - Concorrentes diretos tentando o nicho: 2 (1 com 8k seguidores, 1 com 23k)
   - Janela de entrada: 12-18 meses antes de saturar

RECOMENDAÇÃO
Entrar. Posicionamento sugerido: "Refazendo as contas aos 50+" 
ou "Dinheiro com leveza depois dos 50". Mecanismo: micro-passos + comunidade.

PRÓXIMO PASSO sugerido
Validação rápida: rodar pesquisa de 10 entrevistas com público-alvo antes 
de investir em produto (delegar pra @ux-researcher).
```

### Próximos passos típicos

- Pedir ao `ux-researcher` o roteiro das 10 entrevistas
- Se a recomendação for "entrar": abrir `/haos:rito` pro lançamento de teste (turma piloto pequena)
- Salvar o relatório como `project_nicho_mulheres50.md` na memória — vira input pras próximas decisões

---

## 6. Auditoria de segurança antes de deploy

### Contexto

Você terminou uma feature nova (autenticação por magic link via email) e antes de deployar pra produção quer uma auditoria de segurança. Não é code review genérico — é foco em vulnerabilidades.

### Comando

```
/haos:chuck-norris Auditoria de segurança antes de deploy.

FEATURE: Autenticação por magic link
STACK: Next.js 14 (App Router), Auth.js v5, Postgres, Resend pra email
ARQUIVOS-CHAVE:
  - app/api/auth/[...nextauth]/route.ts
  - lib/auth/magic-link.ts
  - lib/email/templates/magic-link.tsx
  - middleware.ts
ESCOPO:
  - Geração e validação do token
  - Rate limiting
  - Expiração e single-use
  - Vetores de phishing/replay
  - Vazamento via referrer/logs
  - Bypass de middleware

PRECISO DE: lista de vulnerabilidades em ordem de severidade (crítica/alta/média/baixa), 
com PoC quando possível e fix sugerido. Deploy planejado pra amanhã 10h — me diz 
se POSSO deployar.
```

### O que esperar

Chuck-Norris dispara skills `security-review`, `code-review-security` e `insecure-defaults`. Resposta típica:

```
AUDITORIA DE SEGURANÇA — Magic Link Auth

VEREDITO: NÃO deployar. 2 issues CRÍTICAS, 1 ALTA. Estimativa fix: 2-4h.

═══ CRÍTICAS ═══

[CRIT-1] Token previsível
  Arquivo: lib/auth/magic-link.ts:14
  Atual: token = crypto.randomBytes(8).toString('hex')  // 64 bits
  Risco: brute-force viável em <24h com rate limit fraco
  PoC: 2^64 / (req/s) — com 100 req/s = 5.8M anos, mas com paralelismo 
       distribuído + collision birthday paradox = horas
  FIX: crypto.randomBytes(32).toString('base64url')  // 256 bits

[CRIT-2] Token não é single-use
  Arquivo: lib/auth/magic-link.ts:42
  Atual: valida expiração, NÃO marca como usado após consumo
  Risco: replay attack — atacante que intercepta o link (referrer leak, 
         email reencaminhado, log de proxy) usa quantas vezes quiser até expirar
  FIX: após validar, deletar/marcar usado=true atomicamente na mesma transação

═══ ALTA ═══

[ALTA-1] Sem rate limit no endpoint de geração
  Arquivo: app/api/auth/[...nextauth]/route.ts (POST /signin/email)
  Atual: qualquer um pode disparar quantos emails quiser pra qualquer endereço
  Risco: enumeração de usuários + spam + custo de email
  FIX: rate limit por IP (5 req/15min) + por email-destino (3 req/hora). 
       Usar @upstash/ratelimit (já no package.json).

═══ MÉDIAS ═══

[MED-1] Mensagem de erro diferenciada vaza enumeração
  Arquivo: lib/auth/magic-link.ts:67
  "Email não encontrado" vs "Link enviado" — atacante descobre quem tem conta
  FIX: resposta uniforme "Se o email existir, o link foi enviado"

[MED-2] Template de email com URL em texto-plano cru
  Arquivo: lib/email/templates/magic-link.tsx:23
  Clientes de email logam URLs em servidores intermediários
  FIX: adicionar header "X-Auto-Response-Suppress: All" + considerar 
       short-link com expiração rápida

═══ BAIXAS ═══

[LOW-1] middleware.ts não inclui Cache-Control: no-store em rotas /auth
[LOW-2] Sem CSP header restritivo na página /auth/verify

═══ CHECKLIST DE DEPLOY ═══
  □ [CRIT-1] aumentar entropia do token
  □ [CRIT-2] implementar single-use
  □ [ALTA-1] rate limit dual (IP + email)
  □ [MED-1] resposta uniforme
  □ [MED-2] header anti-cache nos emails
  □ Rodar testes de regressão
  □ Re-auditar (15 min)

Quer que eu delegue o fix pro @dev-backend? Eu faço a re-auditoria após.
```

### Próximos passos típicos

- Aprovar fix → `/haos:dev-backend [colar relatório + pedir implementação dos 3 críticos+alta]`
- Após fix: re-rodar `/haos:chuck-norris` pra validar
- Se passar: chuck-norris emite "VEREDITO: pode deployar" → daí sim deploy
- Salvar relatório em `learning_seguranca_magic_link.md` na memória pra reuso futuro

---

## Padrões que aparecem em todos os cenários

1. **Briefing claro = resposta direta.** Os 5 elementos (objetivo, contexto, formato, restrições, prazo) cortam ping-pong.
2. **HAOS sempre dá próximos passos.** Não termina com "espero ter ajudado". Termina com "quer que eu delegue X?" ou "próximo passo é Y".
3. **Modo A vs Rito V2.** Tarefa pontual = agente direto. Lançamento/campanha = Rito V2. Quando em dúvida, peça ao `main` classificar.
4. **Gates humanos preservam controle.** Tudo que gasta, publica ou deleta pede OK.
5. **Memória trabalha a seu favor.** Salve relatórios bons na memória — viram contexto pras próximas decisões.

---

**Mantido por:** HAU Soluções Digitais — veja [LICENSE](../LICENSE) pra créditos completos
**Veja também:** `USER_GUIDE.md` (manual completo)
