def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def process_binary_numbers(input_string):
    binary_numbers = input_string.split(',')
    
    divisible_by_5 = []
    
    for binary in binary_numbers:
        decimal = binary_to_decimal(binary)
        
        if decimal % 5 == 0:
            divisible_by_5.append(binary)
    
    result = ','.join(divisible_by_5)
    
    return result

input_string = "1001,0101,1010,1111"
print(process_binary_numbers(input_string))
