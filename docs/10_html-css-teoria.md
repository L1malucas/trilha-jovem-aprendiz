---
id: 10_html-css-teoria
title: "Módulo 10 — HTML & CSS"
sidebar_position: 100
---

# Módulo 10 — HTML & CSS

> **Objetivo:** entender HTML como estrutura semântica de uma página e CSS como camada de estilo
> separada dela — da estrutura básica de um documento até layout responsivo, acessibilidade e
> DevTools — e preparar o ambiente de trabalho pra começar o desafio prático diário.
> **Pré-requisitos:** Módulo 09 (Algoritmos e Lógica de Programação).
> **Tempo de referência:** bem mais que os outros módulos — este é o maior em número de tópicos,
> mas grande parte do aprendizado acontece na prática diária do desafio, não numa sessão só.
> **Prática correspondente:** [10_html-css-pratica.md](10_html-css-pratica.md)

---

## 1. Por que isso importa

Até aqui, a trilha inteira foi sobre o que acontece "por baixo": bits, circuitos, CPU, sistema
operacional, algoritmos. Este é o primeiro módulo em que o resultado do que você escreve aparece
na tela, visível, pra qualquer pessoa que abrir a página. HTML e CSS são, ao mesmo tempo, o
assunto mais simples de começar da trilha (não tem instalação de linguagem, não tem compilador —
um navegador já basta) e a porta de entrada pra tudo que vem depois: formulários que vão mandar
dado pra um banco (módulos 11/12) e páginas que vão ganhar comportamento com JavaScript
(módulo 13).

## 2. O que são HTML e CSS

**HTML** (HyperText Markup Language) é uma linguagem de **marcação**, não de programação — ela
não tem lógica, condições ou loops (isso vem só no módulo 13, com JavaScript). O que ela faz é
descrever a **estrutura** de um documento: isto é um título, isto é um parágrafo, isto é uma
lista. **CSS** (Cascading Style Sheets) descreve a **aparência** dessa estrutura: cor, tamanho,
posição, espaçamento.

## 3. HTML vs CSS

Pensa na planta de uma casa e na decoração dela como coisas independentes: a planta define onde
ficam paredes e cômodos (a estrutura); a decoração define cor da parede, tipo de piso (a
apresentação) — dá pra redecorar a casa inteira sem mover uma parede. HTML é a planta; CSS é a
decoração. Por isso ficam em arquivos separados (`.html` e `.css`): a mesma estrutura pode ganhar
aparências diferentes só trocando o CSS, sem tocar no HTML.

```css
h1 {
  color: #1a1a1a;
  font-size: 2rem;
}
```
Isso diz: "todo elemento `<h1>` da página usa essa cor e esse tamanho" — a regra mora fora do
HTML, e vale pra todos os `<h1>` de uma vez.

## 4. Como o navegador interpreta uma página

Antes de entrar em tags específicas, vale entender o caminho que uma página percorre até aparecer
na tela — isso explica, mais adiante, por que a ordem do HTML importa e por que CSS "por cima" do
HTML faz sentido:

1. O navegador lê o HTML de cima pra baixo e monta uma árvore de elementos na memória, chamada
   **DOM** (Document Object Model) — cada tag vira um "nó" da árvore.
2. Ele lê o CSS e monta outra árvore, o **CSSOM**, com as regras de estilo aplicáveis.
3. Combina as duas (**render tree**) e só então **desenha** (renderiza) o resultado na tela.

`[TENTE VOCÊ]` Se um script tenta alterar um elemento HTML que ainda nem foi lido pelo navegador
(porque está mais abaixo no arquivo), o que acontece? Resposta: o script não encontra o elemento
— por isso scripts costumam ser colocados no fim do `<body>`, depois que o HTML relevante já foi
lido e virou parte do DOM.

## 5. Preparando o ambiente

Antes de começar o desafio diário, vale montar a bancada de trabalho uma única vez, pra não
perder tempo reconfigurando todo dia.

### 6. VSCode e ferramentas do navegador

O editor recomendado é o **VSCode** (Visual Studio Code, gratuito) — baixe em
code.visualstudio.com e instale normalmente.

1. **Abra uma pasta como projeto** (não um arquivo solto): `Arquivo > Abrir Pasta`, escolha (ou
   crie) a pasta do seu desafio de 30 dias. Trabalhar por pasta, não por arquivo, é o que faz o
   VSCode entender a relação entre seus arquivos `.html`, `.css` e imagens.
2. **Instale duas extensões** (aba de extensões na barra lateral, ícone de blocos):
   - **Live Server**: abre sua página `.html` num navegador e atualiza sozinha toda vez que você
     salva.
   - **Prettier**: formata seu código automaticamente ao salvar.
3. **Use o terminal integrado** (`` Ctrl+` `` no Windows/Linux) quando precisar rodar comandos de
   Git pra fazer o commit diário.
4. **As ferramentas do navegador** (DevTools) são a outra metade do seu ambiente — voltamos a
   elas em detalhe no item 121, depois que você já conhecer o que inspecionar.

`[TENTE VOCÊ]` Instale as duas extensões, crie um arquivo `index.html` simples dentro de uma
pasta de projeto, e clique em "Go Live" (Live Server) no canto inferior direito do VSCode. O que
deve acontecer? Resposta: o navegador abre sozinho mostrando sua página, e qualquer alteração
salva no arquivo aparece automaticamente na aba aberta.

`[ATENÇÃO]` Se as imagens ou o CSS não aparecerem mesmo com os caminhos certos, o erro mais comum
é ter aberto um **arquivo** solto no VSCode em vez da **pasta** do projeto inteiro — sem a pasta
aberta como raiz, caminhos relativos (`./estilo.css`) podem não resolver do jeito esperado.

## 7. Estrutura básica de um documento HTML

Todo arquivo `.html` segue um esqueleto mínimo obrigatório, mesmo antes de qualquer conteúdo
visível:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Minha página</title>
</head>
<body>
  <!-- conteúdo visível vai aqui -->
</body>
</html>
```

### 8. DOCTYPE

A primeira linha, `<!DOCTYPE html>`, avisa o navegador "isto é HTML5, use as regras modernas de
interpretação" — sem ela, navegadores antigos caem num modo de compatibilidade com páginas dos
anos 90 (âncora: pense nisso como dizer "estamos falando o dialeto atual", evitando confusão).

### 9. html, head e body

`<html>` envolve o documento inteiro (com o atributo `lang="pt-BR"`, que ajuda leitores de tela e
tradutores automáticos a saberem o idioma). `<head>` guarda metadados que **não aparecem** na
página (título da aba, charset, links pro CSS). `<body>` guarda tudo que **é exibido**.

### 10. Meta tags

Dentro do `<head>`, `<meta charset="UTF-8">` define a codificação de caracteres (retome o módulo
03 — sem isso, acentos podem aparecer corrompidos). Outras metas comuns: `<meta name="viewport"
content="width=device-width, initial-scale=1">`, essencial pra responsividade (item 102).

### 11. Título da página

`<title>` (dentro do `<head>`) define o texto que aparece na aba do navegador e nos resultados de
busca — diferente de um `<h1>` (que é conteúdo visível dentro do `<body>`).

### 12. Comentários

`<!-- assim -->` — texto que o navegador ignora ao renderizar, útil pra deixar anotações no
código sem afetar a página.

`[TENTE VOCÊ]` Por que colocar `<meta charset="UTF-8">` bem no topo do `<head>`? Resposta: o
navegador precisa saber a codificação antes de interpretar qualquer caractere especial do resto
do documento — declarar tarde pode deixar acentos já lidos incorretamente.

## 13. Elementos HTML

Um punhado de tags cobre a maior parte de qualquer página de conteúdo:

### 14. Títulos
`<h1>` a `<h6>`, do mais importante ao menos importante — não pule níveis só pelo tamanho visual
(ver item 36, hierarquia de títulos).

### 15. Parágrafos
`<p>texto</p>` — bloco de texto corrido.

### 16. Links
`<a href="https://exemplo.com">texto do link</a>` — o `href` é obrigatório; sem ele, não é um
link navegável.

### 17. Imagens
`<img src="foto.jpg" alt="descrição da foto">` — sempre com `alt` (ver item 34).

### 18. Listas
`<ul>` (não ordenada, com `<li>` dentro) ou `<ol>` (ordenada, numerada automaticamente).

### 19. Tabelas
`<table>`, com `<tr>` (linha), `<th>` (cabeçalho de coluna) e `<td>` (célula de dado).

### 20. Formulários
`<form>` agrupa campos de entrada que serão enviados juntos — base de qualquer tela que coleta
dado do usuário (retome os módulos 11/12: é assim que dado chega num banco).

### 21. Inputs
`<input type="text">`, `type="email"`, `type="password"`, `type="checkbox"`, etc. — o `type`
muda tanto a aparência quanto a validação nativa do navegador.

### 22. Buttons
`<button>` — dispara uma ação (enviar o formulário, por padrão, se estiver dentro de um `<form>`).

### 23. Labels
`<label for="id-do-campo">texto</label>` — associa um rótulo a um campo (ver item 35,
acessibilidade em formulários).

`[TENTE VOCÊ]` Você tem um campo de e-mail num formulário de cadastro. Que `type` de `<input>`
usaria, e o que ele ganha "de graça" por causa disso? Resposta: `type="email"` — o navegador
valida automaticamente o formato (exige um `@`), sem precisar de código extra.

## 24. HTML semântico

Existe uma tag "genérica", a `<div>`, que não diz nada sobre o que está dentro dela (só marca
"aqui tem um bloco"). Dá pra montar uma página inteira só com `<div>`s, mas isso joga fora
informação que o HTML já oferece de graça: um leitor de tela sabe anunciar "você está na
navegação" ao ler uma `<nav>`, mas não tem como saber isso de uma `<div>` qualquer.

```html
<header>...</header>   <!-- é o cabeçalho da página -->
```
### 25. header
Cabeçalho da página ou de uma seção — normalmente logo, título, navegação.
### 26. nav
Bloco de navegação (menu de links).
### 27. main
O conteúdo principal da página — só um por página.
### 28. section
Um agrupamento temático de conteúdo, geralmente com seu próprio título.
### 29. article
Conteúdo independente, que faria sentido sozinho fora da página (um post de blog, uma notícia).
### 30. aside
Conteúdo relacionado mas secundário (barra lateral, nota relacionada).
### 31. footer
Rodapé da página ou de uma seção.

### 32. Div vs elementos semânticos

`[ATENÇÃO]` Usar `<div>` pra tudo é o erro mais comum aqui. O que fazer no lugar: antes de
escrever `<div>`, pergunte "esse bloco *é* alguma coisa reconhecível (cabeçalho, navegação,
rodapé)?" — se sim, use a tag semântica; `<div>` fica reservada pra agrupamentos puramente
visuais, sem significado próprio.

`[TENTE VOCÊ]` Você está montando um cabeçalho de página com um menu de links no topo. Que tag
usaria pro menu, em vez de uma `<div>` genérica? Resposta: `<nav>`.

## 33. Acessibilidade

Acessibilidade é escrever HTML que funcione também pra quem usa um leitor de tela, navega só por
teclado, ou tem alguma limitação visual/motora — não é um "extra", é parte de escrever HTML
correto.

### 34. Atributo alt
Todo `<img>` precisa de um `alt` descrevendo a imagem em texto — um leitor de tela lê esse texto
no lugar da imagem. `[ATENÇÃO]` `alt=""` vazio é válido (pra imagens puramente decorativas, sem
informação) — o erro é **omitir** o atributo, não deixá-lo vazio quando apropriado.

### 35. Labels e formulários
Todo `<input>` precisa de um `<label>` associado (via `for`/`id`) — sem isso, quem navega por
teclado ou leitor de tela não sabe o que aquele campo pede.

### 36. Hierarquia de títulos
Não pule níveis de `<h1>`-`<h6>` só pelo tamanho visual desejado — um leitor de tela usa a
hierarquia pra navegar pela estrutura da página; pular de `<h1>` pra `<h4>` quebra essa navegação.

### 37. HTML acessível
Resumo prático: use tags semânticas (item 24), sempre preencha `alt`, sempre associe `label` a
`input`, não pule níveis de título, e garanta que tudo seja alcançável via teclado (links e
botões nativos já são; `<div onclick="...">` não é, por padrão).

### 38. Introdução a ARIA
Quando HTML semântico não cobre um caso (ex: um componente customizado de interface, tipo um
menu suspenso feito na mão), atributos **ARIA** (`role`, `aria-label`, `aria-expanded`) preenchem
a lacuna, informando explicitamente pra tecnologias assistivas o que aquele elemento representa.
`[ATENÇÃO]` ARIA é o último recurso, não o primeiro — "no ARIA is better than bad ARIA": prefira
sempre a tag semântica nativa quando ela existir.

`[TENTE VOCÊ]` Por que `<div onclick="fazAlgo()">Clique aqui</div>` é pior, em acessibilidade,
que `<button onclick="fazAlgo()">Clique aqui</button>`? Resposta: `<button>` já é focável e
ativável via teclado (Tab + Enter/Espaço) nativamente; uma `<div>` não é, a menos que se adicione
ARIA e JavaScript extra pra simular esse comportamento — o botão nativo já resolve de graça.

## 39. CSS

Com a estrutura em pé, CSS entra pra definir a aparência — sempre em arquivo separado, como visto
no item 3.

### 40. Como adicionar CSS ao HTML
### 41. Inline, interno e externo

Três formas, da pior pra melhor prática:
```html
<p style="color: red;">inline — no próprio elemento, evite</p>
```
```html
<head><style>p { color: red; }</style></head>  <!-- interno — no <head>, ok pra testes rápidos -->
```
```html
<head><link rel="stylesheet" href="estilo.css"></head>  <!-- externo — o padrão recomendado -->
```
`[ATENÇÃO]` CSS inline mistura de novo estrutura e apresentação (o problema que o item 3 resolveu)
— use só em testes rápidos, nunca em código pra publicar.

### 42. Sintaxe CSS
### 43. Propriedades e valores

```css
seletor {
  propriedade: valor;
}
```
Cada regra tem um seletor (o que estilizar) e um bloco de declarações — cada declaração é um par
`propriedade: valor;`.

## 44. Seletores

Formas de escolher quais elementos uma regra CSS afeta:

### 45. Seletor de elemento
`p { }` — todo `<p>` da página.
### 46. Seletor de classe
`.destaque { }` — todo elemento com `class="destaque"`.
### 47. Seletor de ID
`#cabecalho { }` — o único elemento com `id="cabecalho"` (IDs devem ser únicos na página).
### 48. Seletores de atributo
`input[type="email"] { }` — elementos com um atributo/valor específico.
### 49. Pseudo-classes
`a:hover { }` — um estado do elemento (ver item 108, estados e interações).
### 50. Pseudo-elementos
`p::first-line { }` — uma parte específica do elemento (a primeira linha do texto, por exemplo).

`[TENTE VOCÊ]` Você quer estilizar só o primeiro item de uma lista, sem adicionar uma classe nova
nele. Que tipo de seletor resolveria isso? Resposta: uma pseudo-classe estrutural,
`li:first-child`.

## 51. Cascata

Quando duas regras CSS tentam estilizar o mesmo elemento, o CSS decide quem vence por um conjunto
de regras chamado cascata.

### 52. Especificidade
Seletores mais específicos vencem os mais genéricos:
```css
p { color: black; }                  /* genérico */
.aviso { color: red; }               /* mais específico */
#alerta-principal { color: orange; } /* ainda mais específico */
```
Ordem de força: ID > classe (e pseudo-classe/atributo) > elemento.

### 53. Herança
Algumas propriedades (como `color`, `font-family`) passam automaticamente do elemento pai pros
filhos, mesmo sem regra explícita — outras (como `border`, `padding`) não herdam por padrão.

### 54. Ordem das regras
Em empate de especificidade, a **última** regra declarada no CSS vence.

### 55. !important
`color: red !important;` força uma regra a vencer, ignorando a especificidade normal.
`[ATENÇÃO]` Não use `!important` como primeira solução pra um conflito de CSS — ele quebra a
cascata pra todo mundo que mexer nesse CSS depois, tornando difícil saber por que uma regra
"normal" não está funcionando. O que fazer no lugar: aumente a especificidade do seletor
corretamente (ex: uma classe mais específica), ou reorganize a ordem das regras.

`[TENTE VOCÊ]` Um elemento tem `class="destaque"` e existem as regras `.destaque { color: blue; }`
e `p { color: green; }`. Qual cor vence? Resposta: azul — seletor de classe é mais específico que
seletor de tag.

## 56. Cores e unidades

### 57. Unidades
### 58. px, %, em, rem
`px` é um valor absoluto (pixels fixos). `%` é relativo ao elemento pai. `em` é relativo ao
tamanho de fonte do próprio elemento (ou do pai, dependendo da propriedade) — o que faz `em`
compor de forma imprevisível em elementos aninhados. `rem` é relativo ao tamanho de fonte do
elemento raiz (`<html>`) — por isso é a unidade mais previsível pra tamanhos de texto.

### 59. vw e vh
Relativas à viewport (área visível da janela): `1vw` = 1% da largura da tela, `1vh` = 1% da
altura — úteis pra elementos que devem ocupar uma fração da tela independente do conteúdo.

### 60. Cores em hexadecimal
`#RRGGBB` — retome o módulo 03: cada par de dígitos hex é um canal (vermelho/verde/azul) de 0 a
255 (`00` a `FF`).

### 61. RGB e HSL
`rgb(255, 87, 51)` — os mesmos três canais, em decimal. `hsl(9, 100%, 60%)` — Matiz (posição na
roda de cores, 0-360°), Saturação e Luminosidade — mais intuitivo pra ajustar uma cor mantendo o
tom (ex: só escurecer, mexendo na luminosidade).

`[TENTE VOCÊ]` Por que `rem` costuma ser preferido a `em` pra definir tamanho de fonte em um
projeto grande? Resposta: `em` acumula — um elemento com `font-size: 1.2em` dentro de outro com
`font-size: 1.2em` fica maior que o esperado, compondo; `rem` sempre se baseia no elemento raiz,
sem esse efeito cascata.

## 62. Tipografia

### 63. Fontes
`font-family: 'Nome da Fonte', sans-serif;` — sempre com uma fonte de fallback genérica
(`sans-serif`, `serif`, `monospace`), caso a fonte principal não carregue.
### 64. Tamanho
`font-size` — prefira `rem` (item 58).
### 65. Peso
`font-weight: 400` (normal) a `700` (negrito), ou palavras-chave (`bold`, `normal`).
### 66. Altura de linha
`line-height` — espaço vertical entre linhas de texto; um valor muito baixo deixa o texto
"apertado" e difícil de ler.
### 67. Alinhamento de texto
`text-align: left | center | right | justify`.

## 68. Box Model

Todo elemento HTML ocupa espaço na tela em forma de caixa retangular, com camadas — igual uma
caixa de papelão.

### 69. Content
O conteúdo em si (texto, imagem).
### 70. Padding
Preenchimento entre o conteúdo e a borda.
### 71. Border
A borda da caixa.
### 72. Margin
Espaço vazio **fora** da caixa, afastando-a de outras.

```css
.card {
  width: 200px;
  padding: 16px;
  border: 1px solid #ccc;
  margin: 8px;
}
```

### 73. Box-sizing
Por padrão (`box-sizing: content-box`), `width` define só a largura do **conteúdo** — padding e
border se somam por cima. Uma caixa com `width: 200px` e `padding: 16px` de cada lado ocupa, na
prática, `200 + 16 + 16 = 232px`. Definir `box-sizing: border-box` muda essa conta: `width` passa
a incluir padding e border, então `width: 200px` continua sendo 200px totais, mesmo com padding.

`[ATENÇÃO]` É comum se surpreender com o layout "vazando" por esperar que `width` já fosse a
largura final. O que fazer no lugar: aplicar `box-sizing: border-box` globalmente logo no início
do projeto (`* { box-sizing: border-box; }`), pra que `width` sempre signifique "largura total".

### 74. Width e Height
Definem largura e altura do conteúdo (ou da caixa total, com `border-box`).

`[TENTE VOCÊ]` Uma caixa tem `width: 100px`, `padding: 10px` em cada lado, `box-sizing:
content-box` (padrão). Qual a largura total? Resposta: `100 + 10 + 10 = 120px`.

## 75. Display

A propriedade `display` define como um elemento se comporta no fluxo da página.

### 76. Block
Ocupa a largura toda disponível, sempre "empurra" o próximo elemento pra linha de baixo
(`<div>`, `<p>`, `<h1>` são block por padrão).
### 77. Inline
Ocupa só o espaço do próprio conteúdo, fica lado a lado com outros elementos inline
(`<span>`, `<a>` são inline por padrão) — não aceita `width`/`height` diretamente.
### 78. Inline-block
Comporta-se como inline (fica lado a lado) mas aceita `width`/`height`/margin vertical como
block.
### 79. None
`display: none` remove o elemento completamente do fluxo — como se ele não existisse na página
(diferente de `visibility: hidden`, que só o torna invisível mas mantém o espaço).

## 80. Posicionamento

A propriedade `position` controla como um elemento é posicionado em relação ao fluxo normal.

### 81. Static
O padrão — o elemento fica exatamente onde o fluxo normal (item 75) o colocaria.
### 82. Relative
O elemento continua ocupando seu espaço original no fluxo, mas pode ser deslocado visualmente
(`top`/`left`/etc.) em relação a essa posição original.
### 83. Absolute
O elemento sai do fluxo normal completamente e se posiciona em relação ao ancestral posicionado
mais próximo (o primeiro pai com `position` diferente de `static`) — ou à página, se nenhum
ancestral for posicionado.
### 84. Fixed
Como `absolute`, mas sempre em relação à janela do navegador — não se move mesmo com a rolagem
da página (útil pra um cabeçalho fixo no topo).
### 85. Sticky
Híbrido: comporta-se como `relative` até a rolagem atingir um ponto definido (`top: 0`, por
exemplo), aí "gruda" naquela posição como `fixed`, até o container pai sair de vista.
### 86. Z-index

Quando elementos posicionados se sobrepõem, `z-index` decide qual fica por cima (valores maiores
ficam acima de valores menores) — só funciona em elementos com `position` diferente de `static`.

`[TENTE VOCÊ]` Você quer um cabeçalho que fica sempre visível no topo da tela, mesmo rolando a
página inteira. Qual valor de `position` usaria? Resposta: `fixed`.

## 87. Flexbox

O Flexbox resolve o problema clássico de alinhar e distribuir elementos dentro de um container,
numa única dimensão (linha ou coluna).

### 88. Flex Container
`display: flex;` no elemento pai transforma os filhos diretos em "flex items".
### 89. Flex Items
Os filhos diretos de um flex container — cada um pode crescer, encolher ou manter seu tamanho
conforme as propriedades abaixo.
### 90. Flex Direction
`flex-direction: row` (padrão, horizontal) ou `column` (vertical) — define o eixo principal.
### 91. Justify Content
Alinha os itens ao longo do **eixo principal** (`center`, `space-between`, `flex-start`, etc.).
### 92. Align Items
Alinha os itens ao longo do **eixo cruzado** (perpendicular ao principal).

```css
.container {
  display: flex;
  justify-content: center; /* eixo principal */
  align-items: center;     /* eixo cruzado */
}
```

### 93. Gap
`gap: 16px;` — espaçamento entre os itens, sem precisar de margin manual em cada um.
### 94. Flex Wrap
`flex-wrap: wrap` — permite que os itens quebrem pra próxima linha quando não cabem mais, em vez
de espremer ou vazar.
### 95. Flex Grow, Shrink e Basis
`flex-grow` (quanto um item cresce pra preencher espaço extra), `flex-shrink` (quanto encolhe se
faltar espaço), `flex-basis` (tamanho inicial antes de crescer/encolher) — juntos controlam como
o espaço é distribuído entre itens de tamanhos diferentes.

`[TENTE VOCÊ]` Você quer três cartões lado a lado, centralizados na tela, com espaço uniforme
entre eles. Que combinação de propriedades usaria? Resposta:
`display: flex; justify-content: center; gap: 16px;` (ou `space-between`/`space-around`,
dependendo se quer os cartões grudados no centro ou espalhados).

## 96. CSS Grid

Onde Flexbox alinha numa dimensão, Grid organiza em **duas** ao mesmo tempo — linhas E colunas
simultaneamente, ideal pra layouts de página inteira.

### 97. Grid Container
`display: grid;` no elemento pai.
### 98. Grid Columns e Rows
`grid-template-columns: 1fr 1fr 1fr;` — três colunas de larguras iguais (`fr` = fração do espaço
disponível). `grid-template-rows` funciona da mesma forma, pra linhas.
### 99. Grid Areas
`grid-template-areas` permite nomear regiões do grid (`"cabecalho cabecalho" "menu conteudo"`) e
posicionar elementos por nome, em vez de coordenadas numéricas.
### 100. Gap
Igual ao Flexbox — espaçamento entre células do grid.
### 101. Grid Responsivo
`grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));` — cria quantas colunas de no
mínimo 200px couberem na largura disponível, ajustando sozinho conforme a tela.

`[TENTE VOCÊ]` Você tem um layout de página com cabeçalho, menu lateral e conteúdo principal —
uma estrutura bidimensional clássica. Flexbox ou Grid seria mais natural? Resposta: Grid — o
layout tem duas dimensões (linha do cabeçalho + colunas de menu/conteúdo), exatamente o que Grid
foi desenhado pra resolver.

## 102. Responsividade

Fazer a página se adaptar a telas de tamanhos diferentes (celular, tablet, desktop).

### 103. Mobile First
Estratégia de projetar o CSS base pensando primeiro no celular (tela pequena), depois usar media
queries pra **adicionar** estilos conforme a tela cresce — em vez do caminho inverso (desktop
primeiro, depois "consertar" pro celular).

### 104. Media Queries
```css
@media (min-width: 768px) {
  .container { flex-direction: row; }
}
```
Aplica um bloco de CSS só quando a condição (largura mínima da tela, nesse caso) é verdadeira.

### 105. Breakpoints
Os valores de largura escolhidos pra media queries (ex: 768px, 1024px) — geralmente escolhidos
onde o layout começa a "quebrar" visualmente, não em valores arbitrários de dispositivo
específico.

### 106. Layouts responsivos
Combinação prática de Flexbox/Grid com media queries — ex: cartões empilhados em coluna no
celular (`flex-direction: column`), lado a lado no desktop (`flex-direction: row` a partir de um
breakpoint).

### 107. Imagens responsivas
`img { max-width: 100%; height: auto; }` — impede que uma imagem "vaze" do seu container em telas
menores, mantendo a proporção.

`[ATENÇÃO]` Esquecer o `<meta name="viewport">` (item 10) é a causa mais comum de media queries
"não funcionarem" — sem ele, navegadores mobile simulam uma tela larga por padrão, e nenhum
breakpoint pra celular chega a disparar.

## 108. Estados e interações

Pseudo-classes de interação — diferentes das pseudo-classes estruturais já vistas no item 49.

### 109. Hover
`:hover` — enquanto o mouse está sobre o elemento.
### 110. Focus
`:focus` — enquanto o elemento está focado (por clique ou navegação por Tab) — importante pra
acessibilidade (item 33): nunca remova o contorno de foco (`outline: none`) sem substituir por
algo igualmente visível.
### 111. Active
`:active` — enquanto o elemento está sendo clicado/pressionado.
### 112. Transitions
`transition: background-color 0.2s ease;` — anima suavemente a mudança de uma propriedade entre
dois estados (ex: cor de fundo no hover), em vez de trocar instantaneamente.
### 113. Transform
`transform: scale(1.05);` ou `translateX(10px)` — move, escala ou rotaciona um elemento
visualmente, sem afetar o layout dos elementos ao redor (diferente de mudar `width`/`margin`).
### 114. Animations
`@keyframes` define uma sequência de estados ao longo do tempo; `animation` aplica essa sequência
a um elemento — usado pra animações mais complexas que uma transição simples de dois estados.

`[TENTE VOCÊ]` Você quer que um botão mude de cor suavemente ao passar o mouse, em vez de trocar
de cor instantaneamente. Que duas propriedades combina? Resposta: `:hover` (define a cor final) +
`transition` (define que a mudança até lá deve ser suave, não instantânea).

## 115. Organização do CSS

### 116. Reutilização de classes
Prefira classes reutilizáveis (`.botao-primario`) a repetir o mesmo bloco de estilo em vários
seletores diferentes.
### 117. Componentização visual
Pense em pedaços reutilizáveis da interface (um "cartão", um "botão") como componentes visuais
com seu próprio bloco de CSS, em vez de estilizar cada instância individualmente.
### 118. Variáveis CSS
```css
:root { --cor-primaria: #1a6fb0; }
.botao { background: var(--cor-primaria); }
```
Centraliza valores repetidos (cores, espaçamentos) num só lugar — mudar a variável muda todo
lugar que a usa.
### 119. CSS Reset
Navegadores diferentes têm estilos padrão levemente diferentes (margin de `<body>`, tamanho de
lista). Um "reset" (ex: zerar margins/paddings padrão no início do CSS) elimina essas diferenças,
garantindo um ponto de partida consistente.
### 120. Organização de arquivos
Em projetos maiores, separar CSS em arquivos por responsabilidade (base/reset, componentes,
layout) em vez de um único arquivo gigante — não obrigatório no desafio de 30 dias, mas bom
hábito pra projetos maiores.

## 121. DevTools

As ferramentas de desenvolvedor do navegador (abra com `F12` ou clique direito → "Inspecionar")
são o par perfeito do VSCode — enquanto o VSCode edita o arquivo, o DevTools mostra exatamente
como o navegador está interpretando o resultado.

### 122. Inspecionando elementos
Clique direito num elemento da página → "Inspecionar" — abre o DevTools já com aquele elemento
selecionado na árvore do DOM (item 4).
### 123. Alterando CSS pelo navegador
No painel de estilos do DevTools, dá pra editar valores CSS ao vivo, só pra testar — as mudanças
**não são salvas no arquivo**, servem só pra experimentar antes de editar o `.css` de verdade no
VSCode.
### 124. Box Model no DevTools
O painel de estilos mostra um diagrama visual do box model (item 68) do elemento selecionado, com
os valores exatos de content/padding/border/margin — útil pra depurar por que um elemento está
maior ou menor que o esperado.
### 125. Flexbox Inspector
Navegadores modernos mostram um selo "flex" ao lado de containers com `display: flex`, e um
painel visual mostrando os eixos principal/cruzado e como cada propriedade os afeta.
### 126. Grid Inspector
Da mesma forma, um selo "grid" com sobreposição visual das linhas e colunas do grid na própria
página.
### 127. Debugging de layout

`[TENTE VOCÊ]` Um elemento não está aparecendo onde você esperava. Qual o primeiro passo de
debug, antes de mudar qualquer código? Resposta: inspecionar o elemento no DevTools e checar o
Box Model — na maioria das vezes, um `margin`/`padding` inesperado (ou herdado de um reset
ausente) explica a posição errada.

## 128. Formulários

Voltando aos formulários (item 20) com mais profundidade — validação e feedback.

### 129. Validação HTML
Atributos nativos como `required`, `pattern`, `min`/`max`, `type="email"` fazem o navegador
validar o campo **antes** de enviar o formulário, sem precisar de JavaScript.
### 130. Estados de formulário
Um campo pode estar `:valid`, `:invalid`, `:focus`, `:disabled` — cada um estilizável via CSS
pra dar feedback visual imediato.
### 131. Feedback visual
Combine estado + estilo: `input:invalid { border-color: red; }` avisa visualmente um campo
preenchido incorretamente, sem esperar o envio do formulário.
### 132. Acessibilidade em formulários
Retome os itens 23 e 35: todo campo com `<label>` associado, mensagens de erro anunciadas (via
`aria-describedby` quando necessário), e navegação completa por teclado.

## 133. Performance básica

### 134. Imagens e formatos
Prefira formatos modernos e comprimidos (`.webp`) a `.png`/`.bmp` sem necessidade — imagens
pesadas são a causa mais comum de páginas lentas pra carregar.
### 135. Carregamento de fontes
Fontes customizadas (item 63) adicionam uma requisição extra antes do texto aparecer
corretamente — evite carregar mais variações de peso/estilo do que realmente usa.
### 136. CSS desnecessário
CSS não utilizado (regras que nunca se aplicam a nada na página) ainda precisa ser baixado e
processado pelo navegador — vale limpar regras órfãs periodicamente.
### 137. Organização e manutenção

`[TENTE VOCÊ]` Entre uma imagem `.png` de 2MB e a mesma imagem em `.webp` de 200KB, qual afeta
mais o tempo de carregamento da página, e por quê? Resposta: a `.png` — o navegador precisa
baixar 10x mais dados antes de conseguir exibir a imagem, atrasando o carregamento percebido da
página inteira.

## Erros comuns

Você já viu estes avisos ao longo do módulo — aqui vai só a revisão rápida:

- Usar `<div>` para tudo, perdendo o significado semântico de tags como `<nav>`/`<article>`.
- Abrir um arquivo solto no VSCode em vez da pasta do projeto — quebra caminhos relativos.
- Esquecer que padding e border se somam ao `width` no comportamento padrão do box model
  (`content-box`) — usar `border-box` evita a surpresa.
- Usar `!important` como primeira solução pra um conflito de CSS, em vez de ajustar a
  especificidade corretamente.
- Esquecer o `<meta name="viewport">` — quebra media queries em telas de celular.
- Remover `outline` do `:focus` sem substituir por algo igualmente visível, quebrando navegação
  por teclado.
- Omitir `alt` em imagens, ou usar `<div onclick>` no lugar de `<button>`, prejudicando
  acessibilidade sem necessidade.

## Conexão com os próximos módulos

| Conceito deste módulo | Reaparece em |
|---|---|
| Formulários HTML e validação | Módulos 11/12 — dados que um formulário coleta acabam salvos num banco |
| Estrutura semântica da página (DOM) | Módulo 13 — JavaScript manipula exatamente essa estrutura |
| Cores em hexadecimal | Módulo 03 — mesma base numérica (base 16) já vista lá |

## `[REFERÊNCIA]`

- [MDN — HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
- [MDN — CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
- [MDN — Acessibilidade](https://developer.mozilla.org/pt-BR/docs/Web/Accessibility)
- [Visual Studio Code — documentação oficial](https://code.visualstudio.com/docs)
- [CSS-Tricks](https://css-tricks.com/) — artigos e guias práticos de CSS.
- [Can I Use](https://caniuse.com/) — compatibilidade de propriedades CSS entre navegadores.
- [CSS Grid Garden](https://cssgridgarden.com/) e [Flexbox Froggy](https://flexboxfroggy.com/) —
  jogos interativos pra praticar Grid e Flexbox.

## Checklist de saída

- [ ] Explico a diferença entre HTML (estrutura) e CSS (apresentação), e por que ficam separados.
- [ ] Descrevo o caminho do HTML/CSS até aparecer na tela (DOM → CSSOM → render).
- [ ] Monto o esqueleto básico de um documento HTML (DOCTYPE, html, head, body, meta charset).
- [ ] Escolho a tag semântica certa para uma parte de página dada, em vez de `<div>` genérica.
- [ ] Aplico as regras básicas de acessibilidade (alt, label, hierarquia de títulos, foco visível).
- [ ] Calculo a largura total de uma caixa considerando padding/border (box model, com e sem
      `border-box`).
- [ ] Explico como a especificidade e a cascata decidem qual regra CSS vence em um conflito.
- [ ] Uso Flexbox para alinhar elementos numa dimensão, e sei quando Grid seria mais apropriado
      (duas dimensões).
- [ ] Escrevo pelo menos uma media query e explico a estratégia mobile first.
- [ ] Uso o DevTools do navegador para inspecionar e depurar um problema de layout.
