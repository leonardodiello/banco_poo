class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("plim plim")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmmm")

    def trocar_marcha(self):
        print("Marcha trocada.")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Azul", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
b1.trocar_marcha()
print(b1)
print(b1.cor, b1.ano, b1.modelo, b1.valor)