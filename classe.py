class Ponto:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def setX(self, x):
    self.x = x

  def setY(self, y):
    self.y = y

  def get(self):
    return self.x, self.y

  def mover(self, offsetx, offsety):
    self.x += offsetx
    self.y += offsety

  def __repr__(self) -> str:
    return '(' + str(self.x) + ',' + str(self.y) + ')'
  
  def __add__(self, other):
    if type(other) == Ponto:
      return Ponto(self.x + other.x, self.y + other.y)
    else:
      return Ponto(self.x + other, self.y + other)


p = Ponto()
p.setX(5)
p.setY(4)

print(p)

q = Ponto(3, 4)

print(p + q)

