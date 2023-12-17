n = int(input("Введите натуральное число n (не превосходящее 100): "))

def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

if 1 <= n <= 100:
    result = sum_of_squares(n)
    print(result)
else:
    print("Пожалуйста, введите натуральное число в диапазоне от 1 до 100.")
