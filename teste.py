import math

x = 2
y = 3
z = -4

conta = (x**y)/abs(z)

# print(conta)

cpf = '457.280.428-41'
# print(cpf[-2:])

notas = [7, 8, 5, 6, 9, 9.1, 8.9]
# print(max(7, 8, 5, 6, 9, 9.1, 8.9))

notas[-1] = 4
print(notas)

print(sorted(notas))

media = sum(notas) / 7

print(media)

print(math.ceil(media))

print(math.log10(2))
print(math.log(2))

print(notas.index(4))
