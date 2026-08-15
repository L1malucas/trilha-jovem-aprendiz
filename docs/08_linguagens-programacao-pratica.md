---
id: 08_linguagens-programacao-pratica
title: "Módulo 08 — Linguagens de Programação — Prática"
sidebar_position: 81
---

# Módulo 08 — Linguagens de Programação — Prática

> **Objetivo da prática:** escrever, compilar e executar programas simples em C++, entendendo
> compilação e execução como dois momentos distintos.
> **Pré-requisito:** [08_linguagens-programacao-teoria.md](08_linguagens-programacao-teoria.md)
> **Entregáveis:** os arquivos `.cpp` desta prática, mais um `README.md` explicando como compilar
> e rodar cada um.
> **Formato de entrega:** publicado no GitHub, com README contendo o passo a passo de execução.

---

## Exemplo resolvido

**Programa que lê um número e imprime o dobro dele:**
```cpp
#include <iostream>

int main() {
    int numero;
    std::cout << "Digite um número: ";
    std::cin >> numero;
    std::cout << "O dobro é: " << numero * 2 << "\n";
    return 0;
}
```

Salve como `dobro.cpp` (no Windows, usando o Bloco de Notas — ver a seção "Escrever, compilar e
rodar C++ no Windows" da teoria se ainda não fez isso, principalmente o cuidado com a extensão
`.cpp.txt`). Agora, dois momentos **distintos**:

1. **Compilar** (traduzir o texto inteiro pra um executável, uma vez só):
   ```
   g++ dobro.cpp -o dobro.exe
   ```
   Nada é executado aqui — só é gerado o arquivo `dobro.exe` (o executável). No Mac/Linux o mesmo
   comando funciona sem o `.exe` (`g++ dobro.cpp -o dobro`), já que esses sistemas não usam essa
   extensão para executáveis.

2. **Executar** (rodar o executável já traduzido, quantas vezes quiser, sem recompilar):
   - No **Prompt de Comando** (Windows): `dobro.exe`
   - No **PowerShell** (Windows): `.\dobro.exe` (o `.\` é obrigatório)
   - No **Mac/Linux**: `./dobro`

   Só agora o programa pede o número e mostra o resultado. Se você editar `dobro.cpp` depois
   disso, precisa repetir o passo 1 antes que a mudança apareça ao rodar o passo 2 de novo.

## Exercícios

### 1. Saudação personalizada

Escreva um programa que leia o nome digitado pelo usuário (como texto) e imprima uma saudação
com esse nome.

### 2. Soma de dois números

Escreva um programa que leia dois números inteiros e imprima a soma deles.

### 3. Compilando e executando, documentando os dois momentos

Compile e execute o programa do exercício 2. No seu `respostas.md`, cole o comando de compilação
usado, o comando de execução usado, e a saída do programa — deixando claro, por escrito, qual
comando corresponde a "traduzir" e qual corresponde a "rodar".

### 4. Provocando overflow de propósito

Declare uma variável do tipo `short` (que usa menos bits que `int`) e tente guardar nela um valor
maior do que ela suporta (pesquise o limite de um `short` antes — em C++ dá pra conferir com
`std::numeric_limits<short>::max()`, do cabeçalho `<limits>`). Imprima o valor guardado e observe
o resultado. Explique, com suas palavras, por que o valor impresso não é o valor que você tentou
guardar.

### 5. Classificando uma nota (decisão)

Escreva um programa que leia uma nota (0 a 100) e imprima o conceito correspondente usando
`if`/`else if`/`else`, seguindo a mesma faixa do exemplo da teoria (≥90 → A, ≥70 → B, ≥50 → C,
resto → D). Teste com pelo menos 4 valores diferentes, um pra cada conceito, documentando a
entrada e a saída de cada teste no `respostas.md`.

### 6. Somando com `for` e lendo até parar com `while`

Escreva dois programas:
- Um que leia um número `N` e some os `N` primeiros números inteiros usando `for` (adaptando o
  exemplo da teoria).
- Um que leia números digitados pelo usuário, um de cada vez, até ele digitar `-1`, e imprima
  quantos números (sem contar o `-1`) foram digitados, usando `while`.

### 7. Setup no Windows, documentado

Se você está usando Windows: escreva o programa do exercício 1 (Saudação personalizada) inteiro
no Bloco de Notas, salve com a extensão `.cpp` correta, compile pelo Prompt de Comando **ou**
PowerShell (escolha um) e rode o executável gerado. Tire um print da tela do terminal mostrando o
comando de compilação, o comando de execução e a saída do programa, e inclua esse print (ou o
texto copiado do terminal) no `respostas.md`. Se você usa Mac/Linux, documente o mesmo processo
no seu sistema, indicando isso claramente no `respostas.md`.

## Laboratórios

### Laboratório 77 — Variáveis

Escreva um programa que declare pelo menos 5 variáveis, uma de cada tipo básico (`int`, `double`,
`char`, `bool`, `std::string`), atribua um valor a cada uma e imprima todas com `std::cout`.
**Antes de compilar**, escreva no `respostas.md` qual saída você espera, linha por linha — só
depois compile e rode, comparando com o que você previu. Se algo divergir do que você esperava,
explique por quê antes de seguir.

### Laboratório 78 — Tipos

1. Escreva um programa que declare dois `int` (ex: `7` e `2`), divida um pelo outro e imprima o
   resultado. Antes de rodar, preveja a saída — a maioria de quem está começando espera `3.5` e se
   surpreende com o resultado real. Explique, com suas palavras, por que a divisão de dois `int`
   não produz um resultado decimal.
2. Corrija o programa acima convertendo (`static_cast<double>(...)`, ou uma conversão implícita
   colocando um `.0` num dos valores) pra obter o resultado decimal correto.

### Laboratório 79 — Operadores

Dada a expressão `10 + 2 * 3 - 4 / 2`, calcule o resultado **na mão**, escrevendo no
`respostas.md` a ordem em que você aplicou cada operador (lembrando da precedência: multiplicação
e divisão antes de soma e subtração). Só depois escreva um programa que imprime o resultado dessa
expressão e confira se bateu com sua conta manual.

### Laboratório 80 — Funções

1. Escreva uma função `int somar(int a, int b)` que recebe dois parâmetros e retorna a soma,
   chamando-a a partir de `main()`.
2. Escreva uma função recursiva `int fatorial(int n)` que calcula o fatorial de `n`. No
   `respostas.md`, narre o que acontece na pilha de chamadas pra `fatorial(4)` — cada chamada
   empilhada até o caso base, depois cada retorno desempilhando e multiplicando.

### Laboratório 81 — Arrays

Sem usar nenhum método pronto da biblioteca padrão (nada de `std::max_element`,
`std::accumulate`, etc. — mesma regra já usada no módulo 09), escreva um programa que, dado um
array de 10 inteiros:
1. Percorra e imprima todos os elementos.
2. Some todos os elementos e imprima o total.
3. Encontre e imprima o maior elemento.

### Laboratório 82 — Ponteiros

1. Escreva uma função `void trocar(int* a, int* b)` que troca o valor de duas variáveis usando
   ponteiros (o clássico `swap` manual), e chame-a a partir de `main()` provando que os valores
   trocaram de fato.
2. Declare uma variável `int x = 10;`, imprima o **endereço** dela com `&x`, depois declare um
   ponteiro `int* p = &x;` e imprima o **valor apontado** por ele com `*p` — confirme que
   `*p` é igual a `x`.

### Laboratório 83 — Compilação

1. Compile um programa com um erro proposital (ex: uma variável não declarada usada em
   `std::cout`) usando a flag de avisos: `g++ -Wall arquivo.cpp -o arquivo.exe`. Cole no
   `respostas.md` a mensagem de aviso/erro exibida, e explique o que ela está dizendo.
2. Usando um programa simples já pronto (ex: o do Laboratório 79), gere o Assembly correspondente
   com `g++ -S arquivo.cpp -o arquivo.s` (a mesma flag já usada no módulo 05) e identifique, no
   arquivo `.s` gerado, pelo menos uma instrução reconhecível (`mov`, `add`, `sub`).

### Laboratório 84 — Debugging

Escreva um programa pequeno com um bug proposital (ex: um loop `for` com a condição errada, que
roda uma vez a menos ou a mais do que deveria — um "off-by-one"). Usando o debugger integrado do
VSCode:
1. Coloque um breakpoint na linha do loop.
2. Rode em modo debug e use "Step Over"/"Step Into" pra avançar linha por linha.
3. Inspecione o valor da variável de controle do loop a cada passo, até identificar exatamente em
   qual iteração o comportamento diverge do esperado.

No `respostas.md`, descreva o bug encontrado, em qual iteração ele ficou evidente, e a correção
aplicada.

## Critérios de entrega

- Todo o conteúdo publicado em um repositório no GitHub.
- Um `README.md` na raiz do repositório, explicando como compilar e rodar cada exercício.
- Cada exercício com o enunciado copiado junto da resposta (código + explicação, quando pedido).

## Checklist de entrega

- [ ] Exercício 1 (saudação) resolvido, compilado e testado.
- [ ] Exercício 2 (soma) resolvido, compilado e testado.
- [ ] Exercício 3 (documentando compilação x execução) resolvido, com os dois comandos e a saída
      colados.
- [ ] Exercício 4 (overflow de propósito) resolvido, com o resultado explicado.
- [ ] Exercício 5 (classificando uma nota) resolvido, com os 4 testes documentados.
- [ ] Exercício 6 (soma com `for` e leitura com `while`) resolvido, os dois programas.
- [ ] Exercício 7 (setup no Windows/Mac/Linux documentado) resolvido, com print ou saída do
      terminal.
- [ ] Laboratório 77 (variáveis) resolvido, com a previsão de saída registrada antes de compilar.
- [ ] Laboratório 78 (tipos) resolvido, com a divisão inteira explicada e corrigida.
- [ ] Laboratório 79 (operadores) resolvido, com a conta manual de precedência registrada.
- [ ] Laboratório 80 (funções) resolvido, com a pilha de chamadas da recursão narrada.
- [ ] Laboratório 81 (arrays) resolvido, sem métodos prontos da biblioteca padrão.
- [ ] Laboratório 82 (ponteiros) resolvido, com o `swap` manual e o endereço/valor apontado.
- [ ] Laboratório 83 (compilação) resolvido, com o aviso do `-Wall` explicado e o Assembly gerado.
- [ ] Laboratório 84 (debugging) resolvido, com o bug e a correção descritos.
- [ ] Publicado no GitHub com README explicando como compilar e rodar.
