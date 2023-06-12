# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
 
def indexes():
    print('Индексы элементов заданного диапазона:')
    for i in range(len(my_array)):
        if min_num <= my_array[i] <= max_num:
            print(i, end=' ')
    print("\n")

min_num = int(input('Введите минимальное число массива: ')) 
max_num = int(input('Введите максимальное число массива: ')) 
my_array = [randint(1, 10) for _ in range(20)]
print(f'\nИсходный массив:\n{my_array}\n')

indexes()
