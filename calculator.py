def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

def calculator():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Некорректный ввод! Попробуйте снова.")
            continue

        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")

        choice = input("Введите номер операции (1/2/3/4/5): ")

        if choice == '1':
            print(f"Результат: {add(num1, num2)}")
        elif choice == '2':
            print(f"Результат: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Результат: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Результат: {divide(num1, num2)}")
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор операции! Попробуйте снова.")

if __name__ == "__main__":
    calculator()
