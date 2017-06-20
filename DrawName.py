import turtle

def draw_name():

    window = turtle.Screen()
    window.bgcolor("purple")

    alec = turtle.Turtle()
    alec.shape("turtle")
    alec.speed(3)
    alec.pu()
    alec.setpos(-600.00,0.00)

    alec.pd()
    alec.left(75)
    alec.forward(300)
    alec.right(150)
    alec.forward(300)
    alec.left(180)
    alec.forward(150)
    alec.left(75)
    alec.forward(80)

    alec.pu()
    alec.setpos(-250.00,0.00)
    alec.pd()
    alec.forward(150)
    alec.right(90)
    alec.forward(275)

    alec.pu()
    alec.setpos(-50.00,0.00)
    alec.pd()
    alec.left(90)
    alec.forward(150)
    alec.right(90)
    alec.forward(135)
    alec.right(90)
    alec.forward(75)
    alec.pu()
    alec.left(180)
    alec.forward(75)
    alec.pd()
    alec.right(90)
    alec.forward(140)
    alec.right(90)
    alec.forward(150)

    alec.pu()
    alec.setpos(150.00,0.00)
    alec.pd()
    alec.left(180)
    alec.forward(150)
    alec.right(90)
    alec.forward(275)
    alec.right(90)
    alec.forward(150)
    
    
    

    window.exitonclick()


draw_name()
