import turtle

# Function to draw a rectangle
def draw_rectangle(x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Function to fill the rectangle with red color when clicked
def fill_rectangle(x, y):
    draw_rectangle(x - 50, y - 25, 100, 50)  # Adjust the coordinates to center the rectangle
    turtle.fillcolor("red")

# Set up the screen
turtle.setup(800, 600)
turtle.title("Drag to Draw Rectangle")
turtle.bgcolor("lightblue")

# Register the fill_rectangle function to be called when the screen is clicked
turtle.onscreenclick(fill_rectangle)

# Hide the turtle and keep the window open
turtle.hideturtle()
turtle.mainloop()
