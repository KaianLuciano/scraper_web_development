from Netshoes_Scrapping import NetshoesScraper

# Autor: Kaian Luciano Alves Dos Santos
# Projeto: Desenvolvimento Web Scraper
# Tecnologias: Python
# Data de Inicio: 03/05/23 13:45

# Utilização do web scraper
scraper = NetshoesScraper('https://www.netshoes.com.br/tenis-mizuno-wave-titan-2-preto-2FU-6367-006')
html = scraper.fetch_html()

# Verifica se a variável html contém algum valor. Se a variável html não for vazia ou nula,
# significa que o HTML da página foi obtido com sucesso. 
if html:
    product_info = scraper.extract_product_info(html)
    print(product_info)
else:
    print("Falha ao obter o HTML da página.")
