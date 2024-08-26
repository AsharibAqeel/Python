def list_intersection(list1, list2):
 
    set1 = set(list1)
    set2 = set(list2)
    
    intersection = set1 & set2
    
    return list(intersection)

list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 55 , 120, 155]

result = list_intersection(list1, list2)

print("Intersection of the lists:", result)
