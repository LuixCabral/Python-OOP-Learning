class Pessoa:
    def __init__(self, nome, sobrenome,idade, dia_aniversario, mes_aniversario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.dia_aniversario = dia_aniversario
        self.mes_aniversario = mes_aniversario

    def trocar_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def nome_completo(self):
        print(self.nome + " " + self.sobrenome)

    def printar_idade(self):
      print(self.idade)

    def fazer_aniversario(self):
        print(str(self.dia_aniversario) + "/" + str(self.mes_aniversario))


# Criando uma instância da classe Pessoa
pessoa = Pessoa("Luis", "Cabral", 20, 17 , 4)

# Chamando os métodos da classe Pessoa
pessoa.fazer_aniversario()  # Saída: 17/4
pessoa.printar_idade()
pessoa.trocar_sobrenome("Nascimento")
pessoa.nome_completo()  # Saída: Luis Nascimento

print("Hello World")
