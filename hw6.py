# Работа с фильмами в Python.
# Импортируем словарь из файла marvel.py
from pprint import pprint
from marvel import small_dict
# Задача 1: Поиск фильмов по названию
# Запрос данных от пользователя
film_name = input('Введите название фильма: ').lower()
# Создаем список для хранения результатов поиска
if film_name == '':
    print('Вы не ввели название фильма')
    exit()
spisok = []
# Проверяем наличие введенного фильма в словаре и добавляем в список
for film in small_dict:
    if film_name in film.lower():
        spisok.append(film)
# Выводим результат
if len(spisok) == 0:
    print('Такого фильма нет в списке')
else:
    print('Фильмы, содержащие в названии введенную строку:')
    print(spisok)

print('--------------------------------------')

# Задача 2: Фильтрация фильмов по году выхода
# Список фильмов
film_list = []
# Словарь фильмов
film_dict = {}
# Список словарей с фильмами
film_dict_list = []
# Цикл 
for film, year in small_dict.items():
    # Обход проблемы с None
    if year is None:
        continue
    # Ищем фильмы вышедшие после 2024 и закидываем их
    if year > 2024:
        film_list.append(film)
        film_dict[film] = year
        film_dict_list.append({film: year})
print('Фильмы вышедшие после 2024:')
for films in film_list:
    # просто фильмы
    print(films)
print('--------------------------------------')
    # список фиьмов
print(film_list)
print('--------------------------------------')
# словарь фильмов
print(film_dict)
print('--------------------------------------')
# список словарей с фильмами
print(f'{film_dict_list}')

