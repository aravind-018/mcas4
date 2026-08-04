import turtle

# Screen setup
screen = turtle.Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.title("Recamán Sequence - Green & White")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Only Green and White
colors = ["green", "white"]

visited = {0}
current = 0
scale = 5

# Start from the left side
left_edge = -screen.window_width() // 2 + 40

for n in range(1, 120):

    # Generate Recamán sequence
    next_num = current - n

    if next_num < 0 or next_num in visited:
        next_num = current + n

    visited.add(next_num)

    # Circle radius
    radius = abs(next_num - current) * scale / 2

    # Circle center
    center_x = left_edge + ((current + next_num) / 2) * scale

    # Draw full circle
    t.penup()
    t.goto(center_x, -radius)
    t.setheading(0)
    t.pendown()

    t.pencolor(colors[n % 2])
    t.circle(radius)

    current = next_num

turtle.done()