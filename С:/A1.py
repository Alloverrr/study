import random
import time


def multiplication_trainer():
    # Запрашиваем количество примеров
    while True:
        try:
            N = int(input("Введите количество примеров: "))
            if N <= 0:
                print("Количество примеров должно быть положительным числом!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")

    correct_answers = 0
    total_time = 0
    question_times = []

    print()

    for i in range(N):
        print(f"Вопрос {i + 1}/{N}")


        a = random.randint(2, 9)
        b = random.randint(2, 9)
        correct_result = a * b

        while True:
            try:
                start_time = time.time()  # Засекаем время начала
                user_input = input(f"{a} × {b} = ")
                end_time = time.time()  # Засекаем время окончания

                time_spent = end_time - start_time
                user_answer = int(user_input)

                # Проверяем ответ
                if user_answer == correct_result:
                    print(f"Верно! (Время: {time_spent:.1f} сек)")
                    correct_answers += 1
                    question_times.append(time_spent)
                    total_time += time_spent
                else:
                    print(f"Неверно! Правильно: {correct_result} (Время: {time_spent:.1f} сек)")
                    question_times.append(time_spent)
                    total_time += time_spent

                break

            except ValueError:
                print("Пожалуйста, введите целое число!")

        print()

    # Выводим статистику
    print("СТАТИСТИКА:")

    if question_times: 
        average_time = total_time / N
        percentage = (correct_answers / N) * 100

        print(f"Общее время: {total_time:.1f} секунд")
        print(f"Среднее время на вопрос: {average_time:.1f} сек")
        print(f"Правильных ответов: {correct_answers}/{N}")
        print(f"Процент правильных: {percentage:.1f}%")
    else:
        print("Нет данных для статистики")


if __name__ == "__main__":
    multiplication_trainer()
