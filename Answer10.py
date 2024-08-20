def process_input(input_string):

    words = input_string.split()
    
    unique_words = list(set(words))
    
    sorted_words = sorted(unique_words)
    
    result = ' '.join(sorted_words)
    
    return result

input_string = "hello world and practice makes perfect "

print(process_input(input_string))
