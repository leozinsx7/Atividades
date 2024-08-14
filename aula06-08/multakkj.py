velocidade = float(input("Qual sua velocidade: "))
if velocidade <=80:
    print('ok, sem problemas')
elif velocidade > 80:
    print('você sera mutado')
    qtdemulta = velocidade - 80.0
    valormulta = 7.0 * qtdemulta
    print("você pagara R${:.2f}".format(valormulta))
print("fim do programa")