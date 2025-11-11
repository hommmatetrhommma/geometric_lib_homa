def area(a, h): 
    '''Принимает два значения a и h, возвращает произведение a на h деленное на 2'''
    if a < 0 or h < 0:
        raise ValueError("Основание и высота не могут быть отрицательными")
    return a * h / 2 

def perimeter(a, b, c): 
    '''Принимает три значения a и b и c, возвращает сумму a,b и c'''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a + b + c 