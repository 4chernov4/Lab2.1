import math

a = float(input("Введите длину катета a: "))
b = float(input("Введите длину катета b: "))

c = math.sqrt(a**2 + b**2)

print(f"Гипотенуза треугольника с катетами {a} и {b} равна {c}")