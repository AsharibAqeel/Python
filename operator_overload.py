class Number:
   def __init__(self , n):
      self.n = n
   def __truediv__(self , num):
      return self.n / num.n

n = Number(6)
m = Number(2)

print(n / m)
