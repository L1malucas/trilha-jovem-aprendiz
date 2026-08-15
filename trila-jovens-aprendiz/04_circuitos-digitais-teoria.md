# Módulo 04 — Circuitos Digitais

> **Objetivo:** entender como portas lógicas implementam operações sobre bits, como combiná-las
> em circuitos maiores (somadores, multiplexadores, comparadores) e como a partir delas nasce
> memória (latches, flip-flops, registradores, contadores, máquinas de estados).
> **Pré-requisitos:** Módulo 03 (Sistemas de Numeração).
> **Tempo de referência:** 5 a 7 horas.
> **Prática correspondente:** [04_circuitos-digitais-pratica.md](04_circuitos-digitais-pratica.md)

---

## 1. Por que isso importa

No módulo 03 você viu o interruptor de luz como analogia para o bit: aceso ou apagado, `1` ou
`0`. Este módulo pega essa ideia e pergunta o próximo passo óbvio: e se você ligar vários
interruptores entre si, de um jeito que o estado de um dependa do estado dos outros? É
exatamente disso que são feitas as portas lógicas — e é a partir delas que se constrói tudo, da
calculadora mais simples até a CPU do módulo 05.

**Uma fronteira importante desde já:** aqui você vai ver *como a lógica é construída* — portas,
circuitos, memória no nível de bit. *Como esses componentes se organizam para formar um
computador de verdade* (CPU, RAM, barramentos, ciclo de instrução) é assunto do módulo 05,
Arquitetura de Computadores. Os registradores que você vai construir aqui (item 34) são a ponte
entre os dois módulos.

## 2. Analógico vs Digital

Pense num dimmer de luz, daqueles que giram e a luz vai clareando aos poucos — ele tem infinitos
níveis possíveis entre "apagado" e "totalmente aceso". Isso é um sinal **analógico**: contínuo,
qualquer valor intermediário é válido. Um interruptor comum liga/desliga é diferente: só existem
dois estados possíveis, sem meio-termo. Isso é **digital**: discreto, um número finito de valores
possíveis (no caso mais simples, dois).

Computadores usam digital, não analógico, principalmente por um motivo: **imunidade a ruído**.
Um sinal elétrico real nunca é perfeitamente estável — sempre tem uma variação pequena por
interferência, temperatura, distância no fio. Num sistema analógico, essa variação *é* o dado, e
qualquer ruído já distorce a informação. Num sistema digital, o circuito só precisa distinguir
"claramente perto de 0" de "claramente perto de 1" — uma variação pequena não muda a
interpretação, porque existe uma margem de segurança entre os dois níveis válidos.

`[TENTE VOCÊ]` Um termômetro de mercúrio (a coluna sobe e desce continuamente) e um termômetro
digital de forno (mostra só números inteiros, um de cada vez) — qual dos dois é analógico e qual
é digital? Resposta: o de mercúrio é analógico (a coluna assume qualquer altura contínua); o
digital de forno é digital (só mostra um conjunto finito e discreto de valores possíveis).

## 3. Níveis de abstração

Você já usa, sem perceber, decisões que combinam duas condições com "e" ou "ou" o tempo todo:
"vou sair de casaco **se** estiver frio **e** estiver chovendo" (as duas precisam ser verdade);
"vou levar guarda-chuva **se** estiver chovendo **ou** o céu estiver nublado" (uma das duas já
basta). Portas lógicas formalizam exatamente esse tipo de decisão — só que com `1` (verdadeiro)
e `0` (falso) no lugar de "está chovendo" ou "não está".

A cadeia de abstração completa é:

```
Transistor (uma chave elétrica, o "interruptor" do módulo 03)
  → Porta lógica (combinação de transistores: AND, OR, NOT...)
    → Circuito digital (combinação de portas)
      → Componente funcional (somador, registrador, memória)
        → CPU
```

Cada nível esconde a complexidade do nível anterior — quem projeta um circuito somador não
precisa pensar em transistores, só em portas lógicas, do mesmo jeito que você não pensa em
transistores quando aperta uma tecla no teclado.

## 4. Sinais digitais

Um sinal digital, na prática, é uma tensão elétrica que o circuito interpreta como `0` ou `1`
dependendo de estar abaixo ou acima de um limiar. Por exemplo, num circuito que opera em 5V, tudo
abaixo de ~0,8V pode ser lido como `0`, e tudo acima de ~2V como `1` — a faixa no meio (a
"zona proibida") existe justamente pra dar essa margem de segurança contra ruído citada no item
2. Um fio "flutuando" nessa zona intermediária é o que causa comportamento imprevisível em
circuitos mal projetados.

## 5. Estados lógicos 0 e 1

`0` e `1`, nesse contexto, não são "números" no sentido aritmético completo do módulo 03 — são
**estados lógicos**: verdadeiro/falso, ligado/desligado, presente/ausente. Eles só viram números
de verdade quando você os organiza em grupos com valor posicional (como visto no módulo 03) ou
quando uma porta lógica os processa como entrada de uma operação booleana. Confundir "bit como
estado lógico" com "bit como dígito numérico" é normal no começo — os dois usos convivem o tempo
todo em um circuito real.

## 6. Lógica booleana

A lógica booleana é o sistema matemático (criado por George Boole, século XIX, bem antes de
existir qualquer computador) que formaliza raciocínio com apenas dois valores: verdadeiro e
falso. Portas lógicas são a implementação física, em hardware, das operações desse sistema — é
por isso que os nomes das portas (AND, OR, NOT) são, literalmente, os operadores lógicos que você
já usa (ou vai usar) em qualquer linguagem de programação (`&&`, `||`, `!`).

## 7. Portas lógicas

Pegando a decisão do casaco ("frio **e** chuva") e formalizando: chame de `A` a condição "está
frio" e `B` a condição "está chovendo", cada uma valendo `1` (verdadeiro) ou `0` (falso). As
subseções abaixo cobrem as sete portas lógicas fundamentais, uma por uma.

### 8. NOT

A porta **NOT** só inverte: se a condição era verdadeira, passa a falsa, e vice-versa ("**não**
está frio").

| A | NOT A |
|---|---|
| 0 | 1 |
| 1 | 0 |

### 9. AND

A porta **AND** representa exatamente "as duas precisam ser verdadeiras" — só dá `1` quando `A`
**e** `B` são `1`:

| A | B | A AND B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### 10. OR

A porta **OR** representa "uma das duas já basta" (o exemplo do guarda-chuva) — dá `1` quando `A`
**ou** `B` (ou ambos) forem `1`:

| A | B | A OR B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### 11. XOR

A porta **XOR** ("ou exclusivo") dá `1` quando `A` e `B` são **diferentes** — é como o OR, mas
exclui o caso em que os dois são `1` ao mesmo tempo:

| A | B | A XOR B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### 12. NAND

**NAND** é AND seguido de NOT — saída `0` só se `A` **e** `B` forem `1`; qualquer outra
combinação dá `1`.

### 13. NOR

**NOR** é OR seguido de NOT — saída `1` só se `A` **e** `B` forem `0`; qualquer outra combinação
dá `0`.

### 14. XNOR

**XNOR** é XOR seguido de NOT — saída `1` se `A` e `B` forem **iguais**.

| Porta | Regra | Relação com as básicas |
|---|---|---|
| NAND | saída 0 só se A **e** B forem 1 | AND, depois invertido (NOT) |
| NOR | saída 1 só se A **e** B forem 0 | OR, depois invertido (NOT) |
| XOR | saída 1 se A e B forem **diferentes** | "OR, mas exclui o caso em que os dois são 1" |
| XNOR | saída 1 se A e B forem **iguais** | XOR, depois invertido (NOT) |

`[TENTE VOCÊ]` Monte a tabela verdade de `A NAND B` para as 4 combinações de A e B, partindo da
tabela do AND que você acabou de ver e invertendo cada resultado. Resposta: `00→1, 01→1, 10→1,
11→0`.

## 15. Tabelas-verdade

Você já usou tabelas-verdade em todas as seções acima sem uma definição formal: é simplesmente a
lista **exaustiva** de todas as combinações possíveis de entrada, com a saída correspondente pra
cada uma. Com `n` entradas, existem `2ⁿ` linhas possíveis (a mesma relação `2ⁿ` do módulo 03) —
uma porta de 2 entradas tem 4 linhas; um circuito de 3 entradas, 8 linhas, e assim por diante. É a
ferramenta universal pra especificar (ou verificar) o comportamento de qualquer circuito
combinacional, por mais complexo que seja.

## 16. Expressões booleanas

Em vez de desenhar portas ou montar tabelas, dá pra escrever o comportamento de um circuito como
uma **expressão booleana** — uma fórmula usando os operadores lógicos. A expressão do meio-somador
que você vai ver no item 27, por exemplo, escreve-se `Soma = A XOR B` e `Carry = A AND B`. É a
mesma relação entre "descrever uma reta por uma equação" e "desenhar a reta num gráfico" — duas
formas de representar a mesma coisa, cada uma útil num momento diferente.

## 17. Álgebra booleana

Assim como a álgebra comum tem regras pra manipular equações (comutatividade, associatividade,
distributividade), a **álgebra booleana** tem regras equivalentes pra manipular expressões
lógicas sem precisar remontar a tabela verdade toda vez. Por exemplo: `A AND B = B AND A`
(comutatividade), `A OR (B AND C) = (A OR B) AND (A OR C)` (distributividade). Essas regras são o
que permite simplificar circuitos — trocar uma expressão grande por uma equivalente menor, que
faz exatamente a mesma coisa com menos portas.

## 18. Leis de De Morgan

As duas leis mais úteis da álgebra booleana, batizadas em homenagem a Augustus De Morgan, dizem
como "distribuir" uma negação sobre um AND ou um OR:

```
NOT (A AND B)  =  (NOT A) OR (NOT B)
NOT (A OR B)   =  (NOT A) AND (NOT B)
```

**Exemplo narrado:** pegue a frase "não é verdade que está frio *e* está chovendo" — isso é o
mesmo que dizer "não está frio, *ou* não está chovendo" (basta uma das duas condições falhar pra
tornar a frase original falsa). É exatamente essa reescrita que a primeira lei de De Morgan
formaliza: `NOT(A AND B) = (NOT A) OR (NOT B)`.

`[TENTE VOCÊ]` Usando a segunda lei de De Morgan, reescreva `NOT (chove OR venta)` sem negar a
expressão inteira de uma vez. Resposta: `(NOT chove) AND (NOT venta)` — "não chove **e** não
venta".

## 19. Simplificação de expressões booleanas

Simplificar uma expressão booleana significa achar uma equivalente com menos portas, usando as
regras da álgebra booleana (incluindo De Morgan). Isso importa na prática porque cada porta a
menos num circuito real significa menos transistores, menos consumo de energia e menos atraso de
propagação do sinal.

**Exemplo narrado:** a expressão `(A AND B) OR (A AND NOT B)` parece precisar de 2 portas AND, 1
NOT e 1 OR. Mas repare: `A` aparece nos dois termos — fatorando (distributividade, ao contrário):
`A AND (B OR NOT B)`. E `B OR NOT B` é **sempre** `1` (uma condição ou sua negação, uma das duas é
sempre verdadeira). Então a expressão inteira simplifica pra só `A AND 1`, que é só `A` — o
circuito inteiro vira um único fio, sem porta nenhuma. É exatamente esse tipo de otimização que
compiladores e ferramentas de síntese de circuito fazem automaticamente.

## 20. NAND e NOR como portas universais

Repare no que já foi visto: XOR foi descrito como "uma combinação das portas básicas", não como
uma porta fundamental à parte. Isso não é acaso — é possível ir além e construir **AND, OR e NOT**
(as três portas "básicas") usando apenas cópias de uma única porta: NAND (ou, alternativamente,
apenas NOR). Essa propriedade é chamada de completude funcional. Na prática, chips reais são
fabricados majoritariamente com portas NAND, e as demais portas são montadas combinando NANDs —
é mais barato fabricar um único tipo de componente em escala do que vários tipos diferentes.

## 21. Circuitos combinacionais

Um circuito é **combinacional** quando a saída depende **apenas** dos valores atuais das
entradas — não existe memória do que aconteceu antes. É o caso de tudo que você viu até aqui: a
tabela verdade de um AND não muda dependendo do que entrou nele um segundo atrás. As próximas
subseções (22-29) são exemplos de circuitos combinacionais mais complexos, montados combinando as
portas básicas.

### 22. Multiplexadores

Um **multiplexador** (MUX) é uma "chave seletora" digital: ele recebe várias entradas de dados e
um sinal de controle que escolhe qual delas passa pra saída — como escolher, com um controle
remoto universal, qual aparelho (TV, som, ar-condicionado) vai receber o comando nesse instante.
Um MUX de 2 entradas usa 1 bit de controle (`0` seleciona a entrada A, `1` seleciona a entrada B);
um MUX de 4 entradas precisa de 2 bits de controle (`2² = 4`, a mesma relação de potências de 2
do módulo 03).

### 23. Demultiplexadores

Um **demultiplexador** (DEMUX) faz o oposto do MUX: recebe uma única entrada de dados e um sinal
de controle, e direciona essa entrada pra **uma** das várias saídas possíveis — como um garçom
levando um único prato pra mesa certa, escolhida pelo número da comanda.

### 24. Codificadores

Um **codificador** (encoder) recebe várias linhas de entrada, das quais só uma está ativa por vez,
e produz na saída o *número binário* correspondente a qual entrada estava ativa. Por exemplo: um
codificador de 8 entradas produz uma saída de 3 bits (`2³ = 8`) identificando qual das 8 entradas
foi ativada.

### 25. Decodificadores

Um **decodificador** (decoder) faz o oposto: recebe um número binário na entrada e ativa **uma
única** saída correspondente a esse número, entre várias possíveis. Isso é exatamente o mecanismo
que, no módulo 05, vai permitir que um endereço de memória binário "aponte" pra uma única posição
específica dentro de milhões — o decodificador de endereço é essa mesma peça, só que em escala
muito maior.

### 26. Comparadores

Um **comparador** recebe dois números binários e diz se são iguais, ou qual dos dois é maior —
é a implementação em hardware dos operadores `==`, `<` e `>` que você usa (ou vai usar) em
qualquer linguagem de programação. Um comparador de 1 bit é simples: `A == B` é verdade quando
`A XNOR B` dá `1` (lembra do item 14 — XNOR é "iguais"); comparadores de números maiores encadeiam
vários desses, bit a bit, da posição mais significativa pra menos significativa.

`[TENTE VOCÊ]` Um MUX de 8 entradas — quantos bits de controle ele precisa? Resposta: 3 bits
(`2³ = 8`), pela mesma relação de potências de 2 vista no módulo 03.

### 27. Meio somador

**Exemplo narrado — o meio-somador (half adder):** some dois bits, `A` e `B`, do jeito que você
já soma binário desde o módulo 03. O resultado tem duas partes: o dígito da soma em si, e o
"vai-um" (carry), caso a soma estoure. Pensando bit a bit: quando `A` e `B` são diferentes
(`0,1` ou `1,0`), a soma é `1` sem vai-um — exatamente a regra do XOR. Quando os dois são `1`, a
soma "estoura" pra `10`: o dígito da soma vira `0` e sobra um vai-um de `1` — exatamente a regra
do AND.

| A | B | Soma (XOR) | Carry (AND) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Ou seja: um somador não é uma porta nova — é XOR e AND, os dois recebendo as mesmas entradas,
cada um respondendo uma pergunta diferente ("qual o dígito?" e "estourou?").

`[TENTE VOCÊ]` Monte a tabela verdade de `A AND (B OR C)` para as 8 combinações de A, B e C —
primeiro resolva `B OR C` pra cada linha, depois combine o resultado com `A` via AND. Resposta:
só dá `1` quando `A = 1` **e** pelo menos um entre `B` ou `C` for `1` (linhas `1,0,1`; `1,1,0`;
`1,1,1`).

### 28. Somador completo

O meio-somador tem uma limitação: ele só soma dois bits isolados, sem considerar um vai-um que
possa ter vindo de uma soma anterior. Um **somador completo** (full adder) resolve isso: recebe
três entradas (`A`, `B`, e `Carry-in` — o vai-um vindo da posição anterior) e produz duas saídas
(`Soma` e `Carry-out` — o vai-um pra próxima posição). Ele pode ser montado com **dois**
meio-somadores em série mais uma porta OR combinando os dois carries.

### 29. Somador binário

Encadeando vários somadores completos — um pra cada posição de bit, cada um passando seu
`Carry-out` como `Carry-in` do próximo — você monta um **somador binário** de N bits, capaz de
somar dois números inteiros completos, não só dois bits isolados.

**Exemplo narrado:** somar `0101` (5) com `0011` (3), 4 bits, usando 4 somadores completos em
cadeia (posição 0 = menos significativa):

```
Posição 0: A=1, B=1, Carry-in=0  → Soma=0, Carry-out=1
Posição 1: A=0, B=1, Carry-in=1  → Soma=0, Carry-out=1
Posição 2: A=1, B=0, Carry-in=1  → Soma=0, Carry-out=1
Posição 3: A=0, B=0, Carry-in=1  → Soma=1, Carry-out=0
```

Lendo as somas da posição 3 até a 0: `1000` = 8. Confere: `5 + 3 = 8`. Esse encadeamento — o
carry de uma posição "esperando" a posição anterior terminar antes de propagar — é chamado de
somador de **carry propagado** (ripple carry), e é literalmente o mesmo mecanismo que você já fez
na mão, no módulo 03, ao somar binário coluna por coluna da direita pra esquerda.

## 30. Circuitos sequenciais

Um circuito é **sequencial** quando a saída depende das entradas **e** de um estado interno
anterior — ou seja, o circuito tem memória. Pense na diferença entre um interruptor comum de luz
e uma trava de porta: o interruptor é puramente combinacional (a luz reflete só a posição atual
do interruptor); já uma trava eletrônica com senha "lembra" se você já digitou os primeiros
dígitos corretos antes de aceitar o último — o resultado depende do que já aconteceu, não só do
dígito atual.

`[ATENÇÃO]` É comum, nesta altura, achar que todo circuito reage "instantaneamente" às entradas,
como um combinacional — mas circuitos sequenciais mudam de estado de forma sincronizada, não a
cada minúscula oscilação elétrica. Para isso, eles usam um **clock** (item 31): um sinal que
"pulsa" em intervalos regulares e sincroniza *quando* o estado pode mudar. Confundir "clock" com
"só velocidade" é outro erro comum — a função dele é sincronização, não apenas ritmo.

**Exemplo narrado — a trava eletrônica com senha de 3 dígitos:** imagine uma trava que só abre
com a senha `4-7-2`, digitada dígito por dígito num teclado. O circuito precisa "lembrar" quanto
já foi digitado corretamente até agora — isso é o estado interno.

```
Estado inicial: "nada digitado ainda" (0 dígitos corretos confirmados)

Dígito 1 digitado: 4  → confere com o 1º dígito da senha (4). Estado avança:
                        "1 dígito correto confirmado".
Dígito 2 digitado: 7  → confere com o 2º dígito da senha (7). Estado avança:
                        "2 dígitos corretos confirmados".
Dígito 3 digitado: 2  → confere com o 3º dígito da senha (2). Estado avança:
                        "senha completa e correta" → a trava abre.
```

Repare que a trava só abre por causa da *sequência* de estados que ela acumulou — se você
digitasse `4-7-2` fora de ordem, ou pulasse direto pro `2`, o resultado seria diferente, mesmo
usando os mesmos três dígitos. Um circuito combinacional (como as portas lógicas vistas antes)
nunca conseguiria fazer isso: ele só enxerga a entrada do instante atual, sem noção de "o que já
veio antes". (No item 36 você vai ver essa mesma trava formalizada como uma máquina de estados.)

`[TENTE VOCÊ]` Nessa trava de 3 dígitos, o usuário digita `4-9-2` (o segundo dígito está errado).
O que acontece com o estado interno no dígito 2, e a trava abre no final? Resposta: o estado
"reseta" — como o dígito 2 (`9`) não confere com o esperado (`7`), o circuito volta pro estado
"nada confirmado" (ou entra num estado de erro), e mesmo o `2` final batendo com o 3º dígito da
senha, a trava não abre, porque a sequência como um todo não foi validada corretamente.

### 31. Clock

O **clock** é um sinal elétrico gerado por um oscilador (fisicamente, geralmente um cristal de
quartzo vibrando numa frequência precisa) que alterna entre `0` e `1` em intervalos regulares.
Cada alternância de `0` pra `1` é chamada de **borda de subida**; de `1` pra `0`, **borda de
descida**. Circuitos sequenciais (latches síncronos, flip-flops, registradores, contadores) usam
essas bordas como "sinal de partida" pra decidir exatamente quando um estado pode mudar — sem
isso, seria impossível garantir que várias partes de um circuito grande mudem de estado no mesmo
instante, de forma consistente.

### 32. Latches

- **Latch (SR latch)**: o circuito de memória mais simples — guarda 1 bit, e muda de estado
  sempre que as entradas de Set/Reset mudam (sem esperar um clock).

### 33. Flip-Flops

- **Flip-flop (ex: tipo D)**: uma evolução do latch que só muda de estado em sincronia com o
  clock (na borda de subida ou descida do sinal) — é o bloco básico usado para construir
  registradores e memória, porque garante que todos os bits de um registrador mudem juntos, no
  mesmo instante, em vez de um de cada vez de forma imprevisível.

**Exemplo narrado — a mesma entrada, dois comportamentos diferentes:** imagine que o mesmo sinal
de entrada `D` (dado a guardar) chega tanto a um latch quanto a um flip-flop tipo D, e observe o
que cada um guarda ao longo do tempo (`↑` marca um pulso de clock):

| Momento | Entrada D | Clock | O que o **latch** guarda | O que o **flip-flop** guarda |
|---|---|---|---|---|
| t0 | 0 | — | 0 | 0 |
| t1 | 1 | — | **1** (mudou na hora) | 0 (ainda não teve pulso) |
| t2 | 0 | — | **0** (mudou na hora de novo) | 0 (ainda não teve pulso) |
| t3 | 1 | ↑ | **1** | **1** (só agora, no pulso) |
| t4 | 0 | — | **0** (mudou na hora) | 1 (mantém até o próximo pulso) |
| t5 | 1 | ↑ | **1** | **1** (só agora, no pulso) |

Repare: o latch "treme" a cada mudança de `D`, mesmo entre pulsos de clock — ele reflete o valor
atual de `D` o tempo todo. O flip-flop ignora completamente o que acontece com `D` entre um pulso
e outro, e só "olha" pra entrada exatamente no instante do pulso. É por isso que registradores
(que precisam trocar vários bits ao mesmo tempo, de forma previsível) usam flip-flops: se
usassem latches, cada bit poderia mudar num instante ligeiramente diferente, conforme o ruído
elétrico de cada fio — com flip-flops, todos esperam o mesmo pulso de clock pra mudar juntos.

`[TENTE VOCÊ]` Na tabela acima, se `D` mudasse de `1` para `0` bem no meio do intervalo entre t3
e t5 (sem nenhum pulso de clock acontecendo nesse meio tempo), o que aconteceria com o valor
guardado no flip-flop? Resposta: nada — o flip-flop mantém o valor `1` do último pulso (t3) até o
próximo pulso de clock (t5), ignorando qualquer mudança de `D` nesse meio tempo. O latch, por
outro lado, mudaria para `0` imediatamente.

### 34. Registradores

Um **registrador** é simplesmente um grupo de flip-flops tipo D lado a lado, todos compartilhando
o mesmo sinal de clock, cada um guardando 1 bit — um registrador de 8 bits é 8 flip-flops D
operando em paralelo. É a "memória mais rápida" que você já viu citada na hierarquia de memória
(módulo 05): fica literalmente dentro da CPU, sem precisar de um barramento pra acessar. Como
cada flip-flop só muda no pulso de clock, e todos compartilham o mesmo clock, o registrador
inteiro troca de valor "de uma vez", de forma consistente — exatamente o comportamento que a
tabela do item 33 demonstrou pra um único bit.

### 35. Contadores

Um **contador** é um circuito sequencial que incrementa seu valor guardado em 1 a cada pulso de
clock — construído encadeando flip-flops de um jeito que a saída de um alimenta a entrada do
próximo. É o mecanismo por trás, por exemplo, do *Program Counter* que você vai encontrar no
módulo 05: ele literalmente conta, pulso a pulso, qual é a próxima instrução a buscar na memória.

`[TENTE VOCÊ]` Um contador de 3 bits, começando em `000`, recebe 5 pulsos de clock seguidos. Em
que valor binário ele para? Resposta: `101` (5 em decimal) — cada pulso soma 1, e `000 → 001 →
010 → 011 → 100 → 101` são exatamente 5 incrementos.

### 36. Máquinas de estados

Uma **máquina de estados** (finite state machine, FSM) generaliza a ideia de "estado interno" que
você já viu na trava de senha do item 30 — formalizando-a com uma lista explícita de estados
possíveis e as regras de transição entre eles. A trava de 3 dígitos, formalizada como FSM, tem
4 estados (`Inicial`, `1 dígito confirmado`, `2 dígitos confirmados`, `Aberta`), e cada dígito
digitado dispara uma transição: ou avança pro próximo estado (se o dígito bate com a senha) ou
volta pro estado `Inicial` (se erra). Máquinas de estados são a ferramenta padrão pra projetar
qualquer circuito sequencial mais complexo do que um contador simples — de semáforos a
controladores de elevador a protocolos de rede.

## Erros comuns

Você já viu estes avisos ao longo do módulo — aqui vai só a revisão rápida:

- Confundir circuito combinacional com sequencial — achar que toda saída é "instantânea".
- Esquecer que NAND (ou NOR) sozinha já é suficiente para construir qualquer circuito.
- Achar que "clock" é só sinônimo de velocidade, quando sua função real é sincronizar *quando* o
  estado pode mudar.
- Confundir "bit como estado lógico" com "bit como dígito numérico" — os dois convivem, mas são
  usos diferentes do mesmo `0`/`1`.

## Conexão com os próximos módulos

| Conceito deste módulo | Reaparece em |
|---|---|
| Registradores, flip-flops / memória | Módulo 05 — hierarquia de memória, Program Counter, ISA |
| Decodificadores | Módulo 05 — decodificação de endereços de memória |
| Contadores | Módulo 05 — Program Counter |
| Portas lógicas (AND, OR, NOT) | Módulo 08 — operadores lógicos em algoritmos (`&&`, `\|\|`, `!`) |
| Comparadores | Módulo 08 — operadores de comparação (`==`, `<`, `>`) |

## `[REFERÊNCIA]`

- BROOKSHEAR, J. Glenn. *Ciência da Computação — Uma Visão Abrangente*, 7ª ed., Bookman, 2005 —
  Capítulo 2 (Armazenamento de Dados / lógica booleana).
- WHITE, Ron. *Como Funciona o Computador*, 8ª ed., Quark, 1998.
- [All About Circuits — Latches e Flip-Flops](https://www.allaboutcircuits.com/textbook/digital/chpt-10/latches/) —
  explicação técnica com diagramas de tempo (em inglês).
- [Ben Eater — Building an SR latch](https://www.youtube.com/watch?v=KM0DdEaY5sY) — vídeo
  montando um latch com portas NOR reais, mão na massa.
- [CircuitVerse](https://circuitverse.org/) — simulador de circuitos digitais online, gratuito,
  onde dá pra montar e testar visualmente qualquer circuito deste módulo (portas, somadores,
  multiplexadores, flip-flops, contadores).
- [Logic.ly](https://logic.ly/demo) — simulador de portas lógicas mais simples, bom pra montar
  as tabelas verdade dos itens 8-14 visualmente.

## Checklist de saída

- [ ] Diferencio sinal analógico de digital, e explico por que computadores usam digital.
- [ ] Monto a tabela verdade de AND, OR, NOT, XOR, NAND, NOR, XNOR a partir de entradas dadas.
- [ ] Explico por que NAND é considerada uma porta "universal".
- [ ] Aplico as leis de De Morgan pra reescrever uma expressão booleana negada.
- [ ] Simplifico uma expressão booleana redundante usando álgebra booleana.
- [ ] Explico o que um multiplexador, um decodificador e um comparador fazem, com uma analogia
      pra cada.
- [ ] Explico por que um meio-somador é só XOR + AND, e monto um somador completo/binário de N
      bits encadeando meio-somadores.
- [ ] Diferencio circuito combinacional de circuito sequencial, com um exemplo de cada.
- [ ] Explico o papel do clock em um circuito sequencial — por que ele sincroniza, não só marca
      velocidade.
- [ ] Explico, com a linha do tempo latch x flip-flop, por que registradores usam flip-flops e
      não latches.
- [ ] Explico como um contador e uma máquina de estados se relacionam com o Program Counter e a
      trava de senha, respectivamente.
