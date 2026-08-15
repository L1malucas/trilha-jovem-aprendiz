---
id: 00_indice
title: "Trilha Jovem Aprendiz — Índice"
sidebar_position: 0
slug: /
sidebar_label: "Índice"
---

# Trilha Jovem Aprendiz — Índice

Trilha de conteúdo para formação de jovens aprendizes, cobrindo do zero (fundamentos de Ciência
da Computação) até as tecnologias usadas no dia a dia dos projetos (Git, MongoDB, SQL Server,
JavaScript/Node, HTML/CSS).

Cada módulo tem no mínimo dois arquivos: `teoria.md` (conceitos, explicações, referências) e
`pratica.md` (exercícios com critério de aceite e regras de entrega). O conteúdo é escrito em
Markdown e publicado como site em <https://l1malucas.github.io/trilha-jovem-aprendiz/>.

---

## Antes de começar

Esta seção é **obrigatória** — faça tudo aqui antes de abrir o Módulo 01. Ela existe porque
quase todo módulo da trilha pede pra você publicar algo no GitHub, e porque instalar tudo de uma
vez agora evita interromper um laboratório no meio pra correr atrás de um instalador.

### 1. Criar sua conta no GitHub

Se você ainda não tem: acesse [github.com/join](https://github.com/join) e crie uma conta.
Escolha um nome de usuário profissional — ele vai aparecer em tudo que você publicar durante a
trilha (e depois dela, no mercado de trabalho). Evite apelidos aleatórios; prefira algo baseado no
seu nome.

### 2. Preencher o perfil

Um perfil vazio (sem foto, sem nome, sem nada) passa a impressão de conta abandonada — e é a
primeira coisa que um recrutador ou outro desenvolvedor vê quando clica no seu usuário. Antes de
começar a trilha, vá em **Settings → Public profile** (ou no seu próprio perfil, botão **Edit
profile**) e preencha:

- **Foto de perfil** — uma foto sua, ou pelo menos um avatar consistente (nada do avatar
  padrão cinza).
- **Nome** — seu nome de verdade, não só o usuário.
- **Bio** — uma linha curta dizendo quem você é e o que está aprendendo (ex: "Estudando
  desenvolvimento — Trilha Jovem Aprendiz").
- **Localização** (opcional, mas ajuda).

`[TENTE VOCÊ]` Depois de preencher, acesse `github.com/<seu-usuario>` de uma aba anônima do
navegador — é assim que qualquer pessoa de fora vai ver seu perfil. Confira se ele já passa uma
boa primeira impressão.

### 3. Criar seu repositório de apresentação pessoal

O GitHub tem um recurso pouco conhecido por quem está começando: se você criar um repositório com
**exatamente o mesmo nome do seu usuário**, o `README.md` desse repositório vira automaticamente
uma seção de apresentação especial, exibida no topo do seu perfil — antes mesmo dos seus outros
repositórios.

**Passo a passo, direto pela interface do GitHub (sem usar o terminal ainda):**

1. No canto superior direito do GitHub, clique no `+` → **New repository**.
2. No campo "Repository name", digite **exatamente** o seu nome de usuário (ex: se seu usuário é
   `mariasilva`, o repositório precisa se chamar `mariasilva`, nem mais nem menos).
3. O GitHub vai mostrar automaticamente uma mensagem especial: *"mariasilva/mariasilva is a
   ✨special✨ repository..."* — se essa mensagem aparecer, você acertou o nome.
4. Marque a opção **Public**.
5. Marque **Add a README file**.
6. Clique em **Create repository**.
7. Edite o `README.md` direto pela interface (ícone de lápis) e escreva uma apresentação curta:
   quem você é, o que está estudando (cite a trilha), e algum link de contato (LinkedIn, e-mail
   profissional). Não precisa ser longo — 4 ou 5 linhas já cumprem o papel.

`[ATENÇÃO]` O nome do repositório precisa bater **exatamente** com o nome do seu usuário
(maiúsculas/minúsculas não importam, mas o texto sim) — um caractere diferente e o GitHub trata
como um repositório normal, sem o efeito especial no perfil.

Você vai voltar a editar esse `README.md` ao longo da trilha — é normal (e recomendado) atualizar
sua apresentação conforme for aprendendo coisas novas e publicando projetos.

### 4. Instalar os softwares usados na trilha inteira

Instale tudo abaixo agora, antes do Módulo 01 — cada item é usado em pelo menos um módulo, e
alguns (Git, VSCode, um navegador) são usados o tempo todo.

| Software | Para quê | Onde baixar (Windows) |
|---|---|---|
| **Git for Windows** | Controle de versão (Módulos 01, 02, e entrega de todos os outros) | [git-scm.com/download/win](https://git-scm.com/download/win) |
| **Visual Studio Code** | Editor de código usado a partir do Módulo 08 | [code.visualstudio.com](https://code.visualstudio.com/) |
| **MSYS2 (com MinGW-w64)** | Compilador de C++, usado nos Módulos 08 e 09 | [msys2.org](https://www.msys2.org/) — instruções completas de instalação e configuração de PATH estão no Módulo 08 |
| **Python 3** | Usado em conferências rápidas de conversão (Módulo 03) e como linguagem alternativa de apoio | [python.org/downloads](https://www.python.org/downloads/) |
| **Node.js (versão LTS)** | Módulo 13 (JavaScript/Node.js) | [nodejs.org](https://nodejs.org/) |
| **Docker Desktop** | Rodar MongoDB e SQL Server em containers (Módulos 11 e 12) sem precisar instalar cada banco manualmente | [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/) |
| **MongoDB Shell (mongosh)** ou **MongoDB Compass** | Conectar e explorar o banco no Módulo 11 | [mongodb.com/try/download/shell](https://www.mongodb.com/try/download/shell) |
| **Azure Data Studio** ou **SQL Server Management Studio (SSMS)** | Conectar e explorar o banco no Módulo 12 | [azure.microsoft.com/products/data-studio](https://azure.microsoft.com/products/data-studio) |
| **WSL2 (Windows Subsystem for Linux)** | Boa parte dos comandos e laboratórios do Módulo 06 (Sistemas Operacionais) são Linux — o Módulo 06 explica como instalar | `wsl --install` no PowerShell como administrador |
| **Um navegador atualizado** (Chrome, Firefox ou Edge) | Módulos 07 e 10, e o DevTools usado ao longo da trilha | Provavelmente você já tem um — só mantenha atualizado |

`[TENTE VOCÊ]` Depois de instalar o Git, abra o Prompt de Comando ou PowerShell e rode
`git --version`. Se aparecer um número de versão, a instalação funcionou — guarde esse hábito de
conferir a instalação de cada ferramenta nova assim que instalar.

### 5. Como aproveitar melhor a trilha

- **Siga a ordem dos módulos.** Cada módulo assume que você já sabe o conteúdo dos anteriores —
  os módulos citam explicitamente "como você viu no Módulo X" o tempo todo. Pular módulos cria
  buracos que só aparecem mais tarde, quando parecem bem mais confusos do que precisavam ser.
- **Não pule a prática.** Ler a teoria e achar que entendeu é diferente de ter realmente
  praticado — os laboratórios existem justamente pra expor a diferença entre "eu entendi lendo" e
  "eu consigo fazer sozinho".
- **Publique tudo no GitHub, mesmo o que não ficou perfeito.** O objetivo não é nunca errar — é
  construir um histórico real de prática. Um repositório com commits mostrando sua evolução vale
  mais do que um projeto "perfeito" feito escondido e só publicado no final.
- **Use os `[TENTE VOCÊ]` de verdade.** Pare e resolva antes de olhar a resposta — eles existem
  pra você testar se entendeu, não pra confirmar o que já sabia.
- **Volte nos módulos anteriores quando precisar.** A trilha foi pensada com referências cruzadas
  entre módulos de propósito — se um conceito novo remete a um módulo anterior e você não lembra
  bem, vale a pena voltar e reler antes de seguir.
- **Pratique além do mínimo.** Cada módulo tem uma seção "Práticas complementares" ou exercícios
  extras quando o assunto permite — fazer só o mínimo pra "passar" no checklist rende bem menos
  do que insistir um pouco mais em cada tópico.

---

## Legenda de tags usadas nos módulos

| Tag | Significado |
|---|---|
| `[TEORIA]` | Conceito necessário, sem prática associada direta |
| `[ATENÇÃO]` | Erro comum ou pegadinha |
| `[APROFUNDAMENTO]` | Vai além do mínimo necessário, para quem quer se aprofundar |
| `[REFERÊNCIA]` | Fontes oficiais/acadêmicas curadas |
| `[CLI]` | Equivalente em linha de comando |
| `[TENTE VOCÊ]` | Prática rápida logo após um exemplo resolvido, com resposta visível ao lado — reforço imediato, não teste de memória |

## Módulos

| Nº | Módulo | Resumo |
|---|---|---|
| 01 | [Git](01_git-teoria.md) | Controle de versão: branches, merges, conflitos, fluxo de trabalho |
| 02 | [Padrões de Projeto](02_padroes-projeto-teoria.md) | Padrões de commit, branch, versionamento semântico e pull requests |
| 03 | [Sistemas de Numeração](03_sistemas-numeracao-teoria.md) | Binário, hexadecimal, decimal: conversões, ponto flutuante |
| 04 | [Circuitos Digitais](04_circuitos-digitais-teoria.md) | Lógica binária, portas lógicas, circuitos combinacionais e sequenciais |
| 05 | [Arquitetura de Computadores](05_arquitetura-computadores-teoria.md) | CPU, memória, E/S, barramentos, ciclo de busca e execução |
| 06 | [Sistemas Operacionais](06_sistemas-operacionais-teoria.md) | Gerência de processos, memória e E/S; Linux e Windows |
| 07 | [Redes de Computadores e Web](07_redes-computadores-web-teoria.md) | Arquitetura em camadas, TCP/IP, HTTP, URL, HTML |
| 08 | [Linguagens de Programação](08_linguagens-programacao-teoria.md) | Interpretadores, compiladores, estruturação de código |
| 09 | [Algoritmos e Lógica de Programação](09_algoritmos-logica-teoria.md) | Resolução de problemas com algoritmos, em C/C++/Python/Java/Pascal |
| 10 | [HTML & CSS](10_html-css-teoria.md) | Fundamentos de HTML5 e CSS3, desafio de 30 dias |
| 11 | [MongoDB](11_mongodb-teoria.md) | Bancos de dados não relacionais |
| 12 | [SQL Server](12_sqlserver-teoria.md) | Bancos de dados relacionais com SQL Server |
| 13 | [JavaScript / Node.js](13_javascript-nodejs-teoria.md) | Fundamentos de JavaScript e Node.js |

Os módulos 03 a 09 seguem a ementa de "Introdução à Computação" (sistemas de numeração →
circuitos digitais → arquitetura → sistemas operacionais → redes → linguagens → algoritmos),
com proporção de aproximadamente 70% teoria / 30% prática, antes de entrar nos exercícios de
lógica de programação propriamente ditos (módulo 09).
