class Employee:
   def __init__(self):
    print("Constructor of Employee")
   a = 1

class Programmer(Employee):
   def __init__(self):
      print("Constructor of Programer")
   b = 2

class Manager(Programmer):
   def __init__(self):
      super().__init__()
   c = 3

O = Employee()
print(O.a)

O = Programmer()
print(O.a , O.b)

O = Manager()
print(O.a , O.b , O.c)