---
id: 05_arquitetura-computadores-teoria
title: "Módulo 05 — Arquitetura de Computadores"
sidebar_position: 50
---

# Módulo 05 — Arquitetura de Computadores

> **Objetivo:** entender os componentes de um computador (CPU, memória, E/S, barramentos), como
> uma instrução é buscada e executada, e como essas peças são organizadas — da ALU até CPUs
> modernas com múltiplos núcleos.
> **Pré-requisitos:** Módulo 04 (Circuitos Digitais).
> **Tempo de referência:** 6 a 8 horas.
> **Prática correspondente:** [05_arquitetura-computadores-pratica.md](05_arquitetura-computadores-pratica.md)

---

## 1. Por que isso importa

No módulo 04 você montou, na teoria, um meio-somador — duas portas lógicas (XOR e AND) somando
dois bits — e viu flip-flops guardando 1 bit de estado. Este módulo responde à pergunta natural
que fica depois disso: como uma pilha desses circuitos vira uma máquina que executa um programa
inteiro? A resposta conecta os bits e portas dos módulos 03 e 04 a uma arquitetura funcional, e
prepara o terreno para entender o papel do sistema operacional (módulo 06) como intermediário
entre esse hardware e as aplicações.

## 2. O que é arquitetura de computadores

Arquitetura de computadores é o estudo de como os componentes de hardware (CPU, memória,
barramentos, dispositivos de E/S) são projetados e organizados para executar programas. Não é
sobre construir um circuito específico (isso já foi visto no módulo 04) — é sobre como circuitos
prontos (ULA, registradores, memória) se conectam e cooperam pra formar uma máquina programável de
propósito geral.

## 3. Arquitetura vs organização

Esses dois termos parecem sinônimos, mas descrevem coisas diferentes: **arquitetura** é o que o
programador enxerga e pode contar com (o conjunto de instruções disponíveis, os registradores
visíveis, como a memória é endereçada) — é o "contrato". **Organização** é como esse contrato é
implementado por dentro (quantos núcleos, como o pipeline funciona, quanto de cache existe) — é a
"implementação".

`[TENTE VOCÊ]` Intel e AMD fabricam processadores com a mesma arquitetura x86/x64 (o mesmo
conjunto de instruções), mas com organizações internas diferentes (pipelines, caches e
quantidades de núcleos diferentes). Isso explica por que um programa compilado pra x86 roda nos
dois fabricantes, mas com desempenhos diferentes? Resposta: sim — a arquitetura (o "vocabulário"
de instruções) é compatível, então o mesmo programa roda nos dois; a organização (como cada
fabricante implementa esse vocabulário por dentro) é que determina a velocidade.

## 4. Componentes de um computador

Todo computador, por mais simples ou complexo que seja, é feito de quatro tipos de peça:

- **CPU**: o "cérebro" — processa instruções e dados.
- **Memória**: armazena programas e dados, em diferentes níveis de velocidade/capacidade (você
  vai ver a hierarquia completa mais adiante).
- **Dispositivos de E/S**: tudo que entra ou sai da máquina — teclado, tela, disco, rede.
- **Barramentos**: os "fios" que conectam essas três peças entre si.

O resto deste módulo é, essencialmente, abrir cada uma dessas quatro caixas.

## 5. CPU

A CPU (Central Processing Unit) é dividida em três partes principais, que você vai ver em detalhe
nas próximas seções: a **Unidade de Controle** (coordena tudo), a **ULA** (faz as contas) e os
**registradores** (guardam os valores em uso no momento). Pense na CPU como uma linha de produção
pequena: a Unidade de Controle é o supervisor lendo a próxima ordem de serviço, a ULA é a máquina
que executa o trabalho, e os registradores são a bandeja onde as peças ficam enquanto são
processadas.

## 6. Unidade de Controle

A Unidade de Controle não faz contas — ela **coordena**. É responsável por buscar a próxima
instrução na memória (usando o Program Counter, seção 9), decodificar o que ela pede, e acionar
as outras partes da CPU (ULA, registradores, barramentos) na ordem certa pra executar essa
instrução. É o mesmo papel de um maestro: não toca nenhum instrumento, mas sem ele a orquestra não
sabe quando cada parte entra.

## 7. Unidade Lógica e Aritmética (ALU)

A ULA (ou ALU, em inglês) é, literalmente, uma coleção de circuitos como os que você montou no
módulo 04 — somadores, comparadores, portas lógicas — combinados pra executar operações
aritméticas (soma, subtração, multiplicação) e lógicas (AND, OR, comparações) sob comando da
Unidade de Controle. Quando a Unidade de Controle decide "esta instrução é uma soma", é a ULA
quem efetivamente soma os dois valores.

`[TENTE VOCÊ]` Se a instrução for "compare X com Y e diga se são iguais", quem faz esse trabalho:
a Unidade de Controle ou a ULA? Resposta: a ULA — comparar é uma operação lógica, e a Unidade de
Controle só identifica que essa é a instrução a executar e aciona a ULA pra fazer a comparação de
fato.

## 8. Registradores

Registradores são a memória mais rápida que existe num computador — ficam dentro da própria CPU,
fisicamente a poucos milímetros da ULA, feitos de flip-flops encadeados exatamente como você viu
no módulo 04. Guardam os valores que a CPU está usando *agora*: os operandos de uma operação, o
resultado, o endereço da próxima instrução. São poucos (algumas dezenas, tipicamente) e pequenos
(32 ou 64 bits cada, na maioria das CPUs modernas), mas sua proximidade física com a ULA é o que
os torna praticamente instantâneos de acessar — sem essa velocidade, a ULA ficaria esperando dado
chegar da memória a cada operação.

## 9. Program Counter

O Program Counter (PC) é um registrador com um único trabalho: guardar o endereço de memória da
**próxima** instrução a ser buscada. A cada ciclo fetch-decode-execute (seção 26), depois que uma
instrução é buscada, o PC avança automaticamente pra apontar pra próxima — é o que garante que o
programa seja executado em ordem, uma instrução de cada vez.

`[ATENÇÃO]` Instruções de desvio (como um `if` ou um loop, em código de mais alto nível) funcionam
justamente sobrescrevendo o valor do PC pra um endereço diferente do "próximo em sequência" — é
assim que um programa consegue pular partes do código ou repetir um trecho, em vez de só andar em
linha reta pela memória.

## 10. Instruction Register

O Instruction Register (IR) é o registrador que guarda a instrução que acabou de ser buscada da
memória (pelo PC), enquanto ela está sendo decodificada e executada. Separar "onde está a próxima
instrução" (PC) de "qual é a instrução que estou processando agora" (IR) é o que permite o PC já
avançar pra próxima posição enquanto a Unidade de Controle ainda está decodificando a instrução
atual guardada no IR.

## 11. Flags

Flags são registradores de 1 bit (ou um grupo deles) que guardam informações sobre o resultado da
última operação da ULA — por exemplo, uma flag "zero" que liga quando o resultado de uma
subtração deu exatamente zero, ou uma flag "carry" que liga quando uma soma estourou o tamanho do
registrador. Instruções de desvio condicional (seção 9) leem essas flags pra decidir se devem ou
não alterar o PC — é assim que um `if` de uma linguagem de alto nível vira, no fundo, "compare,
guarde o resultado numa flag, e desvie o PC dependendo dela".

`[TENTE VOCÊ]` Depois de executar "compare o registrador X com zero" (do exemplo do
fetch-decode-execute mais adiante), qual flag provavelmente liga se X for igual a zero? Resposta:
a flag "zero" — é exatamente pra isso que ela existe: sinalizar quando um resultado de comparação
ou operação deu zero.

## 12. Clock da CPU

Assim como os circuitos sequenciais do módulo 04 só mudam de estado em sincronia com um clock, a
CPU inteira é sincronizada por um clock — um sinal elétrico que pulsa em uma frequência constante
(medida em GHz, bilhões de pulsos por segundo), determinando o ritmo em que cada etapa do ciclo
fetch-decode-execute pode avançar. Um clock de 3 GHz não significa necessariamente "3 bilhões de
instruções por segundo" (várias etapas internas podem levar mais de um pulso, e CPUs modernas
executam mais de uma instrução por pulso via pipeline — seção 49) — significa "3 bilhões de
pulsos de sincronização por segundo".

## 13. Arquitetura de Von Neumann

Imagine cozinhar numa bancada onde a receita escrita e os ingredientes ficam no mesmo espaço
físico — você usa a mesma bancada tanto para ler o próximo passo quanto para pegar o próximo
ingrediente. Na arquitetura de Von Neumann — a base da maioria dos computadores atuais —
acontece algo parecido: programa (a "receita", em forma de instruções) e dados (os
"ingredientes") compartilham a mesma memória.

Isso simplifica o projeto do hardware (uma única forma de acessar memória serve pros dois casos),
mas cria um gargalo: CPU e memória se comunicam por um único barramento compartilhado, então a
velocidade da CPU fica sempre limitada pela velocidade de acesso a essa memória — do mesmo jeito
que, na cozinha, você não consegue ler a receita e pegar um ingrediente ao mesmo tempo se os dois
estão no mesmo espaço apertado.

**Exemplo narrado:** imagine somar 1000 números guardados na memória, um registrador acumulando o
total. Pra cada número, a CPU precisa fazer duas viagens até a memória pelo mesmo barramento
compartilhado: uma pra buscar a *instrução* ("some o próximo valor"), outra pra buscar o *dado*
(o número em si). Com 1000 números, isso são 2000 viagens disputando o mesmo caminho único —
cada viagem espera a anterior liberar o barramento. Se existissem dois barramentos separados (um
só pra instruções, outro só pra dados — o que existe de fato em arquiteturas Harvard, usadas em
alguns microcontroladores), essas viagens poderiam acontecer em paralelo, cortando pela metade o
tempo gasto só em tráfego de memória. É exatamente esse "espaço apertado" da bancada compartilhada
que o gargalo de Von Neumann descreve.

`[TENTE VOCÊ]` Por que um computador com arquitetura Harvard (barramentos separados) não sofre do
mesmo gargalo? Resposta: porque buscar a instrução e buscar o dado não competem pelo mesmo
caminho físico — podem acontecer ao mesmo tempo, em vez de na fila, um de cada vez.

## 14. CPU, memória e barramentos

CPU e memória não se conectam por um cabo genérico — se conectam por três grupos de linhas
elétricas com papéis diferentes, chamados coletivamente de barramento do sistema. Entender os
três separadamente explica como a CPU consegue dizer *o quê* transportar, *para onde*, e
*quando*.

## 15. Barramento de dados

O barramento de dados é por onde o valor em si trafega — os bits do número, instrução ou
caractere sendo lido ou escrito. A largura desse barramento (32 ou 64 bits, tipicamente) limita
quantos bits podem viajar de uma vez: um barramento de 64 bits transporta um valor de 64 bits por
viagem; um de 32 bits precisaria de duas viagens pro mesmo valor.

## 16. Barramento de endereços

O barramento de endereços carrega **onde**, na memória, o dado do barramento de dados deve ser
lido ou escrito. A largura desse barramento determina o limite teórico de memória endereçável —
reconecte com o módulo 03: um barramento de endereços de `n` bits consegue endereçar `2ⁿ`
posições distintas de memória (é a mesma relação de "`n` bits representam `2ⁿ` valores" que você
já viu lá).

`[TENTE VOCÊ]` Um barramento de endereços de 32 bits consegue endereçar, no máximo, `2³²` bytes —
cerca de 4 GB. Isso explica por que sistemas operacionais de 32 bits historicamente não
conseguiam usar mais de ~4 GB de RAM, mesmo que o computador tivesse mais instalada? Resposta:
sim — o limite não é da RAM em si, é de quantos endereços distintos o barramento de endereços
consegue representar com 32 bits.

## 17. Barramento de controle

O barramento de controle carrega os sinais de coordenação: "isso é uma leitura ou uma escrita?",
"o dado já está pronto no barramento de dados?", interrupções (seção 45), sinais de clock. Se o
barramento de dados é "o quê" e o de endereços é "onde", o de controle é o "como e quando" — os
sinais que sincronizam os outros dois.

## 18. Instruções de máquina

Uma instrução de máquina é a unidade mínima de trabalho que uma CPU sabe executar diretamente —
um padrão de bits que, decodificado, significa algo como "some estes dois registradores" ou
"carregue este endereço de memória num registrador". Todo programa, não importa em que linguagem
foi originalmente escrito (C++, Python, JavaScript...), termina virando uma sequência dessas
instruções antes de rodar — é o "menor denominador comum" que todo hardware entende.

## 19. Instruction Set Architecture (ISA)

A ISA é o **vocabulário completo** de instruções de máquina que uma família de CPUs entende — é
literalmente a "arquitetura" da seção 3: o contrato entre hardware e software. x86/x64, ARM e
RISC-V (seções 23-25) são três ISAs diferentes — um programa compilado pra uma delas não roda
diretamente nas outras, porque as próprias instruções binárias que a CPU entende são diferentes.

## 20. Assembly

Assembly é a forma legível por humano das instruções de máquina de uma ISA — cada linha de
Assembly corresponde, quase sempre, a exatamente uma instrução binária que a CPU executa. É o elo
mais direto entre o código que um programador escreve e o que a CPU realmente faz — o oposto do
que você viu no módulo 08 sobre linguagens de alto nível, onde uma linha de código pode virar
dezenas de instruções.

**Exemplo narrado — um trecho mínimo em Assembly x86:**
```
MOV AX, 5      ; carrega o valor 5 no registrador AX
ADD AX, 3      ; soma 3 ao valor que está em AX (AX agora vale 8)
```
Cada linha aqui é, literalmente, uma instrução que passa pelo ciclo fetch-decode-execute completo
(seção 26): a instrução `MOV AX, 5` é buscada da memória, decodificada como "carregar um valor
imediato num registrador", e executada colocando `5` em `AX`.

`[TENTE VOCÊ]` Quantos ciclos completos de fetch-decode-execute o trecho acima dispara? Resposta:
2 — uma instrução por linha, cada uma passando pelo ciclo inteiro.

## 21. CISC

CISC (Complex Instruction Set Computer) é uma filosofia de ISA: poucas instruções, mas cada uma
capaz de fazer bastante coisa de uma vez — como um manual de montagem de móvel que diz "monte a
lateral esquerda completa" numa única instrução, em vez de detalhar cada parafuso. x86/x64 (seção
23) é o exemplo mais usado hoje.

## 22. RISC

RISC (Reduced Instruction Set Computer) é a filosofia oposta: muitas instruções, mas cada uma
simples e de tamanho fixo — como um manual que detalha "pegue o parafuso A", "encaixe na posição
1", "aperte", separadamente. ARM e RISC-V (seções 24-25) seguem essa filosofia.

| | CISC | RISC |
|---|---|---|
| Instruções | Poucas, complexas (uma instrução pode fazer várias coisas) | Muitas, simples e de tamanho fixo |
| Exemplo | x86 (Intel/AMD) | ARM (celulares, Apple Silicon), RISC-V |
| Trade-off | Menos instruções por programa, decodificação mais complexa | Mais instruções por programa, decodificação mais simples e rápida |

Nenhuma abordagem "vence" — cada uma otimiza um lado diferente do mesmo ciclo fetch-decode-execute
(seção 26): CISC economiza no número de instruções buscadas, RISC economiza no tempo de
decodificar cada uma.

**Exemplo narrado:** pegue a operação "multiplique o valor da memória M1 pelo valor da memória M2,
e some o resultado ao valor de M3". Num processador CISC, isso pode existir como **uma única
instrução complexa** (`MULADD M1, M2, M3`) que internamente já sabe buscar os três valores,
multiplicar e somar — o programador escreve uma linha, o hardware faz o resto em vários passos
escondidos. Num processador RISC, a mesma operação vira **várias instruções simples em
sequência**, cada uma fazendo uma coisa só: `CARREGAR M1 em R1`, `CARREGAR M2 em R2`,
`MULTIPLICAR R1 por R2, guardar em R3`, `CARREGAR M3 em R4`, `SOMAR R3 com R4, guardar em R5`,
`GUARDAR R5 de volta na memória`. O resultado final é o mesmo — a diferença é onde mora a
complexidade: escondida numa instrução gorda (CISC) ou explícita em várias instruções magras
(RISC).

`[TENTE VOCÊ]` Nesse exemplo, quantas "viagens" de fetch-decode-execute o processador RISC precisa
fazer, contra quantas o CISC precisa? Resposta: RISC faz 6 ciclos completos (uma instrução por
viagem); CISC faz só 1 ciclo, mas com uma etapa de decodificação bem mais complexa dentro dele —
o trabalho não desaparece, só muda de lugar.

## 23. x86/x64

x86 (e sua extensão de 64 bits, x64/x86-64) é a ISA CISC criada pela Intel nos anos 1970-80,
dominante em PCs e servidores tradicionais até hoje (Intel e AMD ambos fabricam CPUs x86/x64
compatíveis entre si). É a arquitetura que roda a maioria dos notebooks e desktops Windows/Linux
convencionais.

## 24. ARM

ARM é a ISA RISC por trás de praticamente todo celular do mundo, e também dos chips Apple
Silicon (M1, M2, M3...) usados nos Macs atuais. A ARM Holdings não fabrica chips — licencia o
design da ISA pra outras empresas (Apple, Qualcomm, Samsung) fabricarem seus próprios
processadores compatíveis. O apelo de ARM em dispositivos móveis é eficiência energética: menos
instruções complexas por ciclo significa, tipicamente, menos energia consumida — importante numa
bateria.

## 25. RISC-V

RISC-V é uma ISA RISC mais recente, com uma diferença fundamental em relação a x86 e ARM: é
**aberta e livre de royalties** — qualquer empresa pode implementar um chip RISC-V sem pagar
licença, ao contrário de x86 (controlada pela Intel/AMD) ou ARM (licenciada pela ARM Holdings).
Isso tem impulsionado adoção crescente em microcontroladores, e cada vez mais em chips maiores.

`[REFERÊNCIA]` [RISC-V International](https://riscv.org/) — organização sem fins lucrativos que
mantém a especificação aberta da ISA.

## 26. Ciclo Fetch-Decode-Execute

Uma dúvida comum de quem está começando é imaginar que o computador "carrega o programa inteiro e
roda tudo de uma vez". Não é assim: toda instrução passa, uma de cada vez, por três etapas
repetidas continuamente — cada uma detalhada nas próximas três seções.

`[ATENÇÃO]` É fácil imaginar a CPU "executando o programa inteiro de uma vez" — mas o que
realmente acontece é este ciclo de três etapas se repetindo, uma instrução por vez, várias
centenas de milhões (ou bilhões) de vezes por segundo. A sensação de "tudo ao mesmo tempo" é só
efeito da velocidade.

## 27. Fetch

A Unidade de Controle (seção 6) busca, na memória, a instrução que está no endereço apontado pelo
Program Counter (seção 9), e a coloca no Instruction Register (seção 10).

## 28. Decode

A instrução que acabou de chegar ao Instruction Register é interpretada — a Unidade de Controle
identifica qual operação ela pede (soma? comparação? carregar um valor?) e quais registradores ou
endereços de memória são os operandos.

## 29. Execute

A ULA (seção 7) executa a operação identificada no decode, e o resultado é armazenado onde a
instrução indicar — um registrador, ou de volta na memória. Em seguida, o PC avança pra próxima
instrução, e o ciclo recomeça.

## 30. Como uma CPU executa uma instrução

**Exemplo narrado, juntando as três etapas:** suponha a instrução "some o valor do registrador A
com o registrador B, e guarde o resultado em C". No fetch, a Unidade de Controle busca essa
instrução na memória, no endereço apontado pelo PC, e a coloca no IR. No decode, ela identifica:
"isso é uma soma, os operandos são A e B, o destino é C". No execute, a ULA executa a soma de
fato, e o resultado é escrito no registrador C. Só depois disso o PC avança para a próxima
instrução, e o ciclo recomeça — instrução por instrução, nunca "tudo de uma vez".

`[TENTE VOCÊ]` Descreva as três etapas do ciclo para a instrução "compare o valor do registrador
X com zero". Resposta esperada: fetch busca essa instrução no endereço do PC e a coloca no IR;
decode identifica que é uma comparação, com X e a constante 0 como operandos; execute manda a ULA
comparar os dois valores e guarda o resultado numa flag (seção 11, ex: a flag "zero").

## 31. Hierarquia de memória

Pense em como você organiza objetos pela frequência de uso: o que você usa a cada minuto fica em
cima da mesa; o que usa algumas vezes por dia, numa gaveta perto; o que usa raramente, num
armário longe. Quanto mais perto de você, menos cabe — mas mais rápido você alcança. A memória de
um computador segue exatamente essa lógica, do mais rápido/menor ao mais lento/maior:

```
Registradores → Cache (L1, L2, L3) → RAM → Armazenamento (SSD/HD)
```

O princípio por trás dessa hierarquia é a **localidade**: dados usados recentemente (ou perto de
dados usados recentemente) tendem a ser usados de novo em breve, então vale a pena mantê-los mais
perto da CPU — do mesmo jeito que vale a pena manter na mesa o que você vai usar de novo em
segundos, não guardar no armário.

`[TENTE VOCÊ]` Se um programa acabou de ler um valor da RAM e provavelmente vai precisar dele de
novo em milissegundos, pra onde faz sentido movê-lo? Resposta: para a cache — é exatamente o
princípio de localidade em ação.

**Exemplo narrado — noção de escala:** os números abaixo não são exatos (variam por hardware),
mas a ordem de grandeza entre cada nível é o que importa fixar:

| Nível | Tempo de acesso aproximado | Analogia de escala |
|---|---|---|
| Registrador | ~1 ciclo de clock (frações de nanossegundo) | pegar algo que já está na sua mão |
| Cache L1 | poucos nanossegundos | esticar o braço até a mesa |
| RAM | dezenas a ~100 nanossegundos | ir até a gaveta ao lado |
| SSD/disco | centenas de milhares de nanossegundos (microssegundos a milissegundos) | ir até outro cômodo da casa |

Repare o salto: RAM já é dezenas de vezes mais lenta que cache; disco é ordens de grandeza mais
lento que RAM — é esse abismo de velocidade que torna a hierarquia (e a localidade) tão
importante, não só uma questão de organização.

`[TENTE VOCÊ]` Se acessar a cache leva "esticar o braço" e acessar o disco leva "ir a outro
cômodo", por que um programa não guarda tudo direto no disco, evitando a complexidade de vários
níveis? Resposta: porque cada nível troca capacidade por velocidade — disco é gigante mas lento
demais pra ser a única memória usada durante a execução; a hierarquia existe pra manter o que é
usado com frequência nos níveis rápidos, e reservar o disco pro que precisa de espaço, não
velocidade.

## 32. Registradores (no topo da hierarquia)

Você já viu registradores em detalhe na seção 8 — aqui vale só fixar a posição deles na
hierarquia: são o nível mais rápido e menor de todos, o "pegar algo que já está na sua mão" da
tabela acima.

## 33. Cache

Cache é uma memória pequena e rápida, física dentro ou muito perto da CPU, que guarda cópias de
dados da RAM usados recentemente — organizada em níveis (L1 menor e mais rápida, L2 e L3
progressivamente maiores e um pouco mais lentas). Quando a CPU precisa de um dado, ela primeiro
checa a cache; só se não achar lá (um "cache miss") é que vai até a RAM — mais lenta.

## 34. RAM

RAM (Random Access Memory) é a memória geral do sistema — compartilhada por tudo que a CPU
processa: o sistema operacional, o navegador, o jogo, a planilha. É volátil: perde todo o
conteúdo ao desligar. É o nível da hierarquia logo abaixo da cache.

## 35. Memória virtual

Memória virtual é a técnica (implementada pelo sistema operacional, que você vai ver em detalhe
no módulo 06) de dar a cada programa a ilusão de ter a máquina inteira só pra ele, mesmo que
fisicamente vários programas estejam dividindo a mesma RAM — e de permitir usar mais memória do
que a RAM física tem, "emprestando" espaço do disco quando necessário.

## 36. RAM vs VRAM

A RAM que você já viu é a memória geral do sistema. Mas quando o assunto é gráficos (jogos,
edição de vídeo, renderização 3D), existe uma segunda memória, separada, dedicada só a isso: a
**VRAM** (memória de vídeo), que fica fisicamente ao lado da GPU, não da CPU.

O motivo de separar as duas não é capricho — é o mesmo motivo do gargalo de Von Neumann que você
já viu: se GPU e CPU tivessem que disputar a mesma memória pelo mesmo barramento, uma travaria a
outra toda vez que precisasse ler ou escrever um dado. A GPU precisa ler e escrever texturas e
frames inteiros, repetidamente, dezenas de vezes por segundo, em paralelo massivo — um padrão de
acesso totalmente diferente do que a CPU faz. Dar à GPU sua própria memória, otimizada pra esse
padrão, evita que as duas se atravessem.

`[TENTE VOCÊ]` Por que jogos e softwares de edição de vídeo "pesam" mais na VRAM do que na RAM
comum? Resposta: porque o que eles mais manipulam são texturas, frames e dados gráficos —
exatamente o tipo de dado que a GPU processa usando a VRAM, não a RAM geral do sistema.

`[CLI]` No Windows, para ver informações da GPU (incluindo a VRAM disponível), abra a ferramenta
gráfica `dxdiag` (Win+R, digite `dxdiag`, Enter) e veja a aba "Display".

## 37. Armazenamento

Armazenamento é o nível mais lento (e maior/mais barato por GB) da hierarquia de memória — ao
contrário da RAM, não é volátil: mantém os dados mesmo desligado. É onde vivem seus arquivos,
programas instalados, e o próprio sistema operacional quando a máquina está desligada.

## 38. HDD

HDD (Hard Disk Drive) é armazenamento mecânico — discos girando fisicamente a milhares de
rotações por minuto, com um braço/cabeça de leitura se movendo fisicamente até a posição do dado.
É como precisar levantar e caminhar até um armário físico toda vez que precisa de algo.

## 39. SSD

SSD (Solid State Drive) é armazenamento em memória flash — sem nenhuma parte mecânica se
movendo, o dado é lido eletricamente, quase instantaneamente, não importa "onde" ele fisicamente
esteja no chip.

Essa diferença física se traduz em ordens de grandeza de velocidade: um computador com HDD pode
levar dezenas de segundos pra dar boot; o mesmo computador com SSD, poucos segundos — porque não
existe tempo de espera mecânico pra "procurar" o dado. Em troca, SSD custa mais por GB de
capacidade, e HDD ainda é comum quando o que importa é armazenar muito por pouco dinheiro (ex:
servidores de backup) em vez de velocidade.

`[ATENÇÃO]` HDD, por ter partes mecânicas se movendo, é bem mais sensível a impacto físico
(derrubar o computador ligado pode danificar o disco em movimento) — SSD, sem partes móveis, é
muito mais resistente a esse tipo de dano.

`[TENTE VOCÊ]` Por que um SSD não sofre com "tempo de busca" (seek time) da forma que um HDD
sofre? Resposta: porque não existe uma cabeça de leitura física precisando se mover até a posição
do dado — o acesso é elétrico e praticamente instantâneo, independente de onde o dado esteja
guardado no chip.

`[CLI]` No Windows, para ver o modelo e (quando disponível) o tipo de mídia do disco:
```
wmic diskdrive get model,size,mediatype
```
Ou, no PowerShell (mais moderno e detalhado):
```
Get-PhysicalDisk | Select FriendlyName, MediaType, Size
```

## 40. SATA

SATA é uma interface de conexão de armazenamento mais antiga — o "cabo e protocolo" que liga o
disco (HDD ou SSD) à placa-mãe. Foi desenhada numa época em que só existiam HDDs, então seu limite
de velocidade (por volta de 600 MB/s no máximo) já era mais que suficiente pra um HDD mecânico —
mas passou a ser um gargalo real quando SSDs, muito mais rápidos, começaram a usar essa mesma
interface.

## 41. NVMe

NVMe é uma interface mais moderna, criada especificamente pensando em SSDs: em vez de usar o
protocolo antigo do SATA, um SSD NVMe se conecta diretamente ao barramento PCIe (o mesmo usado por
placas de vídeo) — muito mais rápido, sem o teto de velocidade que o SATA impõe. Um SSD NVMe pode
ser várias vezes mais rápido que um SSD SATA, mesmo os dois sendo tecnicamente "SSD".

`[TENTE VOCÊ]` Por que SATA não é um gargalo real pra um HDD, mas é pra um SSD? Resposta: porque
um HDD já é limitado pela sua própria mecânica (bem abaixo do teto do SATA); um SSD, sem parte
mecânica, consegue ser rápido o bastante pra esbarrar no limite de velocidade da própria interface
SATA — daí a necessidade do NVMe pra deixar o SSD "respirar".

## 42. Latência, throughput e IOPS

Três métricas usadas pra medir performance de armazenamento (e também de rede, módulo 07):

- **Latência**: tempo até a *primeira* resposta chegar — pense numa estrada: latência é quanto
  tempo até o primeiro carro chegar ao destino.
- **Throughput**: quantidade de dados transferidos por segundo, depois que a transferência já
  começou — na analogia da estrada, quantos carros por hora passam, uma vez que o trânsito já
  está fluindo.
- **IOPS** (Input/Output Operations Per Second): quantas operações de leitura/escrita separadas
  um dispositivo consegue fazer por segundo — importante quando o padrão de acesso é muitos
  arquivos pequenos, não poucos arquivos grandes (onde throughput importa mais).

`[TENTE VOCÊ]` Um SSD com alta latência baixa mas throughput mediano seria melhor pra qual
cenário: copiar um único arquivo de vídeo gigante, ou abrir rapidamente milhares de arquivos
pequenos de configuração? Resposta: milhares de arquivos pequenos — aí o que importa é responder
rápido a cada pedido individual (latência baixa/IOPS alto), não sustentar um fluxo grande e
contínuo de dados (throughput).

## 43. Entrada e saída

Dispositivos de entrada e saída (E/S) são tudo que conecta o computador ao mundo fora da
CPU/memória/armazenamento interno: teclado, mouse, tela, impressora, placa de rede. As próximas
seções detalham como a CPU consegue conversar com esses dispositivos sem travar esperando cada
um.

## 44. Controladores

A CPU não conversa diretamente com um disco ou uma placa de rede — ela conversa com um
**controlador**, um chip dedicado que sabe operar aquele dispositivo específico. O controlador
traduz os pedidos genéricos da CPU em comandos elétricos específicos daquele hardware.

## 45. Interrupções

Quando um dispositivo termina uma tarefa (ex: terminou de ler um setor do disco), ele avisa a CPU
por meio de uma **interrupção**, em vez de a CPU precisar ficar checando repetidamente se
terminou — a mesma lógica de eficiência que já apareceu na hierarquia de memória: gastar o mínimo
de esforço possível checando algo que ainda não mudou.

**Exemplo narrado:** você aperta uma tecla no teclado. O controlador do teclado detecta o sinal
elétrico e dispara uma interrupção pra CPU — um sinal de "pare o que está fazendo, isso é
urgente". A CPU, no meio do ciclo fetch-decode-execute de outro programa qualquer, termina a
instrução atual, salva o que precisa pra retomar depois (o estado atual), executa uma rotina
curta de tratamento de interrupção (lê qual tecla foi pressionada, guarda isso num buffer), e só
então volta exatamente de onde parou, como se nada tivesse acontecido — o programa original nunca
soube que foi interrompido.

`[ATENÇÃO]` Confundir interrupção com "a CPU fica esperando o dispositivo" é um erro comum — é
exatamente o oposto: a interrupção existe *pra CPU não precisar esperar*. Sem ela, a CPU teria que
checar repetidamente "a tecla foi apertada? e agora? e agora?" (chamado *polling*), desperdiçando
ciclos de processamento em vez de fazer outro trabalho útil enquanto espera.

`[TENTE VOCÊ]` No exemplo do teclado, o que aconteceria se a CPU usasse *polling* em vez de
interrupção? Resposta: a CPU precisaria checar repetidamente, em loop, se uma tecla foi
pressionada — gastando ciclos de processamento constantemente nessa checagem, mesmo nos
(muitos) momentos em que nenhuma tecla é pressionada, em vez de usar esse tempo pra outro
trabalho.

## 46. DMA

DMA (Direct Memory Access) resolve um problema que interrupções sozinhas não resolvem: transferir
um *grande volume* de dados (ex: ler um arquivo inteiro do disco pra memória) sem que a CPU
precise copiar dado por dado, um de cada vez. Sem DMA, a CPU ficaria presa nesse trabalho
repetitivo o tempo todo; com DMA, um controlador dedicado faz a transferência inteira sozinho,
diretamente entre o dispositivo e a memória, e só dispara uma interrupção avisando a CPU quando
termina tudo — liberando a CPU pra fazer outro trabalho durante a transferência.

`[TENTE VOCÊ]` Por que DMA "conecta" com o conceito de interrupção já visto? Resposta: porque é
assim que o DMA avisa a CPU que terminou — a mesma mecânica de interrupção da seção 45, só que
disparada depois de uma transferência inteira, não de um evento único.

## 47. CPU multicore

Uma CPU multicore tem vários núcleos (cores) independentes na mesma pastilha de silício — cada
núcleo é, essencialmente, uma CPU completa (com sua própria ULA, registradores, e via de regra sua
própria cache L1/L2), capaz de executar seu próprio ciclo fetch-decode-execute de forma totalmente
independente dos outros núcleos. É isso que permite executar vários programas (ou várias partes
do mesmo programa) de verdade ao mesmo tempo, não só a "ilusão" de simultaneidade por
escalonamento rápido que você vai ver no módulo 06.

## 48. Threads

Uma thread é uma sequência independente de instruções dentro de um mesmo programa — um programa
pode ter uma única thread (tudo roda em sequência) ou várias (partes diferentes rodando "ao mesmo
tempo"). Com uma CPU multicore, threads diferentes podem, de fato, rodar em núcleos diferentes,
simultaneamente; com um único núcleo, elas se revezam rapidamente (o mesmo escalonamento do
módulo 06).

## 49. Pipeline

Pipeline é uma técnica de organização (lembra da distinção arquitetura x organização da seção 3?)
que sobrepõe as etapas do ciclo fetch-decode-execute de instruções *diferentes*: enquanto uma
instrução está na etapa de execute, a próxima já pode estar sendo decodificada, e a seguinte já
sendo buscada — como uma linha de montagem, onde vários carros estão em estágios diferentes de
produção ao mesmo tempo, em vez de terminar um carro inteiro antes de começar o próximo.

`[TENTE VOCÊ]` Pipeline faz uma única instrução executar mais rápido? Resposta: não diretamente —
cada instrução individual ainda leva o mesmo tempo pelas três etapas; o que melhora é o
*throughput* geral (seção 42): mais instruções completadas por segundo, porque várias estão em
estágios diferentes do pipeline ao mesmo tempo.

## 50. Paralelismo

Paralelismo é o termo geral pra "fazer mais de uma coisa ao mesmo tempo de verdade" — e aparece em
vários níveis que você já viu: pipeline (paralelismo entre etapas de instruções diferentes),
multicore (paralelismo entre núcleos inteiros), e — no próximo tópico — a diferença radical de
escala de paralelismo entre CPU e GPU.

## 51. CPU vs GPU

CPU e GPU são otimizadas pra tipos opostos de trabalho. CPU: poucos núcleos (dezenas, no máximo),
cada um complexo e flexível, otimizado pra executar tarefas sequenciais diversas e cheias de
decisões (`if`s, desvios). GPU: milhares de núcleos simples, otimizados pra fazer a *mesma*
operação simples sobre uma quantidade enorme de dados ao mesmo tempo (ex: calcular a cor de cada
um dos milhões de pixels de uma imagem) — é por isso que GPUs usam VRAM (seção 36) separada,
otimizada pra esse padrão de acesso massivamente paralelo, em vez da RAM geral.

`[TENTE VOCÊ]` Por que renderizar gráficos (calcular a cor de milhões de pixels, cada um de forma
independente e repetitiva) é um trabalho melhor pra GPU do que pra CPU? Resposta: porque é
exatamente o padrão que a GPU foi desenhada pra fazer bem — a mesma operação simples repetida em
paralelo massivo sobre muitos dados, em vez de poucas tarefas complexas e sequenciais.

## Erros comuns

Você já viu estes avisos ao longo do módulo — aqui vai só a revisão rápida:

- Achar que a CPU "executa o programa inteiro de uma vez", em vez de instrução por instrução.
- Confundir RAM (memória volátil, temporária) com armazenamento permanente (disco/SSD).
- Achar que "mais cache" sempre resolve qualquer problema de performance, ignorando o princípio
  de localidade.
- Achar que SATA é um limite igual pra HDD e SSD — na prática só vira gargalo real pro SSD.
- Confundir arquitetura (o conjunto de instruções, o "contrato") com organização (como isso é
  implementado por dentro, ex: pipeline e cache).

## Conexão com os próximos módulos

| Conceito deste módulo | Reaparece em |
|---|---|
| Gerência de memória e processos | Módulo 06 — Sistemas Operacionais |
| Ciclo de instrução | Módulo 08 — como código-fonte vira instrução de máquina |
| Threads, paralelismo | Módulo 06 — threads como conceito do sistema operacional |

## `[REFERÊNCIA]`

- BROOKSHEAR, J. Glenn. *Ciência da Computação — Uma Visão Abrangente*, 7ª ed., Bookman, 2005 —
  Capítulos 3 e 4 (Arquitetura de Máquina / Sistemas Operacionais).
- WHITE, Ron. *Como Funciona o Computador*, 8ª ed., Quark, 1998.
- [Crucial — RAM vs. VRAM: What's the Difference?](https://www.crucial.com/articles/about-ram/ram-vs-vram)
  — artigo técnico explicando a diferença entre memória do sistema e memória de vídeo.
- [Kingston — SSD vs. HDD: What's the Difference?](https://www.kingston.com/en/blog/pc-performance/ssd-vs-hdd)
  — comparação técnica de armazenamento mecânico x flash.
- [Microsoft Learn — WMIC (linha de comando)](https://learn.microsoft.com/pt-br/windows/win32/wmisdk/wmic)
  e [Get-CimInstance (PowerShell)](https://learn.microsoft.com/pt-br/powershell/module/cimcmdlets/get-ciminstance)
  — documentação oficial dos comandos Windows usados na prática deste módulo.
- [RISC-V International](https://riscv.org/) — especificação aberta da ISA RISC-V.
- [ARM Architecture Reference Manual (visão geral)](https://developer.arm.com/documentation) —
  documentação oficial da ARM.

## Checklist de saída

- [ ] Nomeio os componentes básicos de um computador e o papel de cada um, sabendo ligar a ULA
      aos circuitos lógicos do módulo 04.
- [ ] Diferencio arquitetura de organização, com um exemplo (ex: Intel x AMD em x86).
- [ ] Descrevo o papel de Program Counter, Instruction Register e Flags dentro do ciclo de
      execução.
- [ ] Descrevo o ciclo fetch-decode-execute passo a passo, narrando a decisão em cada etapa (não
      só listando os nomes das três fases).
- [ ] Explico o gargalo de Von Neumann usando a analogia da bancada compartilhada, e por que uma
      arquitetura Harvard (barramentos separados) não sofre do mesmo gargalo.
- [ ] Comparo CISC e RISC com pelo menos 2 diferenças, cito x86/x64, ARM e RISC-V como exemplos
      reais, e sei mostrar a mesma operação escrita nos dois estilos.
- [ ] Ordeno a hierarquia de memória do mais rápido ao mais lento, explico o princípio de
      localidade, e tenho noção da ordem de grandeza de tempo entre cada nível.
- [ ] Diferencio SATA de NVMe, e latência de throughput de IOPS.
- [ ] Explico, em termos gerais, o que é uma interrupção e um DMA, e por que ambos existem pra
      evitar que a CPU fique esperando (*polling*).
- [ ] Explico a diferença entre multicore, threads e pipeline, e por que CPU e GPU são otimizadas
      pra tipos opostos de paralelismo.
