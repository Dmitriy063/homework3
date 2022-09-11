# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def SumEven(list):
    s = 0
    for i in range(len(list)):
        if (i > 0) and (i % 2) == 0:
            s = s+int(list[i])
    i += 2
    print(s)


mylist = []
mylist = input('input numbers: ').split()
print(mylist)
SumEven(mylist)
