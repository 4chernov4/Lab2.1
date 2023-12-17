month_number = int(input("Введите номер месяца (от 1 до 12): "))

def season(month):
    if 1 <= month <= 12:
        if 3 <= month <= 5:
            return "весна"
        elif 6 <= month <= 8:
            return "лето"
        elif 9 <= month <= 11:
            return "осень"
        else:
            return "зима"
    else:
        return "Неверный номер месяца"

result = season(month_number)
print(result)