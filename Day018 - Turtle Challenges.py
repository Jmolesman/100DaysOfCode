from turtle import Turtle, Screen, colormode
import random
import turtle
import colorgram #pip install colorgram.py

def drawForm(pointer, sides, distance, angle, fix_angle = 0):
    for _ in range (0,sides):
        pointer.left(angle)
        pointer.forward(distance)
        if (fix_angle != 0):
            pointer.left(fix_angle)

def drawSquare(pointer):
    for point in range(0,4):
        pointer.forward(100)
        pointer.right(90)

def drawTriangle(pointer):
    for point in range (0,3):
        pointer.forward(100)
        pointer.left(120)

def drawPentagon(pointer):
    for point in range (0,5):
        pointer.forward(100)
        pointer.left(72)

def drawHexagon(pointer):
    for point in range (0,6):
        pointer.forward(100)
        pointer.left(60)

def drawSummonFamiliar(pointer):
    for point in range (0,5):
        pointer.left(36)
        pointer.forward(162)
        pointer.left(108)

def drawHeptagon(pointer):
    for point in range (0,7):
        pointer.forward(100)
        pointer.left(51.4285714)

def drawOctagon(pointer):
    for point in range (0,8):
        pointer.forward(100)
        pointer.left(45)

def drawNonagon(pointer):
    for point in range (0,9):
        pointer.forward(100)
        pointer.left(40)

def drawDecagon(pointer):
    for point in range (0,10):
        pointer.forward(100)
        pointer.left(36)

def drawDashedLine(pointer,distance, separation,dashLenght):
    count = 0
    while(count<distance):
        pointer.forward(dashLenght)
        pointer.penup()
        pointer.forward(separation)
        pointer.pendown()
        count += dashLenght+separation

        if (count + dashLenght > distance):
            pointer.forward(count - distance)

def goToPosition(pointer,x,y):
    pointer.penup()
    pointer.setposition([x,y])
    pointer.pendown()

pointer = Turtle()
# drawSquare(pointer)
goToPosition(pointer,0,-20)
# drawDashedLine(pointer,100,2,3)
# drawTriangle(pointer)
# drawPentagon(pointer)
# drawHexagon(pointer)
# drawSummonFamiliar(pointer)
# drawHeptagon(pointer)
# drawOctagon(pointer)
# drawNonagon(pointer)
# drawDecagon(pointer)

# for sides in range(3,11):
#     colormode(255)
#     pointer.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     drawForm(pointer,sides,50,(360/sides))

movements = ["N","S","E","W","Tired"]

def randomWalk(pointer, distance, minMovement = 10):
    colormode(255)
    while (minMovement != 0):
        pos = random.choice(movements)
        pointer.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if (pos == "Tired" and minMovement == 0):
            break

        if (pos == "N"):
            pointer.setheading(90)
        elif(pos == "S"):
            pointer.setheading(270)
        elif (pos == "E"):
            pointer.setheading(0)
        elif (pos == "W"):
            pointer.setheading(180)
        
        pointer.forward(distance)
        minMovement-=1


def drawSpirograph(pointer):
    colormode(255)
    for angle in range (1,360):
        pointer.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pointer.speed(100)
        pointer.circle(100)
        pointer.right(angle)

def getImagenPalette(imagenPath, numColors):
    fullPalette = colorgram.extract(imagenPath,numColors)
    newPalette = []

    for color in fullPalette:
        newPalette.append((color.rgb.r,color.rgb.g,color.rgb.b))
    
    return newPalette

def draw1MillionDollarPainting(pointer, palette):
    colormode(255)
    # 10 x 10, size 20 separation 50
    pointer.penup()
    pointer.setpos(-200,-200)
    pointer.pendown()
    pointer.speed("fastest")

    actualPosition = pointer.position()
    for y in range (10):
        for x in range (10):
            pointer.color(random.choice(palette))
            pointer.begin_fill()
            pointer.dot(20)
            pointer.penup()
            pointer.forward(50)
            pointer.end_fill()
            pointer.pendown()
        actualPosition = (actualPosition[0],actualPosition[1]+50)
        pointer.penup()
        pointer.setpos(actualPosition)
        pointer.pendown()
        

# pointer.hideturtle()
# pointer.pensize(3)
# randomWalk(pointer,20,40)
# drawSpirograph(pointer)
palette = getImagenPalette("Day018 - Turtle Challenges Image.jpg",25)
draw1MillionDollarPainting(pointer,palette)


screen = Screen()
screen.exitonclick()