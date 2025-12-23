def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b if b != 0 else "Деление на ноль!"


def calc():
    while True:
        print("\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Выход")
        op = input("Выберите операцию: ")

        if op == '5':
            print("Выход")
            break

        if op not in ['1', '2', '3', '4']:
            print("Ошибка выбора")
            continue

        try:
            x = float(input("Первое число: "))
            y = float(input("Второе число: "))

            if op == '1':
                res = add(x, y)
            elif op == '2':
                res = sub(x, y)
            elif op == '3':
                res = mul(x, y)
            elif op == '4':
                res = div(x, y)

            print(f"Результат: {res}")

        except ValueError:
            print("Ошибка ввода числа")


calc()