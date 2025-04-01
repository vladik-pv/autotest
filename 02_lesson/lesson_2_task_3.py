
import math


def square(side):
    area = side * side
    return math.ceil(area)


side_length = float(input("Введите длину стороны квадрата: "))
area = square(side_length)
print(f"Площадь квадрата со стороной {side_length} равна {area}.")
