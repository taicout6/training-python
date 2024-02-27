# Estruturas de condição de uma, duas ou mais vias

altura = eval(input('Digite sua altura em metros: '))
genero = input('Digite seu gênero (M/F): ')

if genero == 'M' or genero == 'm':
  pesoIdeal = (72.7 * altura) - 58
elif genero == 'F' or genero == 'f':
  pesoIdeal = (62.1 * altura) - 44.7
else:
  print('Opção inválida')


print(f'Seu peso ideal é: {pesoIdeal}Kg')

