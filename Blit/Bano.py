import pygame

pygame.init()

"""win =pygame.display.set_mode((600,480))"""
win =pygame.display.set_mode((701,580))
pygame.display.set_caption("Bano")
clock=pygame.time.Clock()
font=pygame.font.SysFont('comicsans',50,True)


black= (0,0,0)
blue=(0,0,255)
red=(255,0,0)
white = (255,255,255)


background_color= (210,105,30)
win.fill(white)


class circle():
    def __init__(self,color,x,y,radius,width):
        self.color=color
        self.x=x
        self.y=y
        self.radius=radius
        self.width=width

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius,self.width)

class line():
    def __init__(self,color,a,b,x,y,width):
        self.color=color
        self.a=a
        self.b = b
        self.x = x
        self.y = y
        self.width= width

    def drawLine(self):
        pygame.draw.line(win,self.color,(self.a,self.b),(self.x,self.y), self.width)


def redrawGameWindow():

    circle1.draw()
    circle2.draw()
    circle3.draw()

    line1.drawLine()


    pygame.display.update()

circle1 = circle(black,340,290,32,0)
circle2 = circle(blue,80,90,25,0)
circle3 = circle(blue,200,490,25,0)

line1 = line( black, 200, 490, 200, 200, 3)


PlayerTurn = 1
run= True
click = 0

while run:
    speed = 54
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False

    redrawGameWindow()

pygame.quit()
