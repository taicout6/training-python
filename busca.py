import random

lista = random.sample(range(100), 20)

print(lista)

lista.sort()

print(lista)

def busca_binaria(lista, x, inicio, fim):
  meio = (inicio + fim) // 2

  if x == lista[meio]:
    return meio
  
  if x > lista[meio]:
    return busca_binaria(lista, x, meio + 1, fim)
  
  if x < lista[meio]:
    return busca_binaria(lista, x, inicio, meio -1)
  
print(busca_binaria(lista, 72, 0, 19))

