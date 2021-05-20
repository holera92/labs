import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    if b == 0:
        print("Нет корней")
    else:
        print("x = ", -c / b)
else:
    D = (b * b) - (4 * a * c)
    if D < 0:
        print("Нет корней")
    else:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print("Корни уравнения x1 = {0} и x2 = {1}".format(x1, x2))
