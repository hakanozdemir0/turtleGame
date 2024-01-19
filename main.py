import random
import turtle
from random import randint
from time import *

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("KAPLUMBAĞA")
FONT = ("Arial", 20, "bold")
liste = []
puan = 0
gameOver = False

#score
score = turtle.Turtle()

gerisayim_turtle = turtle.Turtle()





def yukleme():
    score.hideturtle()
    score.penup()
    yukseklik = screen.window_height()
    yukse = yukseklik * 0.45
    score.color("black")
    score.setpos(0, yukse)
    yukseklik = screen.window_height()

    score.write(arg="Score: 0", move=False, align="center", font=FONT)

grid_size = 5
def kaplumbaga(x, y):
    k = turtle.Turtle()
    def tiklama(x,y):
        global puan
        puan += 1
        score.clear()

        score.write(arg="Score:{}".format(puan), move=False,align="center", font=FONT)

    k.onclick(tiklama)
    k.penup()
    k.shape("turtle")
    k.shapesize(1.7, 1.7)

    k.goto((x * grid_size), (y * grid_size))
    # RANDOM KAPLUMBAGA İSTENİRSE
    # k.goto(randint(-350,400), randint(-400,350))
    liste.append(k)
# kaplumbaga(0,0)

def kordinat():
    y = 20
    x = -20
    for i in range(4):
        kaplumbaga(x, y)
        y = y - 10
    y = 20
    x = -10
    for i in range(4):
        kaplumbaga(x, y)
        y = y - 10
    y = 20
    x = 0
    for i in range(4):
        kaplumbaga(x, y)
        y = y - 10
    y = 20
    x = 10
    for i in range(4):
        kaplumbaga(x, y)
        y = y - 10
    y = 20
    x = 20
    for i in range(4):
        kaplumbaga(x, y)
        y = y - 10

def gizle():
    for k in liste:
        k.hideturtle()

def goster():
    if not gameOver:
        gizle()
        random.choice(liste).showturtle()
        screen.ontimer(goster, 500)

def gerisayim(time):
    global gameOver
    gerisayim_turtle.hideturtle()
    gerisayim_turtle.penup()
    yukseklik = screen.window_height()
    yukse = yukseklik * 0.40
    gerisayim_turtle.color("black")
    gerisayim_turtle.setpos(0, yukse)
    yukseklik = screen.window_height()
    gerisayim_turtle.clear()

    if time > 0:
        gerisayim_turtle.clear()
        gerisayim_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda : gerisayim(time - 1 ), 1000)
    else:
        gameOver = True
        gerisayim_turtle.clear()
        gizle()
        gerisayim_turtle.write(arg="GAME OVER !", move=False, align="center", font=FONT)

def oyun_baslat():
    turtle.tracer(0)
    kordinat()
    yukleme()
    gizle()
    goster()
    gerisayim(10)
    turtle.tracer(1)

oyun_baslat()
turtle.mainloop()

