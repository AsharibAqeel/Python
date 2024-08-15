def check_Sequence(s):
    i=0
    n=len(s)

    while i < n:
        zero_count = 0
        while i < n and s[i] == '0':
            zero_count += 1
            i += 1
        
        one_count = 0
        while i < n and s[i] == '1':
            one_count += 1
            i += 1

        if zero_count != one_count:
            return False
        
        return True
    
print(check_Sequence("01010101")) 
print(check_Sequence("00"))       
print(check_Sequence("000111000111"))
print(check_Sequence("00011100011"))   