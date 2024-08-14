#dicionario do estoque
estoque = {
    "tomate": [1000, 2.30]
    "alface": [1000, 1.30]
    "batata": [500, 2.60]
    "feijao": [200, 5.30]
}

total =0     #iniciliza a variavel que vai armazenaro total das vendas
print("Vendas:\n")   #exibe um titulo
while True:
    produto = input("nome do produto fim para sair):")
    if produto =="fim":  #se o usuario digitar fim, encerra o programa
        break
 if produto in estoque:    #verifica se o produto ta no estoque
quantidade = int(input("quantidade:"))   #solicita a quantidade desejada do produto
if quantidade <= estoque[produto][0]:   #verifica se ha quantidade desejada do produto
preço = estoque[produto][1]    #obtem o preco do produto
custo = preço * quantidade   #calcula o custo total da quantidade solicitada
print(f"{produto:12s}"{quantidade:3d} #exibe a linha de venda formada
x {preço:6.2f} = {custo 6.2f}")
estoque[produto][0] -= quantidade #atualiza a quantidade disponivel no estoque
      total += custo   #adiciona o custo de venda total
else:
      print("Quantidade solicitada não disponível") #fala se o produto nao esta no estoque
else:
print("Nome de produto inválido")     #fala que o produto esta no estoque
      print(f" Custo total: {total:21.2f}\n")  #exibe o custo total das vendas
      print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave) #exibe o nome do produto
print("Quantidade: ", dados[0]) #exibe a quantidado do produto
print(f"Preço: {dados[1]:6.2f}\n")   #exibe o preco do produto