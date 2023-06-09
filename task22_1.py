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
# пример 2

n = (int(input("Введите число N: ")))
list_1=[]
for i in range(n):
    element = int(input("Введите элементы списка : "))
    list_1.append(element)

m = (int(input("Введите число M : ")))
list_2 = []
for i in range(m):
    element = int(input("Введите элементы списка: "))
    list_2.append(element)

print(list_1)
print(list_2)

setInList_1 = set(list_1)    # переводим списки в множества, значения будут уникальны
setInList_2 = set(list_2)                       
set.intersection_update(setInList_1, setInList_2)    # пересечение множеств
print(setInList_1)    # выводим значения из списка 1, которые встречаются и в списке 2