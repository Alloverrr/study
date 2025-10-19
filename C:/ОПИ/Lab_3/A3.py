def calculate_gas_bill(previous_reading, current_reading):
    # Определяем объем использованного газа
    if current_reading >= previous_reading:
        used_gas = current_reading - previous_reading
    else:
        used_gas = (10000 - previous_reading) + current_reading  # Учет сброса счетчика

    # Определяем сумму к оплате
    if used_gas <= 300:
        bill = 21.00
    elif used_gas <= 600:
        bill = 21.00 + (used_gas - 300) * 0.06
    elif used_gas <= 800:
        bill = 21.00 + (300 * 0.06) + (used_gas - 600) * 0.04
    else:
        bill = 21.00 + (300 * 0.06) + (200 * 0.04) + (used_gas - 800) * 0.025

    # Вычисляем среднюю цену за кубометр
    average_price = bill / used_gas if used_gas > 0 else 0

    # Округляем результаты до двух знаков после запятой
    return used_gas, round(bill, 2), round(average_price, 2)

def main():
    previous_reading = int(input("Введите предыдущее показание счетчика: "))
    current_reading = int(input("Введите текущее показание счетчика: "))

    used_gas, bill, average_price = calculate_gas_bill(previous_reading, current_reading)

    print("Предыдущее Текущее Использовано К оплате Ср. цена m^3")
    print(f"    {previous_reading}     {current_reading}        {used_gas}        {bill}       {average_price}")

if __name__ == "__main__":
    main()
