import turtle

sides=input("Enter the number of sides: ")
sides=int(sides)
length= int(input("Enter the number of sides: "))

pen=turtle.Turtle()
pen.color("blue")

window=turtle.Screen()

for s in range(sides):
    pen.forward(length)
    pen.right(360/sides)

window.exitonclick()
