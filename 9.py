number_to_check = int(input("Введите число от 0 до 1000: "))

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

if 0 <= number_to_check <= 1000:
    result = is_prime(number_to_check)
    print(f"{number_to_check} {'простое' if result else 'не простое'} число.")
else:
    print("Введите число от 0 до 1000.")
