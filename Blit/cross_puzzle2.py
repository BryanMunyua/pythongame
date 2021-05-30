import pygame
pygame.init()

win1 =pygame.display.set_mode((701,549))
pygame.display.set_caption("Cross_puzzle")
clock1=pygame.time.Clock()
font=pygame.font.SysFont('comicsans',40,True)
bg1 = pygame.image.load("rect835.png")

black= (0,0,0)
blue=(0,0,255)
red=(255,0,0)
white =(255,255,255)
grey = (192,192,192)
brown =(210,105,30)






class rect():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(win1, white,(self.x,self.y,self.width,self.height),1)

def redrawGameWindow1():


    win1.blit(bg1,(0,0))

    text = font.render('Two players', 1, black)
    win1.blit(text, (250, 150))
    text = font.render('One player', 1, black)
    win1.blit(text, (250, 200))

    pygame.display.update()

rectangle1 = rect(240,142,200,40)
rectangle2 = rect(240,192,200,40)


run1= True

while run1:
    clock1.tick(54)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run1= False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if pos[0] >= 240 and pos[1] >= 142:
                if pos[0] <= 440 and pos[1] <= 182:
                    run1 = False

    redrawGameWindow1()




pygame.init()

"""win =pygame.display.set_mode((700,580))"""
win =pygame.display.set_mode((701,580))
pygame.display.set_caption("Cross_puzzle")
clock=pygame.time.Clock()
font=pygame.font.SysFont('comicsans',50,True)


black= (0,0,0)
blue=(0,0,255)
red=(255,0,0)

white = (255,255,255)


background_color= (210,105,30)
win.fill(background_color)

circleone_boolean = True

color_boolean = True

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



    line1.drawLine()
    line2.drawLine()
    line3.drawLine()
    line3.drawLine()
    line4.drawLine()
    line5.drawLine()
    line6.drawLine()
    line7.drawLine()
    line8.drawLine()

    if circleone_boolean == True:
        circle1.draw()
    circle2.draw()
    circle3.draw()
    circle4.draw()
    circle5.draw()
    circle6.draw()

    pygame.display.update()


# First horizontal line
line1 = line( black, 45, 45, 655, 45, 5)
# Second horizontal line
line2 = line(black, 45, 290, 655, 290, 5)
# Third horizontal line
line3 = line(black, 45, 535, 655, 535, 5)
# First vertical line
line4 = line( black, 45, 45, 45, 535, 5)
# Second vertical line
line5 = line(black, 350, 45,350, 535, 5)
# Third vertical line
line6 = line(black, 655, 45, 655, 535, 5)
# First diagonal line
line7 = line(black, 45, 45, 655, 535, 5)
# Second diagonal line
line8 = line(black, 655, 45, 45, 535, 5)

circle1 = circle(blue,45,45,32,0)
circle2 = circle(blue,350,45,32,0)
circle3 = circle(blue,655,45,32,0)
circle4 = circle(red,45,535,32,0)
circle5 = circle(red,350,535,32,0)
circle6 = circle(red,655,535,32,0)
circle7 = circle(brown,45,290,32,0)
circle8 = circle(brown,350,290,32,0)
circle9 = circle(brown,655,290,32,0)

PlayerTurn = 1
run= True

circles = [circle1, circle2,circle3,circle4,circle5,circle6]

while run:
    clock.tick(54)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if pos[0] <= circle1.x + 32 and  pos[1] <= circle1.y + 32:
                if pos[0] >= circle1.x - 32 and pos[1] >= circle1.y - 32:
                    if PlayerTurn == 1 and circle1.color == blue:
                        circle1.x = 400
                        circle1.y = 400

                    elif PlayerTurn == -1 and circle1.color == red:
                        circle1.color=brown
                    elif PlayerTurn == 1 and circle1.color== brown:
                        circle1.color = blue
                        PlayerTurn= -1
                    elif PlayerTurn == -1 and circle1.color== brown:
                        circle1.color = red
                        PlayerTurn = 1

            if pos[0] <= circle2.x + 32 and  pos[1] <= circle2.y + 32:
                if pos[0] >= circle2.x - 32 and pos[1] >= circle2.y - 32:
                    if PlayerTurn == 1 and circle2.color == blue:
                        circle2.color=brown
                    elif PlayerTurn == -1 and circle2.color == red:
                        circle2.color=brown
                    elif PlayerTurn == 1 and circle2.color== brown:
                        circle2.color = blue
                        PlayerTurn= -1
                    elif PlayerTurn == -1 and circle2.color== brown:
                        circle2.color = red
                        PlayerTurn = 1


            if pos[0] <= circle3.x + 32 and  pos[1] <= circle3.y + 32:
                if pos[0] >= circle3.x - 32 and pos[1] >= circle3.y - 32:
                    if PlayerTurn == 1 and circle3.color == blue:
                        circle3.color=brown
                    elif PlayerTurn == -1 and circle3.color == red:
                        circle3.color=brown
                    elif PlayerTurn == 1 and circle3.color== brown:
                        circle3.color = blue
                        PlayerTurn= -1
                    elif PlayerTurn == -1 and circle3.color== brown:
                        circle3.color = red
                        PlayerTurn = 1

            if pos[0] <= circle4.x + 32 and  pos[1] <= circle4.y + 32:
                if pos[0] >= circle4.x - 32 and pos[1] >= circle4.y - 32:
                    if PlayerTurn == -1 and circle4.color == red:
                        circle4.color=brown
                    elif PlayerTurn == 1 and circle4.color == blue:
                        circle4.color=brown
                    elif PlayerTurn == 1 and circle4.color== brown:
                        circle4.color = blue
                        PlayerTurn= -1
                    elif PlayerTurn == -1 and circle4.color== brown:
                        circle4.color = red
                        PlayerTurn = 1

            if pos[0] <= circle5.x + 32 and  pos[1] <= circle5.y + 32:
                if pos[0] >= circle5.x - 32 and pos[1] >= circle5.y - 32:
                    if PlayerTurn == -1 and circle5.color == red:
                        circle5.color=brown
                    elif PlayerTurn == 1 and circle5.color == blue:
                        circle5.color= brown
                    elif PlayerTurn == 1 and circle5.color== brown:
                        circle5.color = blue
                        PlayerTurn= -1
                    elif PlayerTurn == -1 and circle5.color== brown:
                        circle5.color = red
                        PlayerTurn = 1

            if pos[0] <= circle6.x + 32 and  pos[1] <= circle6.y + 32:
                if pos[0] >= circle6.x - 32 and pos[1] >= circle6.y - 32:
                    if PlayerTurn == -1 and circle6.color == red:
                        circle6.color=brown
                    elif PlayerTurn == 1 and circle6.color == blue:
                        circle6.color=brown
                    elif PlayerTurn == 1 and circle6.color== brown:
                        circle6.color = blue
                        PlayerTurn= -1
                    elif PlayerTurn == -1 and circle6.color== brown:
                        circle6.color = red
                        PlayerTurn = 1

            if pos[0] <= circle7.x + 32 and  pos[1] <= circle7.y + 32:
                if pos[0] >= circle7.x - 32 and pos[1] >= circle7.y - 32:
                    if PlayerTurn == 1 and circle7.color == brown:
                        circle7.color=blue
                        PlayerTurn = -1
                    elif PlayerTurn == -1 and circle7.color == brown:
                        circle7.color= red
                        PlayerTurn = 1
                    elif PlayerTurn == 1 and circle7.color == blue:
                        circle7.color=brown
                    elif PlayerTurn == -1 and circle7.color == red:
                        circle7.color= brown

            if pos[0] <= circle8.x + 32 and  pos[1] <= circle8.y + 32:
                if pos[0] >= circle8.x - 32 and pos[1] >= circle8.y - 32:
                    if PlayerTurn == 1 and circle8.color == brown:
                        circle8.color=blue
                        PlayerTurn = -1
                    elif PlayerTurn == -1 and circle8.color == brown:
                        circle8.color= red
                        PlayerTurn= 1
                    elif PlayerTurn == 1 and circle8.color == blue:
                        circle8.color=brown
                    elif PlayerTurn == -1 and circle8.color == red:
                        circle8.color= brown

            if pos[0] <= circle9.x + 32 and  pos[1] <= circle9.y + 32:
                if pos[0] >= circle9.x - 32 and pos[1] >= circle9.y - 32:
                    if PlayerTurn == 1 and circle9.color == brown:
                        circle9.color=blue
                        PlayerTurn = -1
                    elif PlayerTurn == -1 and circle9.color == brown:
                        circle9.color= red
                        PlayerTurn= 1
                    elif PlayerTurn == 1 and circle9.color == blue:
                        circle9.color=brown
                    elif PlayerTurn == -1 and circle9.color == red:
                        circle9.color=brown



    redrawGameWindow()

pygame.quit()