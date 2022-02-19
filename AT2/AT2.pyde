from Vehicle import Vehicle
from Food import Food
from random import randint

def setup():
    global vrumvrum, comidinha, font, contadorMonstruoso
    contadorMonstruoso = 0
    size(640, 360)
    font = createFont("Arial", 16, True)
    velocity = PVector(0, 0)
    vrumvrum = Vehicle(width / 2, height / 2, velocity)
    comidinha = Food(randint(0, width), randint(0, height), PVector(0, 0))

def draw():
    background(255)
    global contadorMonstruoso
    
    if (comidinha.position - vrumvrum.position).mag() < 2:
        comidinha.position = PVector(randint(0, width), randint(0, height))
        contadorMonstruoso += 1
    textFont(font, 16)
    fill(0)
    text("Comidinhas comidas: " + str(contadorMonstruoso), width/2, 20)
    vrumvrum.caca(comidinha.position)
    comidinha.update()
    comidinha.display()
    vrumvrum.update()
    vrumvrum.display()
