import requests
from bs4 import BeautifulSoup
from Product import Product

class NetshoesScraper:
    #Construtor da classe
    def __init__(self, url):
        self.url = url

    #Função que irá tentar uma conexao com a url especificada, caso não consiga retorna None
    def fetch_html(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None

    #Função que irá capturar o (Titulo, preço, imagem e descrição dos produtos na url especificada)
    def extract_product_info(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        # Essa condição verifica se o elemento 'h1' dentro da section com a classe 'short-description' foi encontrado. 
        # Se title_element não for None, o texto do elemento é extraído e armazenado na variável title usando o método
        # text.strip(). Caso contrário, uma mensagem de erro é exibida informando que o elemento não foi encontrado.
        title_element = soup.find('section', class_='short-description').find('h1')#.text.strip()
        if title_element:
            title = title_element.text.strip()
        else:
            print("Elemento 'h1' dentro de 'section' com class='short-description' não encontrado.")

        #Essa condição verifica se o elemento 'strong' dentro do 'span' dentro do 'div' com a classe 'default-price'
        #foi encontrado. Se price_element não for None, o texto do elemento é extraído e armazenado na variável price
        #usando o método text.strip(). Caso contrário, uma mensagem de erro é exibida informando que o elemento não foi encontrado.
        price_element = soup.find('div', class_='default-price').find('span')
        if price_element:
            price = price_element.find('strong').text.strip()
        else:
            print("Elemento 'strong' dentro de 'span' dentro de 'div' com class='default-price' não encontrado.")

        # Essa condição verifica se o elemento 'img' com a classe 'zoom' foi encontrado. Se image_element não for None,
        # o valor do atributo 'src' do elemento é extraído e armazenado na variável image. 
        # Caso contrário, uma mensagem de erro é exibida informando que o elemento não foi encontrado.
        image_element = soup.find('img', class_='zoom')
        if image_element:
            image = image_element['src']
        else:
            print("Elemento 'img' com class='zoom' não encontrado.")

        # Essa condição verifica se o elemento 'p' com o atributo 'itemprop' igual a 'description' foi encontrado. 
        # Se description_element não for None, o texto do elemento é extraído e armazenado na variável description 
        # usando o método get_text(strip=True). Caso contrário, uma mensagem de erro é exibida informando que o elemento
        # não foi encontrado.
        description_element = soup.find('p', itemprop='description')
        if description_element:
            description = description_element.get_text(strip=True)
        else:
            print("Elemento 'p' com atributo itemprop='description' não encontrado.")

        #Retorna o objeto Product com seus atributos preenchidos
        product = Product(title, price, image, description)
        return product

