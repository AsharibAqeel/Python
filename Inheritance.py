class Employee:
     company = "ITC"
     def show(self):
          print(f"The name of Employee is {self.name} and thae salary is {self.salary}")

class Programer(Employee):
     company = "ITC Infotech"
     def showLanguage(self):
          print(f"The name is {self.name} and he is good with {self.language} language")

a=Employee()
b=Programer()
print(a.company , b.company)