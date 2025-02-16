


class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Вік має бути додатним числом")


person = Person("Олег", 25)
print(person.age)  # 25
person.age = '30'  # Оновлення значення
print(person.age)  # 30
person.age = -5  # Виведе повідомлення про помилку
print(person.age)  #30