import math


def area(r):
    '''Принимает значение r, возвращает произведение квадрата r на число пи'''
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r * r


def perimeter(r):
    '''Принимает значние r, возвращает произведение удвоенного r на число пи'''
    if r < 0:
        raise ValueError("Радиус не может быть отрицательной")
    return 2 * math.pi * r

