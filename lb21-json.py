import json

"""students = [
    {
        "name": "Іван Петренко",
        "age": 20,
        "grades": {
            "Математика": 85,
            "Фізика": 90,
            "Програмування": 95
        },
        "enrolled": True
    },
    {
        "name": "Марія Ковальчук",
        "age": 20,
        "grades": {
            "Математика": 88,
            "Фізика": 78,
            "Програмування": 92
        },
        "enrolled": True
    }
]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)"""


"""with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades.values()) / len(grades)
    print(f"Ім'я студента: {name}")
    print(f"Середній бал: {average:.2f}")
    print("-" * 30)"""


with open("books.json", "r", encoding="utf-8") as file:
    books = json.load(file)

recent_books = [book for book in books if book["year"] > 2010]

print("Книги після 2010 року:")
for book in recent_books:
    print(f"- {book['title']} ({book['year']})")