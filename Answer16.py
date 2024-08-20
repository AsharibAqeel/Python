def odd_digits(number):
    
    str_number = str(number)

    for digit in str_number:
        if digit not in '13579':
            return False
        return True

def find_odd_digit_numbers(start, end):
    odd_digit_numbers = [] 
    for num in range(start, end + 1):
        if odd_digits(num):
            odd_digit_numbers.append(num)
    
    result = ','.join(map(str, odd_digit_numbers))
    return result

start =1
end = 10

print(find_odd_digit_numbers(start, end))
