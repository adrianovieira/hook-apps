# README

Essa apresentação requer ***reveal-js*** (<http://lab.hakim.se/reveal-js/>)

## Como gerar a apresentação?

```
pandoc -t revealjs --css css/dataprev.css -s -V theme:dataprev --slide-level 2 \
          --filter pandoc-citeproc \
          --csl=$TEMPLATE_DIR/bibliografia/associacao-brasileira-de-normas-tecnicas-ufmg-face-initials.csl \
          -o index.html st-0x16-Meios_Metodos_criacao_Artigos_Markdown.md
```
