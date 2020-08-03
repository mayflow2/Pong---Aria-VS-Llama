import turtle
import time
import winsound

# screen setup
win = turtle.Screen()
win.title("Pong - Aria VS Llama")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)
win.register_shape("llama.gif")
win.register_shape("aria.gif")

# declare scores
score_a = 0
score_l = 0

# aria
aria = turtle.Turtle()
aria.speed(0)
aria.shape("aria.gif")
aria.penup()
aria.goto(-350, 0)

# llama
llama = turtle.Turtle()
llama.speed(0)
llama.shape("llama.gif")
llama.penup()
llama.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.hideturtle()
ball.dx = .4
ball.dy = .4

# writing
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-350, 110)
pen.write("↑ w", align="center", font=("Courier", 24, "normal"))
pen.goto(-350, 75)
pen.write("↓ x", align="center", font=("Courier", 24, "normal"))
pen.goto(340, 110)
pen.write("↑ 9", align="center", font=("Courier", 24, "normal"))
pen.goto(340, 75)
pen.write("↓ 3", align="center", font=("Courier", 24, "normal"))

# countdown
count = turtle.Turtle()
count.speed(0)
count.color("white")
count.penup()
count.hideturtle()
count.goto(0, -100)

# bind keys
def aria_up():
    aria.sety(aria.ycor() + 20)
def aria_down():
    aria.sety(aria.ycor() - 20)

def llama_up():
    llama.sety(llama.ycor() + 20)
def llama_down():
    llama.sety(llama.ycor() - 20)

win.listen()
win.onkeypress(aria_up,'w')
win.onkeypress(aria_down, 'x')
win.onkeypress(llama_up,'9')
win.onkeypress(llama_down, '3')

# countdown in action
for i in range(5, 0, -1):
    count.write(i, align="center", font=("Courier", 120, "bold"))
    win.update()
    time.sleep(1)
    count.clear()

ball.showturtle()
pen.clear()
pen.goto(0, 260)
pen.write("Aria: 0  Llama: 0", align="center", font=("Courier", 24, "normal"))

def move():
    global score_a
    global score_l

    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Aria: {}  Llama: {}".format(score_a, score_l), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        win.update()
        time.sleep(1)

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_l += 1
        pen.clear()
        pen.write("Aria: {}  Llama: {}".format(score_a, score_l), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        win.update()
        time.sleep(1)

    elif ball.xcor() > 315 and ball.xcor() < 345 and ball.ycor() < llama.ycor() + 48 and ball.ycor() > llama.ycor() - 48 and ball.dx > 0:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.xcor() < -320 and ball.xcor() > -350 and ball.ycor() < aria.ycor() + 48 and ball.ycor() > aria.ycor() - 48 and ball.dx < 0:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

while (score_a + score_l) < 5:
    move() 

ball.hideturtle()
pen.goto(100, 0)
pen.color("cyan")
pen.write("WINS!!!", align="center", font=("Courier", 60, "bold"))
if score_a > score_l:
    llama.hideturtle()
    aria.goto(-200, 60)
else:
    aria.hideturtle()
    llama.goto(-200, 60)
win.update()

win.mainloop()       
