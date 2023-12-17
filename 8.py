k = int(input("Введите количество строк на странице k: "))
n = int(input("Введите номер строки в тексте n: "))

def find_page_and_line(k, n):
    page = (n - 1) // k + 1

    line_on_page = (n - 1) % k + 1

    return page, line_on_page

if 1 <= k <= 200 and 1 <= n <= 20000:
    page_number, line_number = find_page_and_line(k, n)
    print(f"Страница: {page_number}, Номер строки на странице: {line_number}")
else:
    print("Пожалуйста, введите корректные значения.")