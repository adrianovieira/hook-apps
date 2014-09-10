# README

Essa apresentação requer ***reveal-js*** (<http://lab.hakim.se/reveal-js/>)

## Como gerar a apresentação?

```
pandoc -t revealjs --css css/dataprev.css -s -V theme:dataprev --slide-level 2 \
           -o index.html st-0x16-Meios_Metodos_criacao_Artigos_Markdown.md
```
