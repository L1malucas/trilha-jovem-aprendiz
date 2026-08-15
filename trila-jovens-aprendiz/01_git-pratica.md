# Módulo 01 — Git — Prática

> **Objetivo da prática:** dominar Git 100% em laboratório — simulando, com um projeto contínuo,
> as situações reais que acontecem no dia a dia de um repositório (não só decorar comandos).
> **Pré-requisito:** [01_git-teoria.md](01_git-teoria.md)
> **Entregáveis:** o link do seu repositório no GitHub (com todo o histórico dos laboratórios
> visível), mais um arquivo `respostas.md` documentando cada laboratório.
> **Formato de entrega:** publicado no GitHub, com README explicando a organização do repositório.

---

## Exemplo resolvido

Iniciando um repositório, registrando um commit, criando uma branch e mesclando de volta:
```
git init
echo "primeira versão" > app.txt
git add app.txt
git commit -m "adiciona app.txt"

git branch melhoria
git switch melhoria
echo "segunda linha" >> app.txt
git add app.txt
git commit -m "adiciona segunda linha"

git switch main
git merge melhoria
```
Depois do merge, `app.txt` na `main` tem as duas linhas — a mudança feita isoladamente na branch
`melhoria` foi trazida de volta. Rodar `git log --graph --oneline` mostra visualmente os dois
caminhos se juntando.

Agora é a sua vez — mas em vez de exercícios soltos, os laboratórios abaixo formam **um projeto
único e contínuo**: cada laboratório parte exatamente do estado em que o anterior parou, do jeito
que acontece de verdade num projeto real. Resolva na ordem.

---

## Lab 0 — Antes de tudo: navegando pelo terminal no Windows

Antes de qualquer comando Git, você precisa saber se mover pelo sistema de arquivos só com o
teclado — é a base de tudo que vem depois. Abra o **Prompt de Comando** ou o **PowerShell** (os
comandos abaixo funcionam nos dois, salvo indicação contrária) e pratique, na ordem:

1. Veja em qual pasta você está: `cd` (sozinho, sem argumento, no PowerShell) ou `cd` mostra o
   caminho atual em ambos.
2. Liste o conteúdo da pasta atual: `dir` (cmd/PowerShell) — se você estiver usando o Git Bash
   (instalado junto com o Git), o equivalente é `ls`.
3. Crie uma pasta pro projeto desta prática: `mkdir lanchonete-beira-rio`.
4. Entre nela: `cd lanchonete-beira-rio`.
5. Crie um arquivo de texto vazio:
   - Prompt de Comando: `type nul > cardapio.txt`
   - PowerShell: `New-Item cardapio.txt`
6. Abra o arquivo no Bloco de Notas (já usado no módulo 08) pra editar: `notepad cardapio.txt` —
   escreva uma linha qualquer, salve, feche.
7. Confirme que o arquivo tem conteúdo: `dir` (repare no tamanho em bytes, antes era 0).
8. Crie uma pasta de teste e um arquivo dentro dela, depois apague os dois pra praticar remoção:
   ```
   mkdir pasta-teste
   cd pasta-teste
   type nul > temp.txt     (cmd)   ou   New-Item temp.txt   (PowerShell)
   cd ..
   del pasta-teste\temp.txt        (cmd)   ou   Remove-Item pasta-teste\temp.txt   (PowerShell)
   rmdir pasta-teste                (cmd)   ou   Remove-Item pasta-teste            (PowerShell)
   ```

`[ATENÇÃO]` `del`/`rmdir` (Prompt de Comando) e `Remove-Item` (PowerShell) não têm lixeira — o
arquivo/pasta some direto. No PowerShell, apagar uma pasta com conteúdo dentro exige
`Remove-Item -Recurse` (sem isso, ele recusa apagar uma pasta não vazia); no cmd, o equivalente é
`rmdir /s`.

**Critério de aceite:** a pasta `lanchonete-beira-rio` existe, contém `cardapio.txt` com pelo
menos uma linha de texto, e a `pasta-teste` de teste foi criada e apagada com sucesso (confirme
com `dir` que ela não aparece mais).

---

## O projeto contínuo: Cardápio da Lanchonete Beira-Rio

Os laboratórios de 1 a 18 usam a pasta `lanchonete-beira-rio` do Lab 0 como um projeto real: você
vai versionar o cardápio (em arquivos `.txt` simples, editados no Bloco de Notas) de uma
lanchonete fictícia, passando pelas mesmas situações — boas e ruins — que acontecem em qualquer
repositório de verdade. Nível Básico cobre Fundamentos/Commit/Branch/Remote/Fetch-Pull-Push/
Merge/Conflitos; Intermediário cobre Rebase/Reset-Restore-Revert/Stash/Histórico-Reflog/Tags/
Conventional Commits/PR-Code Review; Avançado cobre Git Flow-Trunk Based/Cherry-pick/Bisect/
Worktree/Hooks/Git+CI-CD.

---

## Nível Básico

### Lab 1 — Fundamentos e primeiros commits

Dentro de `lanchonete-beira-rio`:
```
git init
git status
```
`git status` deve mostrar `cardapio.txt` como não rastreado. Adicione e faça o primeiro commit:
```
git add cardapio.txt
git commit -m "feat: adicionar cardapio inicial"
```
Agora edite `cardapio.txt` (Bloco de Notas) adicionando uma seção "Lanches" com 3 itens e preços,
e faça um **commit propositalmente ruim** — sem `git add` de nada de específico e com mensagem
vaga, só pra você ver o problema na prática:
```
git add .
git commit -m "arruma coisas"
```
Esse commit ruim volta no Lab 7 pra ser corrigido — não conserte ainda.

**Critério de aceite:** `git log --oneline` mostra 2 commits; o segundo tem uma mensagem que não
segue o padrão de prefixo do módulo 02 (de propósito).

### Lab 2 — Branch

A lanchonete quer adicionar uma seção de bebidas, mas sem mexer na `main` até estar pronta:
```
git branch feature/cardapio-bebidas
git switch feature/cardapio-bebidas
```
Edite `cardapio.txt` no Bloco de Notas, adicionando uma seção "Bebidas" com 3 itens. Commit
seguindo o padrão do módulo 02:
```
git add cardapio.txt
git commit -m "feat: adicionar secao de bebidas ao cardapio"
```

**Critério de aceite:** `git branch` mostra duas branches, com `*` marcando
`feature/cardapio-bebidas` como a atual; `main` ainda não tem a seção de bebidas (confira
trocando pra `main` com `git switch main` e abrindo o arquivo).

### Lab 3 — Remote, fetch/pull/push

Crie um repositório vazio no GitHub chamado `lanchonete-beira-rio` (pela interface web, sem
inicializar com README). Conecte seu repositório local a ele:
```
git remote add origin https://github.com/SEU-USUARIO/lanchonete-beira-rio.git
git remote -v
git switch main
git push -u origin main
```
O `-u` cria o vínculo de tracking entre a `main` local e a `origin/main` remota — depois disso,
`git push`/`git pull` sozinhos (sem especificar remoto/branch) já sabem pra onde ir. Envie a
branch de feature também:
```
git switch feature/cardapio-bebidas
git push -u origin feature/cardapio-bebidas
```

**Critério de aceite:** as duas branches aparecem no GitHub; `git remote -v` mostra `origin`
listada duas vezes (fetch e push).

### Lab 4 — Merge

A seção de bebidas está pronta — hora de trazer pra `main`:
```
git switch main
git merge feature/cardapio-bebidas
git push
```

**Critério de aceite:** `cardapio.txt` na `main` agora tem lanches e bebidas; `git log --graph
--oneline` mostra os dois caminhos se juntando.

### Lab 5 — Gerando e resolvendo um conflito de verdade

Situação real: duas pessoas (aqui, você mesmo, trocando de branch) editam a **mesma linha** do
cardápio ao mesmo tempo.

```
git switch main
git branch ajuste-preco-main
git switch ajuste-preco-main
```
No Bloco de Notas, mude o preço do primeiro item de "Lanches" (ex: de `R$ 15,00` pra `R$ 17,00`).
```
git add cardapio.txt
git commit -m "fix: corrigir preco do lanche principal"
git switch main
git branch ajuste-preco-feature main
git switch ajuste-preco-feature
```
Agora mude o **mesmo item**, mas pra um preço diferente (ex: `R$ 16,50`) — simulando a segunda
pessoa editando por cima.
```
git add cardapio.txt
git commit -m "fix: atualizar preco do lanche principal"
git switch main
git merge ajuste-preco-main
git merge ajuste-preco-feature
```
O segundo merge vai gerar conflito. Abra `cardapio.txt` no Bloco de Notas — você vai ver os
marcadores `<<<<<<<`, `=======`, `>>>>>>>` em volta da linha do preço. Escolha o preço correto
(ou combine os dois, sua decisão), apague os três marcadores manualmente, salve.
```
git add cardapio.txt
git commit -m "merge: resolver conflito de preco do lanche principal"
git push
```

**Critério de aceite:** `git log --graph --oneline` mostra claramente um commit de merge com dois
pais; `cardapio.txt` não tem mais nenhum marcador `<<<<<<<`/`=======`/`>>>>>>>` sobrando.

---

## Nível Intermediário

### Lab 6 — Rebase

Crie uma branch pra adicionar uma seção "Sobremesas", mas desta vez, em vez de merge, use rebase
pra manter o histórico linear (apropriado aqui porque é uma branch só sua, ainda não
compartilhada com mais ninguém):
```
git switch main
git branch feature/sobremesas
git switch feature/sobremesas
```
Edite o cardápio adicionando "Sobremesas" (2 itens), commit. Enquanto isso, imagine que a `main`
recebeu outro commit direto (simule voltando pra `main`, editando algo pequeno tipo o nome da
lanchonete no topo do arquivo, e commitando lá). Depois:
```
git switch feature/sobremesas
git rebase main
```

`[ATENÇÃO]` Rebase reescreve o histórico da branch — nunca faça isso numa branch que outra pessoa
já baixou e está usando; aqui é seguro porque `feature/sobremesas` ainda não foi enviada.

**Critério de aceite:** depois do rebase, `git log --oneline feature/sobremesas` mostra o commit
da sobremesa **depois** do commit que você fez na `main`, num histórico linear (sem bifurcação).

### Lab 7 — Reset, Restore e Revert

Hora de lidar com o commit ruim do Lab 1 ("arruma coisas") — mas de duas formas diferentes,
dependendo de onde ele está:

**Se esse commit ainda não foi enviado ao GitHub** (só existe local): pode reescrever a história
com `reset`. Rode `git log --oneline` pra achar o hash do commit *antes* dele, e:
```
git reset --soft <hash-do-commit-anterior>
```
Isso desfaz o commit ruim mas mantém as mudanças dele "na área de stage", prontas pra você
recommitar com uma mensagem decente:
```
git commit -m "feat: adicionar secao de lanches ao cardapio"
```

**Se esse commit já foi enviado/compartilhado** (ex: alguém já deu `pull`): reescrever a história
com `reset` é perigoso — use `revert`, que cria um novo commit desfazendo o anterior sem apagar
nada do histórico:
```
git revert <hash-do-commit-ruim>
```

Pratique também `restore`, pra descartar uma mudança que você nem chegou a commitar: edite
`cardapio.txt` com qualquer besteira, sem dar `add`, e rode `git restore cardapio.txt` — a mudança
desaparece, voltando ao último commit.

**Critério de aceite:** você sabe explicar, com suas palavras, por que `reset` foi usado num caso
e `revert` no outro — documente essa decisão no `respostas.md`.

### Lab 8 — Stash

Você está no meio de editar `cardapio.txt` (uma nova seção "Promoções", ainda incompleta, sem
commitar) quando surge um pedido urgente pra trocar de branch e corrigir outra coisa. Você não
quer perder o que já escreveu, mas também não quer commitar algo pela metade:
```
git stash
git switch main
```
(faça uma mudança rápida qualquer na `main`, commit, `git switch` de volta pra onde estava)
```
git switch feature/sobremesas
git stash pop
```

**Critério de aceite:** `git stash list` estava com 1 item antes do `pop`, e vazio depois; a seção
"Promoções" incompleta voltou exatamente como você deixou.

### Lab 9 — Histórico e Reflog

Explore o histórico completo do projeto:
```
git log --oneline
git log --oneline --graph --all
git log --stat -3
```
Agora simule um susto real: rode `git reset --hard HEAD~1` (isso descarta o último commit **e**
as mudanças dele — cuidado, é destrutivo de propósito aqui só pra praticar recuperação). Percebeu
que foi um erro? O commit não sumiu de verdade — ele só ficou "sem referência":
```
git reflog
```
Ache o hash do commit que você "perdeu" na lista do reflog, e recupere:
```
git reset --hard <hash-do-commit-perdido>
```

**Critério de aceite:** depois de recuperar, `git log --oneline` mostra o commit de volta,
exatamente como estava antes do `reset --hard` acidental.

### Lab 10 — Tags

O cardápio está pronto pro lançamento oficial:
```
git switch main
git tag -a v1.0.0 -m "Lancamento oficial do cardapio"
git push origin v1.0.0
```

**Critério de aceite:** a tag `v1.0.0` aparece na página de "Releases/Tags" do repositório no
GitHub.

### Lab 11 — Conventional Commits (revisão)

Volte no `git log --oneline` de todo o projeto até aqui e confira: quantos dos seus commits
seguem o padrão `PREFIXO: descrição` do módulo 02? Escreva no `respostas.md` uma lista de pelo
menos 3 commits que você faria diferente (com o prefixo certo) se pudesse voltar no tempo — sem
precisar reescrever o histórico de verdade, é só o exercício de identificar.

### Lab 12 — Pull Request e Code Review

Crie uma última branch de feature (ex: `feature/secao-contato`, adicionando um bloco "Contato" ao
cardápio com endereço/telefone fictícios), commit e envie:
```
git switch main
git branch feature/secao-contato
git switch feature/secao-contato
```
(edite, commit seguindo Conventional Commits, depois:)
```
git push -u origin feature/secao-contato
```
Na interface do GitHub, abra um **Pull Request** de verdade dessa branch pra `main`, escrevendo a
descrição no formato do módulo 02 (o que foi feito / por que / como). Depois de revisar você
mesmo o diff mostrado pelo GitHub (releia como se fosse um colega revisando), faça o merge do PR
pela própria interface do GitHub (não pelo terminal desta vez).

**Critério de aceite:** o PR existe no histórico do repositório (mesmo já mesclado, ele continua
listado em "Pull Requests" → "Closed"), com título e descrição completos.

---

## Nível Avançado

### Lab 13 — Git Flow x Trunk Based

Depois de sincronizar (`git pull`) a `main` local com o merge feito pela interface no Lab 12,
crie uma branch `develop` a partir dela — o ponto de partida de um fluxo estilo **Git Flow**:
```
git switch main
git branch develop
git switch develop
```
No `respostas.md`, compare em suas palavras: no **Git Flow** (com `develop`, branches de
`release/*` e `hotfix/*` separadas da `main`), o que teria que acontecer pra uma correção urgente
chegar em produção rápido? E no **Trunk Based Development** (todo mundo commitando direto numa
branch principal única, com branches de vida curtíssima)? Qual seria mais adequado pra um projeto
pequeno como o da lanchonete, e por quê?

### Lab 14 — Cherry-pick

Situação: você percebe um erro crítico de preço na branch `develop` (edite `cardapio.txt` lá,
corrigindo um valor, e commit) — mas esse mesmo erro também existe na `main`, que já está em
"produção" (publicada), e não dá tempo de esperar um merge completo de `develop` pra lá:
```
git switch develop
```
(edite o preço errado, commit: `git commit -m "fix: corrigir preco incorreto de item critico"`)
```
git switch main
git cherry-pick <hash-do-commit-do-fix>
```

**Critério de aceite:** o mesmo commit de correção aparece tanto em `develop` quanto em `main`,
com o mesmo conteúdo (você pode conferir com `git log --oneline` nas duas branches).

### Lab 15 — Bisect

Um "bug" foi introduzido em algum lugar dos últimos commits — pra simular, volte e adicione,
espalhados em 2-3 commits diferentes ao longo do histórico (pode ser em qualquer branch, faça uns
commits novos na `main` pra ter material), uma linha de texto quebrada (ex: um caractere estranho
no meio do cardápio) em um deles especificamente, sem lembrar exatamente qual. Depois, ache:
```
git bisect start
git bisect bad                    (o estado atual, com o bug)
git bisect good <hash-bem-antigo> (um commit de que você tem certeza que não tinha o bug)
```
O Git vai te colocar automaticamente no meio do intervalo — abra `cardapio.txt` a cada passo e
responda:
```
git bisect good     (se esse commit NÃO tem o bug)
git bisect bad       (se esse commit TEM o bug)
```
até o Git apontar exatamente o commit culpado. Encerre com:
```
git bisect reset
```

**Critério de aceite:** você identificou corretamente o commit que introduziu o bug, documentando
o hash no `respostas.md`.

### Lab 16 — Worktree

Você precisa trabalhar em duas branches ao mesmo tempo sem ficar trocando (`switch`) o tempo todo
e sem clonar o repositório de novo numa pasta separada manualmente:
```
git worktree add ../lanchonete-hotfix main
```
Isso cria uma **pasta nova** (`../lanchonete-hotfix`, do lado de `lanchonete-beira-rio`) com a
branch `main` já "fora", trabalhável de forma independente — mudanças feitas lá não interferem no
que está aberto na pasta original. Faça uma pequena edição nessa pasta nova, commit, depois volte
pra pasta original e confirme que o commit aparece no histórico compartilhado (é o mesmo
repositório `.git`, só duas "visões" dele abertas ao mesmo tempo). Remova a worktree quando
terminar:
```
git worktree remove ../lanchonete-hotfix
```

**Critério de aceite:** o commit feito na worktree aparece em `git log --oneline` quando rodado
de volta na pasta original `lanchonete-beira-rio`.

### Lab 17 — Hooks

Configure um hook local que bloqueia commits com um `TODO` esquecido no arquivo. Dentro de
`.git/hooks/`, crie (ou edite, se já existir um exemplo) o arquivo `pre-commit` (sem extensão) com
este conteúdo (pode criar/editar pelo Bloco de Notas, salvando sem extensão `.txt`):
```
#!/bin/sh
if git diff --cached | grep -q "TODO"; then
  echo "Commit bloqueado: existe um TODO no que você está tentando commitar."
  exit 1
fi
```
Adicione a palavra `TODO` em algum ponto do `cardapio.txt`, dê `git add` e tente commitar —
o hook deve bloquear. Remova o `TODO` e tente de novo — deve passar normalmente.

`[ATENÇÃO]` Hooks ficam dentro de `.git/hooks/`, que **não é versionado** por padrão (a pasta
`.git` inteira nunca vai pro GitHub) — cada pessoa que clona o repositório precisaria configurar o
hook de novo manualmente, ou o time usa uma ferramenta como Husky pra automatizar isso (fora do
escopo deste laboratório, mas vale saber que existe).

**Critério de aceite:** você documentou, no `respostas.md`, a tentativa de commit bloqueada (cole
a mensagem de erro) e a tentativa seguinte, já sem o `TODO`, passando normalmente.

### Lab 18 — Git + CI/CD

Você já viu, na prática, um pipeline de CI/CD real disparado por push: o próprio site desta
trilha (`trilha-jovem-aprendiz`) publica automaticamente no GitHub Pages a cada `git push` na
branch `main`, através do workflow `.github/workflows/deploy.yml`. Abra esse arquivo (ou peça o
link do repositório da trilha pro instrutor) e identifique: qual evento dispara o workflow
(`on: push: branches: [main]`), e quais passos ele executa antes de publicar.

No `respostas.md`, explique em suas palavras como a tag `v1.0.0` que você criou no Lab 10 poderia,
num projeto real, disparar um pipeline **diferente** do pipeline de push normal — por exemplo, um
que só publica uma nova versão "oficial" quando uma tag no formato `v*.*.*` é criada, em vez de
publicar a cada commit.

**Critério de aceite:** explicação escrita, referenciando a diferença entre o gatilho `on: push`
(a cada commit) e um gatilho baseado em tags (só em lançamentos oficiais).

---

## Exercícios complementares

### Learn Git Branching

Acesse [learngitbranching.js.org](https://learngitbranching.js.org/?locale=pt_BR) e complete:
- A sequência **"Introduction Sequence"** (níveis 1 a 4).
- Pelo menos os 3 primeiros níveis de **"Ramping Up"**.

Para cada nível completado, anote qual comando (ou sequência de comandos) resolveu o desafio.

### Material em vídeo

Assista pelo menos 3 vídeos de uma das playlists indicadas na teoria
([playlist 1](https://www.youtube.com/playlist?list=PLHz_AreHm4dm7ZULPAmadvNhH6vk9oNZA) ou
[playlist 2](https://www.youtube.com/playlist?list=PLucm8g_ezqNq0dOgug6paAkH0AQSJPlIe)) e escreva
um parágrafo curto sobre um conceito que ficou mais claro depois de assistir.

## Critérios de entrega

- Repositório `lanchonete-beira-rio` publicado no GitHub, com todo o histórico dos 18
  laboratórios visível (`git log --graph --all --oneline` contando a história completa).
- `respostas.md` documentando cada laboratório: o que foi feito, a saída de terminal relevante
  (colada como texto ou print), e as respostas às perguntas abertas (Labs 7, 13, 15, 17, 18).
- Um `README.md` explicando a organização do repositório.
- Níveis do Learn Git Branching completados e documentados.
- Parágrafo sobre o vídeo assistido.

## Checklist de entrega

- [ ] Lab 0 — terminal Windows: pasta e arquivo criados, pasta de teste criada e apagada.
- [ ] Lab 1 — dois primeiros commits, incluindo o commit "ruim" de propósito.
- [ ] Lab 2 — branch `feature/cardapio-bebidas` criada e com commit próprio.
- [ ] Lab 3 — remoto configurado, `main` e branch de feature enviadas ao GitHub.
- [ ] Lab 4 — merge da branch de bebidas na `main`.
- [ ] Lab 5 — conflito de merge gerado e resolvido manualmente, sem marcadores sobrando.
- [ ] Lab 6 — rebase de uma branch local, histórico linear confirmado.
- [ ] Lab 7 — commit ruim corrigido com `reset`/`revert`, decisão documentada.
- [ ] Lab 8 — stash salvo e recuperado com sucesso.
- [ ] Lab 9 — `reset --hard` acidental recuperado via `reflog`.
- [ ] Lab 10 — tag `v1.0.0` criada e enviada.
- [ ] Lab 11 — revisão de Conventional Commits documentada.
- [ ] Lab 12 — Pull Request real aberto, descrito e mesclado pela interface do GitHub.
- [ ] Lab 13 — comparação Git Flow x Trunk Based documentada.
- [ ] Lab 14 — cherry-pick de um fix crítico entre branches.
- [ ] Lab 15 — bug encontrado via `git bisect`.
- [ ] Lab 16 — worktree criada, usada e removida.
- [ ] Lab 17 — hook `pre-commit` bloqueando e liberando commits.
- [ ] Lab 18 — pipeline de CI/CD real analisado e gatilho por tag explicado.
- [ ] Learn Git Branching — níveis completados e documentados.
- [ ] Vídeo assistido e resumido.
- [ ] Publicado no GitHub com README.
