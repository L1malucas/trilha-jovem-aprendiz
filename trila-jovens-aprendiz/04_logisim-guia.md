# Módulo 04 — Guia do Logisim

> **Objetivo:** aprender a montar, testar e entregar circuitos digitais no Logisim.
> **Ferramenta:** [logisim.app](https://logisim.app/) — Logisim 2.7.2 rodando no navegador (WebAssembly), sem instalação.
> **Usado em:** [teoria](04_circuitos-digitais-teoria.md) (experimentos) e [prática](04_circuitos-digitais-pratica.md) (exercícios e laboratórios).

---

## 1. Primeiros passos

1. Abra [logisim.app](https://logisim.app/).
2. Baixe o arquivo inicial do exercício (links na prática) e abra com **File > Open**.
3. Monte o circuito, teste, e salve com **File > Save** (gera um arquivo `.circ`).

> O logisim.app é uma adaptação do Logisim 2.7.2 para o navegador. Se algum recurso deste guia
> não aparecer, use o Logisim Evolution (desktop) — os arquivos `.circ` são compatíveis.
> Se o navegador não guardar o arquivo, **salve sempre uma cópia no seu computador** antes de fechar a aba.

## 2. A interface

| Área | Para que serve |
|---|---|
| Barra de ferramentas | Poke (mão), Edit (seta), texto, e as portas mais usadas |
| Explorer (esquerda) | Bibliotecas de componentes: Wiring, Gates, Plexers, Arithmetic, Memory, Input/Output |
| Attribute table | Propriedades do componente selecionado (nome, nº de bits, nº de entradas) |
| Canvas | Onde o circuito é montado |

Ferramentas principais:

- **Poke (mão):** muda o valor dos pins de entrada clicando neles. É assim que você testa.
- **Edit (seta):** seleciona, move e liga componentes.
- Para ligar: arraste de um ponto de conexão a outro com a ferramenta Edit.

## 3. Componentes que você vai usar

| Biblioteca | Componente | Uso no módulo |
|---|---|---|
| Wiring | Pin (entrada/saída) | Entradas A, B… e saídas |
| Wiring | Splitter, Constant, Clock | Barramentos de bits, valor fixo, pulso de clock |
| Gates | NOT, AND, OR, XOR, NAND, NOR, XNOR | Itens 8–14 da teoria |
| Plexers | Multiplexer, Demultiplexer, Decoder | Itens 22–25 |
| Arithmetic | Adder, Comparator | Itens 26–29 |
| Memory | D Flip-Flop, Register, Counter | Itens 32–35 |
| Input/Output | LED, Hex Digit Display | Ver a saída de forma visual |

## 4. Como testar

1. **Manual:** clique nos pins de entrada com a Poke e observe a saída. Fio verde-escuro = 0, verde-claro = 1.
2. **Tabela-verdade automática:** menu **Window > Combinational Analysis**. Ela lê as entradas e saídas do circuito e gera a tabela-verdade; compare com a tabela que você montou à mão. Também funciona no sentido contrário: preencha a tabela e a ferramenta sugere a expressão e o circuito.
3. **Circuitos com clock:** use **Simulate > Ticks Enabled** (ou **Ctrl+K** para um tick manual) e observe o `Q` mudar somente na borda de subida.

## 5. Convenções do módulo

- Dê **nome a todos os pins** (atributo *Label*): `A`, `B`, `SOMA`, `CARRY`… Os arquivos iniciais já vêm com os nomes certos — não renomeie.
- Entradas à esquerda, saídas à direita, fluxo da esquerda para a direita.
- Um circuito por arquivo, circuito principal chamado `main`.
- Nome do arquivo entregue: o mesmo do arquivo inicial (ex.: `ex05_meio_somador.circ`).

## 6. Como entregar

Na pasta `modulo-04/` do seu repositório, junto do `respostas.md`:

- os arquivos `.circ`;
- um **print** de cada circuito funcionando (um caso de teste visível), salvo como PNG;
- referência aos arquivos no `respostas.md`.

## 7. Problemas comuns

| Sintoma | Causa provável |
|---|---|
| Fio **vermelho** | Conflito: duas saídas ligadas no mesmo fio |
| Fio **azul** ou saída `E`/`x` | Entrada sem conexão ou ponta de fio solta |
| Saída em `x` depois de ligar | Faltou ligar uma entrada da porta; confira os pontos de conexão |
| Fio cruzando outro não liga | Fios só se conectam em pontas — termine o fio exatamente no ponto |
| Flip-flop não muda | O clock não está ativo ou `D` mudou fora da borda de subida |
| Larguras diferentes | Pin de 4 bits ligado em pin de 1 bit: use Splitter |

## 8. Exemplos prontos

Abra no Logisim para ver circuitos completos (também citados na teoria):

- [`portas_basicas.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/examples/portas_basicas.circ) — AND, OR, XOR, NAND, NOR, XNOR.
- [`meio_somador.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/examples/meio_somador.circ) — meio somador.
- [`somador_completo.circ`](pathname:///trilha-jovem-aprendiz/logisim/04/examples/somador_completo.circ) — somador completo.
