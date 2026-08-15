# Trilha Jovem Aprendiz

Trilha de formação para jovens aprendizes, do zero (fundamentos de Ciência da Computação) até as
tecnologias usadas no dia a dia dos projetos: Git, lógica de programação em C++, HTML/CSS,
MongoDB, SQL Server e JavaScript/Node.js. 13 módulos em Markdown, cada um com teoria e prática
separadas, publicados como site com Docusaurus.

Site publicado: https://l1malucas.github.io/trilha-jovem-aprendiz/

## Estrutura

- `trila-jovens-aprendiz/` — conteúdo "cru": os módulos em Markdown puro (sem frontmatter do
  Docusaurus) e as apostilas-fonte originais (convertidas de PDF), usadas como base de conteúdo
  para os módulos técnicos (Git, MongoDB, SQL Server, lógica de programação, etc.).
- `docs/` — espelho dos módulos, com frontmatter do Docusaurus (id/title/sidebar_position),
  gerado a partir de `trila-jovens-aprendiz/` pelo script `scripts/build_docs.py`.
- `scripts/build_docs.py` — regenera `docs/` a partir de `trila-jovens-aprendiz/` depois de
  qualquer edição de conteúdo.

## Desenvolvimento local

```
npm install
npm run start
```

Depois de editar algo em `trila-jovens-aprendiz/`, regenere `docs/`:

```
python3 scripts/build_docs.py
```

## Build

```
npm run build
npm run serve
```

## Deploy

Publicação automática via GitHub Actions a cada push na branch `main`
(`.github/workflows/deploy.yml`), publicando em GitHub Pages.
