from turtle import Screen
from turtle import Turtle
import time
import winsound

class Player():
    def __init__(self, pic):
        self.tur = Turtle()
        self.score = 0

        self.tur.shape(pic)
        self.tur.speed(0)
        self.tur.penup()

    def incScore(self):
        self.score += 1

class Ball(Turtle):
    def __init__(self, dx, dy):
        self.tur = Turtle()
        self.dx = dx
        self.dy = dy

        self.tur.shape("circle")
        self.tur.color("white")
        self.tur.speed(0)
        self.tur.penup()
        self.tur.goto(0, 0)

class Writing(Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()

# define player moves
def aria_up():
    aria.tur.sety(aria.tur.ycor() + 20)
def aria_down():
    aria.tur.sety(aria.tur.ycor() - 20)

def llama_up():
    llama.tur.sety(llama.tur.ycor() + 20)
def llama_down():
    llama.tur.sety(llama.tur.ycor() - 20)

def getScreen(ariaPic, llamaPic):
    win = Screen()
    win.title("Pong - Aria VS Llama")
    win.bgcolor("black")
    win.setup(width=800, height=600)
    win.tracer(0)
    win.register_shape(ariaPic)
    win.register_shape(llamaPic)

    # bind keys with player moves
    win.listen()
    win.onkeypress(aria_up,'w')
    win.onkeypress(aria_down, 'x')
    win.onkeypress(llama_up,'9')
    win.onkeypress(llama_down, '3')

    return win

def main():
    # set up screen & players
    global aria
    global llama
    win = getScreen("aria.gif", "llama.gif")
    aria = Player("aria.gif")
    aria.tur.goto(-350, 0)
    llama = Player("llama.gif")
    llama.tur.goto(350, 0)

    # VS
    vs = Writing()
    vs.goto(0, -100)
    vs.write("VS", align="center", font=("Courier", 120, "bold"))
    win.update()
    time.sleep(2)
    vs.clear()

    # instructions
    info = Writing()
    info.goto(-350, 110)
    info.write("↑ w", align="center", font=("Courier", 24, "normal"))
    info.goto(-350, 75)
    info.write("↓ x", align="center", font=("Courier", 24, "normal"))
    info.goto(340, 110)
    info.write("↑ 9", align="center", font=("Courier", 24, "normal"))
    info.goto(340, 75)
    info.write("↓ 3", align="center", font=("Courier", 24, "normal"))

    # countdown
    count = Writing()
    count.goto(0, -100)
    for i in range(5, 0, -1):
        count.write(i, align="center", font=("Courier", 120, "bold"))
        win.update()
        time.sleep(1)
        count.clear()

    # set up ball & scoreboard
    info.clear()
    ball = Ball(.4, .4)
    scoreBd = Writing()
    scoreBd.goto(0, 260)
    scoreBd.write("Aria: 0  Llama: 0", align="center", font=("Courier", 24, "normal"))
    
    # game loop
    while(aria.score + llama.score) < 5:
        win.update()

        ball.tur.setx(ball.tur.xcor() + ball.dx)
        ball.tur.sety(ball.tur.ycor() + ball.dy)

        if ball.tur.ycor() > 290:
            ball.tur.sety(290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        elif ball.tur.ycor() < -290:
            ball.tur.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        elif ball.tur.xcor() > 390:
            ball.tur.goto(0, 0)
            ball.dx *= -1
            aria.incScore()
            scoreBd.clear()
            scoreBd.write("Aria: {}  Llama: {}".format(aria.score, llama.score), align="center", font=("Courier", 24, "normal"))
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            win.update()
            time.sleep(1)

        elif ball.tur.xcor() < -390:
            ball.tur.goto(0, 0)
            ball.dx *= -1
            llama.incScore()
            scoreBd.clear()
            scoreBd.write("Aria: {}  Llama: {}".format(aria.score, llama.score), align="center", font=("Courier", 24, "normal"))
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            win.update()
            time.sleep(1)

        elif ball.tur.xcor() > 315 and ball.tur.xcor() < 345 and ball.tur.ycor() < llama.tur.ycor() + 48 and ball.tur.ycor() > llama.tur.ycor() - 48 and ball.dx > 0:
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        elif ball.tur.xcor() < -320 and ball.tur.xcor() > -350 and ball.tur.ycor() < aria.tur.ycor() + 48 and ball.tur.ycor() > aria.tur.ycor() - 48 and ball.dx < 0:
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # announce winner
    ball.tur.hideturtle()
    info.goto(100, 0)
    info.color("cyan")
    info.write("WINS!!!", align="center", font=("Courier", 60, "bold"))
    if aria.score > llama.score:
        llama.tur.hideturtle()
        aria.tur.goto(-200, 60)
    else:
        aria.tur.hideturtle()
        llama.tur.goto(-200, 60)
    win.update()
    win.mainloop()

if __name__ == "__main__":
    main()
