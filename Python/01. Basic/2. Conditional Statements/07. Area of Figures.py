import math
from math import pi

type_of_figure = input()


def square(a):
    face_fig = a * a
    print(f"{face_fig:.3f}")


def rectangle(a, b):
    face_fig = a * b
    print(f"{face_fig:.3f}")


def circle(a):
    face_fig = math.pi * a * a
    print(f"{face_fig:.3f}")


def triangle(a, h):
    face_fig = (a * h) / 2
    print(f"{face_fig:.3f}")


if type_of_figure == "square":
    a = float(input())
    square(a)
if type_of_figure == "rectangle":
    a = float(input())
    b = float(input())
    rectangle(a, b)
if type_of_figure == "circle":
    a = float(input())
    circle(a)
if type_of_figure == "triangle":
    a = float(input())
    h = float(input())
    triangle(a, h)


