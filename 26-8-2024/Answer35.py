def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  

sorted_list = [1, 3, 5, 7, 9, 11, 13]
target = 13
index = binary_search(sorted_list, target)

if index != -1:
    print(f"Element found at index {index}.")
else:
    print("Element not found in the list.")
