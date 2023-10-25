# def sum(x):
#     return x
#
#
# print(sum(5))
#
# sum1 = lambda x: x
# print(sum1(6))
#
# print((lambda x: x)(8))
#
# number = "12345"
# number = list(number)
# print(number)
#
# number = list(map(int, number))
# print(number)
#
# number = list(map(lambda number: number * 2, number))
# print(number)
#
# res = list(filter(lambda x: x % 4 == 0, number))
# print(res)

# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
# Пример ввода и вывода данных представлены на следующем слайде
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformation = list(map(lambda values: values, values))
print(transformation)
if values == transformation:
    print("ok")
else:
    print("fail")

# ////////////////////////
# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики,
# и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов,
# функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

values = [0, 2, 10, 6]


def same_by(characteristic, objects):
    # return len(objects) == len(list(filter(characteristic, objects)))
    return len(list(filter(characteristic, objects))) == 0
if same_by(lambda x: x % 2 , values):
    print('same')
else:
    print('different')
