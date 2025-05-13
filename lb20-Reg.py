

import re

###1


#text = text = "Мої номери: 093-123-4567, 067-999-8888, інший текст, qwe-qwe-qweq, 123--123-12345, (050)-123-1234"
#pattern = r"\d{3}-\d{3}-\d{4}"

#numbers = re.findall(pattern, text)
#print("Знайдені номери:", numbers)

###2
#email = "example_user123@gmail.com"
#pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

#if re.match(pattern, email):
#    print("Коректна e-mail адреса")
#else:
#    print("Невірна адреса")


###3

#text = "Дати: 12.02.1990, 01.01.2025, 13-05-2025, 13/05/2025"
#pattern = r"\d{2}\.\d{2}\.\d{4}"

#result = re.sub(pattern, "DATE", text)
#print(result)

###4

#text = "мене звати Олег, мій брат — Іван. А наш пес — Шарик."
#pattern = r"\b[A-ЯA-Z][а-яa-z]+\b"

#names = re.findall(pattern, text)
#print("Імена:", names)


###5
#html = "<html><body><h1>Заголовок</h1></body></html>"
#pattern = r"</?[a-zA-Z0-9]+>"

#tags = re.findall(pattern, html)
#print("Знайдені теги:", tags)

###Додаткове завдання

def is_strong_password(password):
    if len(password) < 8:
        return "Пароль має бути не менше 8 символів"

    if not re.search(r"[A-Z]", password):
        return "Пароль має містити хоча б одну велику літеру"

    if not re.search(r"\d", password):
        return "Пароль має містити хоча б одну цифру"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Пароль має містити хоча б один спеціальний символ"

    return "Пароль надійний"

user_password = input("Введіть пароль: ")
message = is_strong_password(user_password)
print(message)

