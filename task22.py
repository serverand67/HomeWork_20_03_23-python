"""
Задача 22: Даны два неупорядоченных набора целых чисел 
(может быть, с повторениями). Выдать без повторений в 
порядке возрастания все те числа, которые встречаются 
в обоих наборах.
Пользователь вводит 2 числа. 
n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
Пример:
ввод 11 6 2 4 6 8 10 12 10 8 6 4 2
ввод 3 6 9 12 15 18
вывод 6 12
"""
# пример 1

n = (int(input("Введите число N: ")))  # количество значений в 1 списке
list_1=[]
for i in range(n):
    element = int(input("Введите элементы списка : "))  # заполняем список
    list_1.append(element)

m = (int(input("Введите число M : ")))  # количество значений в 2 списке
list_2 = []
for i in range(m):
    element = int(input("Введите элементы списка: "))  # заполняем список 
    list_2.append(element)

print(list_1)             # воводим списки
print(list_2)
list_3 = list_1 + list_2      # объеденяем списки в один

for i in set(list_3):           # перебираем элементы в списке       
    if list_3.count(i) > 1:     # и если число повторяется больше 1 раза,       
        print(i, end=" ")       # выводим его 