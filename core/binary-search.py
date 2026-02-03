def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_arr = [1, 3, 5, 7, 9]

print(binary_search(my_arr, 9)) # 4
print(binary_search(my_arr, 10)) # None