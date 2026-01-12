import random

def draw_rectangle(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            print(ch, end='')
        print()

def draw_right_triangle(rows, ch):
    for i in range(rows):
        for j in range(i + 1):
            print(ch, end='')
        print()

def draw_frame(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(ch, end='')
            else:
                print(' ', end='')
        print()

print("Используя вложенные циклы, изобразите следующие фигуры:")

n = int(input("Введите n (количество строк): "))
m = int(input("Введите m (количество столбцов): "))

# Прямоугольник
print(f"\nПРЯМОУГОЛЬНИК {n}x{m}:")
draw_rectangle(n, m, '#')

# Правый треугольник
print(f"\nПРАВЫЙ ТРЕУГОЛЬНИК ({n} строк):")
draw_right_triangle(n, '#')

# Рамка
print(f"\nРАМКА {n}*{m}:")
draw_frame(n, m, '#')