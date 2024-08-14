class Pessoa:
 def __init__(self, nome, idade):
 self.nome = nome
 self.idade = idade
 def imprimir(self):
 print('nome:',self.nome,'idade:',self.idade)

p1 = Pessoa('Maria', 20)
p1.imprimir()
