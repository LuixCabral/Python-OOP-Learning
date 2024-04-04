class Automovel():
    def __init__(self, nome, marca, rodas):
        self.nome = nome
        self.marca = marca
        self.rodas = rodas

    def print_nome(self):
        print(self.nome)

    def print_marca(self):
        print(self.marca)

    def print_rodas(self):
        print(self.rodas)


class Carro(Automovel):
    def __init__(self, nome, marca, rodas, assentos):
        super().__init__(nome, marca, rodas)
        self.assentos = assentos

    def print_assentos(self):
        print(self.assentos)

class Moto(Automovel):
  pass

automovel1 = Carro("Fiesta", "Ford", 4, 5)

automovel1.print_nome()
automovel1.print_marca()
automovel1.print_rodas()
automovel1.print_assentos()

print(" ")

automovel2 = Moto("pop100","Honda",2)

automovel2.print_nome()
automovel2.print_marca()
automovel2.print_rodas()