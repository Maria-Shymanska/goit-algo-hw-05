def binary_search(arr, target):
    iterations = 0
    left = 0
    right = len(arr) - 1
    upper_bound = None
    
    while left <= right:
        mid = (left + right) // 2
        iterations += 1
        
        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1
    
    # If target is not found
    return iterations, upper_bound

# Examples:
sorted_array = [0.1, 0.5, 1.2, 2.3, 3.5, 5.8, 8.9]
target_value = 2.3
iterations, upper_bound = binary_search(sorted_array, target_value)
print("Кількість ітерацій:", iterations)
print("Верхня межа:", upper_bound)