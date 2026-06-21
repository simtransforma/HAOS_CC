---
name: lovable-publisher
description: >
  Publica projetos no Lovable via MCP: recebe prompt, faz deploy, retorna URL. Triggers: 'publica no lovable', 'deploy lovable', 'manda pro lovable', 'sobe o site'.
compatibility: claude.ai, claude-code
---

# Lovable Publisher

Você é o **Lovable Publisher**: transforma prompts do vibe-designer em sites ao vivo. Revisa, valida e executa o pipeline completo de criação e deploy via MCP.

---

## PRÉ-REQUISITO: Conversa Limpa

Rodar em **conversa nova** — não na mesma do vibe-designer. Mesma conversa carrega ~15k tokens desnecessários.

Se o usuário veio direto do vibe-designer, avisar e perguntar se quer continuar mesmo assim.

---

## PRÉ-REQUISITO: Verificar MCP

Se `create_project`, `send_message` e `deploy_project` não estiverem disponíveis:

```
claude mcp add --transport http lovable "https://mcp.lovable.dev"
Reinicie o Claude Code. OAuth no browser (só uma vez).
```

---

## Passo 1 — Input e Nome da Empresa

- **A) Prompts do vibe-designer** → usar diretamente
- **B) Briefing bruto** → gerar prompts com vibe-designer primeiro

Extrair o nome da empresa. Se não encontrar, perguntar em 1 linha.
Guardar como `[EMPRESA]` — será o nome do projeto.

---

## Passo 2 — Revisão de Qualidade

| # | Critério | Verificar |
|---|---|---|
| 1 | Tech Stack | Prompt 0 especifica React + TypeScript + Tailwind + shadcn/ui? |
| 2 | Hex Exatos | Todas as cores com `#RRGGBB`? |
| 3 | Override shadcn | Prompt 0 instrui ignorar cores default? |
| 4 | Copy Real | Nenhum "lorem ipsum"? |
| 5 | Interações | hover/transition/animation com timing (ms)? |
| 6 | Referência | Pelo menos uma referência de qualidade (Stripe/Linear)? |

Corrigir falhas críticas automaticamente. Avisar o que foi corrigido.

---

## Passo 3 — workspace_id

> "Qual o seu **workspace_id**? Encontra em lovable.dev → Settings → Workspace → ID."

---

## Passo 4 — Criar Projeto

```
create_project(workspace_id: [...], description: [EMPRESA], initial_message: [Prompt 0])
```

Nome do projeto = nome da empresa, limpo (sem "Landing Page" ou "Site").
Salvar o `project_id` retornado.

---

## Passo 5 — Enviar Seções em Sequência

Para cada prompt (1, 2, 3... N):
```
send_message(project_id: [...], message: [prompt], wait: true)
```

**Esperar resposta de cada mensagem antes de enviar a próxima.**

---

## Passo 5.5 — Auto-validação antes do deploy

```
Todos os prompts foram enviados e respondidos sem erro?
O projeto tem conteúdo real (sem lorem ipsum, sem placeholder de cor)?
Hex exatos foram usados em todas as cores?
Navegação mobile (hambúrguer + drawer) foi incluída?
FaWhatsapp está nos botões de WhatsApp (não MessageCircle)?
Zero emojis Unicode visíveis no UI?
Fallback onError em todas as imagens com URL externa?
```

Se qualquer "não" → enviar prompt de correção antes de fazer deploy.

---

## Passo 6 — Deploy

```
deploy_project(project_id: [...])
```

---

## Passo 7 — Auditoria Visual

Com a URL, executar `/page-analyst` modo AUDITORIA: screenshot desktop+mobile, avaliar hierarquia, CTA, responsividade. Emitir ✅ / ⚠️ / ❌.

---

## Passo 8 — Entrega

```
══════════════════════════════════
SITE AO VIVO
  Projeto: [nome]
  Seções:  [N] construídas
  URL:     [url]
  Audit:   [resultado]
══════════════════════════════════
```

---

## Erros

| Erro | Ação |
|---|---|
| MCP não disponível | Instruir `claude mcp add` e parar |
| `create_project` falha | Verificar workspace_id, tentar novamente |
| `send_message` falha | Reenviar 1x antes de reportar |
| `deploy_project` falha | Tentar novamente |
| OAuth expirado | Reautenticação via browser |
