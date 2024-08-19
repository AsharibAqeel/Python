class Employee:
   a = 1

class Programmer(Employee):
   b = 2

class Manager(Programmer):
   c = 3

O = Employee()
print(O.a)

O = Programmer()
print(O.a , O.b)

O = Manager()
print(O.a , O.b , O.c)