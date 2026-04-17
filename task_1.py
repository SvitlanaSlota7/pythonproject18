import re

class User:
    def __init__(self, email: str):
        if self.validate(email):
            self.email = email
            print(f"Об'єкт створено успішно з email: {self.email}")
        else:
            raise ValueError("Некоректний формат email")

    @classmethod
    def validate(cls, email: str) -> bool:
        # Регулярний вираз для перевірки email
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if not isinstance(email, str):
            print("Помилка: email має бути рядком.")
            return False

        if re.match(email_regex, email):
            return True
        else:
            print(f"Помилка: '{email}' не є валідним форматом email.")
            return False

if __name__ == "__main__":
    try:
        user1 = User("test05@gmail.com")

        user2 = User("invalid-email.com")
    except ValueError as e:
        print(f"Помилка {e}")