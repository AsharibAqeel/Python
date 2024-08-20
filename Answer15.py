def compute_expression(a):
    a_str = str(a)
    
    term1 = int(a_str)
    term2 = int(a_str * 2)
    term3 = int(a_str * 3)
    term4 = int(a_str * 4)
    
    result = term1 + term2 + term3 + term4
    
    return result

input_digit = 2

output = compute_expression(input_digit)

print(output)
