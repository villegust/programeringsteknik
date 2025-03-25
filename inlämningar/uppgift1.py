import turtle
import random

#Globala variabler
L = 100
l = L/2
offset_L = L/4

#Lista på olika färger (Kan lägga till mer om man vill)
lst_colours = ['blue','green','red','yellow','black','purple','orange']

def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def make_turtle(x, y):
    t = turtle.Turtle()
    t.speed(0)
    jump(t, x, y)
    return t

#Funktionen till kvadraten.
def square(x0, y0, length, color):
    t= make_turtle(x0, y0)
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()

    for dist in [length, length, length, length]:
        t.forward(dist)
        t.left(90)

    t.end_fill()

#Den stora kvadraten
square(0, 0, L,color="")

#Ett offset på vart de små trianglarna ska placeras
corner_offset = [(-offset_L, -offset_L), (L - offset_L, -offset_L), (-offset_L, L - offset_L), (L - offset_L, L - offset_L)]

for x, y in corner_offset:
    #Slumpar en färg
    r_color = random.choice(lst_colours)
    #Tar bort den slumpade färgen ur listan av färger så att den inte kan väljas igen.
    lst_colours.remove(r_color)

    square(x, y, l, color=r_color)

turtle.done()