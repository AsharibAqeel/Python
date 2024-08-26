def print_docs():
    print("Documentation for abs():")
    print(abs.__doc__)
    print("\nDocumentation for int():")
    print(int.__doc__)
    
    print("\nDocumentation for input():")
    print(input.__doc__)
    
    def custom_function(x, y):
       
        return x + y

    print("\nDocumentation for custom_function(x, y):")
    print(custom_function.__doc__)

print_docs()
