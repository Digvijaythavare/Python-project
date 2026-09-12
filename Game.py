import turtle
import time
import random

# Screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

# Snake body
body = []

# Score
score = 0
high_score = 0

pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0",
          align="center",
          font=("Arial", 18, "bold"))


# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)


# Keyboard controls
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")


# Game loop
while True:
    screen.update()

    # Check wall collision
    if (head.xcor() > 290 or head.xcor() < -290 or
            head.ycor() > 290 or head.ycor() < -290):

        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide body
        for segment in body:
            segment.goto(1000, 1000)

        body.clear()

        score = 0

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center",
                  font=("Arial", 18, "bold"))

    # Check food collision
    if head.distance(food) < 20:

        # Move food
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        # Add body segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()

        body.append(new_segment)

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center",
                  font=("Arial", 18, "bold"))

    # Move body from last to first
    for i in range(len(body) - 1, 0, -1):
        body[i].goto(body[i - 1].xcor(),
                     body[i - 1].ycor())

    if len(body) > 0:
        body[0].goto(head.xcor(), head.ycor())

    move()

    # Check body collision
    for segment in body:
        if segment.distance(head) < 20:
            time.sleep(1)

            head.goto(0, 0)
            head.direction = "stop"

            for segment in body:
                segment.goto(1000, 1000)

            body.clear()
            score = 0

            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}",
                      align="center",
                      font=("Arial", 18, "bold"))

    time.sleep(0.1)

screen.mainloop()