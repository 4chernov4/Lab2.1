num = int(input("Введите не более четырехзначное число: "))

if 0 <= num <= 9999:
    digit1 = num // 1000
    digit2 = (num % 1000) // 100
    digit3 = (num % 100) // 10
    digit4 = num % 10

    sum_of_digits = digit1 + digit2 + digit3 + digit4
    print(f"Сумма цифр числа {num} равна {sum_of_digits}")
else:
    print("Пожалуйста, введите не более четырехзначное число.")
