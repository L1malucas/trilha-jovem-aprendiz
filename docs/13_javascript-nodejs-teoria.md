---
id: 13_javascript-nodejs-teoria
title: "Módulo 13 — JavaScript / Node.js"
sidebar_position: 130
---

# Módulo 13 — JavaScript / Node.js

> **Objetivo:** entender JavaScript como linguagem interpretada, o runtime Node.js (V8 + libuv,
> Event Loop) e os módulos nativos que sustentam qualquer ferramenta de linha de comando real
> (fs, readline, http).
> **Pré-requisitos:** Módulo 12 (SQL Server) concluído.
> **Tempo de referência:** 14 a 18 horas (módulo mais extenso da trilha — cobre os 12 módulos
> completos do workshop-fonte: runtime, assincronicidade, arquivos, terminal, rede, processos,
> streams, pacotes, CLI, classes e estruturas de dados lineares/não-lineares, performance e
> segurança).
> **Prática correspondente:** [13_javascript-nodejs-pratica.md](13_javascript-nodejs-pratica.md)

---

## Por que isso importa

Este é o módulo final da trilha, e ele reúne o que veio antes: o raciocínio algorítmico do
módulo 09, a estruturação de código do módulo 08, a manipulação de dados dos módulos 11 e 12, e
até os conceitos de processo/E-S do módulo 06 — tudo numa única linguagem que roda tanto no
navegador quanto no servidor. A prática deste módulo é construir, peça por peça, uma ferramenta
de linha de comando real (o **DevTrack**) — então a teoria aqui foi escolhida a dedo pra te dar
exatamente o que você vai precisar nela.

## `[TEORIA]` JavaScript como linguagem interpretada

No módulo 08 você viu a diferença entre linguagem compilada (o código inteiro é traduzido pra
máquina antes de rodar) e interpretada (o código é lido e executado, sem uma etapa de compilação
separada visível pra você). JavaScript é interpretada: você escreve o código, manda rodar, e ele
executa direto.

```js
console.log("Olá, mundo!");
```
Essa linha, sozinha, já é um programa completo e executável.

## `[TEORIA]` Variáveis e tipagem dinâmica

No módulo 08, C++ exigia declarar o tipo de cada variável antes de usá-la (`int idade = 20;`) — o
compilador checa esses tipos antes mesmo do programa rodar. JavaScript faz o oposto: você declara
a variável sem dizer o tipo, e o tipo é decidido em tempo de execução, pelo valor que ela recebe
naquele momento — e pode até mudar depois:

```js
let idade = 20;        // aqui, idade é um número
idade = "vinte anos";  // agora, a mesma variável virou texto — sem erro
```

Isso é **tipagem dinâmica**. Ela dá flexibilidade, mas troca a segurança que a checagem de tipos
do compilador C++ te dava — um erro de tipo em JavaScript só aparece quando aquela linha
específica roda, não antes.

`[TENTE VOCÊ]` O que a linha `console.log("2" + 3)` imprime, e por quê? Resposta: `"23"` — como
`"2"` é texto, o operador `+` concatena em vez de somar números.

`[ATENÇÃO]` Esse comportamento — `+` ora somando, ora concatenando, dependendo do tipo em tempo
de execução — é fonte clássica de bugs silenciosos. Confira sempre o tipo de um valor que vem de
fora (input do usuário, resposta de rede, leitura de arquivo) antes de operar com ele.

## `[TEORIA]` Node.js: o runtime por trás do DevTrack

JavaScript nasceu pra rodar dentro do navegador — cada navegador tem um motor que interpreta o
código (o do Chrome se chama **V8**). O Node.js pegou esse mesmo motor V8 e o combinou com uma
segunda peça, a **libuv**, uma biblioteca de E/S assíncrona — e empacotou os dois pra rodar
sozinhos no terminal, sem navegador. É essa dupla que faz o Node funcionar:

| Componente | Papel | O que faz |
|---|---|---|
| **V8** | Motor JS | Compila e executa o JavaScript — gerencia a Call Stack, memória e otimizações |
| **libuv** | E/S assíncrona | Gerencia o Event Loop, o thread pool de disco/rede/DNS |
| **Bindings C++** | Ponte | Conectam as APIs do Node (`fs`, `http`, `crypto`) ao sistema operacional |

`[ATENÇÃO]` É comum ouvir "Node é single-threaded" e concluir que ele não usa nenhuma outra
thread — impreciso. A *sua* Call Stack (o código JavaScript que você escreve) roda numa única
thread. Mas a libuv usa um pool de threads *por baixo dos panos* para as operações de E/S — é
isso que permite ao Node atender milhares de conexões sem travar, delegando o trabalho pesado
para fora da thread principal, exatamente como o sistema operacional intermedia E/S visto no
módulo 06.

## `[TEORIA]` O Event Loop: por que o Node não trava esperando

**Call Stack** é a estrutura (LIFO — Last In, First Out) que rastreia onde o programa está na
execução: uma função chamada entra na pilha, uma função que retorna sai. Se ela nunca esvaziar
(loop infinito, recursão sem caso base), o processo trava — **stack overflow**.

Operações de E/S (ler um arquivo, fazer uma requisição HTTP) levam tempo — colocá-las direto na
Call Stack travaria tudo enquanto esperam. Em vez disso, o Node delega essas operações à libuv, e
o **Event Loop** — o mecanismo que faz o Node "não-bloqueante" — fica de olho em filas de
callbacks prontos pra rodar assim que a Call Stack esvazia:

```js
console.log("1 — síncrono");
setTimeout(() => console.log("3 — macrotask (setTimeout)"), 0);
Promise.resolve().then(() => console.log("2 — microtask (Promise)"));
console.log("1.5 — ainda síncrono");
```
**Raciocínio, linha por linha:** as duas chamadas de `console.log` síncronas rodam primeiro,
porque estão direto na Call Stack. `Promise.resolve().then(...)` agenda uma **microtask** — o
Node esvazia completamente a fila de microtasks assim que a Call Stack fica livre, antes de
qualquer outra coisa. `setTimeout(..., 0)` agenda uma **macrotask** — só roda depois, na fase
seguinte do loop, mesmo com delay zero.

`[TENTE VOCÊ]` Qual é a ordem real de saída do código acima? Resposta:
`"1 — síncrono"`, `"1.5 — ainda síncrono"`, `"2 — microtask (Promise)"`,
`"3 — macrotask (setTimeout)"` — síncrono primeiro, microtasks segundo, macrotasks por último.

## `[TEORIA]` De callbacks a async/await

O padrão mais antigo de assincronicidade em JavaScript é o **callback**: uma função passada como
argumento, chamada quando a operação termina. Node.js consagrou o padrão **error-first callback**
— o primeiro argumento do callback é sempre um erro (ou `null`):

```js
fs.readFile("dados.json", "utf-8", (err, conteudo) => {
  if (err) { console.error("Erro:", err.message); return; }
  console.log(JSON.parse(conteudo));
});
console.log("Isso executa ANTES do callback acima");
```

Quando várias operações assíncronas precisam acontecer em sequência, os callbacks se aninham —
o "Pyramid of Doom". **Promises** resolvem isso: um objeto que representa o resultado futuro de
uma operação, em um de três estados (`pending`, `fulfilled`, `rejected`), permitindo encadear com
`.then()`/`.catch()` em vez de aninhar.

`async/await` é **açúcar sintático** sobre Promises — não é um mecanismo novo, é a mesma coisa
escrita de um jeito que lê como código síncrono:

```js
async function carregarConfig() {
  try {
    const texto = await fs.promises.readFile("config.json", "utf-8");
    return JSON.parse(texto);
  } catch (err) {
    if (err.code === "ENOENT") return { porta: 3000 }; // valor padrão
    throw err; // re-lança o que não sabemos tratar
  }
}
```
Com `async/await`, o tratamento de erro volta ao `try/catch` de sempre — o fluxo de erro fica
visualmente colado ao código que pode falhar, diferente da cadeia de `.catch()` das Promises.

`[ATENÇÃO]` Esquecer o `await` antes de uma chamada assíncrona é um dos erros mais comuns — a
função continua executando sem esperar o resultado, e você acaba com uma Promise pendente no
lugar do valor esperado, em vez de um erro óbvio.

## `[TEORIA]` Sistema de arquivos com `fs/promises`

O DevTrack (a ferramenta que você vai construir na prática) persiste tudo em um arquivo JSON
local — e para isso usa o submódulo `fs/promises`, a versão moderna do `fs` que retorna Promises
em vez de pedir callback:

```js
import { readFile, writeFile, rename } from "fs/promises";

async function salvarJSON(caminho, dados) {
  const tmp = caminho + ".tmp";
  await writeFile(tmp, JSON.stringify(dados, null, 2), "utf-8");
  await rename(tmp, caminho); // operação atômica: não corrompe se falhar no meio
}
```
Por que escrever num arquivo temporário e depois renomear, em vez de escrever direto no arquivo
final? Porque `rename` é atômico no sistema operacional — ou o arquivo final é totalmente
substituído, ou nada muda. Escrever direto arrisca deixar um JSON pela metade se o processo cair
no meio da escrita.

`[ATENÇÃO]` Existe uma versão síncrona (`readFileSync`, `writeFileSync`) que bloqueia a Call
Stack até terminar. É aceitável só em dois casos: scripts simples de linha de comando que não
precisam atender mais ninguém enquanto isso, ou ler configuração uma única vez, no início do
programa, antes de qualquer outra coisa rodar. Num servidor (como o que você vai construir na
Tarefa 9 da prática), usar a versão síncrona trava *todas* as conexões enquanto um único arquivo
é lido.

## `[TEORIA]` Terminal interativo com `readline`

O módulo `readline` lê entrada do usuário linha por linha — é a base de qualquer menu interativo
no terminal, como o primeiro CLI do DevTrack:

```js
import readline from "readline";
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

// rl.question é baseado em callback — envolver em Promise permite usar await
const perguntar = (texto) => new Promise((resolve) => rl.question(texto, resolve));

const nome = await perguntar("Qual o título da tarefa? ");
console.log(`Tarefa "${nome}" registrada.`);
```

Um detalhe que muda o comportamento de um CLI real: `process.stdout.isTTY` é `true` só quando a
saída vai para um terminal interativo de verdade — `false` quando é redirecionada para um arquivo
ou outro programa (`node cli.js | cat`). Programas bem-feitos detectam isso e trocam tabelas
coloridas por um JSON limpo quando não há terminal do outro lado.

`[TENTE VOCÊ]` Se você rodar `node cli.js` direto no terminal, `process.stdout.isTTY` é `true` ou
`false`? E se rodar `node cli.js | cat`? Resposta: `true` no primeiro caso (terminal interativo
real); `false` no segundo (a saída está sendo redirecionada para outro processo).

## `[TEORIA]` Rede e HTTP no Node

O módulo 07 já cobriu os conceitos de HTTP/URL em geral — aqui é como o Node os expõe como código.
Um servidor HTTP nativo, sem framework:

```js
import http from "http";

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host}`);
  res.setHeader("Content-Type", "application/json");

  if (req.method === "GET" && url.pathname === "/health") {
    res.writeHead(200);
    return res.end(JSON.stringify({ status: "ok" }));
  }
  res.writeHead(404);
  res.end(JSON.stringify({ error: "Not Found" }));
});
server.listen(3000, () => console.log("Servidor em http://localhost:3000"));
```

Para *consumir* uma API externa, o Node 18+ já traz `fetch` global — sem precisar importar nada:

```js
const resposta = await fetch("https://api.github.com/repos/nodejs/node/issues");
if (!resposta.ok) throw new Error(`HTTP ${resposta.status}`);
const issues = await resposta.json();
```

## `[TEORIA]` Módulos: CommonJS x ES Modules

O Node suporta dois sistemas de módulos, e você vai encontrar os dois em projetos reais.
**CommonJS (CJS)** é o padrão histórico — síncrono, usa `require`/`module.exports`. **ES Modules
(ESM)** é o padrão moderno — usa `import`/`export`, é estático (analisável antes de rodar, o que
permite otimizações) e suporta `await` no nível superior do arquivo.

```js
// CommonJS — math.js
function soma(a, b) { return a + b; }
module.exports = { soma };

// app.js
const { soma } = require("./math");

// ES Modules — math.mjs (ou package.json com "type": "module")
export function soma(a, b) { return a + b; }

// app.mjs
import { soma } from "./math.mjs";
const dados = await readFile("config.json", "utf-8"); // top-level await só em ESM
```

`[ATENÇÃO]` Em CommonJS, `__dirname` e `__filename` existem automaticamente. Em ESM, não —
recrie-os assim:
```js
import { fileURLToPath } from "url";
import path from "path";
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
```

## `[TEORIA]` O objeto global `process`

`process` é a interface entre o seu script e o processo do sistema operacional — sempre
disponível, sem precisar de `import`. É essencial pra qualquer ferramenta de linha de comando.

```js
// Argumentos: node app.js add "Minha tarefa" --prioridade=alta
const [,, comando, ...args] = process.argv;
console.log(comando); // "add"

// Variáveis de ambiente
const porta = process.env.PORT ?? 3000;

// Informações do processo
console.log(process.pid, process.platform, process.cwd());

// Controle de saída — 0 = sucesso, qualquer outro = erro (convenção Unix)
process.exit(0);

// Capturar sinais do sistema operacional
process.on("SIGINT", () => {          // Ctrl+C
  console.log("\nEncerrando...");
  process.exit(0);
});
process.on("SIGTERM", () => {         // enviado por docker stop, systemctl stop
  limpezaGraciosa().then(() => process.exit(0));
});
```

`[TENTE VOCÊ]` Você roda `node app.js remover 42` — o que `process.argv[2]` contém? Resposta:
`"remover"` — os dois primeiros itens de `process.argv` são sempre o caminho do executável Node e
o caminho do script; os argumentos reais começam no índice 2.

## `[TEORIA]` Promise combinators e `util.promisify`

Além de encadear Promises uma a uma, existem quatro formas de esperar **várias ao mesmo tempo**:

| Combinador | Comportamento |
|---|---|
| `Promise.all` | Espera todas; falha se qualquer uma falhar |
| `Promise.allSettled` | Espera todas, mesmo com falhas — retorna status de cada uma |
| `Promise.race` | Retorna assim que a primeira resolver **ou** rejeitar |
| `Promise.any` | Retorna a primeira que resolver com sucesso; só falha se todas falharem |

```js
const [usuarios, posts, config] = await Promise.all([
  buscarUsuarios(), buscarPosts(), lerConfig(),
]);
```

`util.promisify` converte qualquer função no padrão error-first callback (como `exec`, do módulo
que você vai ver a seguir) numa função que retorna Promise, sem reescrevê-la:
```js
import { promisify } from "util";
import { exec } from "child_process";
const execAsync = promisify(exec);
const { stdout } = await execAsync("git log --oneline -5");
```

## `[TEORIA]` O módulo `path` — caminhos entre sistemas operacionais

Nunca concatene caminhos de arquivo com `+` — Windows usa `\`, Unix usa `/`. O módulo `path`
resolve isso automaticamente, gerando o separador certo pro sistema onde o código está rodando:

```js
import path from "path";
const dbPath = path.join(__dirname, "data", "db.json");
// Windows:  C:\Users\voce\projeto\data\db.json
// Linux/Mac: /home/voce/projeto/data/db.json

path.dirname("/home/voce/src/index.js");  // "/home/voce/src"
path.basename("/home/voce/src/index.js"); // "index.js"
path.extname("/home/voce/src/index.js");  // ".js"
```

## `[TEORIA]` `fs.watch` — monitorando arquivos em tempo real

`fs.watch` observa um arquivo ou pasta e chama um callback a cada mudança — é a base de
ferramentas como hot-reload:
```js
import { watch } from "fs";
watch("./src", { recursive: true }, (evento, caminho) => {
  if (caminho?.endsWith(".js")) console.log(`Arquivo modificado: ${caminho}`);
});
```

## `[TEORIA]` Processos e sistema: `child_process`

Retome o módulo 06 (Sistemas Operacionais): lá você aprendeu que um processo pode criar processos
filhos. `child_process` é como o Node faz isso — deixa seu script executar outros programas
(comandos de shell, outros scripts, executáveis) e capturar o resultado.

| Método | Comportamento | Usar quando |
|---|---|---|
| `exec()` | Bufferiza toda a saída na memória, entrega no final | Comandos curtos, saída pequena |
| `execSync()` | Igual, mas síncrono — bloqueia a thread | Scripts simples, configuração pontual |
| `spawn()` | Entrega a saída em streams, em tempo real | Processos longos com muita saída |
| `fork()` | Cria um processo Node filho com canal de comunicação (IPC) | Comunicação entre processos Node |

```js
import { exec, spawn } from "child_process";
import { promisify } from "util";
const execAsync = promisify(exec);

// exec (promisificado) — resultado curto, de uma vez
async function getBranchAtual() {
  const { stdout } = await execAsync("git branch --show-current");
  return stdout.trim();
}

// spawn — saída em tempo real (ex: instalando dependências)
function instalarDependencias() {
  return new Promise((resolve, reject) => {
    const npm = spawn("npm", ["install"], { stdio: "inherit" });
    npm.on("close", (code) => code === 0 ? resolve() : reject(new Error(`código ${code}`)));
  });
}
```

O módulo `os` (irmão do `child_process`) expõe informações do sistema — retome o módulo 05
(hardware) e o módulo 06 (SO), agora acessíveis via código:
```js
import os from "os";
console.log({
  plataforma: os.platform(),   // "linux" | "darwin" | "win32"
  nucleos: os.cpus().length,   // conecta com CPU multicore, módulo 05
  ramLivre: os.freemem(),      // conecta com memória, módulo 05
});
```

`[ATENÇÃO]` `exec`/`execSync` rodam o comando através de um shell — se você concatenar entrada de
usuário direto na string do comando, abre brecha pra injeção de shell. Prefira `execFile`/`spawn`
com argumentos como array separado quando a entrada não é 100% controlada por você.

## `[TEORIA]` Streams: processar dados sem carregar tudo na memória

Retome a hierarquia de memória do módulo 05: RAM é limitada, e carregar um arquivo de 500MB
inteiro na memória antes de processar é desperdício, quando dá pra processar em pedaços. É
exatamente isso que uma **stream** faz — processa dados em **chunks** (pedaços pequenos,
tipicamente 64KB), sem esperar o arquivo inteiro chegar.

Isso não é exclusivo do Node: é o mesmo princípio por trás de assistir um vídeo no YouTube antes
dele terminar de baixar, ou fazer upload de um arquivo de 10GB pro Google Drive sem o servidor
precisar de 10GB de RAM livre.

**Exemplo narrado — o ganho é real, não só teórico:** processando um arquivo de log de 500MB
carregando tudo de uma vez, o processo usa ~500MB de RAM e leva 4800ms. Processando o mesmo
arquivo como stream, chunk por chunk, o processo usa ~64KB de RAM (7800 vezes menos) e leva
1200ms (4x mais rápido) — porque o processamento de um chunk já começa enquanto o próximo ainda
está sendo lido do disco.

Existem 4 tipos de stream: **Readable** (fonte de dados, ex: ler um arquivo), **Writable**
(destino, ex: escrever um arquivo), **Transform** (lê, transforma, e passa adiante — ex:
compressão), **Duplex** (readable e writable ao mesmo tempo, ex: um socket de rede). A forma
segura de conectar streams é `pipeline`, que já trata erros automaticamente:

```js
import { createReadStream, createWriteStream } from "fs";
import { pipeline } from "stream/promises";
import zlib from "zlib";

await pipeline(
  createReadStream("logs/app.log"),      // Readable
  zlib.createGzip(),                     // Transform — comprime
  createWriteStream("logs/app.log.gz"),  // Writable
);
```

`[TENTE VOCÊ]` Por que usar `pipeline` em vez de conectar as streams manualmente com `.pipe()`
encadeado? Resposta: `pipeline` garante que, se qualquer stream do meio falhar, todas as outras
são fechadas corretamente — conectar manualmente exige tratar isso você mesmo, e é fácil esquecer,
deixando handles de arquivo abertos.

## `[TEORIA]` Gerenciamento de pacotes: npm e `package.json`

O `package.json` é o manifesto completo do seu projeto — não é só uma lista de dependências:

```json
{
  "name": "devtrack",
  "version": "1.0.0",
  "type": "module",
  "bin": { "devtrack": "./cli.js" },
  "scripts": {
    "start": "node src/index.js",
    "test": "node --test"
  },
  "dependencies": { "commander": "^12.0.0", "chalk": "^5.3.0" },
  "devDependencies": { "eslint": "^8.57.0" },
  "engines": { "node": ">=18" }
}
```

`dependencies` vai junto com o pacote publicado (necessário em produção); `devDependencies` só
existe durante o desenvolvimento (ex: linter, ferramentas de teste).

O **Versionamento Semântico** (já visto no módulo 02, agora do lado de bibliotecas de terceiros)
controla como o npm decide qual versão instalar:

| Notação | Significado | Exemplo |
|---|---|---|
| `^4.2.1` | Aceita qualquer `4.x.x >= 4.2.1` | Pode instalar `4.9.0` |
| `~4.2.1` | Aceita qualquer `4.2.x >= 4.2.1` | Só instala `4.2.x` |
| `4.2.1` (sem prefixo) | Só essa versão exata | Nunca atualiza sozinho |

## `[TEORIA]` CLI profissional: Commander, Chalk, Ora, Inquirer

Os fundamentos nativos (readline, process.argv) resolvem o básico — bibliotecas do ecossistema
elevam uma ferramenta de linha de comando a nível profissional:

```js
// Commander.js — estrutura de comandos e flags, no lugar de parsear argv na mão
import { Command } from "commander";
new Command()
  .name("devtrack")
  .command("add <titulo>")
  .option("-p, --prioridade <n>", "alta|media|baixa", "media")
  .action(async (titulo, opts) => await adicionarTarefa(titulo, opts))
  .parse(process.argv);
// $ devtrack add "Implementar login" -p alta

// Chalk — cores no terminal
import chalk from "chalk";
console.log(chalk.green("✓ Tarefa criada!"), chalk.red.bold("✗ Erro"));

// Ora — indicador de progresso (spinner)
import ora from "ora";
const spinner = ora("Sincronizando...").start();
try { await sincronizar(); spinner.succeed("Sincronizado!"); }
catch (err) { spinner.fail(`Erro: ${err.message}`); }

// Inquirer — formulários interativos no terminal
import inquirer from "inquirer";
const respostas = await inquirer.prompt([
  { type: "input", name: "titulo", message: "Título:" },
  { type: "list", name: "prioridade", choices: ["alta", "media", "baixa"] },
]);
```

## `[TEORIA]` Sintaxe de classes em JavaScript

Classes em JS são açúcar sintático — uma forma mais legível de organizar código que, por baixo,
continua sendo baseado em protótipos. É a sintaxe usada daqui pra frente pra construir estruturas
de dados.

```js
class Estrutura {
  #itens = [];               // campo privado (ES2022) — SyntaxError se acessado de fora
  static totalCriadas = 0;   // campo estático — compartilhado por todas as instâncias

  constructor(nome) {
    this.nome = nome;
    Estrutura.totalCriadas++;
  }

  adicionar(item) {           // método público
    this.#itens.push(item);
    return this;              // permite encadear: est.adicionar(a).adicionar(b)
  }

  get tamanho() { return this.#itens.length; }   // getter — lido sem parênteses
  toString() { return `${this.nome}(${this.tamanho})`; }
  [Symbol.iterator]() { return this.#itens[Symbol.iterator](); } // habilita for...of
}
```

**Herança** com `extends`/`super` — a classe filha herda tudo da mãe e pode sobrescrever métodos:
```js
class Stack extends Estrutura {
  #items = [];
  constructor() { super("Stack"); } // super() é obrigatório antes de usar `this`
  push(item) { this.#items.push(item); }
  pop() { return this.#items.pop(); }
}
```

`[ATENÇÃO]` Esquecer `super()` no construtor de uma classe filha (antes de usar `this`) gera
erro — é o equivalente, em herança, de tentar usar uma variável antes de inicializá-la.

Um uso muito prático de `extends`: **classes de erro customizadas**, que permitem capturar tipos
específicos com `instanceof`:
```js
class DevTrackError extends Error {
  constructor(mensagem, codigo) {
    super(mensagem);
    this.codigo = codigo;
  }
}
class TarefaNaoEncontrada extends DevTrackError {
  constructor(id) { super(`Tarefa "${id}" não encontrada`, "TASK_NOT_FOUND"); }
}
// captura seletiva por tipo de erro
try { await buscarTarefa("abc"); }
catch (err) {
  if (err instanceof TarefaNaoEncontrada) console.error("404:", err.message);
  else throw err;
}
```

## `[TEORIA]` Stack e Queue — estruturas de dados lineares

**Stack (pilha)** segue **LIFO** — o último item que entra é o primeiro que sai (uma pilha de
pratos). Aplicação real: histórico de desfazer/refazer.
```js
class Stack {
  #items = [];
  push(item) { this.#items.push(item); }   // O(1)
  pop() { return this.#items.pop(); }      // O(1)
  peek() { return this.#items.at(-1); }
}
```

**Queue (fila)** segue **FIFO** — o primeiro que entra é o primeiro que sai (uma fila de banco).
Implementar com `Array.shift()` funciona, mas é O(n) — reindexia todo o array a cada remoção. A
versão eficiente usa um objeto com ponteiros de início/fim, O(1) nas duas operações:
```js
class Queue {
  #store = {}; #head = 0; #tail = 0;
  enqueue(item) { this.#store[this.#tail++] = item; }
  dequeue() {
    if (this.#head === this.#tail) return undefined;
    const item = this.#store[this.#head];
    delete this.#store[this.#head++];
    return item;
  }
}
```

`[TENTE VOCÊ]` Uma fila de notificações que cresce até 10.000 itens — por que `Array.shift()`
seria uma escolha ruim aqui? Resposta: cada `shift()` precisa reindexar todos os elementos
restantes — com 10.000 itens, remover um de cada vez fica cada vez mais lento (O(n) por remoção),
enquanto a `Queue` com ponteiros mantém O(1) sempre, não importa o tamanho.

## `[TEORIA]` Map (estrutura) x `.map()` (método de array) — não confunda

`Array.prototype.map()` é um **método** que transforma um array (`[1,2,3].map(x => x*2)` →
`[2,4,6]`). `Map` (M maiúsculo) é uma **estrutura de dados** — um dicionário chave→valor, com
chaves de qualquer tipo e tamanho rastreado automaticamente (`.size`), diferente de um objeto
comum:
```js
const grafo = new Map();
grafo.set("A", ["B", "C"]);
grafo.get("A");   // ["B", "C"]
grafo.size;       // 1 — propriedade, não método
```

## `[TEORIA]` Estruturas de dados não-lineares: Trie, Graph, LRU Cache

**Trie** (árvore de prefixos) é especializada em strings — busca por prefixo em tempo O(m), onde
`m` é o tamanho da string buscada, não importa quantas palavras estejam guardadas. Aplicação:
autocompletar.
```js
class TrieNode { filhos = new Map(); fimDaChave = false; }
class Trie {
  #raiz = new TrieNode();
  inserir(palavra) {
    let no = this.#raiz;
    for (const ch of palavra) {
      if (!no.filhos.has(ch)) no.filhos.set(ch, new TrieNode());
      no = no.filhos.get(ch);
    }
    no.fimDaChave = true;
  }
}
```

**Graph (grafo)** modela relacionamentos entre entidades — um grafo **dirigido** é ideal pra
dependências ("tarefa A depende de B"). Duas buscas clássicas: **BFS** (busca em largura, nível
por nível, usando uma fila) e **DFS** (busca em profundidade, usada aqui pra detectar ciclos):
```js
class Graph {
  #adj = new Map();
  addEdge(u, v) { this.#adj.get(u)?.push(v); }
  bfs(inicio) {
    const visitados = new Set([inicio]), fila = [inicio], ordem = [];
    while (fila.length) {
      const v = fila.shift();
      ordem.push(v);
      for (const viz of this.#adj.get(v) ?? [])
        if (!visitados.has(viz)) { visitados.add(viz); fila.push(viz); }
    }
    return ordem;
  }
}
```
`[ATENÇÃO]` Um grafo de dependências com ciclo (A depende de B, que depende de A) trava qualquer
tentativa de resolver a ordem de execução — por isso detectar ciclo (via DFS com coloração
branco/cinza/preto) é um passo obrigatório antes de processar dependências reais.

**LRU Cache** (Least Recently Used) guarda os N itens mais recentemente acessados e descarta o
menos usado quando fica cheio — implementável com `Map`, já que ele preserva ordem de inserção,
em O(1):
```js
class LRUCache {
  #cache = new Map(); #cap;
  constructor(cap) { this.#cap = cap; }
  get(chave) {
    if (!this.#cache.has(chave)) return undefined;
    const valor = this.#cache.get(chave);
    this.#cache.delete(chave); this.#cache.set(chave, valor); // move pro "fim" (mais recente)
    return valor;
  }
  set(chave, valor) {
    if (this.#cache.size >= this.#cap && !this.#cache.has(chave))
      this.#cache.delete(this.#cache.keys().next().value); // remove o mais antigo
    this.#cache.set(chave, valor);
  }
}
```

## `[TEORIA]` Performance: `worker_threads` e `perf_hooks`

Retome o módulo 05 (CPU multicore): o Node, por padrão, roda seu código numa única thread — mas
`worker_threads` cria **threads reais**, cada uma com seu próprio Event Loop, que executam
JavaScript em paralelo de verdade, aproveitando múltiplos núcleos. Ideal pra tarefas
CPU-intensivas (que travariam a thread principal se rodassem nela).

```js
import { Worker } from "worker_threads";
function executarWorker(dados) {
  return new Promise((resolve, reject) => {
    const w = new Worker(new URL("./worker.js", import.meta.url), { workerData: dados });
    w.on("message", resolve);
    w.on("error", reject);
  });
}
```

`perf_hooks` mede tempo com muito mais precisão que um `console.log` com timestamp:
```js
import { performance } from "perf_hooks";
const inicio = performance.now();
processarDados();
console.log(`${(performance.now() - inicio).toFixed(4)}ms`);
```

## `[TEORIA]` Segurança: hash, HMAC e criptografia com `crypto`

Quatro conceitos que não podem ser confundidos:
- **Hash** (ex: SHA-256): função de mão única — o mesmo input sempre produz o mesmo output, mas é
  praticamente impossível reverter. Usado pra verificar integridade (o arquivo mudou?).
- **HMAC**: hash combinado com uma chave secreta — autentica que uma mensagem não foi alterada
  *e* veio de quem tem a chave.
- **Criptografia simétrica** (ex: AES-256-GCM): a mesma chave cifra e decifra — rápida, usada pra
  grandes volumes de dados.
- **Criptografia assimétrica** (RSA, Ed25519): uma chave pública cifra, só a privada decifra —
  base do HTTPS/TLS (retome o módulo 07).

```js
import crypto from "crypto";

// Hash — integridade
crypto.createHash("sha256").update(conteudo).digest("hex");

// Token seguro
crypto.randomBytes(32).toString("hex");

// HMAC — autenticar que uma mensagem não foi alterada
crypto.createHmac("sha256", segredo).update(JSON.stringify(payload)).digest("hex");
```

`[ATENÇÃO]` `Math.random()` **não** é seguro pra nada relacionado a segurança (senhas, tokens,
chaves) — é previsível, feito pra jogos e simulações. Para qualquer dado sensível, use sempre
`crypto.randomBytes()` ou `crypto.randomUUID()`.

## Erros comuns

Você já viu estes avisos ao longo do módulo — aqui vai a revisão:

- Confiar que `+` sempre soma, sem checar se os dois lados são realmente números.
- Esquecer o `await` antes de uma chamada assíncrona.
- Usar `fs.readFileSync`/`writeFileSync` num servidor, bloqueando todas as conexões.
- Achar que "Node é single-threaded" significa que nenhuma outra thread existe — a libuv usa um
  pool de threads por baixo, só a sua Call Stack é single-threaded.
- Esquecer `super()` no construtor de uma classe filha antes de usar `this`.
- Confundir `Map` (estrutura de dados) com `.map()` (método de array) — são coisas diferentes.
- Usar `exec`/`execSync` com entrada de usuário concatenada direto na string do comando —
  brecha de injeção de shell.
- Usar `Math.random()` pra gerar token, senha ou qualquer dado sensível — não é seguro.

## Conexão com os próximos módulos

| Conceito deste módulo | Reaparece em |
|---|---|
| Event Loop / processos assíncronos | Módulo 06 (SO) — mesma lógica de E/S não-bloqueante, agora em código |
| Servidor HTTP / fetch | Módulo 07 (Redes) — os mesmos conceitos de HTTP, agora implementados |
| `child_process` / `os` | Módulo 06 (SO) — processos e informações de hardware, agora acessados por código |
| Streams | Módulo 05 (Arquitetura) — mesmo princípio de processar em pedaços por causa da memória limitada |
| `worker_threads` | Módulo 05 (Arquitetura) — CPU multicore, agora aproveitada em JavaScript |
| Todo o módulo | Prática: projeto DevTrack, que usa cada um destes tópicos numa ferramenta real |

## `[REFERÊNCIA]`

- `workshop_nodejs_v3 (1).md` (já presente em `trila-jovens-aprendiz/`) — workshop completo de
  referência por tópico, fonte deste módulo (12 módulos, todos cobertos acima).
- `apostila_devtrack_v2 (1).md` (já presente em `trila-jovens-aprendiz/`) — as 24 tarefas do
  projeto DevTrack, base da prática deste módulo.
- Documentação oficial: [Node.js — process](https://nodejs.org/api/process.html),
  [Node.js — fs/promises](https://nodejs.org/api/fs.html#promises-api),
  [Node.js — readline](https://nodejs.org/api/readline.html),
  [Node.js — Event Loop, Timers e process.nextTick()](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/),
  [Node.js — child_process](https://nodejs.org/api/child_process.html),
  [Node.js — Streams](https://nodejs.org/api/stream.html),
  [Node.js — worker_threads](https://nodejs.org/api/worker_threads.html),
  [Node.js — crypto](https://nodejs.org/api/crypto.html),
  [npm — package.json](https://docs.npmjs.com/cli/v10/configuring-npm/package-json).
- Bibliotecas do ecossistema: [Commander.js](https://github.com/tj/commander.js),
  [Chalk](https://github.com/chalk/chalk), [Inquirer.js](https://github.com/SBoudrias/Inquirer.js).
- [Node.js — Documentação completa](https://nodejs.org/docs/latest/api/)
- [MDN — JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
- [OWASP Node.js Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html)
- Loiane Groner — *Estruturas de Dados e Algoritmos com JavaScript* (livro citado como referência
  de apoio para Stack, Queue, Trie, Graph e LRU Cache).

## Checklist de saída

- [ ] Explico por que JavaScript é interpretada, ligando com compilador/interpretador do módulo 08.
- [ ] Explico a diferença entre tipagem estática (C++, módulo 08) e dinâmica (JavaScript).
- [ ] Descrevo o papel do V8 e da libuv no runtime Node, e por que "single-threaded" é uma
      simplificação.
- [ ] Explico a ordem de execução entre código síncrono, microtasks e macrotasks no Event Loop.
- [ ] Escrevo uma função `async` com `try/catch` para tratar erro de leitura de arquivo.
- [ ] Explico por que `fs/promises` é preferível a `fs` síncrono num servidor.
- [ ] Sei o que `process.stdout.isTTY` detecta e por que isso importa num CLI.
- [ ] Sei a diferença entre CommonJS e ES Modules, e por que `__dirname` precisa ser recriado em ESM.
- [ ] Escolho o combinador de Promise certo (`all`, `allSettled`, `race`, `any`) para um cenário dado.
- [ ] Explico quando usar `exec`, `spawn` ou `fork` em `child_process`.
- [ ] Explico por que processar um arquivo grande como stream usa muito menos memória.
- [ ] Escrevo uma classe com campo privado, getter e herança (`extends`/`super`).
- [ ] Implemento Stack e Queue do zero, sabendo por que `Array.shift()` é ruim pra fila grande.
- [ ] Diferencio `Map` de `.map()`.
- [ ] Explico o que `worker_threads` resolve que a thread principal do Node não resolve sozinha.
- [ ] Sei a diferença entre hash, HMAC e criptografia simétrica, e por que nunca usar
      `Math.random()` para segurança.
