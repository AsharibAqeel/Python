word = input("Enter a sequence of words: ")

word_list = word.split(',')

sorted_list = sorted(word_list)

sorted_word = ','.join(sorted_list)

print(sorted_word)
