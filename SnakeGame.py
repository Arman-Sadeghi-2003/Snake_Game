import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
wrap_mode = False  # Change to True if you want wrap-around walls

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game 🐍 - Upgraded Edition")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Normal food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Special golden food
gold_food = turtle.Turtle()
gold_food.speed(0)
gold_food.shape("circle")
gold_food.color("gold")
gold_food.penup()
gold_food.hideturtle()
gold_timer = 0

segments = []

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
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

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Border collision
    if not wrap_mode:
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
    else:
        if head.xcor() > 290:
            head.setx(-290)
        elif head.xcor() < -290:
            head.setx(290)
        elif head.ycor() > 290:
            head.sety(-290)
        elif head.ycor() < -290:
            head.sety(290)

    # Normal food collision
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score

        # Speed up slightly
        delay = max(0.05, delay - 0.002)

        # Chance to spawn golden food
        if random.randint(1, 5) == 3 and not gold_food.isvisible():
            gx = random.randint(-290, 290)
            gy = random.randint(-290, 290)
            gold_food.goto(gx, gy)
            gold_food.showturtle()
            gold_timer = 50  # frames until it disappears

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Golden food collision
    if gold_food.isvisible() and head.distance(gold_food) < 20:
        gold_food.hideturtle()
        score += 50
        if score > high_score:
            high_score = score
        delay = max(0.05, delay - 0.005)
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Golden food timer
    if gold_food.isvisible():
        gold_timer -= 1
        if gold_timer <= 0:
            gold_food.hideturtle()

    # Move segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
