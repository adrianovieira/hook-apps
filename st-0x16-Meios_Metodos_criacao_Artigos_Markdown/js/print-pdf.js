<!-- Para gerar PDF -->
<!-- If the query includes '?print-pdf', include the PDF print sheet -->
<script>
    if( window.location.search.match( /print-pdf/gi ) ) {
            var link = document.createElement( 'link' );
            link.rel = 'stylesheet';
            link.type = 'text/css';
            link.href = 'css/print/pdf.css';
            document.getElementsByTagName( 'head' )[0].appendChild( link );
        }
</script>
<!-- via URL deve ser usado ?print-pdf -->
