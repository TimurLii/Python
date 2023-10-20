# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с
# помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


# s = " a a a b c a a d c d d".split()
# # s1 = s.replace(" ", "+").split()
# slow = {}
# for i in s:
#         if i not in slow:
#                 slow[i] = 1
#                 print(i, end="")
#         else:
#                 print(f"{i}_{slow[i]}", end=" ")
#                 slow[i] += 1
#
#         slow[i] = slow.get(i, 0) + 1

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# text = ("She sells sea shells on the sea shore The shells that she sells are sea shells Im sure."
#         "So fi she sells sea shells on the sea shore, Im sure that the shells are sea shore shells.").split()
# print(type(text))
# print(text)
# word = []
# for i in text:
#         if i not in word:
#                 word.append(i)
# print(len(word))
n = int(input(" Введите число"))
k = n.split()
max_number = 0
while n != 0:
        if max_number > n:
                max_number = n
print(max_number)
