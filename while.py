# Estrutura de repetição -> while <-

# Encontre o maior valor de n tal que n! seja menor que L.
def nFatorial(L):
  n = 0
  fatorial = 1
  while fatorial <= L:
    n += 1
    fatorial *= n
  return n-1

print(nFatorial(120))