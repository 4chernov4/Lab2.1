def negative_numbers(arr):
    count = 0
    for element in arr:
        if element < 0:
            count += 1
    return count

array = [1, -2, 3, -4, 5, -6]
result = negative_numbers(array)
print(result)
