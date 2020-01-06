# day3.py
import math

age = 32
height = 1.6    # meters
complex = 1 + 1j

# b = float(input('Enter base: '))
# h = float(input('Enter heigh: '))
# area = 0.5 * b * h
# print('The area of the triangle is ', area)

# a = float(input('Enter side a: '))
# b = float(input('Enter side b: '))
# c = float(input('Enter side c: '))
# perimeter = a + b + c
# print('The perimeter of the triangle is ', perimeter)

# length = float(input('Enter length: '))
# width = float(input('Enter width: '))
# area = length * width
# perimeter = 2 * (length + width)
# print('The area of the rectangle is ', area)
# print('The perimeter of the rectangle is ', perimeter)

# PI = 3.14
# r = float(input('Enter radius: '))
# area = PI * r ** 2
# c = 2 * PI * r
# print('The area of the circle is ', area)
# print('The circumference of the circle is ', c)


# def y(x):
#     return 2 * x - 2
#
# def x(y):
#     return (y - 2) / 2
#
# def m(x1, y1, x2, y2):
#     return (y2 - y1) / (x2 - x1)
# x1 = 1
# y1 = y(x1)
# x2 = 2
# y2 = y(x2)
# m1 = m(x1, y1, x2, y2)
#
# print(m1)
# print(y(0))
# print(x(0))
#
# x1 = 2
# y1 = 2
# x2 = 6
# y2 = 10
# m2 = m(x1, y1, x2, y2)
# print(m2)
# print(m1 > m2)

def y(x):
    return x ** 2 + 6 * x + 9

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return [x1,x2]

print(quadratic(1, 6, 9))
print(y(-3))

python_length = len('python')
jargon_length = len('jargon')
print(python_length > jargon_length)

if('on' in 'python' and 'on' in 'jargon'):
    print('on is in both python and jargon')

print('jargon' in 'I hope this course is not full of jargon')

print('on' in ('dragon' and 'python'))

print(str(float(len('python'))))

def even(x):
    return x % 2 == 0

print(even(11))
print(even(10))

print(int(7/3))

print(type('10') == type(10))

print(int(float('9.8')) == 10)

# hours = int(input('Enter hours: '))
# rate = int(input('Enter rate per hour: '))
# print('Your weekly earning is', hours * rate)

# years = int(input('Enter the number of years you live: '))
# print('You lived', 365 * 24 * 60 * 60 * years, 'seconds')

def third_power(x):
    return (str(x) + ' ' + '1 ' + str(x) + ' ' + str(x ** 2) + ' ' + str(x ** 3))

print(third_power(1))
print(third_power(2))
print(third_power(3))
print(third_power(4))
print(third_power(5))
