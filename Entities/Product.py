class Product:
    #Construtor da Classe
    def __init__(self, title, price, image, description):
        self.title = title
        self.price = price
        self.image = image
        self.description = description

    #ToString da classe
    def __str__(self):
        return f"Title: {self.title}\nPrice: {self.price}\nImage: {self.image}\nDescription: \n{self.description}\n"
