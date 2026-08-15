---
id: 09_algoritmos-logica-teoria
title: "Módulo 09 — Algoritmos e Lógica de Programação"
sidebar_position: 90
---

# Módulo 09 — Algoritmos e Lógica de Programação

> **Objetivo:** desenvolver o raciocínio de decompor um problema em passos precisos — pseudocódigo
> antes de código — e aplicar as estruturas de controle pra resolver problemas clássicos.
> **Pré-requisitos:** Módulo 08 (Linguagens de Programação).
> **Tempo de referência:** 8 a 12 horas.
> **Prática correspondente:** [09_algoritmos-logica-pratica.md](09_algoritmos-logica-pratica.md)

---

## 1. Por que isso importa

No módulo 08 você ganhou um idioma pra dar instruções ao computador (C++). Este módulo responde à
pergunta que vem logo depois: **como pensar e resolver problemas usando programação?** — não é
sobre decorar mais sintaxe, é sobre o raciocínio que separa quem programa resolvendo problemas de
quem só copia trechos prontos sem entender por que funcionam.

Este módulo também é a base do curso de Lógica de Programação do professor Gustavo Guanabara
(recomendado como material audiovisual complementar, disponível no YouTube) e reaproveita
apostilas já disponíveis nesta pasta (`APOSTILA_2.pdf`, `lista de exercio.webp`,
`renova_exercicios.pdf`) — mas o conteúdo escrito aqui ensina por si só, sem depender de assistir
o curso antes.

## 2. O que é um algoritmo

Você já segue algoritmos todos os dias sem chamá-los assim: uma receita de cozinha (passos em
ordem até chegar no prato pronto), instruções de trajeto até a casa de alguém ("vire aqui, siga
200m, vire ali"). Um **algoritmo** é exatamente isso, formalizado: uma sequência ordenada e
precisa de passos que resolve um problema — precisa o suficiente para que qualquer pessoa (ou
qualquer computador) seguindo-a exatamente chegue ao mesmo resultado.

`[TENTE VOCÊ]` As instruções de montagem de um móvel são um algoritmo? Resposta: sim — passos
ordenados, precisos, que qualquer pessoa seguindo exatamente chega ao mesmo resultado (o móvel
montado).

## 3. Problema vs solução

Antes de programar, separe duas coisas que é fácil confundir: o **problema** (o que precisa ser
resolvido, descrito em termos do mundo real — "descobrir o maior valor de uma lista de preços") e
a **solução** (o algoritmo específico que resolve esse problema). O mesmo problema pode ter várias
soluções diferentes (percorrer a lista comparando, ou ordenar e pegar o último) — o erro comum de
quem está começando é pular direto pra uma solução sem ter certeza de que entendeu o problema.

## 4. Entrada, processamento e saída

Todo algoritmo pode ser descrito nesses três blocos: **entrada** (os dados que você recebe),
**processamento** (os passos que transformam a entrada), **saída** (o resultado produzido).
Antes de escrever qualquer passo, pergunte: o que exatamente entra, e o que exatamente precisa
sair? Essa pergunta sozinha já evita boa parte da confusão inicial.

## 5. Pensamento algorítmico

A habilidade central deste módulo não é "saber a sintaxe de uma linguagem" — é quebrar um
problema grande em passos pequenos o bastante pra que cada um seja trivial de traduzir em código.
As próximas quatro seções (6-9) são as ferramentas mentais pra fazer essa quebra.

## 6. Decomposição de problemas

Pense em organizar uma festa: é um problema grande demais pra atacar de uma vez, mas fica trivial
quando você quebra em sub-problemas menores — comida, convidados, local, decoração. **Decompor**
um problema de programação é a mesma ideia: dividir um problema grande em pedaços menores,
resolvíveis um de cada vez.

## 7. Abstração

Ao decompor "organizar a festa" em "cuidar da comida", você não precisa pensar, nesse momento, em
convidados ou decoração — **abstração** é ignorar deliberadamente os detalhes irrelevantes pro
sub-problema que você está resolvendo agora, confiando que os outros pedaços serão resolvidos em
seu próprio momento.

## 8. Identificação de padrões

Depois de resolver "encontrar o maior número de uma lista de preços", você percebe que "encontrar
o mais velho de uma lista de idades" é *o mesmo problema* com outro rótulo — **identificar
padrões** é reconhecer que um sub-problema já resolvido se repete, disfarçado, em outro contexto.

## 9. Refinamento de problemas

Um enunciado de problema raramente já vem pronto pra virar algoritmo — "ordenar os preços" ainda
deixa em aberto: ordenar do maior pro menor ou o contrário? o que fazer com preços iguais?
**Refinar** é fazer essas perguntas até o problema ficar preciso o bastante pra não sobrar
ambiguidade nenhuma.

`[ATENÇÃO]` Pular o refinamento é a causa mais comum de "implementei certo, mas não é isso que
era pra fazer" — o código funcionou, só que resolveu um problema ligeiramente diferente do que
foi pedido.

## 10. Passo a passo de uma solução

Juntando 6-9: decompor o problema, abstrair o que não importa agora, reconhecer padrões já
conhecidos, refinar até não sobrar ambiguidade — só depois disso faz sentido começar a escrever
pseudocódigo (próxima seção). Pular direto pro código sem passar por esse raciocínio é a causa
mais comum de lógica confusa que precisa ser refeita do zero.

## 11. Pseudocódigo

Pseudocódigo é escrever os passos do algoritmo em linguagem quase natural, sem se preocupar com a
sintaxe exata de C++ ou qualquer outra linguagem. A vantagem de escrever pseudocódigo primeiro é
separar dois problemas diferentes: "o que fazer" (lógica) de "como escrever isso numa linguagem
específica" (sintaxe) — assim, um erro de lógica fica visível antes mesmo de você abrir o editor
de código.

**Exemplo narrado — encontrar o maior número de uma lista, em pseudocódigo:**
```
maior ← primeiro número da lista
para cada número da lista, a partir do segundo:
    se número > maior:
        maior ← número
retorne maior
```
Repare que cada linha é uma decisão de raciocínio, não uma linha de código: "comece assumindo que
o primeiro já é o maior", "compare com cada um dos outros", "se achar algo maior, atualize sua
resposta".

`[TENTE VOCÊ]` Escreva, em pseudocódigo, os passos para verificar se um número é par. Resposta
possível: `se o resto da divisão do número por 2 for igual a 0, então é par; senão, é ímpar`.

## 12. Fluxogramas

Fluxograma é a mesma ideia do pseudocódigo, só que desenhada: símbolos padronizados conectados
por setas — retângulo pra um passo de processamento, losango pra uma decisão (com duas setas
saindo, "sim" e "não"), e um formato arredondado pra início/fim.

```
(Início) → [ler número] → <número % 2 == 0?> --sim--> [imprimir "par"] → (Fim)
                                      |
                                      não
                                      ↓
                              [imprimir "ímpar"] → (Fim)
```

## 13. Representação de algoritmos

Pseudocódigo e fluxograma representam o mesmo algoritmo de formas diferentes — pseudocódigo é
mais rápido de escrever e mais parecido com código real; fluxograma deixa o *caminho* das decisões
mais visível de relance, útil quando o algoritmo tem muitos desvios. Nenhum dos dois é "melhor" —
use o que deixar o seu raciocínio mais claro no momento.

## 14. Transformando problema em algoritmo

Fechando o bloco 2-13: pegue um problema (3), separe entrada/processamento/saída (4), decomponha-o
(6-9), represente a solução em pseudocódigo ou fluxograma (11-13) — só então parta pro código. As
próximas seções (15 em diante) são os blocos de construção que preenchem esse pseudocódigo.

## 15. Sequência

A estrutura de controle mais simples: passos executados em ordem, um depois do outro — como os
passos numerados de uma receita. Todo algoritmo é, no mínimo, uma sequência; decisão e repetição
(a seguir) são o que dão a ele a capacidade de reagir a dados diferentes.

## 16. Decisão

Um caminho ou outro, dependendo de uma condição — "se está chovendo, leve guarda-chuva" (a mesma
lógica condicional formalizada como porta lógica no módulo 04, e como `if`/`else` no módulo 08).

### 18. Operadores relacionais

Comparam dois valores: `==` (igual), `!=` (diferente), `>`, `<`, `>=`, `<=`. O resultado de uma
comparação é sempre um booleano (verdadeiro/falso) — é isso que uma decisão avalia.

### 19. Operadores lógicos

Combinam condições booleanas: `&&` (E — as duas precisam ser verdadeiras), `||` (OU — uma já
basta), `!` (NÃO — inverte). Já vistos como portas lógicas no módulo 04 — aqui é a mesma álgebra
booleana, aplicada dentro de um `if`.

### 20. Condições compostas

Juntar operadores relacionais com operadores lógicos numa única condição: `idade >= 18 && idade
<= 65`. `[ATENÇÃO]` erro comum: escrever `18 <= idade <= 65` (não funciona como em matemática — a
maioria das linguagens avalia da esquerda pra direita, produzindo um resultado incorreto sem
avisar).

### 21. Condições aninhadas

Um `if` dentro de outro `if` — usado quando a segunda decisão só faz sentido depois que a primeira
já foi confirmada. `[TENTE VOCÊ]` Classifique um número em "negativo", "zero" ou "positivo, par"
/"positivo, ímpar" — precisa de uma decisão aninhada? Resposta: sim — primeiro decide o sinal,
depois (só se for positivo) decide par/ímpar.

## 17. Repetição

Repetir um passo várias vezes, até uma condição parar de valer — "bata o ovo até a massa ficar
homogênea" (`for`/`while`, já vistos no módulo 08).

### 22. Repetição com contador

Quando você já sabe, de antemão, quantas vezes repetir (`for i de 1 até 10`) — o caso clássico de
`for`.

### 23. Repetição com condição

Quando você não sabe quantas vezes de antemão, só sabe a condição de parada (`enquanto o usuário
não digitar "fim"`) — o caso clássico de `while`.

### 24. Acumuladores

Uma variável que vai somando (ou multiplicando) um valor a cada repetição, guardando um total —
ex: somar todos os números de uma lista, `soma ← soma + numero_atual` dentro do laço.

### 25. Contadores

Parecido com acumulador, mas conta *quantas vezes* algo aconteceu, não o valor em si — ex:
`quantidade_pares ← quantidade_pares + 1` toda vez que um número par aparece.

### 26. Validação de entrada

Repetir *pedindo* um valor até que ele seja válido — ex: `enquanto idade < 0: leia idade de
novo`. Conecta com o módulo 08 (por que confiar cegamente numa entrada do usuário é arriscado).

### 27. Loops aninhados

Um laço de repetição dentro de outro — usado pra percorrer estruturas de duas dimensões (linhas e
colunas de uma matriz, por exemplo, visto na seção 32). `[ATENÇÃO]` cada volta do laço externo
executa o laço interno inteiro de novo — um erro comum é subestimar quantas repetições totais
isso gera (laço externo de 10 × laço interno de 10 = 100 repetições, não 20).

**Exemplo narrado — verificar se um número é primo (juntando sequência, decisão e repetição):**
um número é primo se só é divisível por 1 e por ele mesmo. O algoritmo: (sequência) leia o número;
(repetição) teste, um por um, se ele é divisível por cada número de 2 até ele menos 1; (decisão)
se algum desses testes for divisível sem resto, ele não é primo — pode parar de testar e responder
"não"; se nenhum for, ele é primo. Repare como as três estruturas trabalham juntas: a repetição
fornece os candidatos a divisor, a decisão avalia cada um, e assim que a decisão encontra um
divisor, o algoritmo já pode parar (não precisa testar os que sobraram).

## 28. Variáveis em algoritmos

Um "espaço nomeado" que guarda um valor durante a execução do algoritmo — já visto em profundidade
no módulo 08 ("gavetas nomeadas na memória"); aqui, o foco é em como nomear variáveis de forma que
o próprio nome já explique o pseudocódigo (`maior`, `soma`, `encontrado` — não `x`, `y`, `z`).

## 29. Tipos de dados

Já cobertos em detalhe no módulo 08 (inteiros, decimais, caracteres, booleanos) — aqui, o que
importa pro raciocínio algorítmico é escolher o tipo certo pro que a variável representa (um
contador é inteiro; uma média é decimal; "encontrado ou não" é booleano, não um inteiro 0/1
disfarçado).

## 30. Entrada e saída

Já visto na seção 4 em termos gerais — aqui, na prática: ler um valor do usuário (`leia numero`
em pseudocódigo, `std::cin` em C++) e mostrar um resultado (`escreva resultado`, `std::cout`).

## 31. Arrays

Uma coleção de valores do mesmo tipo, guardados em sequência, acessados por posição (índice) —
`lista[0]` é o primeiro elemento (índices começam em 0). `[ATENÇÃO]` tentar acessar
`lista[tamanho]` é um erro clássico: o último índice válido é `tamanho - 1`.

## 32. Matrizes

Um array de duas dimensões — linhas e colunas, acessado por dois índices (`matriz[linha][coluna]`).
Percorrer uma matriz inteira normalmente usa loops aninhados (seção 27): um `for` pra linha, outro
`for` dentro dele pra coluna.

## 33. Strings

Uma sequência de caracteres — em muitas linguagens (incluindo C++, com `std::string`), pode ser
tratada como um array de caracteres: `texto[0]` é o primeiro caractere. Percorrer uma string
caractere a caractere usa a mesma lógica de percorrer um array.

## 34. Funções

Um bloco de algoritmo nomeado, que pode ser chamado várias vezes sem reescrever os passos — âncora
já vista no módulo 08.

### 35. Parâmetros

Os valores que uma função recebe de fora, declarados na definição (`funcao maior(a, b)`) — `a` e
`b` são os parâmetros.

### 36. Retorno

O valor que a função devolve pra quem a chamou (`retorne maior`). Uma função sem retorno só
executa passos, sem produzir um valor de volta.

### 37. Escopo

Onde uma variável "existe" e pode ser usada — uma variável criada dentro de uma função geralmente
só existe ali dentro (escopo local); uma variável fora de qualquer função pode ser acessível de
vários lugares (escopo global). `[ATENÇÃO]` depender demais de variáveis globais dificulta saber
quem alterou o quê — prefira passar valores como parâmetro.

### 38. Recursão

Uma função que chama a si mesma, resolvendo um problema em termos de uma versão menor dele mesmo,
até chegar num caso base que não precisa mais chamar a função. **Exemplo narrado — fatorial:**
`fatorial(n) = n × fatorial(n-1)`, com caso base `fatorial(0) = 1`. `fatorial(3)` chama
`fatorial(2)`, que chama `fatorial(1)`, que chama `fatorial(0)` (caso base, para de chamar) — e aí
as respostas "sobem" multiplicando: `1 → 1×1=1 → 2×1=2 → 3×2=6`.

`[TENTE VOCÊ]` Qual é o caso base de uma função recursiva que soma os números de 1 até N? Resposta:
`soma(1) = 1` (ou `soma(0) = 0`) — o ponto onde a função para de chamar a si mesma.

## 39. Rastreamento de algoritmos

Antes de rodar um algoritmo no computador, dá pra "rodar" ele na cabeça (ou no papel), anotando o
que cada variável vale a cada passo — é assim que você encontra um erro de lógica sem precisar
compilar nada.

### 40. Table Trace

A técnica formal de rastreamento: uma tabela com uma coluna por variável, uma linha por passo do
algoritmo, preenchida manualmente conforme você segue o pseudocódigo.

### 41. Dry Run

O nome mais comum (em inglês) pra "rodar a seco" — executar o algoritmo na cabeça, com uma entrada
de exemplo, sem rodar código de verdade.

### 42. Identificação de erros lógicos

Um erro lógico não impede o programa de compilar ou rodar — ele só produz o resultado errado. O
table trace é a ferramenta certa pra achar esse tipo de erro, porque expõe o valor de cada
variável passo a passo, em vez de só o resultado final.

### 43. Debugging de algoritmos

**Exemplo narrado:** um algoritmo pra somar os números de 1 a 5 devolveu 10 em vez de 15. Table
trace: `soma ← 0`; laço `i` de 1 a 5, `soma ← soma + i`. Rastreando: `i=1, soma=1`; `i=2, soma=3`;
`i=3, soma=6`; `i=4, soma=10`... e o laço para aqui — o erro estava na condição do laço, que
terminava em `i < 5` em vez de `i <= 5`, pulando o último passo.

## 44. Busca linear

Percorrer uma coleção item por item, comparando cada um com o que se busca, até achar ou chegar ao
fim — funciona em qualquer lista, ordenada ou não.

## 45. Busca binária

Só funciona em listas **já ordenadas**: em vez de checar item por item, compara com o elemento do
meio e descarta metade da lista a cada passo (se o valor buscado é maior que o do meio, só a
metade da direita pode conter ele; se menor, só a da esquerda). **Exemplo narrado:** buscar `7`
numa lista ordenada de 1 a 100 — busca linear pode levar até 100 comparações; busca binária leva
no máximo 7 (cada comparação corta a lista pela metade: 100→50→25→13→7→4→2→1).

`[TENTE VOCÊ]` Por que busca binária não funciona numa lista desordenada? Resposta: porque
descartar "a metade da direita" só é uma decisão válida se você já souber que ela está ordenada
em relação ao meio — numa lista bagunçada, o valor buscado pode estar em qualquer posição.

## 46. Ordenação

Reorganizar os elementos de uma coleção numa ordem (crescente ou decrescente). Os três algoritmos
a seguir resolvem o mesmo problema com estratégias diferentes — nenhum usa `std::sort` (ver seção
`[ATENÇÃO]` mais abaixo).

### 47. Bubble Sort

A cada passada, compara pares de elementos vizinhos e troca se estiverem fora de ordem — os
maiores "borbulham" pro final a cada passada completa. **Exemplo narrado** com `[5, 2, 4, 1]`:
passada 1 compara (5,2)→troca→`[2,5,4,1]`, (5,4)→troca→`[2,4,5,1]`, (5,1)→troca→`[2,4,1,5]`;
passada 2 repete até não haver mais trocas.

### 48. Selection Sort

A cada passada, encontra o menor elemento *restante* e o coloca na posição correta (troca com o
primeiro da parte ainda não ordenada). Diferente do bubble sort, faz uma única troca por passada,
não várias.

### 49. Insertion Sort

Constrói a lista ordenada um elemento de cada vez, pegando o próximo elemento e "inserindo" ele na
posição correta entre os já ordenados — parecido com organizar cartas de baralho na mão, uma a
uma.

## 50. Complexidade

Como comparar dois algoritmos que resolvem o mesmo problema, sem depender de "qual computador
rodou mais rápido" (isso muda de máquina pra máquina) — complexidade mede como o *trabalho* do
algoritmo cresce conforme a entrada cresce.

### 51. Notação Big O

A forma padrão de expressar complexidade: `O(n)` (busca linear — no pior caso, uma comparação por
elemento), `O(log n)` (busca binária — corta pela metade a cada passo), `O(n²)` (bubble/selection/
insertion sort — um laço dentro de outro, ambos percorrendo a entrada).

`[TENTE VOCÊ]` Numa lista de 1 milhão de itens, quantas comparações uma busca linear faz, no pior
caso? E uma busca binária? Resposta: linear, até 1 milhão; binária, até ~20 (`log₂(1.000.000) ≈
20`) — a diferença fica gigante conforme a entrada cresce, mesmo os dois "funcionando".

### 52. Tempo vs espaço

Complexidade de tempo (quantos passos o algoritmo executa) não é a única métrica — complexidade de
espaço mede quanta memória extra o algoritmo usa além da entrada original. Às vezes um algoritmo
mais rápido gasta mais memória, e vice-versa — é uma troca (trade-off), não uma resposta única.

### 53. Complexidade de algoritmos simples

Um único laço percorrendo `n` elementos é `O(n)`. Um laço dentro de outro, ambos percorrendo `n`
elementos (como nos três algoritmos de ordenação da seção 46), é `O(n²)` — o trabalho cresce com o
*quadrado* do tamanho da entrada, não proporcionalmente.

## 54. Resolução de problemas

Fechando o módulo: um resumo prático de como abordar qualquer problema novo de lógica.

### 55. Divisão de problemas

Retomando a decomposição (seção 6): diante de um problema novo, a primeira pergunta não é "que
código eu escrevo", é "em que sub-problemas menores eu quebro isso".

### 56. Estratégias de solução

Antes de codificar, considere mais de uma abordagem (ex: busca linear é mais simples de escrever;
busca binária é mais rápida, mas exige lista ordenada) — a "melhor" solução depende do contexto
(tamanho dos dados, se já estão ordenados, quantas vezes o algoritmo vai rodar).

### 57. Casos extremos

Sempre pergunte: o que meu algoritmo faz com uma lista vazia? Com um único elemento? Com valores
repetidos? Com o maior/menor valor possível? Esses "casos extremos" são onde a maioria dos bugs
de lógica se esconde — um algoritmo que "funciona" só foi testado com entradas confortáveis.

### 58. Testes de entrada

Antes de considerar um algoritmo pronto, teste com pelo menos: um caso "normal", um caso extremo
(seção 57), e um caso que você *espera* que quebre — se ele não quebrar, ótimo; se quebrar, você
achou o bug antes de alguém achar por você.

## `[ATENÇÃO]` Proibido usar métodos embutidos da linguagem

Nos exercícios deste módulo (e nas apostilas de apoio), **é proibido usar métodos ou funções
prontas da linguagem que já resolvem o problema por você** — por exemplo, usar `std::find()` do
C++ pra buscar um elemento numa lista, `std::sort()` pra ordenar, ou `std::max_element()` pra
achar o maior valor. O objetivo do exercício não é resolver usando uma função pronta da biblioteca
padrão — é entender e implementar **você mesmo** o algoritmo por trás disso (busca linear/binária
da seção 44-45, os três algoritmos de ordenação da seção 46-49).

O que **não** fazer:
```cpp
auto it = std::find(itens.begin(), itens.end(), busca);  // resolve sem ensinar nada sobre o algoritmo
std::sort(itens.begin(), itens.end());                   // idem — implemente bubble/selection/insertion
```
O que fazer no lugar: implementar manualmente (como no exercício "Inventário caótico", busca
linear, ou nos novos laboratórios de busca e ordenação da prática), percorrendo a lista item por
item com um `for`, comparando/trocando conforme o algoritmo escolhido pede.

**Linguagem dos exercícios deste módulo**: C++ (a mesma introduzida no módulo 08).

## Erros comuns

Você já viu estes avisos ao longo do módulo — aqui vai só a revisão rápida:

- Pular direto pro código sem escrever o pseudocódigo primeiro, ou sem decompor o problema — geralmente resulta em lógica confusa que precisa ser refeita do zero.
- Usar um método embutido da linguagem pra resolver o exercício, violando a regra da trilha.
- Confundir "condição de parada" (quando o `while` deve parar) com "nunca parar" — sempre revisar se a condição do laço eventualmente vira falsa.
- Escrever `18 <= idade <= 65` esperando o comportamento matemático (não funciona assim na maioria das linguagens).
- Testar só o "caminho feliz", sem considerar casos extremos (lista vazia, um único elemento).
- Subestimar quantas repetições um loop aninhado realmente executa.

## Conexão com os próximos módulos

| Conceito deste módulo | Reaparece em |
|---|---|
| Pseudocódigo / estruturas de controle | Todos os módulos técnicos seguintes (10-13) — cada exercício pede raciocínio antes de código |
| Busca e ordenação manuais | Módulos 11/12 (bancos de dados) — entender por que um índice ou um JOIN existe usa o mesmo raciocínio de "como encontrar algo numa coleção de dados", só que otimizado por quem construiu o banco |
| Complexidade (Big O) | Qualquer decisão futura de "essa solução escala?" em projetos maiores |

## `[REFERÊNCIA]`

- Curso de Lógica de Programação — Prof. Gustavo Guanabara (YouTube).
- Material de apoio já disponível na pasta: `APOSTILA_2.pdf`, `lista de exercio.webp`,
  `renova_exercicios.pdf`.
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/) — referência visual rápida de complexidade
  dos algoritmos e estruturas de dados mais comuns.

## Checklist de saída

- [ ] Decomponho um problema em sub-problemas menores antes de escrever qualquer código.
- [ ] Escrevo pseudocódigo (ou fluxograma) para um problema simples antes de traduzir para uma linguagem.
- [ ] Identifico as três estruturas de controle dentro de um algoritmo dado.
- [ ] Uso table trace/dry run pra encontrar um erro de lógica sem rodar o código.
- [ ] Implemento busca linear e busca binária sem usar métodos embutidos da linguagem.
- [ ] Implemento pelo menos um algoritmo de ordenação (bubble, selection ou insertion) manualmente.
- [ ] Explico, em termos gerais, a diferença entre O(n), O(log n) e O(n²).
- [ ] Testo um algoritmo com casos extremos, não só com entradas "confortáveis".
