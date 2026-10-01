---
name: basedash-design
description: Sistema visual obrigatório (Basedash — "Midnight data terminal"). Use SEMPRE que criar ou editar qualquer interface visual - página de vendas, landing page, site, app, dashboard, componente, HTML/CSS/Tailwind, artifact, mockup, slide ou peça gráfica. Aplica fundo preto, tipografia Inter + serifa de display, botões brancos 6px, cards 16px sem sombra. Não use só se o usuário pedir explicitamente outro estilo ou marca.
---

# Basedash Design System — regras obrigatórias

Este sistema vale para **todo** entregável visual. Não é sugestão: siga as regras abaixo e, se o pedido do usuário conflitar com elas, avise o conflito em uma linha e siga o sistema, a menos que o usuário peça explicitamente para sair dele.

Fonte completa e detalhada: `references/DESIGN.md` (leia quando precisar de medidas de um componente). Tokens prontos: `assets/tokens.css`.

## Fluxo obrigatório
1. **Antes de escrever UI**, copie/importe `assets/tokens.css` e use só variáveis (`var(--color-*)`, `--radius-*`, `--spacing-*`). Nunca hex solto fora da paleta.
2. Monte a página com os componentes de `references/DESIGN.md` (Hero Centered Stack, Section Header, Metric Card, Testimonial, Pill Badge, botões).
3. **Antes de entregar**, rode `python .claude/skills/basedash-design/scripts/check_design.py <arquivos .html/.css>` e corrija toda violação. Reporte ao usuário o resultado.
4. Confira visualmente (screenshot) desktop e celular.

## Regras invioláveis

**Cores** (só estas; neutros sempre frios, nunca cinza quente)
- Canvas `#000000` · Card `#050607` · Texto primário `#ffffff` · Texto secundário/corpo `#b3b3b3` · Bordas/ícones `#808080` · Separadores pesados `#333333` · Faixa clara rara `#e8eaee`.
- Violeta `#9984d8` e verde `#3fcb7f`: **apenas** dados/gráficos, tags de borda e status "Live". Nunca em texto decorativo, fundo decorativo ou preenchimento de botão.
- Gradiente permitido só como atmosfera atrás do hero/divisores: roxo `rgba(163,102,255,.38) → rgba(123,78,245,.24) → rgba(82,49,184,.12) → transparent`.

**Tipografia**
- Inter 400/500/600 em todo texto funcional, com `letter-spacing: -0.03em` (use os tokens `--tracking-*`).
- Títulos h1/h2 de seção: serifa de display **48px, peso 400, line-height 1.0**, sem escalar nem mudar peso. Fonte "Alpha Lyrae" (proprietária) → use o substituto **Cormorant Garamond** (ou EB Garamond / PT Serif) com `font-feature-settings: "ss01","ss02"`. Em telas ≤ 600px pode reduzir para 36px (único desvio permitido).
- Citações de depoimento: serifa light 24px, peso 300, line-height 1.25, tracking -0.025em (Iowan Old Style → Source Serif / Lora / Palatino).
- Nunca usar Inter em título de display. Nunca texto de corpo em `#ffffff` puro: use `#b3b3b3`.
- Escala: 12 / 14 / 16 / 18 / 24 / 30 / 34 / 48.

**Formas e espaço**
- Botões e inputs: raio **6px**. Cards: raio **16px**. Badges: **999px**. Nunca trocar nem interpolar.
- Base 4px; padding de card 16–20px; gap de elementos 12px; gap entre seções 80–120px; largura máx. 1200px centralizada.
- **Zero box-shadow.** Elevação = `#000000` → `#050607` (poço rebaixado). Sem cards claros com borda dura sobre o preto.

**Botões**
- Primário: fundo `#ffffff`, texto `#000000`, Inter 500 14px, padding 12×20, sem borda/sombra. É o único objeto brilhante da tela: **uma ação primária por seção**.
- Secundário: ghost (sem fundo/borda, texto branco, sublinhado no hover) ou outlined (1px `#808080`, hover borda branca).

**Layout e imagem**
- Cabeçalhos de hero e seção sempre **centralizados**. Hero: pill badge → título serifa → subtítulo Inter 18 `#b3b3b3` (máx. 640px) → par de botões → linha de confiança.
- Sem fotografia de estilo de vida nem ilustração decorativa: o visual é produto/dashboard/screenshot escuro, avatares circulares, ícones de linha 16–20px brancos/`#808080`. Logos de terceiros em cores nativas sobre o preto.
- Tema é **somente escuro**. Não criar modo claro.

## Contradições do arquivo-fonte (decisão já tomada)
- O "Quick Reference" lista `primary action: #000000`; o texto e os componentes definem botão **branco com texto preto**. Vale: botão branco.
- Lavender é descrito como "contorno de tags/divisores" e também como "dados". Vale: pode ser **borda fina** de tag/foco e cor de série de gráfico, nunca fundo ou texto.
- Tracking: -0.03em em tudo, exceto o display 48px (0).

## Adaptação a projetos do usuário (afiliado / presell / vendas)
- Mantém-se o sistema, mas CTAs de compra seguem o botão primário branco. Para urgência, use pill badge com ponto verde "Live"/"Vagas" (verde é permitido em status), não botões coloridos.
- Prova social = Testimonial Card do sistema; garantias e bônus = Metric/Carbon Cards.
- Sites do usuário são **sempre Python** (Flask + Jinja); importe `tokens.css` em `static/`.
- Não invente preço, garantia, depoimento nem números.
