#! /usr/bin/python3
n = int(input('Введите число: '))
summ = 0
for i in range(1, n +1):
    summ = summ + ((i +1) / i)
print('Сумма: ', summ)