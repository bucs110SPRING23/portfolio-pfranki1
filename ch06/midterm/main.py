import turtle

"""Function Implementation: drawing each ring, 
Arguments: color changes each time for the 5 different rings and the x and y cordinates are used to change the location of each circle as to create the olympic shape.  X and Y are also integers"""
def draw_ring(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(50)

turtle.setup(width=600, height=400)
turtle.title("Olympic Rings")

ring_colors = ["blue", "black", "red", "yellow", "green"]
ring_positions = [(-110, 0), (0, 0), (110, 0), (-55, -50), (55, -50)]

for i in range(len(ring_colors)):
    draw_ring(ring_colors[i], ring_positions[i][0], ring_positions[i][1])

turtle.hideturtle()
turtle.exitonclick()
