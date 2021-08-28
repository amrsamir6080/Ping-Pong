import turtle

#window game
wind = turtle.Screen()
wind.title("ping pong")
wind.bgcolor("black")
wind.setup(width = 800 , height = 600)
wind.tracer(0)#stop the window from updating autmaticlly


#game tools
#paddle1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid=5 , stretch_len=1)
paddle1.penup()
paddle1.goto(-350 , 0)
#paddle2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=5 , stretch_len=1)
paddle2.penup()
paddle2.goto(350 , 0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0 , 0)
ball.dx = 0.1
ball.dy = 0.1
#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("green")
score.penup()
score.hideturtle()
score.goto(0 , 260)
score.write("player 1: 0 player 2: 0", align = "center" , font = ("arial" , 24, "normal"))
#Functions
#paddle height 100px
#paddle1 move
def paddle1_up():
    y = paddle1.ycor() #get the Y coordinate of baddle1
    y += 20 #increase y
    paddle1.sety(y) #set the new y

def paddle1_down():
    y = paddle1.ycor() #get the Y coordinate of baddle1
    y -= 20
    paddle1.sety(y)
#keybaord
wind.listen()
wind.onkeypress(paddle1_up , "w")#paddle1 up
wind.onkeypress(paddle1_down , "s")#paddle1 down
#paddle2 move
def paddle2_up():
    y = paddle2.ycor()#get the Y coordinate of baddle2
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()#get the Y coordinate of baddle2
    y -= 20
    paddle2.sety(y)
#keybaord
wind.listen()
wind.onkeypress(paddle2_up , "Up")#paddle2 up
wind.onkeypress(paddle2_down , "Down")#paddle2 down
#ball move


#game loop
while True:
    wind.update()

    #ball move
    ball.setx(ball.xcor() + ball.dx) #ball start at 0 and every time loo run  xaxis += 0.05
    ball.sety(ball.ycor() + ball.dy)#ball start at 0 and every time loo run  xaxis += 0.05

    #border check
    if ball.ycor() > 290 : #check if touch top border
        ball.sety(290) #set y +290
        ball.dy *= -1 #revers direction
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0 , 0) #return ball to center
        ball.dx *= -1
        score1 +=1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1 , score2), align = "center" , font = ("arial" , 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score2 +=1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1 , score2), align = "center" , font = ("arial" , 24, "normal"))

    #paddle collesion
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40) and (ball.ycor() > paddle2.ycor() - 40 ):
            ball.setx(340)
            ball.dx *= -1
    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 )and (ball.ycor() > paddle1.ycor() - 40 ):
            ball.setx(-340)
            ball.dx *= -1
