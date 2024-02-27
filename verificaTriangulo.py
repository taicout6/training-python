# Receber 3 valores positivos (ladoA, ladoB e ladoC) e verificar se formam um triângulo, e se sim, que tipo de triângulo

lado_a = eval(input('Digite o valor para o lado A: '))
lado_b = eval(input('Digite o valor para o lado B: '))
lado_c = eval(input('Digite o valor para o lado C: '))

maior_lado = max(lado_a, lado_b, lado_c)

if maior_lado < lado_a + lado_b + lado_c -maior_lado:
  print('Os lados formam um triângulo!')
  if lado_a == lado_b and lado_b == lado_c and lado_a == lado_c:
    print('É um triângulo equilátero!')
  elif lado_a != lado_b and lado_b != lado_c and lado_a != lado_c:
    print('É um triângulo escaleno!')
  else:
    print('É um triângulo isóseles!')
else:
  print('Os lados não formam um triângulo!')

