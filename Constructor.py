class Employee:
    language = "Py"
    salary = 1200000

    def __init__(self):
        print("I am creating an Object")
        pass
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee()
harry.getInfo()
Employee.greet()