# Estrutura de repetição <for> 

lista = ['cão', 'gato', 'coelho']

for indice in lista:
  print(indice)


palavra = 'algoritmos'

for letra in palavra:
  if letra in 'aiueo':
    print(letra)


# Função range(start, stop, step)

for n in range(10):
  print(n)


for x in range(1, 11):
  print(x)


for y in range(2, 20, 2):
  print(y)


# Acumuladores (acc = accumulator)
  
acc = 0

for number in range(1, 101):
  # acc = acc + number
  # Soma de todos os valores páres entre 1 e 100
  if number % 2 == 0:
    acc += number

print(acc)

