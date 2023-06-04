"""
Uloha:  Vytvorte program, ktory pomocou turtle graphics vykresli jednoduchy domcek zlozeny z geometrickych utvarov
        stvorec, obdlznik, trojuholnik (rovnostranny) a kruh/kruznica
"""

# import potrebnych modulov
import turtle
import random


def rectangle(a, b, color):
    """
    Vykreslenie obdlznika

    :param a: dlzka obdlznika
    :param b: sirka obdlznika
    :param color: farba obdlznika
    """

    turtle.color(color)
    turtle.begin_fill()

    for _ in range(0, 2):
        turtle.fd(a)
        turtle.lt(90)
        turtle.fd(b)
        turtle.lt(90)

    turtle.end_fill()


def square(a, color):
    """
    Vykreslenie stvorca

    :param a: dlzka strany stvorca
    :param color: farba stvorca
    """

    rectangle(a, a, color)


def triangle(a, color):
    """
    Vykreslenie trojuholnika

    :param a: dlzka strany trojuholnika
    :param color: farba trojuholnika
    """

    turtle.color(color)
    turtle.begin_fill()

    turtle.lt(60)
    turtle.fd(a)
    turtle.rt(120)
    turtle.fd(a)
    turtle.lt(60)
    turtle.bk(a)

    turtle.end_fill()


def circle(r, color):
    """
    Vykreslenie kruhu/kruznice

    :param r: polomer kruhu/kruznice
    :param color: farba kruhu/kruznice
    """

    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def to_position(x, y):
    """
    Presun na danu poziciu

    :param x: x-ova suradnica
    :param y: y-ova suradnica
    """

    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()


for _ in range(0, 100):
    # definovanie zaciatocnej pozicie
    begin_x = random.randint(-300, 300)
    begin_y = random.randint(-300, 300)

    # definovanie potrebnych premennych
    house_width = random.randint(0, 150)
    house_height = random.randint(0, 150)
    door_width = 0.3 * house_width
    door_height = 0.4 * house_height
    window_width = 0.25 * house_width
    window_x_offset = 0.15 * house_width
    window_y_offset = house_height - 0.4 * house_height
    round_window_y_offset = 0.15 * house_width
    round_window_radius = 0.15 * house_width

    # presunutie na danu poziciu
    to_position(begin_x, begin_y)

    # vykreslenie zakladu domu a strechy
    rectangle(house_width, house_height, "yellow")
    to_position(begin_x, house_height + begin_y)
    triangle(house_width, "red")

    # vykreslenie dveri
    to_position(house_width / 2 - door_width / 2 + begin_x, begin_y)
    rectangle(door_width, door_height, "brown")

    # vykreslenie okien
    to_position(window_x_offset + begin_x, window_y_offset + begin_y)
    square(window_width, "blue")
    to_position(house_width - window_x_offset - window_width + begin_x, window_y_offset + begin_y)
    square(window_width, "blue")
    to_position(house_width / 2 + begin_x, house_height + round_window_y_offset + begin_y)
    circle(round_window_radius, "blue")
    to_position(begin_x, begin_y)

turtle.done()
