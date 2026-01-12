import re

def is_valid_number(card_number):
    # Проверяем, что все символы - цифры и длина номера соответствует требованиям
    return card_number.isdigit() and len(card_number) in [13, 15, 16]

def get_card_type(card_number):
    # Определяем тип карты
    if len(card_number) in [13, 16] and card_number.startswith("4"):
        return "Visa"
    elif len(card_number) == 15 and (card_number.startswith("34") or card_number.startswith("37")):
        return "American Express"
    elif len(card_number) == 16 and re.match(r'5[1-5]', card_number[:2]):
        return "MasterCard"
    else:
        return "Invalid"

def get_check_sum(card_number):
    # Алгоритм Луна
    total_sum = 0
    reversed_digits = [int(d) for d in card_number[::-1]]

    for i in range(len(reversed_digits)):
        if i % 2 == 1:  # Умножаем каждую вторую цифру на 2
            doubled = reversed_digits[i] * 2
            total_sum += (doubled // 10) + (doubled % 10)  # Суммируем цифры произведения
        else:
            total_sum += reversed_digits[i]  # Суммируем цифры, которые не умножались на 2

    return total_sum

# Запуск программы
card_number = input("Введите номер банковской карты: ")

if is_valid_number(card_number):
    if get_check_sum(card_number) % 10 == 0:
        print(f"Тип карты: {get_card_type(card_number)}")
    else:
        print("Invalid")
else:
    print("Invalid")
