altura = eval(input('Digite sua altura em metros: '))
genero = input('Digite seu gênero (M/F): ')

if (genero == 'M'):
  pesoIdeal = (72.7 * altura) - 58
else:
  pesoIdeal = (62.1 * altura) - 44.7

print(f'Seu peso ideal é: {pesoIdeal}Kg')

