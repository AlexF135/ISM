



#Вивести в консоль поточний час в Unix-форматі та в отформатованому за шаблоном
#Unix-час: 1745251209.000702
#Локальний час: 2025-04-21 19:00:09

import time

"""print("Unix-час:", time.time())

local_time = time.localtime()
print(local_time)
print("Локальний час:", time.strftime("%Y-%m-%d %H:%M:%S", local_time))"""


#Зробить затримку на 5 секунд у виконанні будь-якої програми

"""print("Початок затримки...")
time.sleep(5)
print("Пройшло 5 секунд!")"""

#Вивести в консоль поточний час та час в отформатованому за шаблоном
#Поточна дата і час: 2025-04-21 19:05:03.010602
#Форматована дата: Monday, 21 April 2025, 19:05
#Використати модуль datetime.

from datetime import datetime

"""now = datetime.now()
print("Поточна дата і час:", now)
print("Форматована дата:", now.strftime("%A, %d %B %Y, %H:%M"))"""


#Визначити, скільки днів залишилось до Нового року.

"""today = datetime.today()
new_year = datetime(today.year + 1, 1, 1)

delta = new_year - today
print("Залишилось до Нового року:", delta.days, "днів")"""


#Перетворити рядок з датою «22-04-2025 9:30» у формат datetime. Вивід: 2025-04-22 9:30:00


"""date_str = "22-04-2025 9:30"
dt = datetime.strptime(date_str, "%d-%m-%Y %H:%M")
print("Дата з рядка:", dt)"""


#Напишіть програму, яка приймає з клавіатури число секунд і виконує зворотний відлік до нуля.
# Після завершення програма повинна вивести повідомлення "Час вийшов!".

"""seconds = int(input("Введіть кількість секунд: "))

for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)

print("Час вийшов!")"""

#Напишіть програму, яка запитує у користувача його дату народження у форматі ДД-ММ-РРРР і обчислює його вік у роках


birth_input = input("Введіть дату народження (ДД-ММ-РРРР): ")

birth_date = datetime.strptime(birth_input, "%d-%m-%Y")

today = datetime.today()

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"Вам {age} років.")


