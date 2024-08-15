x = input("Enter a sequence of comma-separated numbers: ")

num_list = x.split(',')

num_tuple = tuple(num_list)

print("List:", num_list)
print("Tuple:", num_tuple)