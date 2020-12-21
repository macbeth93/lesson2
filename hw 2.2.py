# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


elements_quantity = input("Введите число элементов списка: \n>>>")
elements_quantity = int(elements_quantity)
i = 0
my_list = []
loop = 1
while i < elements_quantity:
    my_list.append(input("Введите новый элемент списка: \n>>>"))
    i += 1

for elem in range(int(len(my_list) / 2)):
    my_list[loop], my_list[loop + 1] = my_list[loop + 1], my_list[loop]
    loop += 2
print(my_list)
