import math



def calculator():
    while True:
        print("\nОберіть операцію:")
        print("1. Додавання (+)")
        print("2. Віднімання (-)")
        print("3. Множення (*)")
        print("4. Ділення (/)")
        print("5. Зведення у ступінь (^)")
        print("6. Добування кореня (√)")
        print("7. Вийти")

        choice = input("Введіть номер операції: ")

        if choice == '7':
            print("Калькулятор завершив роботу.")
            break

        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))

            if choice == '1':
                print(f"Результат: {num1 + num2}")
            elif choice == '2':
                print(f"Результат: {num1 - num2}")
            elif choice == '3':
                print(f"Результат: {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"Результат: {num1 / num2}")
                else:
                    print("Помилка: ділення на нуль!")
            elif choice == '5':
                print(f"Результат: {num1 ** num2}")


        elif choice == '6':
            num = float(input("Введіть число: "))
            if num >= 0:
                print(f"Результат: {math.sqrt(num)}")
            else:
                print("Помилка: не можна обчислити корінь з від’ємного числа!")

        else:
            print("Неправильний вибір, спробуйте ще раз.")

calculator()
