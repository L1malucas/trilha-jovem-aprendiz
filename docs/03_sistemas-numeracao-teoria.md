---
id: 03_sistemas-numeracao-teoria
title: "Módulo 03 — Sistemas de Numeração"
sidebar_position: 30
---

# Módulo 03 — Sistemas de Numeração

> **Objetivo:** entender como computadores representam números e caracteres internamente, e
> converter com segurança entre decimal, binário, octal e hexadecimal.
> **Pré-requisitos:** nenhum — primeiro módulo da trilha de fundamentos de computação.
> **Tempo de referência:** 5 a 7 horas.
> **Prática correspondente:** [03_sistemas-numeracao-pratica.md](03_sistemas-numeracao-pratica.md)

---

## Por que isso importa antes de programar

Todo dado que um computador manipula — um número, uma letra, uma cor, uma instrução — é, no
nível mais baixo, uma sequência de bits. Entender como esses bits viram números, letras e frações
(e vice-versa) não é decoreba de conversão: é o que torna compreensível, mais adiante, por que um
tipo numérico "estoura", por que um endereço de memória é escrito em hexadecimal, por que
`0.1 + 0.2` não dá exatamente `0.3`, ou por que um emoji às vezes quebra ao ser salvo num sistema
antigo.

Este módulo não pede pra você decorar procedimentos — pede pra entender **por que** eles
funcionam. É esse entendimento que se aplica em situações que a apostila nunca vai cobrir
explicitamente; decorar uma receita só resolve o exemplo que você já viu.

## 1. Decimal, binário, octal e hexadecimal

Você já usa diariamente o sistema **decimal** (base 10, dígitos `0-9`) sem nunca ter pensado nele
como "uma escolha entre várias possíveis". Mas é só isso: uma convenção de quantos símbolos usar
por posição. Nada impede de usar menos símbolos, ou mais.

Um computador não tem 10 estados elétricos distintos para representar dígitos — tem 2: circuito
ligado ou desligado, alta ou baixa tensão. Por isso o hardware usa nativamente o **binário**
(base 2, só `0` e `1`).

Só que binário é verboso: escrever endereços de memória inteiramente em `0`s e `1`s fica ilegível
rápido. Por isso existem dois "atalhos de leitura" para o binário, usados por convenção em
contextos diferentes:

- O **hexadecimal** (base 16, dígitos `0-9` e `A-F`) — o mais comum hoje, usado em endereços de
  memória, códigos de cor (`#FF5733`), hashes de commit do Git.
- O **octal** (base 8, dígitos `0-7`) — menos comum hoje, mas ainda aparece em lugares
  específicos, como permissões de arquivo no Linux (`chmod 755` — você vai reencontrar isso de
  verdade no Módulo 06).

A razão de existirem *dois* atalhos, e não um só, é histórica e prática: octal agrupa bits de 3
em 3 (`2³ = 8`); hexadecimal agrupa de 4 em 4 (`2⁴ = 16`). Como bytes modernos têm 8 bits (múltiplo
de 4, não de 3), hexadecimal encaixa mais "redondo" — por isso é o padrão dominante hoje, e octal
sobrevive só em nichos legados.

`[TENTE VOCÊ]` Sem fazer nenhuma conta ainda: por que você acha que faz mais sentido agrupar
bits de 4 em 4 para hex do que de 3 em 3? Resposta: porque um byte (8 bits) se divide exatamente
em dois grupos de 4 (sobra zero), mas não se divide exatamente em grupos de 3 (8 não é múltiplo
de 3) — hexadecimal "fecha" com o tamanho do byte, octal não.

## 2. Valor posicional e bases numéricas

O mecanismo que faz *qualquer* uma dessas bases funcionar é o mesmo, e você já usa ele sem
perceber: no número decimal `341`, o dígito `3` não vale só "3" — vale `3 × 100`, porque está na
posição das centenas. O `4` vale `4 × 10`. O `1` vale `1 × 1`. Ou seja:
`341 = 3·10² + 4·10¹ + 1·10⁰`.

Cada posição vale 10 vezes mais que a anterior porque a **base** do sistema decimal é 10 — e
"base" é justamente isso: quantos símbolos diferentes existem, e quanto cada posição pesa em
relação à anterior. Generalizando: numa base `B` qualquer, a posição `i` (contando da direita,
começando em 0) vale `Bⁱ`.

| Base | Símbolos | Peso de cada posição (da direita) |
|---|---|---|
| Decimal (10) | `0-9` | `1, 10, 100, 1000...` |
| Binário (2) | `0-1` | `1, 2, 4, 8, 16...` |
| Octal (8) | `0-7` | `1, 8, 64, 512...` |
| Hexadecimal (16) | `0-9, A-F` | `1, 16, 256, 4096...` |

Não existe mágica nenhuma trocando de base — é sempre a mesma mecânica de posição, só muda quanto
cada posição pesa.

`[TENTE VOCÊ]` Sem converter formalmente, só usando a tabela: quanto vale o dígito octal `5` na
segunda posição (da direita) do número octal `52`? Resposta: `5 × 8¹ = 40` (mais o `2 × 8⁰ = 2` da
primeira posição, total decimal `42`).

## 3. Bits e bytes

Um **bit** (*binary digit*) é a menor unidade de informação possível: um `0` ou um `1`, uma
resposta de sim/não. Sozinho, um bit representa muito pouco — mas agrupados, bits ganham poder
rápido: `n` bits não representam `n` valores, representam **`2ⁿ` valores**. Com 1 bit dá pra
representar 2 valores (`0` e `1`); com 2 bits, 4 valores (`00, 01, 10, 11`); com 8 bits, `2⁸ = 256`
valores.

Esse agrupamento de 8 bits tem nome: **byte**. Por que 8, e não 6 ou 10? Historicamente, 8 bits
foi o tamanho que se firmou como padrão da indústria (grande o suficiente para representar todo o
alfabeto latino + pontuação + dígitos num único byte, como você vai ver na seção de ASCII mais
adiante) — hoje é universal: memória, armazenamento e velocidade de rede são todos medidos em
múltiplos de byte (KB, MB, GB...). Um agrupamento menor, de 4 bits, também tem nome: **nibble**
("meio byte") — e é exatamente o tamanho que um dígito hexadecimal representa, por isso a
conversão binário↔hex encaixa tão bem.

`[ATENÇÃO]` Confundir "quantidade de bits" com "quantidade de valores representáveis" é o erro
mais comum nesta fase — sempre que for calcular quantos valores algo representa, a resposta é
`2ⁿ`, nunca `n`.

`[TENTE VOCÊ]` Quantos valores diferentes cabem num nibble (4 bits)? E por que isso bate
exatamente com a quantidade de símbolos hexadecimais? Resposta: `2⁴ = 16` valores — exatamente os
16 símbolos (`0-9`, `A-F`) que um dígito hexadecimal cobre.

## 4. Decimal → binário

Você já viu que, em qualquer base, cada posição vale um múltiplo da posição anterior — em
binário, potências de 2 (`1, 2, 4, 8, 16, 32…`). Converter um número decimal pra binário é
descobrir quanto ele tem de cada uma dessas potências.

Existe um jeito mecânico de fazer isso sem testar potência por potência: a **divisão sucessiva
por 2**. A lógica por trás: dividir um número por 2 revela se ele é par ou ímpar, e "par ou ímpar"
é exatamente a informação que o bit menos significativo (`2⁰`) carrega — `0` pra par, `1` pra
ímpar. Anotado esse bit, você descarta essa informação (divide de novo, ignorando o resto) e faz
a mesma pergunta pro próximo bit. É como descascar uma cebola: cada divisão revela uma camada, da
posição menos significativa até a mais significativa — por isso, no fim, os restos são lidos de
baixo pra cima.

Acompanhe com `41`:
```
41 ÷ 2 = 20 resto 1   → ímpar → último bit = 1
20 ÷ 2 = 10 resto 0   → par   → próximo bit = 0
10 ÷ 2 =  5 resto 0   → par   → próximo bit = 0
 5 ÷ 2 =  2 resto 1   → ímpar → próximo bit = 1
 2 ÷ 2 =  1 resto 0   → par   → próximo bit = 0
 1 ÷ 2 =  0 resto 1   → chegou a 0: este é o bit mais significativo
```
De baixo pra cima: `41 = 101001`.

`[TENTE VOCÊ]` Converta `13` sozinho, usando o mesmo raciocínio (par ou ímpar a cada passo).
Resposta: `1101`.

Mais um pra fixar, com um número maior — `114`:
```
114 ÷ 2 = 57 resto 0   → par   → último bit = 0
 57 ÷ 2 = 28 resto 1   → ímpar → próximo bit = 1
 28 ÷ 2 = 14 resto 0   → par   → próximo bit = 0
 14 ÷ 2 =  7 resto 0   → par   → próximo bit = 0
  7 ÷ 2 =  3 resto 1   → ímpar → próximo bit = 1
  3 ÷ 2 =  1 resto 1   → ímpar → próximo bit = 1
  1 ÷ 2 =  0 resto 1   → chegou a 0: bit mais significativo
```
De baixo pra cima: `114 = 1110010`.

`[TENTE VOCÊ]` Converta `77` sozinho, mesmo raciocínio. Resposta: `1001101`.

## 5. Binário → decimal

Essa conversão é mais direta que a anterior, porque a informação que você precisava descobrir ali
— quais potências de 2 "cabem" no número — já está pronta, escrita nos próprios bits: cada `1`
marca "essa potência entra na soma"; cada `0` marca "essa potência não entra". Basta somar o
valor de posição de cada `1`.

Exemplo: `101001`
```
1·2⁵ + 0·2⁴ + 1·2³ + 0·2² + 0·2¹ + 1·2⁰
= 32 + 0 + 8 + 0 + 0 + 1 = 41
```
Repare que é o mesmo número convertido na seção anterior — as duas direções são inversas uma da
outra, por isso batem.

`[TENTE VOCÊ]` Converta `1101` de volta pra decimal — é o mesmo número do exercício anterior, na
direção contrária. Resposta: `13`.

## 6. Decimal ↔ hexadecimal

A mesma divisão sucessiva que converteu decimal→binário funciona pra qualquer base — só troca o
divisor. Pra hexadecimal, divide-se sucessivamente por **16** em vez de por 2, e cada resto (que
pode ir de 0 a 15) já vira diretamente um símbolo hex.

Acompanhe com `430`:
```
430 ÷ 16 = 26 resto 14   → 14 em hex é 'E'
 26 ÷ 16 =  1 resto 10   → 10 em hex é 'A'
  1 ÷ 16 =  0 resto  1   → chegou a 0: dígito mais significativo
```
De baixo pra cima: `430 = 0x1AE`.

`[TENTE VOCÊ]` Converta `48` pra hexadecimal pelo mesmo método.
Resposta: `48 ÷ 16 = 3` resto `0`; `3 ÷ 16 = 0` resto `3` → `0x30`.

Hexadecimal→decimal é o espelho: soma o valor posicional de cada dígito, usando potências de 16.
Exemplo: `0x1AE = 1·16² + 10·16¹ + 14·16⁰ = 256 + 160 + 14 = 430` — confere com a conversão acima.

`[TENTE VOCÊ]` Converta `0x30` de volta pra decimal.
Resposta: `3·16¹ + 0·16⁰ = 48`.

`[CLI]` Conferindo conversões no terminal (Python já vem instalado na maioria dos sistemas):
```
python3 -c "print(bin(41), hex(41), oct(41))"
python3 -c "print(int('101001', 2), int('29', 16), int('51', 8))"
```

## 7. Binário ↔ hexadecimal

Você já sabe por que isso funciona: cada dígito hexadecimal vale exatamente 4 bits (um nibble),
porque `2⁴ = 16` é a base do hexadecimal. Então converter binário↔hex não exige recalcular o
número inteiro — só agrupar os bits de 4 em 4 (a partir da direita, completando com zeros à
esquerda se faltar) e converter cada grupo isoladamente, como um dígito solto.

Exemplo: `101001` → agrupando de 4 em 4 a partir da direita: `0010 1001` (o zero à esquerda é só
pra completar o grupo) → `2 9` → `0x29`.

`[TENTE VOCÊ]` Agrupe `11110101` de 4 em 4 e converta pra hexadecimal.
Resposta: `1111 0101` → `F5` → `0xF5`.

**A mesma lógica vale pra octal**, só que agrupando de 3 em 3 bits (porque `2³ = 8`): `101001` →
agrupando de 3 em 3 a partir da direita: `101 001` → `5 1` → `octal 51`.

**Onde você já viu hexadecimal sem perceber:** toda cor numa página web é escrita em hexadecimal,
tipo `#FF5733`. Não é um código arbitrário — são três valores de 0-255 (intensidade de
Vermelho/Verde/Azul), cada um escrito como 2 dígitos hex (porque `255 = 0xFF`, o maior valor que
2 dígitos hex representam — `16² - 1`). Decompondo `#FF5733`: `FF` = 255 (vermelho no máximo),
`57` = `5·16 + 7 = 87` (verde), `33` = `3·16 + 3 = 51` (azul). É a mesma conversão hex→decimal
de sempre, só que em pares de dígitos em vez de um número inteiro de uma vez.

`[TENTE VOCÊ]` Decomponha a cor `#1A2B3C` em R, G, B decimais.
Resposta: R = `0x1A` = `1·16+10 = 26`; G = `0x2B` = `2·16+11 = 43`; B = `0x3C` = `3·16+12 = 60`.

## 8. Soma e subtração binária

A soma binária segue a mesma lógica da soma decimal — o que muda é **quando** o vai-um acontece.
Em qualquer base, o vai-um ocorre quando a soma de uma posição alcança o valor da própria base:
em decimal (base 10), isso acontece quando a soma da posição chega a 10 (`9 + 2 = 11`: escreve
`1`, vai um `1`); em binário (base 2), o mesmo bate muito mais cedo, em `1 + 1 = 10` (escreve `0`,
vai um `1`).

```
  0111   (7)
+ 0101   (5)
------
  1100   (12)
```

`[ATENÇÃO]` Ao somar de cabeça, é fácil esquecer de carregar o vai-um adiante — principalmente
quando ele se repete em cadeia, posição após posição, como acontece nas duas primeiras posições
da direita neste exemplo. Confira sempre da direita pra esquerda, carregando explicitamente cada
vai-um antes de somar a próxima coluna.

`[TENTE VOCÊ]` Some `0110 + 0011` sozinho, prestando atenção em cada vai-um.
Resposta: `1001` (9).

**Quando o vai-um "propaga" por várias colunas seguidas** — o caso que mais gera erro de conta —
some `0111 + 0001`:
```
  0111   (7)
+ 0001   (1)
------
  1000   (8)
```
Coluna 1: `1+1 = 10` → escreve `0`, vai-um `1`. Coluna 2: `1+0+vai-um(1) = 10` → escreve `0`,
vai-um `1` de novo. Coluna 3: `1+0+vai-um(1) = 10` → escreve `0`, vai-um `1` mais uma vez.
Coluna 4: `0+0+vai-um(1) = 1` → escreve `1`. O vai-um "empurrou" a soma por três colunas seguidas
antes de parar — é exatamente esse efeito em cadeia que o `[ATENÇÃO]` acima avisa: parar de
carregar o vai-um no meio da cadeia (ex: esquecer na coluna 3) dá um resultado errado sem parecer
óbvio que algo quebrou.

`[TENTE VOCÊ]` Some `1111 + 0001`, acompanhando o vai-um se propagar por toda a soma.
Resposta: `10000` (16) — o vai-um propaga pelas 4 colunas.

**Subtração binária** segue o espelho da soma: em decimal, quando o dígito de cima é menor que o
de baixo, você "empresta" 1 da próxima coluna (ex: em `32 - 17`, pra fazer `2 - 7` você empresta,
vira `12 - 7 = 5`). Em binário, o mesmo empréstimo acontece — só que emprestar de uma coluna
binária vale `2`, não `10`.

Acompanhe `0110 - 0011` (6 − 3):
```
  0110   (6)
- 0011   (3)
------
  0011   (3)
```
Coluna 1 (direita): `0 - 1` não dá — empresta da coluna 2: vira `10 - 1 = 1` (escreve `1`, deve 1
pra coluna 2). Coluna 2: tinha `1`, já deve 1, sobra `0`; `0 - 1` não dá de novo — empresta da
coluna 3: vira `10 - 1 = 1` (escreve `1`, deve 1 pra coluna 3). Coluna 3: tinha `1`, já deve 1,
sobra `0`; `0 - 0 = 0` (escreve `0`). Coluna 4: `0 - 0 = 0`. Resultado: `0011 = 3`. Confere:
`6 - 3 = 3`.

`[ATENÇÃO]` Na prática, processadores raramente implementam um circuito de subtração separado —
eles somam usando o **complemento de 2** do número a subtrair (você vai ver exatamente como e por
que na seção 10). Vale entender o empréstimo manual primeiro, porque é mais intuitivo — mas saiba
que "por baixo dos panos" a subtração vira uma soma disfarçada.

`[TENTE VOCÊ]` Subtraia `1010 - 0011` (10 − 3) usando empréstimo, coluna por coluna.
Resposta: `0111` (7).

## 9. Overflow

Todo tipo de dado tem um número fixo de bits reservados pra ele — e isso significa um limite
máximo de valores representáveis (lembra do `2ⁿ` da seção 3?). **Overflow** é o que acontece
quando uma conta ultrapassa esse limite: o valor "roda" e volta pro começo, como um odômetro de
carro que passa de `999999` e volta pro `000000`.

**Exemplo narrado:** imagine um tipo de 8 bits sem sinal (`unsigned char` em C++, que você vai ver
no Módulo 08) — representa de `0` a `255` (`2⁸ - 1`). Se um programa tem uma variável desse tipo
guardando `255` e soma `1`, matematicamente o resultado seria `256` — mas `256` não cabe em 8
bits. O que sobra é só a parte que cabe: `256` em binário é `1 0000 0000` (9 bits), e como só há
espaço pra 8, o bit mais significativo é descartado, sobrando `0000 0000` — o valor "estourou" e
voltou pra `0`.

`[ATENÇÃO]` Overflow não gera um erro/aviso automático na maioria das linguagens — o programa
continua rodando normalmente, só que com um valor errado. É um dos bugs mais traiçoeiros de
encontrar justamente por isso: nada "quebra" visivelmente.

`[TENTE VOCÊ]` Um tipo de 4 bits sem sinal representa de `0` a `15`. Se ele guarda `15` e soma
`2`, qual o resultado após o overflow? Resposta: `17` em binário são 5 bits (`10001`); descartando
o bit mais significativo (que não cabe), sobra `0001` = `1`.

## 10. Complemento de 2

A seção anterior tratou de tipos **sem sinal** (só positivos). Mas como representar números
**negativos** em binário, se só existem os símbolos `0` e `1` — sem um símbolo de "menos"?

A solução universal é o **complemento de 2**. A ideia: reservar o bit mais significativo pra
indicar o sinal (`0` = positivo, `1` = negativo), e construir o valor negativo de um jeito que
faça a soma funcionar automaticamente, sem precisar de um circuito de subtração separado.

**Como construir o complemento de 2 de um número** (em 8 bits, por exemplo): pegue o número
positivo, **inverta todos os bits** (0 vira 1, 1 vira 0— isso chama-se complemento de 1), e
**some 1** ao resultado.

Exemplo — representar `-5` em 8 bits:
```
5 em binário (8 bits):        0000 0101
Inverte todos os bits:        1111 1010   (complemento de 1)
Soma 1:                     + 0000 0001
                             -----------
                               1111 1011   → isso é -5 em complemento de 2
```

`[TENTE VOCÊ]` Some `5 + (-5)` usando as representações binárias acima (`0000 0101 + 1111 1011`),
ignorando o vai-um que "sobra" além de 8 bits (ele é descartado). Resposta: `0000 0000` — deu
zero, exatamente como `5 + (-5)` deveria dar. É por isso que o complemento de 2 funciona: soma
comum, sem lógica especial, já resolve subtração.

`[ATENÇÃO]` No complemento de 2, o bit mais significativo em `1` não significa "valor grande" como
num número sem sinal — significa "negativo". É por isso que um `int` (com sinal) e um `unsigned
int` do mesmo tamanho em bits têm faixas de valores diferentes, mesmo ocupando o mesmo espaço.

## 11. ASCII / Unicode / UTF-8

Números binários representam quantidades — mas como uma **letra** vira número, pro computador
guardar? A resposta é uma tabela de correspondência combinada previamente entre todo mundo.

A primeira tabela amplamente adotada foi a **ASCII** (1963): associa cada letra do alfabeto
latino (maiúscula e minúscula), dígitos, pontuação e alguns caracteres de controle a um número de
**7 bits** (0 a 127) — por exemplo, `'A'` = `65`, `'a'` = `97`, `'0'` = `48`.

`[TENTE VOCÊ]` Sabendo que `'A' = 65`, e que o alfabeto é sequencial na tabela ASCII, qual o
código de `'D'`? Resposta: `68` (`A=65, B=66, C=67, D=68`).

O problema: ASCII cobre só o alfabeto latino básico — não representa `ç`, `ã`, `€`, emoji, nem
alfabetos como cirílico, árabe ou mandarim. A solução moderna é o **Unicode**: um padrão universal
que atribui um número único (chamado *code point*) pra praticamente todo caractere usado por
qualquer sistema de escrita humano, incluindo emoji.

Só que Unicode define *quais números* representam cada caractere — não define *como esses
números viram bytes* pra guardar em arquivo ou mandar pela rede. Essa segunda parte é papel de
uma **codificação**, e a mais usada hoje é a **UTF-8**: usa de 1 a 4 bytes por caractere,
dependendo do caractere — os primeiros 128 code points (que coincidem exatamente com a tabela
ASCII original) usam só 1 byte, mantendo total compatibilidade com arquivos ASCII antigos;
caracteres acentuados ou de outros alfabetos usam 2-4 bytes.

`[ATENÇÃO]` Um arquivo salvo com codificação errada (ex: gerado como UTF-8 mas lido como se fosse
outra codificação) mostra caracteres corrompidos em acentos — é o clássico "Ã§Ã£o" no lugar de
"ção". Não é um erro de digitação: é um byte sendo interpretado com a tabela errada.

## 12. Representação de ponto flutuante

Números com casas decimais também usam a ideia de "posição vale uma potência da base", que você
já usou pra parte inteira — só que agora com potências **negativas**: a primeira casa depois da
vírgula binária vale `2⁻¹` (0,5), a segunda `2⁻²` (0,25), e assim por diante.

O problema é que nem toda fração decimal tem representação binária finita nesse esquema — do
mesmo jeito que nem toda fração tem representação decimal finita (`1/3`, por exemplo, vira uma
dízima infinita em base 10). O motivo é aritmético: `0,1` decimal equivale à fração `1/10`, e
`10 = 2 × 5`. Como o fator `5` não é potência de 2, essa fração nunca "fecha" em binário — vira
uma dízima infinita, do mesmo jeito que `1/3` faz em decimal (porque `3` não é fator de `10`).
Quando o computador guarda essa dízima infinita num número finito de bits, ela precisa ser
cortada em algum ponto — e é esse corte que gera o pequeno erro de arredondamento. Por isso
`0.1 + 0.2` acumula um erro e não dá exatamente `0.3`.

Esse não é um "bug" da linguagem: é uma limitação inerente de como frações são armazenadas em
qualquer base finita — só que, como o hardware usa base 2, ela aparece até em frações decimais
"redondas" como `0,1`, que não são redondas nenhuma pro binário.

## 13. IEEE 754

A seção anterior explicou *por que* ponto flutuante é impreciso — esta explica *como* ele é
armazenado de fato. O padrão **IEEE 754** define o formato usado por quase toda linguagem de
programação moderna, dividindo os bits em três partes.

Para um `float` de 32 bits:

| Parte | Tamanho | Função |
|---|---|---|
| Sinal | 1 bit | `0` = positivo, `1` = negativo |
| Expoente | 8 bits | "desloca" a vírgula, com um deslocamento (*bias*) de 127 somado |
| Mantissa | 23 bits | os dígitos significativos do número, em binário |

`[APROFUNDAMENTO]` O IEEE 754 também reserva combinações especiais de bits pra representar
valores que não são números "normais": infinito positivo/negativo (resultado de dividir por
zero) e `NaN` ("Not a Number", resultado de operações inválidas tipo `0/0`). Isso explica por que
uma divisão por zero em ponto flutuante não trava o programa como uma divisão inteira por zero
faria — ela retorna um valor especial em vez de um erro.

`[CLI]` A ferramenta [float.exposed](https://float.exposed/) mostra, bit a bit, como um número
decimal fica armazenado nas três partes acima — vale digitar `0.1` lá e ver a mantissa sendo
cortada de verdade.

## 14. Exercícios práticos

Tudo que você viu até aqui (conversões entre as quatro bases, soma/subtração binária, overflow,
complemento de 2, ASCII/Unicode) tem exercícios correspondentes em
[03_sistemas-numeracao-pratica.md](03_sistemas-numeracao-pratica.md) — a leitura sozinha não
fixa esses mecanismos; é resolvendo na mão, com o raciocínio explícito, que a intuição fica.

## 15. Aplicações em programação

- **Tipos de dados**: o tamanho em bits de um tipo (`char`, `int`, `long`...) define diretamente
  seu intervalo de valores — e por isso onde overflow pode acontecer (Módulo 08).
- **Strings e caracteres**: toda string que você manipula em código é, por baixo, uma sequência
  de bytes codificados (geralmente UTF-8) — é por isso que "tamanho de uma string" pode significar
  coisas diferentes (quantidade de caracteres vs. quantidade de bytes) quando há acentos.
- **Máscaras de bits e flags**: operações bit a bit (`&`, `|`, `^`) sobre a representação binária
  de um número são usadas pra guardar várias opções `sim/não` num único inteiro, de forma
  compacta — comum em permissões e configurações de baixo nível.

## 16. Aplicações em redes e Circuitos Digitais

Este módulo termina onde os dois próximos começam. No **Módulo 04 (Circuitos Digitais)**, você
vai ver como portas lógicas físicas operam diretamente sobre esses mesmos bits — um circuito AND,
OR, XOR não entende "números", só entende `0` e `1` chegando em fios. No **Módulo 07 (Redes de
Computadores e Web)**, endereços IP e portas — que parecem números decimais comuns (tipo
`192.168.1.1`) — são, por baixo, exatamente os mesmos conceitos de representação binária vistos
aqui: um endereço IPv4 é só 32 bits agrupados em 4 octetos de 8 bits cada, escritos em decimal por
convenção de leitura humana.

- **Endereçamento**: endereços de memória são quase sempre exibidos em hexadecimal, por ser mais
  compacto que binário e mais preciso que decimal para representar múltiplos de potências de 2.
- **Transmissão de dados**: velocidades de rede e tamanhos de arquivo são medidos em bits/bytes —
  entender a base binária explica por que 1 KB "prático" (1024 bytes) difere do 1 KB "comercial"
  (1000 bytes).
- **Controle**: máscaras de bits e *flags* (usadas em permissões de arquivo, registradores de
  status de CPU, etc.) são operações diretas sobre a representação binária de um número.

## Erros comuns

Você já viu estes avisos ao longo do módulo — aqui vai só a revisão rápida:

- **Confundir "quantidade de bits" com "quantidade de valores representáveis"**: `n` bits
  representam `2ⁿ` valores, não `n` valores (seção 3).
- **Esquecer o vai-um na soma binária**, especialmente quando ele se repete em cadeia por várias
  posições (seção 8).
- **Achar que overflow gera um erro visível** — na maioria das linguagens ele é silencioso, o
  valor só fica errado (seção 9).
- **Confundir o bit de sinal do complemento de 2 com "valor grande"** — ele indica negativo, não
  magnitude (seção 10).
- **Achar que ponto flutuante representa qualquer número decimal com exatidão** — a limitação é
  aritmética, não um defeito de implementação (seções 12-13).

## Conexão com os próximos módulos

| Conceito deste módulo | Reaparece em |
|---|---|
| Bits e portas lógicas | Módulo 04 — Circuitos Digitais |
| Endereçamento em hexadecimal | Módulo 05 — Arquitetura de Computadores |
| Octal em permissões de arquivo | Módulo 06 — Sistemas Operacionais (`chmod`) |
| Overflow, complemento de 2 e representação de tipos | Módulo 08 — Linguagens de Programação |
| ASCII/UTF-8 em strings | Módulo 08, 13 — manipulação de texto em C++/JavaScript |
| Bits em endereços IP | Módulo 07 — Redes de Computadores e Web |

## `[REFERÊNCIA]`

- BROOKSHEAR, J. Glenn. *Ciência da Computação — Uma Visão Abrangente*, 7ª ed., Bookman, 2005 —
  Capítulo 1 (Armazenamento e Manipulação de Dados).
- VELLOSO, Fernando de Castro. *Informática: Conceitos Básicos*, 6ª ed., Campus, 2002.
- [IEEE 754 explicado visualmente](https://float.exposed/) — ferramenta interativa que mostra bit
  a bit como um número em ponto flutuante é armazenado.
- [RapidTables — Conversor binário/decimal/hexadecimal/octal](https://www.rapidtables.com/convert/number/binary-to-decimal.html) —
  para conferir suas conversões manuais.
- [Unicode.org — O que é Unicode](https://home.unicode.org/basic-info/faq/) — perguntas frequentes
  oficiais sobre o padrão.
- [MDN — Codificação de caracteres em JavaScript/UTF-8](https://developer.mozilla.org/pt-BR/docs/Glossary/UTF-8) —
  explicação prática de codificação de texto.

## Checklist de saída

- [ ] Converto um número decimal para binário, octal e hexadecimal manualmente — e sei explicar
      por que o método funciona, não só executá-lo.
- [ ] Converto binário/octal/hexadecimal de volta para decimal.
- [ ] Somo e subtraio dois números binários, aplicando vai-um/empréstimo corretamente.
- [ ] Explico o que é overflow e por que ele costuma ser silencioso.
- [ ] Construo o complemento de 2 de um número e explico por que ele faz subtração virar soma.
- [ ] Explico a diferença entre ASCII, Unicode e UTF-8, e por que uma é necessária.
- [ ] Entendo, em termos gerais, por que ponto flutuante tem imprecisão, e sei localizar as três
      partes do IEEE 754 (sinal, expoente, mantissa) num número.
- [ ] Sei por que `n` bits representam `2ⁿ` valores, não `n` valores.
