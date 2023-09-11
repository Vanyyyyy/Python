def laba1():
    input_list = [] # Создаем пустой список для ввода чисел

    n = int(input("Введите количество чисел: ")) # Пользователь вводит количество чисел

    for i in range(n):
        num = int(input(f"Введите число {i + 1}: ")) # Пользователь вводит числа
        input_list.append(num) # Добавляем число в список

    count = 0 # Начальное количество четных чисел

    for num in input_list:
        if num % 2 == 0:
            count += 1 # Увеличиваем счетчик на 1, если число четное

    return count
result = laba1()
print("Количество четных чисел:", result)
