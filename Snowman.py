import turtle

#Creating a screen
screen = turtle.Screen()
screen.title('SnowMan')
screen.bgcolor('black')

#Creating & Positioning the turtle
t = turtle.Turtle()
t.penup()
t.goto(0,-200)
t.speed(0)
t.color('white')
t.hideturtle()

#Variables for radius & distance
r = 100
d = 200

#For loop to draw body of Snowman
for i in range(0,3):
    t.pendown()
    t.fillcolor('white')
    t.circle(r)
    t.left(90)
    t.penup()
    t.forward(d)
    t.right(90)
    r -= 30
    d -= 60

#Creating the eyes
t.goto(-20,185)
t.pensize(5)
t.pendown()
t.forward(0)
t.penup()
t.goto(20,185)
t.pendown()
t.forward(0)

#Getting in position to create a smile
t.penup()
t.right(90)
t.forward(15)
t.pensize(1)
t.pendown()

#Creating a smile
for i in range(60):
    t.forward(1)
    t.right(3)

#Creating a nose
t.color('orange')
t.penup()
t.right(60)
t.forward(14)
t.right(100)
t.pendown()
t.forward(20)
t.left(136)
t.forward(22)
t.color('white')

#Creating Hands
x = -70
y = -90
for i in range(0,2):
    t.penup()
    t.goto(x,70)
    t.right(y)
    t.pendown()
    t.forward(110)
    t.right(60)
    x = abs(x)
    y = abs(y)
    #Creating fingers on each hand
    for i in range(0,3):
        t.forward(20)
        t.backward(20)
        t.left(60)
    t.left(150)

#Text at the top
t.penup()
t.goto(0,250)
t.write('Mr.Snowman',align='center',font=('Arial',24,'bold'))

#Extending lifespan of screen indefinitely, and closing the screen by pressing 'a'
loop_breaker = 0
def end():
    loop_breaker = 1
    screen.bye() 

while loop_breaker == 0:
        t.forward(1)
        screen.listen()
        screen.onkeypress(end,'a')