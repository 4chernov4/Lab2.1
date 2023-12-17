import random

array_size = 10

array = [random.randint(50, 100) for _ in range(array_size)]

print("Исходный массив:", array)

sum_even_positions = sum(array[1::2])

print("Сумма элементов на четных позициях:", sum_even_positions)
