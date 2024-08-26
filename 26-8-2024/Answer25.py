class MyClass:
    class_param = "This is a class parameter"

    def __init__(self, instance_param):
        self.instance_param = instance_param

obj1 = MyClass("This is an instance parameter for obj1")
obj2 = MyClass("This is an instance parameter for obj2")

print("Class parameter accessed from obj1:", obj1.class_param)
print("Instance parameter of obj1:", obj1.instance_param)
print("Class parameter accessed from obj2:", obj2.class_param)
print("Instance parameter of obj2:", obj2.instance_param)

print("Class parameter accessed directly from MyClass:", MyClass.class_param)
