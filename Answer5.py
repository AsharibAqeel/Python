class StringManipulator:
    def __init__(self):
        self.string = ""
    
    def getString(self):
        self.string = input("Enter a string: ")
    
    def printString(self):
        print(self.string.upper())

def test_string_manipulator():
    sm = StringManipulator()
    sm.getString()
    sm.printString()

test_string_manipulator()
