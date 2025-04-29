

import math

"""radius = float(input("Введіть радіус кола: "))
area = math.pi * math.pow(radius, 2)
print(f"Площа кола: {area:.2f}")"""


"""number = float(input("Введіть число для обчислення квадратного кореня: "))
sqrt_result = math.sqrt(number)
print(f"Квадратний корінь з {number} дорівнює {sqrt_result:.2f}")"""



"""angle_degrees = float(input("Введіть кут у градусах: "))
angle_radians = math.radians(angle_degrees)

sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = math.tan(angle_radians)

print(f"Синус: {sin_value:.2f}")
print(f"Косинус: {cos_value:.2f}")
print(f"Тангенс: {tan_value:.2f}")"""



"""num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

gcd_result = math.gcd(num1, num2)
print(f"НСД ({num1}, {num2}) = {gcd_result}")"""



"""angle = float(input("Введіть кут у градусах: "))
function = input("Оберіть функцію (sin, cos, tan): ").lower()

angle_rad = math.radians(angle)

if function == "sin":
    print(f"Синус кута {angle}°: {math.sin(angle_rad):.2f}")
elif function == "cos":
    print(f"Косинус кута {angle}°: {math.cos(angle_rad):.2f}")
elif function == "tan":
    print(f"Тангенс кута {angle}°: {math.tan(angle_rad):.2f}")
else:
    print("Невідома функція!")"""



"""number = float(input("Введіть число: "))
base = float(input("Введіть основу логарифма: "))

log_result = math.log(number, base)
print(f"Логарифм числа {number} за основою {base} дорівнює {log_result:.2f}")"""

######### RANDOM ###########

import random

"""number = random.randint(1, 100)
print("Випадкове число:", number)"""



"""for i in range(5):
    number = random.uniform(0, 10)
    print(number)"""


"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruit = random.choice(fruits)
print("Випадковий фрукт:", fruit)"""


"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
random.shuffle(fruits)
print("Перемішаний список:", fruits)"""



"""numbers = random.sample(range(0, 51), 3)
print("Випадкові числа без повторень:", numbers)"""



random_numbers = [random.randint(0, 100) for i in range(10)]
print("Список випадкових чисел:", random_numbers)


















