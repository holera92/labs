import math

SIDES = 1
COORDINATES = 2

def length(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


method = int(input("[1] - длины сторон треугольника; [2] - координаты вершин: "))
if method == SIDES:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    if a + b < c or b + c < a or c + a < b:
        print("Такого треугольника не существует")
    else:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Площадь треугольника = ", s)

elif method == COORDINATES:
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    x3, y3 = map(float, input().split())

    a = length(x1, y1, x2, y2)
    b = length(x2, y2, x3, y3)
    c = length(x3, y3, x1, y1)

    if a + b < c or b + c < a or c + a < b:
        print("Такого треугольника не существует")
    else:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("S треугольника = ", s)
else:
    pass
