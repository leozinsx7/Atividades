try:
 n1 = int(input('Digite o primeiro número: '))
 n2 = int(input('Digite o segundo número: '))
 resultado = n1 / n2
 print('O resultado da divisão é:', resultado)
except ValueError:
 print('Erro de Entrada inválida')
except ZeroDivisionError:
 print('Erro de Divisão por zero')
