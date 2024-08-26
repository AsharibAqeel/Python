def print_max_length_string(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)
    else:
        print(str1)
        print(str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print_max_length_string(string1, string2)
