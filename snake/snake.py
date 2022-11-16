#Dev by Pyrrox
#Simple snake Game in Python 3 with Turtle

import turtle
import time

delay = 0.1
#set up a windows

wn = turtle.Screen()
wn.title("snake game by Pyrrox")
wn.bgcolor("blue")
wn.setup(width = 600 , height = 600)
wn.tracer(0) #turns off the screens refresh

#snake head
headsnake = turtle.Turtle()
headsnake.speed(0)
headsnake.shape("circle")
headsnake.color("white")
headsnake.penup()
headsnake.goto(0,0)
headsnake.direction = "stop"

#Functions
def move():
        if headsnake.direction == "up":
            y = headsnake.ycor()
            headsnake.sety(y+10)

        if headsnake.direction == "down":
            y = headsnake.ycor()
            headsnake.sety(y-10)

        if headsnake.direction == "left":
            x = headsnake.xcor()
            headsnake.setx(x-10)

        if headsnake.direction == "right":
            x = headsnake.xcor()
            headsnake.setx(x+10)

def go_up():
    headsnake.direction ="up"
def go_down():
    headsnake.direction ="down"
def go_left():
    headsnake.direction ="left"
def go_right():
    headsnake.direction ="right"


wn.listen()
wn.onkeypress(go_up,"z")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"q")
wn.onkeypress(go_right,"d")
while True:
    wn.update()

    move()
    time.sleep(delay)


wn.mainloop()