# Módulo 08 — Linguagens de Programação

> **Objetivo:** entender como um código-fonte escrito em texto legível se transforma nas
> instruções binárias que a CPU realmente executa, e como usar essa base pra escrever programas
> de verdade em C++.
> **Pré-requisitos:** Módulo 05 (Arquitetura de Computadores).
> **Tempo de referência:** 6 a 8 horas.
> **Prática correspondente:** [08_linguagens-programacao-pratica.md](08_linguagens-programacao-pratica.md)

---

## 1. Por que isso importa

No módulo 05 você viu o ciclo fetch-decode-execute: a CPU só entende instrução de máquina —
sequências binárias, específicas do processador. Mas você nunca escreve código em binário; escreve
em palavras como `se`, `soma`, `repita`. Este módulo inteiro responde a uma pergunta guarda-chuva:
**como uma linguagem funciona, e como escrevemos programas de verdade com ela?** — do texto que
você digita até o executável que a CPU roda, e das primeiras variáveis até funções e ponteiros.
Ele prepara o terreno pra você escrever seus primeiros algoritmos completos no módulo 09.

## 2. O que é uma linguagem de programação

Uma linguagem de programação é um conjunto de regras (sintaxe) e significados (semântica) que
permite descrever, de forma precisa e não ambígua, uma sequência de passos pra um computador
executar. A diferença central pra uma língua humana: linguagem de programação não tolera
ambiguidade — cada instrução precisa ter exatamente um significado, porque quem vai "interpretar"
o texto não é uma pessoa capaz de inferir intenção, é uma máquina seguindo regras rígidas.

## 3. Linguagem de máquina

É o único "idioma" que a CPU realmente entende nativamente: sequências binárias que correspondem
diretamente a instruções do conjunto de instruções (ISA) do processador — o que você já viu no
módulo 05. Ninguém escreve programas reais direto em linguagem de máquina hoje; ela existe como a
camada mais baixa pra onde tudo, eventualmente, precisa ser traduzido.

## 4. Assembly

É a forma legível por humano da linguagem de máquina — cada instrução Assembly corresponde (quase
sempre) a exatamente uma instrução binária real, só que escrita com mnemônicos (`MOV`, `ADD`,
`JMP`) em vez de números. Você já viu um exemplo no módulo 05, gerado a partir de C++ com a flag
`-S` do compilador. Assembly ainda depende diretamente da arquitetura — um programa em Assembly
x86 não roda numa CPU ARM sem tradução.

## 5. Linguagens de alto nível

São linguagens como C++, Python ou JavaScript, que abstraem os detalhes do hardware (registradores
específicos, endereços de memória exatos) e deixam o compilador ou interpretador decidir como
traduzir isso pra instruções de máquina. A vantagem: você pensa no problema, não no processador; o
mesmo código-fonte, em teoria, pode rodar em arquiteturas diferentes, bastando recompilar (ou, se
interpretado, rodar com o interpretador certo).

## 6. Compiladas vs interpretadas

Existem dois caminhos principais pra transformar código-fonte em algo que a máquina executa.

Um **compilador** traduz o programa inteiro, de uma vez, antes de qualquer execução começar — o
resultado é um arquivo executável, em instruções de máquina, que depois roda sozinho, direto no
hardware, sem precisar do compilador presente. Um **interpretador** faz o oposto: lê e executa o
código linha por linha, traduzindo e rodando ao mesmo tempo, sem gerar um executável separado —
precisa do interpretador presente toda vez que o programa roda.

A analogia ajuda a fixar: compilar é como traduzir um livro inteiro pra outro idioma antes de
entregar pra alguém ler; interpretar é como um intérprete simultâneo traduzindo frase por frase
enquanto a pessoa fala, ao vivo.

O trade-off é direto: código compilado roda mais rápido (a tradução já foi feita antes, uma única
vez), mas qualquer mudança exige recompilar antes de rodar de novo. Código interpretado é mais
ágil pra testar (edita e roda na hora), mas paga o custo de traduzir de novo a cada execução.

`[TENTE VOCÊ]` Você mudou uma linha de um programa escrito numa linguagem compilada. O que
precisa acontecer antes de rodar a versão nova? Resposta: recompilar — gerar um executável novo a
partir do código atualizado. Rodar o executável antigo mostraria o comportamento de antes da
mudança.

## 7. Compiladores

Um compilador é o programa responsável por essa tradução completa. C++ (a linguagem usada neste
módulo) é compilada — o compilador usado é o `g++`, do conjunto GCC/MinGW, já configurado na
seção de setup Windows mais abaixo.

## 8. Interpretadores

Python e JavaScript são exemplos de linguagens interpretadas (embora, na prática, muitas
implementações modernas usem técnicas híbridas — isso é um `[APROFUNDAMENTO]` opcional: motores
como o V8 do Chrome, usado pelo Node.js já citado no módulo 05, compilam partes do código "on the
fly" pra acelerar — chamado de JIT, Just-In-Time compilation — misturando as duas ideias).

## 9. Runtime

É o ambiente que dá suporte a um programa enquanto ele roda — gerenciamento de memória, tratamento
de exceções, funções da biblioteca padrão disponíveis a qualquer momento. Um executável C++ tem um
runtime relativamente enxuto, ligado (linkado) durante a compilação; linguagens interpretadas
dependem de um runtime bem mais presente (o próprio interpretador), rodando o tempo todo.

## 10. Código-fonte

É o texto que você escreve — no caso deste módulo, em arquivos `.cpp`, usando a sintaxe de C++.
Nenhum hardware executa código-fonte diretamente; ele precisa passar pelo processo de compilação.

## 11. Código objeto

É o resultado intermediário da compilação: já é binário (instruções de máquina), mas ainda não é
um programa completo e executável — falta ligar (linkar) as referências a bibliotecas e outras
partes do programa. Arquivos de código objeto costumam ter extensão `.o` (Linux/Mac) ou `.obj`
(Windows).

## 12. Executável

É o resultado final, depois da linkedição — um arquivo binário completo, pronto pra rodar sozinho,
sem precisar mais do compilador. No Windows, executáveis usam extensão `.exe` (é o que você já
gera com `g++ programa.cpp -o programa.exe`).

## 13. Processo de compilação

Compilar C++ não é um passo único — são várias etapas encadeadas:

```
código-fonte (.cpp)
  → pré-processamento (resolve #include, macros)
    → compilação propriamente dita (gera código objeto, .o/.obj)
      → linkedição (liga o código objeto às bibliotecas necessárias)
        → executável (.exe)
```

Quando você roda `g++ programa.cpp -o programa.exe`, o `g++` executa essas quatro etapas
automaticamente, uma atrás da outra, sem você precisar chamá-las separadamente — mas saber que
elas existem ajuda a entender mensagens de erro: um erro de "sintaxe" acontece na etapa de
compilação; um erro de "referência indefinida" (`undefined reference`) acontece na linkedição,
porque algo que o código pede não foi encontrado pra ligar.

`[TENTE VOCÊ]` Se o compilador reclama de `undefined reference to 'algumaFuncao'`, em qual etapa
do processo isso acontece? Resposta: na linkedição — o código compilou (a sintaxe estava certa),
mas o linker não achou onde `algumaFuncao` está implementada.

## 14. Processo de execução

Depois de pronto, o executável roda em etapas que você já viu no módulo 05: o sistema operacional
carrega o programa na memória, cria um processo (módulo 06) pra ele, e a CPU começa a buscar,
decodificar e executar as instruções desse programa, uma por vez, seguindo o ciclo
fetch-decode-execute.

## 15. Variáveis: gavetas nomeadas na memória

Lembra do módulo 03: um número, dentro do computador, é uma sequência de bits guardada na
memória. Uma **variável** é só um nome que você dá pra uma dessas posições de memória, pra não
precisar lembrar o endereço exato — é uma gaveta com etiqueta, em vez de uma gaveta numerada.

## 16. Tipos de dados

Em uma linguagem de tipagem estática (como C++), declarar o **tipo** da variável diz ao
compilador quantos bits reservar naquela gaveta, e como interpretar o conteúdo dela. C++ tem
vários tipos primitivos — os mais comuns:

### 17. Inteiros

`int` (tipicamente 32 bits), `short` (16 bits), `long`/`long long` (variam, geralmente 32 ou 64
bits) — guardam números sem casas decimais. Como você viu no módulo 03, `n` bits representam `2ⁿ`
valores possíveis, não um número ilimitado.

### 18. Números reais

`float` (32 bits) e `double` (64 bits, mais precisão) — guardam números com casas decimais,
usando a representação de ponto flutuante/IEEE 754 já vista no módulo 03.

### 19. Caracteres

`char` — guarda um único caractere, internamente como um número (o código ASCII/Unicode dele, já
visto no módulo 03). `'A'` e `65` são, por baixo dos panos, a mesma coisa guardada num `char`.

### 20. Strings

C++ tem `std::string` (da biblioteca padrão) pra guardar texto — uma sequência de caracteres,
com tamanho que pode crescer/encolher dinamicamente (diferente de um `char` isolado).

### 21. Booleanos

`bool` guarda só dois valores possíveis: `true` ou `false` — é o tipo mais natural pra representar
o resultado de uma condição, e se conecta direto com os `0` e `1` lógicos do módulo 04.

## 22. Constantes

Uma variável comum pode ser alterada depois de declarada; uma **constante** (`const` em C++) é
declarada com um valor que **não pode mudar** depois. Use constantes pra valores que representam
uma regra fixa do seu programa (ex: `const int DIAS_NA_SEMANA = 7;`) — isso comunica intenção (
"isso nunca deveria mudar") e faz o compilador barrar qualquer tentativa acidental de alterar.

`[ATENÇÃO]` Tentar reatribuir uma `const` depois de declarada não compila — o compilador rejeita
o programa inteiro. É intencional: o objetivo de uma constante é justamente impedir isso.

## 23. Variáveis e memória

Um `int` normalmente usa 32 bits — e, como já dito, `n` bits representam `2ⁿ` valores possíveis.

`[ATENÇÃO]` Se um cálculo tentar guardar um valor maior do que o tipo suporta, acontece
**overflow** — em C++, isso não gera erro nem aviso: o valor simplesmente "dá a volta" e vira
outro número, silenciosamente. É o mesmo overflow que você já foi avisado a respeito no módulo
03, agora acontecendo de verdade dentro de um programa.

## 24. Operadores

Operadores são os símbolos que combinam ou transformam valores de variáveis. C++ agrupa vários
tipos:

### 25. Operadores aritméticos

`+`, `-`, `*`, `/` (divisão) e `%` (resto da divisão — módulo). `[ATENÇÃO]` divisão entre dois
`int` em C++ é **divisão inteira** — `7 / 2` dá `3`, não `3.5` (o resultado é truncado, não
arredondado). Pra obter `3.5`, pelo menos um dos operandos precisa ser `float`/`double`.

### 26. Operadores relacionais

`==` (igual), `!=` (diferente), `>`, `<`, `>=`, `<=` — comparam dois valores e resultam num
`bool`. Já visto o `[ATENÇÃO]` clássico de confundir `=` (atribuição) com `==` (comparação).

### 27. Operadores lógicos

`&&` (E lógico), `||` (OU lógico), `!` (NÃO lógico) — a mesma lógica das portas AND/OR/NOT do
módulo 04, agora combinando condições booleanas em código: `if (idade >= 18 && temDocumento)`.

### 28. Operadores de atribuição

`=` (atribuição simples), e as formas compostas `+=`, `-=`, `*=`, `/=` (ex: `soma += i;` é
exatamente igual a `soma = soma + i;`, só mais curto).

### 29. Precedência de operadores

Assim como em matemática (multiplicação antes de soma), operadores em C++ têm ordem de avaliação:
multiplicação/divisão antes de soma/subtração, comparações antes de `&&`/`||`. Na dúvida, use
parênteses — eles nunca deixam a expressão ambígua, mesmo quando a precedência "natural" já
resolveria certo.

`[TENTE VOCÊ]` Qual o valor de `2 + 3 * 4`? Resposta: `14` — multiplicação acontece antes da
soma (`3 * 4 = 12`, depois `2 + 12 = 14`), não `20`.

## 30. Expressões

Uma expressão é qualquer combinação de valores, variáveis e operadores que **produz um valor**
(ex: `idade + 1`, `nota >= 70`). Diferente de um comando, uma expressão sempre "vira" um valor que
pode ser usado em outro lugar.

## 31. Comandos

Um comando é uma instrução completa que o programa executa (ex: uma declaração de variável, um
`if`, um `for`). Em C++, comandos terminam com `;` (exceto blocos com chaves). A diferença chave
pra expressão: um comando **faz** algo; uma expressão **vale** algo (embora em C++ uma expressão
sozinha seguida de `;` também seja um comando válido).

## 32. Blocos de código

Um bloco é um grupo de comandos agrupados entre `{ }`, tratado como uma unidade — é o que aparece
dentro de um `if`, um `for`, uma função. Um bloco também define um **escopo** (mais sobre isso na
seção de funções).

## 33. Entrada e saída

Em C++, `std::cin >>` lê da entrada padrão (o teclado); `std::cout <<` escreve na saída padrão (o
terminal). Ambos vêm da biblioteca padrão (`std`), incluída com `#include <iostream>`.

**Exemplo narrado — um programa mínimo:**
```cpp
#include <iostream>

int main() {
    int idade;
    std::cout << "Digite sua idade: ";
    std::cin >> idade;
    std::cout << "Você terá " << idade + 1 << " anos no ano que vem.\n";
    return 0;
}
```
Narrando: `int idade;` reserva a gaveta de memória (32 bits, tipo inteiro); `std::cin >> idade`
lê o valor digitado do teclado e guarda nela; `std::cout <<` usa o valor guardado pra montar a
mensagem de saída, somando `1` antes de exibir.

## 34. Conversão de tipos

Às vezes você precisa transformar um valor de um tipo pra outro — ex: um `int` lido do teclado
precisa virar `double` pra participar de uma divisão exata. Em C++, isso é feito com um "cast"
explícito: `double(idade)` ou `static_cast<double>(idade)`. Conversões implícitas também
acontecem automaticamente em certos casos (ex: somar um `int` com um `double` promove o `int`
pra `double` antes de somar) — mas depender demais disso sem entender é fonte de bug.

## 35. Tipagem estática vs dinâmica

C++ é **estaticamente tipada**: o tipo de cada variável é fixado em tempo de compilação, e não
muda depois (uma variável `int` sempre vai guardar um `int`). Linguagens como Python ou
JavaScript são **dinamicamente tipadas**: uma mesma variável pode guardar um número, depois um
texto, sem avisar o compilador de antemão — o tipo é checado em tempo de execução, não de
compilação.

## 36. Tipagem forte vs fraca

Tipagem forte significa que a linguagem não permite operações entre tipos incompatíveis sem uma
conversão explícita (C++ é relativamente forte — somar um `int` com uma `std::string` não
compila sem tratamento). Tipagem fraca (ex: JavaScript) permite esse tipo de mistura, convertendo
automaticamente de formas que às vezes surpreendem (`"5" + 1` em JavaScript vira a string
`"51"`, não o número `6`).

## 37. Estruturas de controle

Toda lógica de programação, por mais complexa que pareça, é construída com só três blocos —
sequência, decisão e repetição. Você já executou uma **sequência** sem perceber: o programa da
"idade" acima roda de cima pra baixo, um passo depois do outro, como os passos numerados de uma
receita. Os outros dois blocos merecem mais tempo, porque é neles que a lógica de verdade
acontece.

### 38. if

"Se está chovendo, leve guarda-chuva" é a mesma lógica condicional que você já formalizou como
porta lógica no módulo 04 — agora expressa em código. Em C++, isso vira `if`:

```cpp
int nota;
std::cin >> nota;

if (nota >= 90) {
    std::cout << "Conceito A\n";
}
```

### 39. else if

Encadeia condições alternativas, checadas em ordem, uma depois da outra:

```cpp
} else if (nota >= 70) {
    std::cout << "Conceito B\n";
} else if (nota >= 50) {
    std::cout << "Conceito C\n";
```

Narrando: as condições são checadas **de cima pra baixo**, e a primeira que for verdadeira
"ganha" — as outras nem chegam a ser avaliadas.

### 40. else

```cpp
} else {
    std::cout << "Conceito D\n";
}
```
É o "nenhuma das anteriores", pega tudo que sobrou (por isso não tem condição própria).

`[TENTE VOCÊ]` Com `nota = 72`, qual conceito imprime? Resposta: **Conceito B** — `72 >= 90` é
falso, mas `72 >= 70` é verdadeiro, e como o `if` para na primeira condição verdadeira, nunca
chega a testar `>= 50`.

`[ATENÇÃO]` Um erro clássico é escrever `if (nota = 90)` com um único `=` em vez de `if (nota ==
90)`. Em C++, `=` é **atribuição** (guarda 90 em `nota`), não comparação — e o `if` avalia o
resultado dessa atribuição como verdadeiro (porque `90` é diferente de zero), então essa condição
é **sempre verdadeira**, e de quebra `nota` é sobrescrita silenciosamente para `90`. O que fazer:
sempre `==` (dois sinais de igual) para comparar; `=` (um sinal) é para atribuir.

### 41. for

Use `for` quando você já sabe, de antemão, quantas vezes vai repetir:

```cpp
int soma = 0;
for (int i = 1; i <= 10; i++) {
    soma += i;
}
std::cout << "Soma: " << soma << "\n";
```

Narrando as três partes do `for`, separadas por `;`: `int i = 1` roda **uma vez só**, no início
(inicialização); `i <= 10` é checada **antes de cada repetição** — se for falsa, o laço para;
`i++` roda **depois de cada repetição**, incrementando `i`. O corpo (`soma += i`) roda uma vez
para cada valor de `i` de 1 a 10.

`[TENTE VOCÊ]` Como você mudaria esse `for` para somar os primeiros `N` números, onde `N` é lido
do teclado (em vez de fixo em 10)? Resposta: ler `N` com `std::cin >> N` antes do laço, e trocar a
condição para `i <= N`.

### 42. while

`for` funciona bem quando o número de repetições é conhecido antes de começar. Quando você **não
sabe** quantas vezes vai repetir — só sabe a condição que faz parar — use `while`:

```cpp
int numero;
std::cin >> numero;
while (numero != -1) {
    std::cout << "Você digitou: " << numero << "\n";
    std::cin >> numero;
}
```

Narrando: o programa lê números até o usuário digitar `-1` (o "sentinela" — um valor combinado
pra sinalizar "parei"). Ninguém sabe de antemão quantos números o usuário vai digitar antes disso
— por isso `while`, não `for`.

`[ATENÇÃO]` Um `while` sem uma condição que eventualmente vira falsa é um laço infinito. O que
**não** fazer:
```cpp
while (true) {
    std::cout << "Isso nunca para\n";
}
```
O que fazer no lugar: garantir que algo dentro do laço eventualmente torne a condição falsa — no
exemplo do sentinela acima, é o `std::cin >> numero` dentro do laço que dá a chance da condição
`numero != -1` virar falsa a cada repetição.

### 43. do-while

Repare que, no `while` acima, se o primeiro valor digitado já for `-1`, o corpo do laço **nunca
roda** — a condição é checada **antes**. Às vezes você precisa do oposto: rodar o corpo **pelo
menos uma vez**, e só depois checar se repete.

```cpp
std::string senha;
do {
    std::cout << "Digite a senha: ";
    std::cin >> senha;
} while (senha != "1234");
std::cout << "Acesso liberado!\n";
```

`[TENTE VOCÊ]` Quantas vezes o corpo roda em `while (false) { ... }`? E em
`do { ... } while (false)`? Resposta: o `while (false)` roda **zero vezes**; o `do-while` roda
**uma vez** (o corpo sempre roda ao menos uma vez, antes de a condição ser checada pela primeira
vez).

### 44. break

Interrompe imediatamente o laço mais interno onde está, mesmo que a condição de repetição ainda
seja verdadeira — útil pra "sair mais cedo" quando algo específico é encontrado:

```cpp
for (int i = 1; i <= 100; i++) {
    if (i == 7) {
        break;
    }
    std::cout << i << " ";
}
// imprime 1 2 3 4 5 6, e para -- nunca chega no 100
```

### 45. continue

Pula direto pra próxima repetição do laço, sem executar o resto do corpo naquela volta:

```cpp
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) {
        continue;  // pula os pares
    }
    std::cout << i << " ";
}
// imprime só os ímpares: 1 3 5 7 9
```

`[TENTE VOCÊ]` Qual a diferença de efeito entre `break` e `continue` dentro de um `for`? Resposta:
`break` encerra o laço inteiro; `continue` só pula o resto da repetição atual e segue pra próxima.

## 46. Funções

Uma função é um bloco de código nomeado, que você pode chamar (executar) de vários lugares do
programa sem reescrever a lógica toda vez — o mesmo princípio de reaproveitamento que já apareceu
com bibliotecas no módulo 05.

```cpp
int somar(int a, int b) {
    return a + b;
}

int main() {
    int resultado = somar(3, 4);
    std::cout << resultado << "\n";  // 7
}
```

### 47. Parâmetros

São as "gavetas" declaradas na assinatura da função (`int a, int b` acima) — os nomes que a
função usa internamente pra se referir aos valores recebidos.

### 48. Argumentos

São os valores reais passados numa chamada específica (`3` e `4` na chamada `somar(3, 4)`).
Parâmetro é o "nome combinado"; argumento é "o valor de verdade enviado" naquela chamada.

### 49. Retorno

`return` devolve um valor de volta pra quem chamou a função, e encerra a execução da função
naquele ponto. O tipo declarado antes do nome da função (`int somar(...)`) precisa bater com o
tipo do que é retornado.

### 50. Escopo

É a região do código onde uma variável "existe" e pode ser usada. Uma variável declarada dentro
de uma função (ou de um bloco `{ }`) só existe ali dentro — fora dali, o nome não significa nada.

### 51. Variáveis locais e globais

Variável local: declarada dentro de uma função, só existe enquanto aquela função está rodando.
Variável global: declarada fora de qualquer função, existe durante todo o programa e é visível de
qualquer lugar. `[ATENÇÃO]` variáveis globais são convenientes mas perigosas — qualquer função
pode alterá-las, tornando difícil rastrear onde um valor mudou. O que fazer no lugar: prefira
passar valores como parâmetro e retornar resultados, reservando globais pra casos realmente
necessários.

### 52. Recursão

Uma função que chama a si mesma, geralmente reduzindo o problema a um caso menor a cada chamada,
até atingir um "caso base" que não chama mais nada:

```cpp
int fatorial(int n) {
    if (n <= 1) {
        return 1;  // caso base
    }
    return n * fatorial(n - 1);  // chamada recursiva
}
```

`[ATENÇÃO]` Uma função recursiva sem caso base (ou com um caso base que nunca é alcançado) chama
a si mesma infinitamente, até estourar a pilha de chamadas (stack overflow — conecta com stack
vs heap, mais adiante).

## 53. Estruturas de dados básicas

Além de variáveis simples (um valor por vez), C++ oferece formas de agrupar vários valores.

### 54. Arrays

Uma sequência de elementos do mesmo tipo, com tamanho fixo, acessados por índice (começando em
`0`):

```cpp
int notas[5] = {8, 7, 9, 6, 10};
std::cout << notas[0];  // 8 -- primeiro elemento
std::cout << notas[4];  // 10 -- último elemento (índice 4, não 5)
```

`[ATENÇÃO]` Acessar um índice fora do array (ex: `notas[5]` num array de tamanho 5) não gera erro
de compilação nem, necessariamente, de execução — é um comportamento indefinido em C++, podendo
ler memória de outra variável por acidente. O que fazer: sempre confira que o índice está entre
`0` e `tamanho - 1`.

### 55. Matrizes

Um array de arrays — uma grade de linhas e colunas:

```cpp
int tabuleiro[3][3] = {{1,2,3}, {4,5,6}, {7,8,9}};
std::cout << tabuleiro[1][2];  // 6 -- linha 1, coluna 2
```

### 56. Structs

Uma forma de agrupar vários dados relacionados num único tipo novo — como uma "ficha" com vários
campos:

```cpp
struct Aluno {
    std::string nome;
    int idade;
    double media;
};

Aluno a1 = {"Maria", 17, 8.5};
std::cout << a1.nome << " tem " << a1.idade << " anos.\n";
```

### 57. Enumerações

Uma forma de nomear um conjunto fixo de valores possíveis, em vez de usar números soltos sem
significado — conecta com a máquina de estados do módulo 04:

```cpp
enum EstadoTrava { ESPERANDO_DIGITO_1, ESPERANDO_DIGITO_2, LIBERADA };
EstadoTrava estado = ESPERANDO_DIGITO_1;
```

## 58. Ponteiros

Uma variável comum guarda um valor; um **ponteiro** guarda o *endereço de memória* onde um valor
está guardado — como anotar o número da casa em vez de morar nela.

```cpp
int idade = 17;
int* p = &idade;  // p guarda o ENDEREÇO de idade, não o valor 17

std::cout << idade;   // 17 -- o valor
std::cout << &idade;  // um endereço de memória, tipo 0x7ffee...
std::cout << p;       // o mesmo endereço
std::cout << *p;      // 17 -- "desreferenciar" p: ir até o endereço e ler o valor lá
```

`[ATENÇÃO]` Um ponteiro que não aponta pra lugar nenhum válido (ou que já foi liberado) é chamado
de "ponteiro pendurado" (dangling pointer) — desreferenciá-lo é comportamento indefinido, uma das
causas mais comuns de programas C++ travarem. O que fazer: sempre inicialize ponteiros, e nunca
use um ponteiro depois de liberar a memória que ele apontava (mais sobre isso na alocação
dinâmica).

### 59. Referências

Um "apelido" pra uma variável já existente — mais seguro que ponteiro porque não pode ser nulo e
não precisa de sintaxe de desreferência:

```cpp
int idade = 17;
int& ref = idade;  // ref É idade, não um endereço separado
ref = 18;
std::cout << idade;  // 18 -- mudar ref muda idade, porque são a mesma coisa
```

### 60. Endereços de memória

Todo dado num programa em execução mora em algum endereço específico da memória RAM (módulo 05).
O operador `&` (endereço-de) devolve esse endereço; ponteiros e referências são as duas formas
que C++ oferece pra trabalhar com esses endereços diretamente.

### 61. Alocação dinâmica

Às vezes você só sabe, em tempo de execução, quanto espaço vai precisar (ex: o tamanho de um
array depende de algo que o usuário digita). Alocação dinâmica (`new`/`delete` em C++) reserva
memória sob demanda, em vez de ter um tamanho fixo decidido em tempo de compilação:

```cpp
int* numeros = new int[5];  // aloca espaço pra 5 inteiros, em tempo de execução
// ... usa numeros[0] a numeros[4] normalmente ...
delete[] numeros;  // libera a memória quando não precisar mais
```

`[ATENÇÃO]` Esquecer o `delete` depois de um `new` é um vazamento de memória (memory leak) — a
memória fica reservada, inacessível, pelo resto da execução do programa. O que fazer: todo `new`
precisa de um `delete` correspondente (ou, em C++ moderno, prefira contêineres da biblioteca
padrão como `std::vector`, que gerenciam isso automaticamente).

### 62. Stack vs Heap

Duas regiões de memória com propósitos diferentes — o mesmo Stack/Heap que o módulo 06 já
introduziu do lado do sistema operacional. **Stack**: rápida, gerenciada automaticamente,
guarda variáveis locais de funções (é onde as chamadas recursivas se empilham — e por isso uma
recursão sem caso base estoura a stack). **Heap**: mais lenta, gerenciada manualmente com
`new`/`delete`, usada pra alocação dinâmica de tamanho variável.

## 63. Bibliotecas

Código que outra pessoa já escreveu e testou, que você reaproveita em vez de reescrever do zero
— `std::cout`, `std::string`, tudo isso vem da biblioteca padrão de C++.

### 64. Imports e Includes

Em C++, `#include <iostream>` é como você "importa" uma biblioteca — diz ao pré-processador pra
inserir as declarações daquele arquivo de cabeçalho antes de compilar. Outras linguagens usam
`import` (Python) ou `require`/`import` (JavaScript) pra um propósito equivalente.

### 65. Dependências

Uma dependência é qualquer código externo que seu programa **precisa** pra funcionar — se a
biblioteca não estiver disponível na hora de compilar/rodar, o programa não funciona.

### 66. Pacotes

É a forma empacotada e distribuível de uma biblioteca — algo que você baixa e instala (ex: via um
gerenciador de pacotes), em vez de escrever ou copiar manualmente. C++ tradicionalmente tem menos
cultura de gerenciador de pacotes centralizado que linguagens mais novas (você vai ver um
gerenciador de pacotes de verdade — o `npm` — no módulo 13, com Node.js).

### 67. Runtime e ambiente de execução

Retomando o conceito de runtime (tópico 9): o "ambiente de execução" é tudo que precisa estar
presente pra um programa rodar — no caso de um executável C++ compilado, é bem enxuto (o próprio
sistema operacional e as bibliotecas linkadas); em linguagens interpretadas, o ambiente de
execução inclui o interpretador inteiro.

## 68. Erros de compilação

Acontecem **antes** do programa existir como executável — o código tem algum problema de sintaxe
ou de tipos que o compilador consegue detectar sem nem rodar nada (ex: esquecer um `;`, usar uma
variável não declarada, passar um tipo errado pra uma função). O programa simplesmente não gera
um `.exe`.

## 69. Erros de execução

Acontecem **depois** que o programa já compilou e começou a rodar — o código estava
sintaticamente correto, mas alguma condição em tempo de execução quebra (ex: divisão por zero,
acessar um índice de array fora dos limites, desreferenciar um ponteiro inválido).

`[TENTE VOCÊ]` Esquecer um `;` no fim de uma linha é erro de compilação ou de execução? Resposta:
compilação — o compilador nem consegue terminar de traduzir o programa, então nenhum executável é
gerado.

## 70. Debugging

É o processo de encontrar e corrigir a causa de um comportamento errado no programa — seja um
erro de compilação (mais fácil, o compilador aponta a linha) ou de execução (mais difícil,
exige investigação: o que o programa estava fazendo quando quebrou?).

## 71. Debugger

Uma ferramenta que permite pausar um programa em execução, inspecionar o valor das variáveis
naquele momento exato, e avançar linha por linha — em vez de só adivinhar o que está acontecendo
a partir do resultado final. O VSCode (já usado desde o setup deste módulo) tem um debugger
integrado pra C++, configurável com poucos cliques uma vez que o compilador já está instalado.

### 72. Stack Trace

Quando um programa quebra em tempo de execução, o stack trace é o "rastro" das chamadas de
função que levaram até o ponto do erro — qual função chamou qual função, até chegar na que
quebrou. É a primeira coisa a olhar pra entender **onde**, no fluxo do programa, o problema
começou.

## 73. Escrever um programa

Até agora você só leu blocos de código. Chegou a hora de sair da teoria — esta seção é um guia
passo a passo para quem nunca escreveu e rodou um programa C++ no Windows (se você usa Mac ou
Linux, o compilador já vem pronto no sistema — veja a prática deste módulo).

Você não precisa de um programa especial pra escrever código — código-fonte é só texto puro. O
**Bloco de Notas** (Notepad), que já vem instalado no Windows, serve perfeitamente.

Abra o Bloco de Notas, digite o código, e use "Salvar como". Aqui mora uma pegadinha: o Windows
esconde a extensão de arquivos por padrão, então o Bloco de Notas pode salvar seu arquivo como
`programa.cpp.txt` sem avisar — o `.txt` é adicionado sozinho por trás das câmaras. Para evitar
isso, no campo "Nome do arquivo" da janela "Salvar como", digite o nome **entre aspas**:
`"programa.cpp"` — as aspas forçam o Windows a usar exatamente essa extensão, ignorando o `.txt`
que ele tentaria acrescentar.

`[ATENÇÃO]` Se o arquivo ficar `programa.cpp.txt` sem você perceber, o compilador não vai
reconhecê-lo como C++ na hora de compilar (o erro geralmente menciona não saber o que fazer com o
arquivo). O que fazer: no Explorador de Arquivos, ative a exibição de extensões (Exibir > mostrar
> Extensões de nomes de arquivos, ou equivalente na sua versão do Windows) antes de começar, para
sempre conseguir ver a extensão real de qualquer arquivo salvo.

## 74. Compilar um programa

Diferente de Mac e Linux, o Windows **não vem** com um compilador C++ pronto — é preciso instalar
um separadamente antes de conseguir compilar qualquer coisa. O caminho mais usado hoje é o
**MinGW-w64**, distribuído através do MSYS2:

1. Baixe e instale o MSYS2 (site oficial: `msys2.org`).
2. Abra o terminal do MSYS2 (instalado junto) e rode o comando de instalação do compilador
   indicado na documentação oficial do MSYS2 no momento (geralmente algo como
   `pacman -S mingw-w64-ucrt-x86_64-gcc`).
3. Adicione a pasta `bin` do MinGW instalado ao **PATH** do Windows (Painel de Controle > Sistema
   > Configurações avançadas do sistema > Variáveis de Ambiente > selecionar `Path` > Editar >
   Novo, colando o caminho da pasta `bin`) — isso é o que permite chamar `g++` de **qualquer**
   pasta, sem precisar copiar o compilador pra perto de cada programa.

`[TENTE VOCÊ]` Depois de instalar, como você confirma que o `g++` está acessível de qualquer
lugar? Resposta: abra o Prompt de Comando (ou PowerShell) em **qualquer** pasta e rode
`g++ --version`. Se aparecer a versão do compilador, o PATH está configurado certo. Se aparecer
"não é reconhecido como um comando", o PATH ainda não está certo (ou o terminal foi aberto antes
de configurar — feche e abra de novo).

Com o compilador instalado, abra o Prompt de Comando ou o PowerShell na pasta onde o `.cpp` foi
salvo — navegue até ela com `cd`, por exemplo:
```
cd Desktop
cd meus-programas
```
Depois, compile:
```
g++ programa.cpp -o programa.exe
```
Nada é executado aqui — só é gerado o arquivo `programa.exe` (o processo de compilação completo,
visto no tópico 13, roda por trás desse único comando).

## 75. Executar um programa

No **Prompt de Comando** (cmd): basta o nome do executável.
```
programa.exe
```
No **PowerShell**: é preciso prefixar com `.\`.
```
.\programa.exe
```
O `.\` é obrigatório no PowerShell por segurança (evita rodar sem querer um programa malicioso
que tenha o mesmo nome de um comando do sistema) — no Prompt de Comando clássico, isso não é
exigido. Essa diferença pega muita gente de surpresa na primeira vez.

`[ATENÇÃO]` Resumo dos três erros mais comuns nesse processo, e o que fazer em cada um:
- **`'g++' não é reconhecido como um comando interno ou externo`** → o PATH não foi configurado
  corretamente, ou o terminal foi aberto antes da configuração. O que fazer: revisar o tópico 74,
  e fechar/reabrir o terminal depois de qualquer mudança no PATH.
- **Arquivo salvo como `programa.cpp.txt` sem perceber** → ver o `[ATENÇÃO]` do tópico 73. O que
  fazer: ativar a exibição de extensões no Explorador de Arquivos e conferir antes de compilar.
- **Esquecer o `.\` no PowerShell** → o PowerShell reclama que não reconhece `programa.exe` como
  comando (ele procura primeiro nos comandos do sistema, não na pasta atual). O que fazer: sempre
  usar `.\programa.exe` no PowerShell (não é necessário no Prompt de Comando clássico).

## 76. Debuggar um programa

Fechando o ciclo completo do módulo: escrever (tópico 73) → compilar (tópico 74) → executar
(tópico 75) → e, quando algo dá errado, debugar (tópicos 70-72). No VSCode, com o compilador já
configurado, você pode colocar um breakpoint (clicando à esquerda do número da linha) e rodar em
modo debug — o programa pausa naquele ponto exato, e o painel lateral mostra o valor de cada
variável naquele instante. Isso substitui a estratégia (mais lenta, mas válida como primeiro
passo) de espalhar `std::cout` pelo código só pra "ver" o que está acontecendo.

`[TENTE VOCÊ]` Se um programa compila sem erro mas imprime um resultado errado, isso é um erro de
compilação ou de execução — e qual ferramenta ajuda mais a investigar? Resposta: erro de execução
(lógico, nesse caso) — um debugger, pausando o programa e inspecionando as variáveis passo a
passo, ajuda a achar exatamente onde o valor começa a divergir do esperado.

## Erros comuns

Você já viu estes avisos ao longo do módulo — aqui vai só a revisão rápida:

- Esquecer de recompilar depois de editar o código, e testar sem perceber que ainda está rodando
  a versão antiga.
- Escolher um tipo pequeno demais para o valor esperado, sem considerar o risco de overflow.
- Confundir decisão (`if`, um caminho ou outro) com repetição (`while`, o mesmo caminho várias
  vezes) na hora de montar o raciocínio de um algoritmo.
- Usar `=` em vez de `==` dentro de um `if` — a condição vira sempre verdadeira, e de quebra a
  variável é sobrescrita.
- Escrever um `while (true)` sem garantir que algo dentro do laço eventualmente torne a condição
  falsa — resultado é um laço infinito.
- Acessar um índice de array fora dos limites — comportamento indefinido, não um erro claro.
- Usar variáveis globais em vez de passar valores como parâmetro — dificulta rastrear onde um
  valor foi alterado.
- Esquecer `delete` depois de `new` — vazamento de memória.
- Recursão sem caso base — estoura a pilha (stack overflow).
- No Windows, salvar o arquivo como `programa.cpp.txt` sem perceber, ou esquecer o `.\` ao rodar
  um executável no PowerShell.

## Conexão com os próximos módulos

| Conceito deste módulo | Reaparece em |
|---|---|
| Sequência, decisão, repetição (`if`/`for`/`while`/`do-while`) | Módulo 09 — construção de algoritmos completos |
| Tipos e overflow | Reforça o módulo 03, agora dentro de um programa real |
| Funções, arrays, ponteiros | Módulo 09 — implementação dos algoritmos e estruturas de dados |
| C++ como linguagem-base, compilado no Windows | A linguagem e o fluxo de compilação usados nos exercícios do módulo 09 |

## `[REFERÊNCIA]`

- SEBESTA, Robert W. *Conceitos de Linguagens de Programação*, 5ª ed., Bookman, 2003.
- MSYS2 — documentação oficial de instalação: `https://www.msys2.org/`
- [cppreference.com](https://en.cppreference.com/w/) — referência oficial da linguagem C++
  (sintaxe, biblioteca padrão) — vale ter aberta enquanto pratica.
- [MinGW-w64](https://www.mingw-w64.org/) — documentação do compilador usado no setup Windows.

## Checklist de saída

- [ ] Explico a diferença entre compilador e interpretador, com o trade-off de cada um, e o
      caminho completo de código-fonte até executável.
- [ ] Explico o que é uma variável, os tipos primitivos de C++, e por que o tipo importa, ligando
      a overflow do módulo 03.
- [ ] Uso corretamente os operadores aritméticos, relacionais, lógicos e de atribuição, sabendo a
      precedência entre eles.
- [ ] Escrevo uma decisão (`if`/`else if`/`else`) em C++ para um problema dado, sem confundir `=`
      com `==`.
- [ ] Escrevo uma repetição em C++ escolhendo corretamente entre `for`, `while` e `do-while`, e
      uso `break`/`continue` quando fizer sentido.
- [ ] Escrevo e chamo funções com parâmetros e retorno, entendendo escopo local x global, e
      implemento uma recursão simples com caso base.
- [ ] Uso arrays, matrizes, structs e enumerações pra organizar dados relacionados.
- [ ] Explico o que é um ponteiro, uma referência, e a diferença entre stack e heap.
- [ ] Distingo um erro de compilação de um erro de execução, e sei usar um debugger básico.
- [ ] Escrevo o código no Bloco de Notas, salvo com a extensão `.cpp` correta, compilo com `g++`
      e executo o programa no Prompt de Comando ou PowerShell, sabendo a diferença entre os dois
      (`programa.exe` x `.\programa.exe`).
