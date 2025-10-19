import string
def check_password_strength(password):
    errors = []
    allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'

    # Проверка длины пароля
    if len(password) != 8:
        errors.append("Длина пароля не равна 8")

    # Проверка наличия заглавных букв
    if not any(char.isupper() for char in password):
        errors.append("В пароле отсутствуют заглавные буквы")

    # Проверка наличия строчных букв
    if not any(char.islower() for char in password):
        errors.append("В пароле отсутствуют строчные буквы")

    # Проверка наличия цифр
    if not any(char.isdigit() for char in password):
        errors.append("В пароле отсутствуют цифры")

    # Проверка наличия специальных символов
    if not any(char in '*-#' for char in password):
        errors.append("В пароле отсутствуют специальные символы")

    # Проверка на наличие недопустимых символов
    if not all(char in allowed for char in password):
        errors.append("В пароле используются непредусмотренные символы")

    # Вывод результатов
    if errors:
        for error in errors:
            print(error)
    else:
        print("Надежный пароль")

def main():
    password = input("Введите пароль: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()
