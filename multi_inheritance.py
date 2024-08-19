class Employee:
     company = "ITC"
     name = "Arshoo"
     def show(self):
          print(f"The name of Employee is {self.name} and thae salary is {self.company}")

class Coder:
       language = "Python"
       def printlanguage(self):
          print(f"Out of all languages here is your language : {self.language} ")


class Programer(Employee , Coder):
     company = "ITC Infotech"
     def showLanguage(self):
          print(f"The name is {self.company} and he is good with {self.language} language")

a=Employee()
b=Programer()

b.show()
b.showLanguage()
b.printlanguage()
