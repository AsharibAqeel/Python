X , Y = map(int, input("Enter The numbers : ").split(','))

array = [[i * j for j in range(Y)] for i in range(X)]

print(array)
