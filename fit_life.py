# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_IN_LITER = 1000
MIN_AGE = 0
MAX_AGE = 120
MIN_WEIGHT = 0
MAX_WEIGHT = 300
MIN_HEIGHT = 0
MAX_HEIGHT = 3
SEPARATOR_CHAR = "*"
SEPARATOR_CHAR_WIDTH = 50
MSG_INVALID_RANGE = "Пожалуйста, проверьте введенные данные."
MSG_INVALID_FORMAT = "Вы ввели не число или использовали запятую."

print("Здравствуйте! Я ваш персональный бот FitLife!")

user_name = input("Как вас зовут? ").strip().title()
"""
Запрашиваем имя пользователя,
убираем лишние пробелы по краям
добавляем правку, если пользователь ввел имя с маленькой буквы

"""
# Цикл для корректного получения данных о возрасте пользователя
while True:
    try:
        # Запрашиваем возраст пользователя, убираем лишние пробелы по краям
        user_age = int(input("Сколько вам полных лет?(например, 25) "))

        # Логическая проверка введенных данных
        if MIN_AGE < user_age < MAX_AGE:
            break
        else:
            print(MSG_INVALID_RANGE)

    except ValueError:
        print(MSG_INVALID_RANGE)

print()
print(f"Рад знакомству, {user_name}!")
print("Давайте теперь рассчитаем ваш ИМТ (индекс массы тела).")
print()

# Цикл для корректного получения данных о весе пользователя
while True:
    try:
        # Запрашиваем вес пользователя, убираем лишние пробелы по краям
        user_weight = float(input("Введите ваш вес в кг (например, 67.3): "))

        # Логическая проверка введенных данных
        if MIN_WEIGHT < user_weight < MAX_WEIGHT:
            break
        else:
            print(MSG_INVALID_RANGE)

    except ValueError:
        # Сюда мы попадаем, если были введены буквы, запятая и т.д.
        print(MSG_INVALID_FORMAT)

# Цикл для корректного получения данных о росте пользователя
while True:
    try:
        # Запрашиваем рост пользователя
        user_height = float(input("Введите рост в метрах (например, 1.75): "))
        # Логическая проверка введенных данных
        if MIN_HEIGHT < user_height < MAX_HEIGHT:
            break
        else:
            print(MSG_INVALID_RANGE)

    except ValueError:
        # Сюда мы попадаем, если были введены буквы, запятая и т.д.
        print(MSG_INVALID_FORMAT)

# Расчет ИМТ
bmi = round(user_weight / (user_height ** 2), 1)
# Расчет нормы воды в миллилитрах
water_ml = user_weight * WATER_PER_KG
# Перевод полученного значения нормы воды в литры
water_l = water_ml / ML_IN_LITER

# Вывод результата
print()
print(SEPARATOR_CHAR * SEPARATOR_CHAR_WIDTH)
print(f"Отчет для пользователя: {user_name}, {user_age} г.")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print(SEPARATOR_CHAR * SEPARATOR_CHAR_WIDTH)
print()
print("Расчет окончен. Будьте здоровы!")
