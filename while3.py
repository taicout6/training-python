# Armazenar nomes em uma lista enquanto o usuário digitar strings
# diferentes de vazio

lista = []

nome = input('Digite um nome: ')

while nome != '':
  lista.append(nome)
  nome = input('Digite um nome: ')

for item in lista:
  print(item)

  