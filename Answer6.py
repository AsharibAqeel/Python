import math

def calculate_a(d_values):
    C = 50
    H = 30
    result = []
    
    for D in d_values:
        Q = math.sqrt((2 * C * D) / H)
        result.append(int(Q))
    
    return result

def main():
    values = input("Enter values for D: ")
    d_values = list(map(int, values.split(',')))
    
    results = calculate_a(d_values)
    
    print(','.join(map(str, results)))

main()
