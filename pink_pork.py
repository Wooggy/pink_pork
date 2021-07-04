import turtle
from random import choice, randint

# main setup
window = turtle.Screen()
window.title('Pink Pork')
window.setup(width=1.0, height=1.0)
window.bgcolor('black')
# window.tracer(2)


class Rocket:
    def __init__(self):
        self.rocket = turtle.Turtle()

    def set_rocket(self, color, height=5, width=1, direction=(0, 0)):
        self.rocket.color(color)
        self.rocket.shape('square')
        self.rocket.shapesize(stretch_len=width, stretch_wid=height)
        self.rocket.penup()
        self.rocket.goto(direction)

    def move_logic(self, key_up, key_down):

        def move_up():
            y = self.rocket.ycor() + 10
            if y > 250:
                y = 250
            self.rocket.sety(y)

        def move_down():
            y = self.rocket.ycor() - 10
            if y < - 250:
                y = -250
            self.rocket.sety(y)

        window.listen()
        window.onkeypress(move_up, key_up)
        window.onkeypress(move_down, key_down)


def table(table_color='pink', border_color='#6b156b'):
    border = turtle.Turtle()
    border.speed(0)
    border.color(table_color)
    border.begin_fill()
    border.goto(-500, 300)
    border.goto(500, 300)
    border.goto(500, -300)
    border.goto(-500, -300)
    border.goto(-500, 300)
    border.end_fill()

    # central border
    border.goto(0, 300)
    border.color(border_color)
    border.setheading(270)
    for i in range(25):
        if i % 2 == 0:
            border.forward(24)
        else:
            border.up()
            border.forward(24)
            border.down()
    border.hideturtle()


def pork_ball():
    # points
    FONT = ("Arial", 44)
    left_points, right_points = 0, 0

    points_1 = turtle.Turtle(visible=False)
    points_1.color('white')
    points_1.penup()
    points_1.setposition(-200, 300)
    points_1.write(arg=left_points, font=FONT)

    points_2 = turtle.Turtle(visible=False)
    points_2.color('white')
    points_2.penup()
    points_2.setposition(200, 300)
    points_2.write(arg=left_points, font=FONT)

    # ball
    window.addshape('pig_head.gif')
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape('pig_head.gif')
    ball.dx = 3
    ball.dy = -3
    ball.penup()

    # ball logic
    while True:
        window.update()

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() >= 290:
            ball.dy = -ball.dy

        if ball.ycor() <= -290:
            ball.dy = -ball.dy

        if ball.xcor() >= 490:
            right_points += 1
            points_2.clear()
            points_2.write(right_points, font=FONT)
            ball.goto(0, randint(-150, 150))
            ball.dx = choice([-4, -3, -2, 2, 3, 4])
            ball.dy = choice([-4, -3, -2, 2, 3, 4])

        if ball.xcor() <= -490:
            left_points += 1
            points_1.clear()
            points_1.write(left_points, font=FONT)
            ball.goto(0, randint(-150, 150))
            ball.dx = choice([-4, -3, -2, 2, 3, 4])
            ball.dy = choice([-4, -3, -2, 2, 3, 4])

        if left_rocket.rocket.ycor() - 50 <= ball.ycor() <= left_rocket.rocket.ycor() + 50 \
                and left_rocket.rocket.xcor() - 5 <= ball.xcor() <= left_rocket.rocket.xcor() + 5:
            ball.dx = -ball.dx

        if right_rocket.rocket.ycor() - 50 <= ball.ycor() <= right_rocket.rocket.ycor() + 50 \
                and right_rocket.rocket.xcor() - 5 <= ball.xcor() <= right_rocket.rocket.xcor() + 5:
            ball.dx = -ball.dx


table()

left_rocket = Rocket()
left_rocket.set_rocket(color='#800080', direction=(-450, 0))
left_rocket.move_logic('w', 's')
right_rocket = Rocket()
right_rocket.set_rocket(color='#800080', direction=(450, 0))
right_rocket.move_logic('Up', 'Down')

pork_ball()

window.mainloop()
