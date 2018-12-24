import turtle

#draw squares
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window=turtle.Screen()
    window.bgcolor("red")
    #create the turtle brad
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    #making 36 squares at an angle difference of 10
    for i in range(0,36):
        draw_square(brad)
        brad.right(10)
    #making 2nd pattern
    pulak=turtle.Turtle()
    pulak.setx(-300)
    pulak.sety(-225)
    pulak.shape("turtle")
    pulak.color("green")

    pulak.speed(2)
    for i in range(0,36):
        draw_square(pulak)
        pulak.right(10)

    #making 3rd pattern
    any=turtle.Turtle()
    any.setx(300)
    any.sety(-225)
    any.shape("turtle")
    any.color("blue")
    any.speed(2)

    for i in range(0,36):
        draw_square(any)
        any.right(10)
    window.exitonclick()

draw_art()
