# pedir para o usuário digitar um número inteiro positivo
# Caso contrario, emitir uma mensagem e pedir para digitar novamente.

numero = eval(input('Digite um número maior que zero: '))

while numero < 0:
  print(f'{numero} é menor do que 0, tente novamente')
  numero = eval(input('Digite um número maior que zero: '))

