import turtle

def curve():
    turtle.speed(50)

    for i in range(200):        
        turtle.right(1)
        turtle.forward(1)

def main():
    turtle.bgcolor('Thistle')
    turtle.pensize(2)
    turtle.speed(2)
    turtle.color('deep pink', 'deep pink')

    turtle.begin_fill()
    turtle.speed()
    turtle.left(140)
    turtle.forward(111.65)
    curve()

    turtle.left(120)
    curve()
    turtle.forward(111.65)
    
    turtle.speed(120)
    turtle.end_fill()
    turtle.hideturtle()
    
    turtle.penup()
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('Thistle')
    turtle.setposition(20,-50)
    
    turtle.color('deep pink')
    turtle.write("Para meu amor Emilly", move=True, align='center', font=('Courier',30,'italic'))
    turtle.color('Thistle')
    turtle.end_fill()
    turtle.hideturtle()

if __name__ == "__main__":
    main()
    turtle.mainloop()