# Loop <for> aninhado

lista_nomes = ['Tai', 'Bele', 'Katarina', 'Celso']
vogais = 'aiueo'

for nome in lista_nomes:
  for letra in nome:
    if letra in vogais:
      print(letra)

