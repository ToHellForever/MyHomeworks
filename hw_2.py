# Задание №1: Конвертация секунд
# получаем пользовательский ввод секунд
user_input = int(input("Введите количество секунд: "))
# сколько часов
hours = user_input // 3600
# сколько минут
minutes = (user_input % 3600) // 60
# сколько секунд
seconds = user_input % 60
# выводим результат
print(f'В указанном количестве секунд ({user_input}):\nЧасов: {hours};\nМинут: {minutes};\nСекунд: {seconds}\n')


# Задание №2: Конвертация температуры
# получаем пользовательский ввод температуры
user_input_temp = round(float(input("Введите температуру в градусах Цельсия: ")), 2)
# конвертируем в Кельвины
kelvin = round((user_input_temp) + 273.15, 2)
# конвертируем в Фаренгейты
fahrenheit = round((user_input_temp * 9 / 5) + 32, 2)
# конвертируем в Реомюры
reamur = round((user_input_temp) * 4/5, 2)
# выводим результат
print(f'Температура в градусах Цельсия: {user_input_temp} °C\nТемпература в градусах Кельвина: {kelvin} K\nТемпература в градусах Фаренгейта: {fahrenheit} °F\nТемпература в градусах Реомюра: {reamur} °Ré\n')





