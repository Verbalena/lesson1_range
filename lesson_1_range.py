# #Задачи на range:
# Задача 1: Создайте два списка строк. Используя генератор, найдите произведение длин строк в парах,
#  для которых длины не равны. Проверьте, совпадают ли первые буквы этих строк. """

list_1 = ['яблоко', 'груша', 'виноград', 'абрикос', 'вишня']
list_2 = ['муха', 'комар', 'стрекоза', 'богомол', 'ваза']
# 1.1
print('Задача 1. Вариант 1')

length_lines = (len(x) * len(y) for x, y in zip(list_1, list_2) if len(x) != len(y))
print(list(length_lines))
result = [x[0] == y[0] for x, y in zip(list_1, list_2) if len(x) != len(y)]
print(result)
print()
# 1.2
print('Задача 1. Вариант 2')

for x, y in zip(list_1, list_2):
    if len(x) != len(y):
        res = len(x) * len(y)
        print(res)
        res2 = x[0] == y[0]
        print(res2)

# ------------------------------
# Задача 2: Определите два списка животных на английском и
# русском. Преобразуйте слова в верхний регистр, если английская версия длиннее.
# Проверьте, совпадают ли строки с русской и английской стороны при чтении с конца. """

print()
print('Задача 2')
animal_rus = ['медведь', 'заяц', 'волк', 'мышь', 'гепард']
animal_eng = ['bear', 'hare', 'wolf', 'mouse', 'cheetah']

for x,y in zip(animal_rus, animal_eng):
    if len(x) < len(y):
        print(x.upper(), y.upper())
print()  # пустая строка
# # Проверьте, совпадают ли строки с русской и английской стороны при чтении с конца.
animal_rus_reverse = animal_rus[::-1]
print(animal_rus_reverse)
for x,y in zip(animal_rus_reverse, animal_eng):
    print(len(x) == len(y))

animal_eng_reverse = animal_eng[::-1]
print(animal_eng_reverse)
for x,y in zip(animal_eng_reverse, animal_rus):
    print(len(x) == len(y))


# ----------------------------
# # """3. Задача 3: Создайте списки с названиями цветов на английском и русском.
# # Объедините строки в парах, где русская версия длиннее.
# # Проверяйте, длиннее ли английские слова или равны русским."""
print()
print('Задача 3')
flowers_rus = ['фиалка', 'ромашка', 'роза', 'тюльпан', 'ирис']
flowers_eng = ['violet', 'chamomile', 'rose', 'tulip', 'Iris']
# 1 вариант. В списке (result) представлены кортежи из пар, где русское слово длиннее английского.
# Все возможные варианты сравнения.
# В списке (result2) представлены кортежи из пар, где слова равны.
# В списке (result3) представлены кортежи из пар, где английское слово длиннее русского.
result = [(x, y) for x in flowers_rus for y in flowers_eng if len(x) > len(y)]
print(result)
result2 = [(x, y) for x in flowers_rus for y in flowers_eng if len(x) == len(y)]
print(result2)
result3 = [(x, y) for x in flowers_rus for y in flowers_eng if len(x) < len(y)]
print(result3)
# 2 вариант. Сравниваем по длине слова только в одинаковых индексах.
for x in range(len(flowers_rus)):
    if len(flowers_rus[x]) > len(flowers_eng[x]):
        print(f'Русская версия слова {flowers_rus[x]} длиннее {flowers_eng[x]}')
    elif len(flowers_rus[x]) == len(flowers_eng[x]):
        print(f'Длина слова {flowers_rus[x]} равна длине слова {flowers_eng[x]}')
    else:
        print(f'Cлово {flowers_eng[x]} длиннее слова {flowers_rus[x]}')

# ----------------------------------------------
#  # 4. Задача 4: Задайте списки светил на английском и русском. Возьмите первые
#  #три буквы английских слов в парах, где длина русских слов в два раза
#  #больше. Проверьте, заканчиваются ли русские слова на 'а'."""
print()
print('Задача 4')
planets_eng = ['Aldebaran', 'Sirius', 'Elektra', 'Altair', 'Aliot']
planets_rus = ['Альдебаран', 'Сириус', 'Электра', 'Альтаир', 'Алиот']

for word in range(len(planets_eng)):
    if len(planets_eng[word]) == 2 * len(planets_rus[word]):
        res = planets_eng[word]
        res2 = res[0:3]
        print(res2)
    else:
        print('В списке нет английских слов в 2 раза длинне русских')
# 1 вариант. Проверьте, заканчиваются ли русские слова на 'а'.
for i in planets_rus:
    if i[-1] == 'а':
        print(f'Слово {i} заканчивается на "а".')
# 2 вариант. Проверьте, заканчиваются ли русские слова на 'а'.
for i in planets_rus:
    print(i.endswith('а'))


