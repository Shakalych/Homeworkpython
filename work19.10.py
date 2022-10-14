#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

a = int(input('Введите номер дня недели: '))
if a < 6:
    print('Этот день рабочий')
elif 5 < a < 8:
    print ('Этот день выходной')
else:
    print ('Неправильное число')

#2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)

#3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите значение x отличное от нуля: '))
y = int(input('Введите значение y отличное от нуля: '))
if x > 0 and y > 0:
    print(f'x = {x}, y = {y} -> ' 'Первая четверть')
elif x > 0 and y < 0:
    print(f'x = {x}, y = {y} -> ' 'Четвертая четверть')
elif x < 0 and y > 0:
    print(f'x = {x}, y = {y} -> ' 'Вторая четверть')
elif x < 0 and y < 0:
    print (f'x = {x}, y = {y} -> ' 'Третья четверть')
else:
    print(f'x = {x}, y = {y} -> ' 'Число должно быть не 0')

#4. Напишите программу, которая по заданному номеру четверти,
#показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input('Введите номер четверти от 1 до 4 - '))
if x==1:
    print('x(0;+et) and y(0;+et)')
elif x==2:
    print('x(-et;0) and y(0;+et)')
elif x==3:
    print('x(-et;0) and y(-et;0)')
elif x==4 :
    print('x(0;+et) and y(-et;0)')
else:
    print('Неправильное число')

#5. Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

x_coordinate_A = float(input('Введите координату точки А по оси Х: '))
y_coordinate_A = float(input('Введите координату точки А по оси Y: '))
x_coordinate_B = float(input('Введите координату точки B по оси Х: '))
y_coordinate_B = float(input('Введите координату точки B по оси Y: '))

distance = round(((x_coordinate_B - x_coordinate_A)**2 + (y_coordinate_B - y_coordinate_A)**2) ** (0.5), 2)
print(distance)