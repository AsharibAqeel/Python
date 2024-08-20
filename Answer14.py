def count_case_letters(sentence):
    upper_case_count = 0
    lower_case_count = 0
    
    for char in sentence:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lower_case_count += 1
    
    return upper_case_count, lower_case_count

input_sentence = "HELLO world!"

upper_case, lower_case = count_case_letters(input_sentence)

print(f"UPPER CASE {upper_case}")
print(f"LOWER CASE {lower_case}")
