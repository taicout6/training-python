import random

class MyList(list):
  def choice(self):
    return random.choice(self)
  
l = MyList([1, 2, 3, 4])

print(l)
print(len(l))

l.append(5)
print(len(l))

print(l)

print(l.choice())
print(l.choice())

