"""
Uloha:  Vytvorte program, ktory pomocou turtle graphics vykresli stvorec, obdlznik, trojuholnik a kruh/kruznicu
"""

# importovanie potrebnych modulov
import turtle
import random


def shape_color():
    """
    Nastavenie farby na kreslenie
    """

    turtle.colormode(255)
    turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def change_position():
    """
    Nastavenie pozicie
    """

    turtle.penup()
    turtle.lt(random.randint(0, 360))
    turtle.fd(random.randint(1, 20) * random.randint(1, 20))
    turtle.pendown()


def square():
    """
    Vykreslenie stvorca
    """

    sq_length = random.randint(1, 15) * random.randint(1, 15)
    shape_color()
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(sq_length)
        turtle.rt(90)
    turtle.end_fill()


def rectangle():
    """
    Vykreslenie obdlznika
    """

    re_length = random.randint(1, 15) * random.randint(1, 15)
    re_width = random.randint(1, 15) * random.randint(1, 15)
    shape_color()
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(re_length)
        turtle.rt(90)
        turtle.fd(re_width)
        turtle.rt(90)
    turtle.end_fill()


def triangle():
    """
    Vykreslenie trouholnika
    """

    rand_num = random.randint(1, 15) * random.randint(1, 15)
    shape_color()
    turtle.begin_fill()
    for i in range(3):
        turtle.fd(rand_num)
        turtle.rt(180 - 180 / 3)
    turtle.end_fill()


def circle():
    """
    Vykreslenie kruhu/kruznice
    :return:
    """
    rand_num = random.randint(1, 10) * random.randint(1, 10)
    shape_color()
    turtle.begin_fill()
    turtle.circle(rand_num)
    turtle.end_fill()


j = 0
while True:
    # vykreslenie jednotlivych utvarov
    change_position()
    square()
    change_position()
    circle()
    change_position()
    triangle()
    change_position()
    rectangle()
    turtle.penup()
    turtle.goto(0, 0)

    # kedze sa v tomto pripade jedna o nekonecny cyklus, tak po 50 opakovani sa zresetuje vykreslovacia plocha
    if j == 50:
        turtle.reset()
        j = -1
    j += 1

