## Script para Captura de Taxas de Câmbio
Este script em Python foi desenvolvido para obter as taxas de câmbio atuais do dólar (USD), euro (EUR) e iene (JPY) a partir dos resultados de pesquisa do Google.

## Requisitos
Python 3.x
Bibliotecas necessárias: requests, BeautifulSoup
Uso
Certifique-se de ter o Python 3.x instalado no seu sistema.

Instale as bibliotecas necessárias utilizando os seguintes comandos:

pip install requests
pip install beautifulsoup4

O script irá buscar as taxas de câmbio atuais de USD, EUR e JPY nos resultados de pesquisa do Google, exibindo os valores.

## Descrição do Código
currency_scraper.py contém o código principal.
A biblioteca requests é usada para enviar requisições HTTP.
BeautifulSoup é utilizada para analisar o conteúdo HTML.
Três URLs são usados para obter as taxas de câmbio de USD, EUR e JPY.
São fornecidos cabeçalhos User-Agent para simular um navegador ao fazer as requisições.
O script extrai os valores das moedas do conteúdo HTML utilizando BeautifulSoup.
Notas Importantes
As páginas de resultados de pesquisa do Google são acessadas, e mudanças na estrutura podem fazer o script parar de funcionar.
A confiabilidade do script depende da estrutura HTML dos resultados de busca do Google, que pode ser modificada.
Aviso
Este script foi desenvolvido para fins educacionais, demonstrando como fazer raspagem de dados da web usando Python. Use com responsabilidade e certifique-se de cumprir os termos de serviço do site.
