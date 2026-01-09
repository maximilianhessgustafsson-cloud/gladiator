import time
from turtle import Turtle, Screen

spel = True
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

boll_hastighet = 0.2
racket_hastighet = 0.5

score_a = 0
score_b = 0

pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

ping = Turtle()
ping.speed(0)
ping.shape("square")
ping.shapesize(stretch_wid=5, stretch_len=1)
ping.color("white")
ping.penup()
ping.setposition(350, 0)
ping.movement = 0

pong = Turtle()
pong.speed(0)
pong.shape("square")
pong.shapesize(stretch_wid=5, stretch_len=1)
pong.color("white")
pong.penup()
pong.setposition(-350, 0)
pong.movement = 0

pongboll = Turtle()
pongboll.speed(0)
pongboll.shape("circle")
pongboll.color("white")
pongboll.penup()
pongboll.dx = boll_hastighet
pongboll.dy = boll_hastighet

def ping_upp():
    ping.movement = racket_hastighet

def ping_ner():
    ping.movement = -racket_hastighet

def ping_stopp():
    ping.movement = 0

def pong_upp():
    pong.movement = racket_hastighet

def pong_ner():
    pong.movement = -racket_hastighet

def pong_stopp():
    pong.movement = 0

game_active = False

def starta_spelet():
    global game_active
    game_active = True

screen.listen()
screen.onkeypress(ping_upp, "Up")
screen.onkeyrelease(ping_stopp, "Up")
screen.onkeypress(ping_ner, "Down")
screen.onkeyrelease(ping_stopp, "Down")
screen.onkeypress(pong_upp, "w")
screen.onkeyrelease(pong_stopp, "w")
screen.onkeypress(pong_ner, "s")
screen.onkeyrelease(pong_stopp, "s")
screen.onkeypress(starta_spelet, "Return")

pen.goto(0, 0)
pen.write("Tryck ENTER för att starta", align="center", font=("Courier", 30, "bold"))

while not game_active:
    screen.update()
    time.sleep(0.05)

pen.clear()
pen.goto(0, 50)

for i in range(3, 0, -1):
    pen.write(str(i), align="center", font=("Courier", 80, "bold"))
    screen.update()
    time.sleep(1)
    pen.clear()

pen.write("KÖR!", align="center", font=("Courier", 80, "bold"))
screen.update()
time.sleep(0.5)
pen.clear()

pen.goto(0, 260)
pen.write("0  0", align="center", font=("Courier", 24, "normal"))

while spel:
    screen.update()

    ping.sety(ping.ycor() + ping.movement)
    if ping.ycor() > 250:
        ping.sety(250)
    if ping.ycor() < -240:
        ping.sety(-240)

    pong.sety(pong.ycor() + pong.movement)
    if pong.ycor() > 250:
        pong.sety(250)
    if pong.ycor() < -240:
        pong.sety(-240)

    pongboll.setx(pongboll.xcor() + pongboll.dx)
    pongboll.sety(pongboll.ycor() + pongboll.dy)

    if pongboll.ycor() > 290:
        pongboll.sety(290)
        pongboll.dy = -boll_hastighet

    if pongboll.ycor() < -290:
        pongboll.sety(-290)
        pongboll.dy = boll_hastighet

    if pongboll.xcor() > 390:
        pongboll.goto(0, 0)
        ping.goto(350, 0)
        pong.goto(-350, 0)
        pongboll.dx = -boll_hastighet
        score_a += 1
        pen.clear()
        pen.write("{}  {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        screen.update()
        time.sleep(1)

    if pongboll.xcor() < -390:
        pongboll.goto(0, 0)
        ping.goto(350, 0)
        pong.goto(-350, 0)
        pongboll.dx = boll_hastighet
        score_b += 1
        pen.clear()
        pen.write("{}  {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        screen.update()
        time.sleep(1)

    if (pongboll.xcor() > 340 and pongboll.xcor() < 350) and (pongboll.ycor() < ping.ycor() + 50 and pongboll.ycor() > ping.ycor() - 50):
        pongboll.setx(340)
        pongboll.dx = -boll_hastighet

    if (pongboll.xcor() < -340 and pongboll.xcor() > -350) and (pongboll.ycor() < pong.ycor() + 50 and pongboll.ycor() > pong.ycor() - 50):
        pongboll.setx(-340)
        pongboll.dx = boll_hastighet

screen.exitonclick()