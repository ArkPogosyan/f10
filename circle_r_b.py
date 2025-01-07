from math import pi


# объявление функции
def get_circle(radius):
    lenght = 2*pi*r
    square = pi*(r**2)
    return lenght, square


# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)