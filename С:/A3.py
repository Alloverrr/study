def analyze_packet_loss():
    # Ввод строки, состоящей из 0 и 1
    packets = input("Введите последовательность из 0 и 1 (не менее 5 символов): ")

    # Проверка корректности ввода
    if len(packets) < 5 or not all(char in '01' for char in packets):
        print("Неверный ввод. Убедитесь, что строка состоит только из символов '0' и '1' и имеет длину не менее 5.")
        return

    # Общее количество пакетов
    total_packets = len(packets)

    # Количество потерянных пакетов
    lost_packets = packets.count('0')

    # Длина самой длинной последовательности потерянных пакетов
    max_zero_sequence = 0
    current_zero_sequence = 0

    for packet in packets:
        if packet == '0':
            current_zero_sequence += 1
            max_zero_sequence = max(max_zero_sequence, current_zero_sequence)
        else:
            current_zero_sequence = 0

    # Процент потерь
    loss_percentage = (lost_packets / total_packets) * 100 if total_packets > 0 else 0

    # Оценка качества связи
    if loss_percentage > 20:
        quality = "критическое состояние сети"
    elif loss_percentage > 10:
        quality = "плохое качество"
    elif loss_percentage > 5:
        quality = "удовлетворительное качество"
    elif loss_percentage > 1:
        quality = "хорошее качество"
    else:
        quality = "отличное качество"

    # Вывод результатов
    print(f"• Общее количество пакетов: {total_packets}")
    print(f"• Количество потерянных пакетов: {lost_packets}")
    print(f"• Длина самой длинной последовательности потерянных пакетов: {max_zero_sequence}")
    print(f"• Процент потерь: {loss_percentage:.1f}%")
    print(f"• Качество связи: {quality}")

analyze_packet_loss()
