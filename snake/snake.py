#Dev by Pyrrox
#Simple snake Game in Python 3 with Turtle

import turtle
import time
import random
delay = 0.1
speed = 20

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

#Food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Functions
def move():
        if headsnake.direction == "up":
            y = headsnake.ycor()
            headsnake.sety(y+speed)

        if headsnake.direction == "down":
            y = headsnake.ycor()
            headsnake.sety(y-speed)

        if headsnake.direction == "left":
            x = headsnake.xcor()
            headsnake.setx(x-speed)

        if headsnake.direction == "right":
            x = headsnake.xcor()
            headsnake.setx(x+speed)

def go_up():
    if headsnake.direction != "down":
        headsnake.direction ="up"
def go_down():
    if headsnake.direction != "up":
        headsnake.direction ="down"
def go_left():
    if headsnake.direction != "right":
        headsnake.direction ="left"
def go_right():
    if headsnake.direction != "left":
        headsnake.direction ="right"

#Keyboard action
wn.listen()
wn.onkeypress(go_up,"z")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"q")
wn.onkeypress(go_right,"d")
while True:
    wn.update()

    #check collision border

    if headsnake.xcor() > 290 or headsnake.xcor() < -290 or  headsnake.ycor() > 290 or headsnake.ycor() < -290 :
        time.sleep(1)
        headsnake.goto(0,0)
        headsnake.direction="stop"

        #Hide the segments
        for segment in segments :
            segment.goto(1000,1000)

        #clear segment list
        segments.clear()

    #check for collision with food
    if headsnake.distance(food)< 20:
        #Move the food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add segment 
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    #Move the end segments first in revers order
    for index in range(len(segments)-1,0,-1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x,y)
    #Move segments 0 to head pos
    if len(segments)> 0:
        x = headsnake.xcor()
        y = headsnake.ycor()
        segments[0].goto(x,y)
    move()

    #check body collision
    for segment in segments :
        if segment.distance(headsnake) < 20:
            time.sleep(1)
            headsnake.goto(0,0)
            headsnake.direction = "stop"
            #Hide the segments
            for segment in segments :
                segment.goto(1000,1000)

            #clear segment list
            segments.clear()

    time.sleep(delay)


wn.mainloop()