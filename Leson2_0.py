# Урок 1


# Задача 1

# Задача 2


# time = int(input('Введите время в секундах : '))
# sec = time % 60
# minute1 = time // 60
# minute = minute1 % 60
# hour = minute1 // 60
# print(f'{hour}:{minute}:{sec}')


# Задача 3

# n = int(input('Введите число: '))
# print(n+n**2+n**3)



# Задача 4


# number = int(input('Введите положительное целое число: '))
# a = 0
# b = 0
# c = 0
# if number < 0 :
#     print('Неверно')
#     number = int(input('Введите положительное целое число: '))
# while number > 100:
#     number = number - 100
#     a = a + 1
# while number > 10:
#     number = number -10
#     b = b + 1
# while number > 0:
#     number = number - 1
#     c = c + 1
# if a > b:
#     if a > c:
#         print(a)
#     elif b > c:
#         print(b)
#     else:
#         print(c)

# Задача 5


# revenue = int(input('Введите выручку компании '))
# cost = int(input('Введите издержки компании '))
# if revenue > cost:
#     print('Компания прибыльная')
#     profit = revenue - cost
#     rent = profit / revenue
#     print('Рентабельность ',rent)
# else:
#     print('Компания убыточна')
#     exit()
#
#
# personal = int(input('Введите количество персонала '))
# print('зарплата ',profit/personal )


# Задача 6


# a = int(input('Введите количество километров в 1 день '))
# b = int(input('Введите количество достигнутого результата '))
# days = 1
# while a < b:
#     i = a/100
#     a = a + i*10
#     days = days+1
# print('на',days,'день,был достигнут результат не менее',b,'км')