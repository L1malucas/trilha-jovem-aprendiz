// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

const GITHUB_USER = 'L1malucas';
const REPO_NAME = 'trilha-jovem-aprendiz';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Trilha Jovem Aprendiz',
  tagline: 'Do zero até as tecnologias do dia a dia — Git, lógica, bancos de dados e web',
  favicon: 'img/favicon.png',

  future: {
    v4: true,
  },

  url: `https://${GITHUB_USER}.github.io`,
  baseUrl: `/${REPO_NAME}/`,

  organizationName: GITHUB_USER,
  projectName: REPO_NAME,

  onBrokenLinks: 'throw',

  // Os módulos são Markdown puro (com blocos de código C++/SQL/JSON, tabelas
  // e `<placeholders>` em prosa) — não foram escritos para MDX/JSX. 'detect'
  // mantém arquivos .md como Commonmark tradicional.
  markdown: {
    format: 'detect',
  },

  i18n: {
    defaultLocale: 'pt-BR',
    locales: ['pt-BR'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
          editUrl: `https://github.com/${GITHUB_USER}/${REPO_NAME}/tree/main/docs/`,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'Trilha Jovem Aprendiz',
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Trilha',
          },
          {
            href: `https://github.com/${GITHUB_USER}/${REPO_NAME}`,
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Trilha',
            items: [
              {
                label: 'Início',
                to: '/',
              },
            ],
          },
          {
            title: 'Mais',
            items: [
              {
                label: 'GitHub',
                href: `https://github.com/${GITHUB_USER}/${REPO_NAME}`,
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Trilha Jovem Aprendiz. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
