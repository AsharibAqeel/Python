def is_all_even_digits(number):
    
    str_number = str(number)

    for digit in str_number:
        if digit not in '02468':
            return False
        
    return True

def find_even_digit_numbers(start, end):
    even_digit_numbers = []
    
    for num in range(start, end + 1):
        if is_all_even_digits(num):
            even_digit_numbers.append(num)
    
    result = ','.join(map(str, even_digit_numbers))
    
    return result

start =10
end = 30

print(find_even_digit_numbers(start, end))
