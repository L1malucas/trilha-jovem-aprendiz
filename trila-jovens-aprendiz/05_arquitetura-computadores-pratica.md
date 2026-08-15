# Módulo 05 — Arquitetura de Computadores — Prática

> **Objetivo da prática:** consolidar o ciclo de execução de instruções e explorar, no seu
> próprio computador, os conceitos de CPU e memória vistos na teoria.
> **Pré-requisito:** [05_arquitetura-computadores-teoria.md](05_arquitetura-computadores-teoria.md)
> **Entregáveis:** um arquivo `respostas.md` neste módulo, no seu repositório do GitHub.
> **Formato de entrega:** publicado no GitHub, com README explicando a organização do repositório.

---

## Exercícios

### 1. Ciclo fetch–decode–execute

Descreva, passo a passo, o que aconteceria no ciclo fetch-decode-execute para uma instrução que
soma o valor de dois registradores e guarda o resultado em um terceiro. Use as três etapas
(busca, decodificação, execução) explicitamente.

### 2. CISC x RISC

Monte uma tabela comparando CISC e RISC com pelo menos 3 critérios (ex: complexidade das
instruções, exemplos de processadores, tamanho típico do código gerado).

### 3. Hierarquia de memória

Ordene do mais rápido/menor para o mais lento/maior: registrador, cache L1, RAM, disco SSD.
Explique, para cada salto na hierarquia, qual o trade-off entre velocidade e capacidade.

### 4. Explorando o seu computador

`[CLI]` Rode no terminal:
- Linux: `lscpu` (informações da CPU) e `free -h` (memória).
- Mac: `sysctl -n machdep.cpu.brand_string` (CPU) e `vm_stat` (memória).
- Windows: `systeminfo` (Prompt de Comando) para uma visão geral, ou de forma mais específica:
  `wmic cpu get name` (CPU), `wmic diskdrive get model,size,mediatype` (disco, incluindo se é
  HDD ou SSD quando disponível), e `dxdiag` (ferramenta gráfica, aba "Display") para a GPU/VRAM.
  No PowerShell, o equivalente mais moderno é `Get-CimInstance Win32_Processor | Select Name` e
  `Get-PhysicalDisk | Select FriendlyName, MediaType, Size`.

Cole a saída relevante e identifique, na saída, pelo menos 2 informações que apareceram na
teoria (ex: número de núcleos, clock, quantidade de memória, tipo de disco HDD/SSD).

### 5. Desafio

Pesquise o clock (em GHz) e o número de núcleos do processador do seu computador. Explique com
suas palavras o que cada um desses dois números significa na prática.

## Laboratórios

Sem hardware físico pra abrir, os laboratórios abaixo usam o que já está disponível: o compilador
C++ (Módulo 08) e o próprio terminal do seu computador.

### Laboratório 52 — Assembly

Não é preciso instalar nada novo — o compilador C++ que você já configurou no Módulo 08 consegue
gerar Assembly diretamente. Escreva um programa mínimo:
```cpp
int soma(int a, int b) {
    return a + b;
}
int main() {
    int r = soma(3, 4);
    return r;
}
```
Compile pedindo Assembly em vez de executável:
```
g++ -S programa.cpp -o programa.s
```
Abra `programa.s` (é texto puro, dá pra abrir no Bloco de Notas). Procure e cole, na sua entrega,
pelo menos duas instruções reconhecíveis (ex: alguma linha com `mov`, `add`, `call`). Explique com
suas palavras: essas instruções são o que a seção "Instruções de máquina / Assembly" da teoria
chamou de ISA — o vocabulário que a CPU entende, um passo antes do binário puro.

### Laboratório 53 — Memória

Rode o comando de memória do exercício 4 (`free -h`, `vm_stat`, ou `systeminfo`/`Get-CimInstance`
no Windows) de novo, mas desta vez também abra o Gerenciador de Tarefas (ou `top`/`htop` no
Linux/Mac) ao lado. Identifique **qual processo está consumindo mais memória** no momento e
calcule que porcentagem da RAM total instalada isso representa.

### Laboratório 54 — Cache (conceitual)

Sem comando pra "ver" a cache diretamente, resolva este cenário: um programa acessa repetidamente
a mesma variável dentro de um laço 1 milhão de vezes (padrão A); outro programa acessa 1 milhão de
posições diferentes e distantes de um array gigante, uma vez cada (padrão B). Responda, com
justificativa baseada no princípio de localidade já visto na teoria: qual dos dois se beneficia
mais da cache, e por quê o outro tende a gerar mais *cache misses*?

### Laboratório 55 — Fetch-Decode-Execute (mesa de simulação)

Considere este conjunto fictício de instruções e um PC (Program Counter) começando em `0`:
```
0: LOAD  R1, 10      // R1 = 10
1: LOAD  R2, 5       // R2 = 5
2: ADD   R3, R1, R2  // R3 = R1 + R2
3: STORE R3          // guarda R3 na memória
```
Preencha uma tabela com uma linha por instrução e três colunas (Fetch, Decode, Execute),
descrevendo o que acontece em cada etapa pra cada instrução (ex: na linha 2 — Fetch: busca a
instrução no endereço 2; Decode: identifica que é uma soma, operandos R1 e R2, destino R3;
Execute: a ULA soma os valores e grava em R3). Confirme, ao final, os valores de R1, R2 e R3.

### Laboratório 56 — CPU simplificada (desafio integrador)

Implemente em C++ uma "CPU simplificada" que executa a lista de instruções do Laboratório 55.
Use um `enum class Operacao { LOAD, ADD, STORE }`, uma `struct Instrucao` com os campos
necessários, um array/vector representando os registradores, e um `PC` (`int`) que avança a cada
instrução executada. A cada instrução processada, imprima o estado (PC atual + valores dos
registradores) — isso conecta, no mesmo exercício, os circuitos do Módulo 04 (a lógica), a
arquitetura deste módulo (a organização em ciclo fetch-decode-execute) e a programação do Módulo
08 (a implementação).

## Critérios de entrega

- Todo o conteúdo publicado em um repositório no GitHub.
- Um `README.md` na raiz do repositório, explicando a organização dos arquivos.
- Cada exercício com o enunciado copiado junto da resposta.
- No exercício 4 e nos laboratórios 52-53, a saída real do seu terminal — não um exemplo genérico.
- No laboratório 56, o código C++ deve compilar e rodar (documente a saída do terminal).

## Checklist de entrega

- [ ] Exercício 1 (ciclo fetch-decode-execute) resolvido com as 3 etapas explícitas.
- [ ] Exercício 2 (CISC x RISC) resolvido com tabela comparativa.
- [ ] Exercício 3 (hierarquia de memória) resolvido com trade-offs explicados.
- [ ] Exercício 4 (explorando o computador) resolvido com saída real do terminal.
- [ ] Exercício 5 (clock e núcleos) resolvido com explicação própria.
- [ ] Laboratório 52 (Assembly) resolvido, com trechos reais do `.s` gerado.
- [ ] Laboratório 53 (memória) resolvido, com processo mais pesado identificado.
- [ ] Laboratório 54 (cache) resolvido, com justificativa baseada em localidade.
- [ ] Laboratório 55 (Fetch-Decode-Execute) resolvido, com a tabela das 4 instruções.
- [ ] Laboratório 56 (CPU simplificada) resolvido, compilando e imprimindo o estado a cada passo.
