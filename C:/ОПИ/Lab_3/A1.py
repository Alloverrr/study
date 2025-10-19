def determine_quadrant(x, y):
    if x > 0 and y > 0:
        return "I"
    elif x < 0 and y > 0:
        return "II"
    elif x < 0 and y < 0:
        return "III"
    elif x > 0 and y < 0:
        return "IV"
    else:
        return None  # Не должно произойти, так как координаты не равны 0

def main():
    # Ввод координат точек
    x1 = float(input("Введите x1: "))
    y1 = float(input("Введите y1: "))
    x2 = float(input("Введите x2: "))
    y2 = float(input("Введите y2: "))

    # Определяем четверти для каждой точки
    quadrant1 = determine_quadrant(x1, y1)
    quadrant2 = determine_quadrant(x2, y2)

    # Проверяем, лежат ли точки в одной четверти
    if quadrant1 == quadrant2:
        print(f"Yes, {quadrant1}")
    else:
        print("No")

if __name__ == "__main__":
    main()3