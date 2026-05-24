---
name: hero-visual-prompt-generator
description: >
  Gera prompts premium de imagem e vídeo AI para hero sections de landing pages.
  Cria prompts visuais cinematográficos, com qualidade comercial, otimizados pra
  Nano Banana, FreePik AI, Google Veo Flow, Runway ML e Pika Labs. Suporta
  bebidas, comida, tech, cosméticos, moda, produtos lifestyle. Entrega prompts
  estruturados em inglês com versões desktop (16:9) e mobile (9:16).
---

# Hero Visual Prompt Generator

Gera prompts premium AI pra imagens e vídeos de hero section.

## Workflow

### Fase 1: Coleta de Informações

**Sempre perguntar antes de gerar:**
1. "Qual o produto/objeto principal da landing page?"
2. "Você pode compartilhar uma imagem de referência do produto?"
3. "Estamos criando pra desktop, mobile ou ambos?"
4. "Qual sentimento queremos transmitir? (premium, energético, natural, sofisticado)"

**Inputs obrigatórios:**
- Tipo de produto e imagem de referência
- Plataforma alvo (Desktop/Mobile/Ambos)
- Estilo/mood desejado
- Paleta de cores dominante (extrair da imagem ou perguntar)

### Fase 2: Geração de Prompt de Imagem

**Estrutura (sempre em inglês):**
```
Subject: [Descrição dinâmica do produto/ingrediente em ação]
Composition: [Tipo de fotografia — macro, commercial, high-speed, etc.]
Key Elements: [Elementos visuais principais — texturas, partículas, líquidos, etc.]
Environment: [Background — monochrome void, gradient, studio, etc.]
Lighting: [Iluminação dramática — backlight, rim light, golden hour, etc.]
Style & Details: [Qualidade técnica — hyper-realistic, 8K, cinematic, etc.]
Aspect Ratio: [Razão baseada na plataforma]
```

**Elementos técnicos obrigatórios:**
- Hyper-realistic, 8K resolution, Ultra-sharp focus
- Cinematic color grading, Textural detail emphasis
- Professional commercial photography style

**Aspect ratios:**
- Desktop: 16:9 ou 21:9
- Mobile: 9:16 ou 4:5

### Fase 3: Revisão e Seleção

Depois que o usuário gerar imagens e voltar com as favoritas:
1. Pedir as imagens geradas que ele mais gostou
2. Analisar composição, movimento implícito, elementos destacados
3. Usar imagens selecionadas como base pros prompts de vídeo

### Fase 4: Geração de Prompt de Vídeo

**Estrutura (sempre em inglês):**
```
Sequence: [Tipo de sequência — product assembly, reveal, explosion, etc.]
Visuals:
- Start: [Estado inicial]
- Middle: [Transição/ação principal]
- End: [Composição final]
Lighting & Camera: [Transições de luz e movimento de câmera]
Style: [Qualidade técnica — 4K, slow motion, commercial videography]
Duration: [Duração sugerida — 3-5 segundos pra hero]
Aspect Ratio: [Razão baseada na plataforma]
```

**Aspect ratios de vídeo:**
- Desktop: 16:9 (1920x1080) ou 21:9 (2560x1080)
- Mobile: 9:16 (1080x1920) ou 4:5 (1080x1350)

## Referências

- **Fórmulas por categoria:** Ver [references/image-prompt-formulas.md](references/image-prompt-formulas.md)
- **Padrões de vídeo:** Ver [references/video-prompt-formulas.md](references/video-prompt-formulas.md)
- **Técnicas de iluminação:** Ver [references/lighting-techniques.md](references/lighting-techniques.md)
- **Movimentos de câmera:** Ver [references/camera-movements.md](references/camera-movements.md)
- **Guia de aspect ratio:** Ver [references/aspect-ratios.md](references/aspect-ratios.md)
- **Style keywords:** Ver [references/style-keywords.md](references/style-keywords.md)

## Formato de Output

### Para Imagens:
```markdown
## IMAGE PROMPT - [PRODUTO] - [PLATAFORMA]

### Desktop Version (16:9)
[Prompt completo em inglês]

### Mobile Version (9:16)
[Prompt adaptado para razão vertical]

---
**Ferramenta recomendada:** Nano Banana / Midjourney / DALL-E
**Style keywords:** [lista de keywords]
**Notas técnicas:** [observações de geração]
```

### Para Vídeos:
```markdown
## VIDEO PROMPT - [PRODUTO] - [PLATAFORMA]

### Desktop Version (16:9)
[Prompt completo em inglês]

### Mobile Version (9:16)
[Prompt adaptado para razão vertical]

---
**Ferramentas compatíveis:** FreePik AI, Google Veo Flow, Runway ML, Pika Labs
**Duração sugerida:** [X segundos]
**Movimento principal:** [tipo de movimento]
**Notas de animação:** [dicas pra melhores resultados]
```

## Regras

1. **PROMPTS SEMPRE EM INGLÊS** — Por compatibilidade com as ferramentas AI (o texto da skill é PT-BR, mas o conteúdo dos prompts entregues fica em EN)
2. **SEMPRE perguntar a plataforma** — Desktop, Mobile ou Ambos antes de gerar
3. **SEMPRE pedir imagem de referência** — Pra entender o produto e extrair cores
4. **SEMPRE gerar versões duplas** — Quando o usuário escolher "Ambos"
5. **SEMPRE usar terminologia técnica** — 8K, hyper-realistic, cinematic
6. **SEMPRE descrever a iluminação** — Crucial pra qualidade premium
7. **NUNCA gerar prompts genéricos** — Cada prompt único pro produto

## Validação

Usar `scripts/prompt-validator.py` pra checar completude do prompt:
```bash
python scripts/prompt-validator.py "prompt text" --type image
python scripts/prompt-validator.py "prompt text" --type video
```
