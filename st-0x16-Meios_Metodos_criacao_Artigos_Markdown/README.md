# README

Essa apresentação requer:

- ***reveal-js*** (<http://lab.hakim.se/reveal-js/>)
- CSL de <http://www-git/documentos/markdown-template>

## Como gerar a apresentação?

```
pandoc -t revealjs --css css/dataprev.css -s -V theme:dataprev --slide-level 2 \
          --filter pandoc-citeproc \
          --csl=$TEMPLATE_DIR/bibliografia/associacao-brasileira-de-normas-tecnicas-ufmg-face-full.csl \
          -o index.html st-0x16-Meios_Metodos_criacao_Artigos_Markdown.md
```

- gerar PDF: é necessário incluir o parâmetro ```-A js/print-pdf.js``` que permitirá ao navegador (browser) gerar ```html``` de toda a apresentação.
