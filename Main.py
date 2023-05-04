from Netshoes_Scrapping import NetshoesScraper

# Autor: Kaian Luciano Alves Dos Santos
# Projeto: Desenvolvimento Web Scraper
# Tecnologias: Python
# Data de Inicio: 03/05/23 13:45

# Utilização do web scraper
scraper = NetshoesScraper('https://www.netshoes.com.br/tenis-mizuno-wave-titan-2-preto-2FU-6367-006')
html = scraper.get_html_content()

# Verifica se a variável html contém algum valor. Se a variável html não for vazia ou nula,
# significa que o HTML da página foi obtido com sucesso. 
if html:
    product_info = scraper.parse_product_html(html)
    print(product_info)

    # Cria um arquivo para salvar os resultados
    with open('resultados.txt', 'w', encoding='utf-8') as arquivo:
        # Salva os resultados no arquivo
        arquivo.write(str(product_info))

    # Fecha o arquivo
    arquivo.close()

    # Imprime uma mensagem de confirmação
    print('Resultados salvos no arquivo resultados.txt')
else:
    print("Falha ao obter o HTML da página.")
