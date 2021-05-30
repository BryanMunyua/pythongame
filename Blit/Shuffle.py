import pygame
pygame.init()

win =pygame.display.set_mode((700,580))
pygame.display.set_caption("Lettuce")
clock=pygame.time.Clock()

black= (0,0,0)
blue=(0,0,255)
red=(255,0,0)
white= (255,255,255)

Hero1= pygame.image.load('L1.png')
Hero2= pygame.image.load('L1E.png')
Enemy= pygame.image.load('R1.png')



background_color= (255,255,255)
win.fill(background_color)

class circle():
    def __init__(self,color,x,y,radius,width):
        self.color=color
        self.x=x
        self.y=y
        self.radius=radius
        self.width=width

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius,self.width)



def redrawGameWindow():
    # First horizontal line
    line1 = pygame.draw.line(win, black, (45, 45), (655, 45), 5)
    # Second horizontal line
    line2 = pygame.draw.line(win, black, (45, 290), (655, 290), 5)
    # Third horizontal line
    line3 = pygame.draw.line(win, black, (45, 535), (655, 535), 5)
    # First vertical line
    line4 = pygame.draw.line(win, black, (45, 45), (45, 535), 5)
    # Second vertical line
    line5 = pygame.draw.line(win, black, (350, 45), (350, 535), 5)
    # Third vertical line
    line6 = pygame.draw.line(win, black, (655, 45), (655, 535), 5)
    # First diagonal line
    line7 = pygame.draw.line(win, black, (45, 45), (655, 535), 5)
    # Second diagonal line
    line8 = pygame.draw.line(win, black, (655, 45), (45, 535), 5)

    line1
    line2
    line3
    line3
    line4
    line5
    line6
    line7
    line8

    circle1.draw()
    circle2.draw()
    circle3.draw()
    circle4.draw()
    circle5.draw()
    circle6.draw()
    circle7.draw()
    circle8.draw()
    circle9.draw()


    pygame.display.update()

circle1 = circle(blue,45,45,32,0)
circle2 = circle(blue,350,45,32,0)
circle3 = circle(blue,655,45,32,0)
circle4 = circle(red,45,535,32,0)
circle5 = circle(red,350,535,32,0)
circle6 = circle(red,655,535,32,0)
circle7 = circle(white,45,290,32,0)
circle8 = circle(white,350,290,32,0)
circle9 = circle(white,655,290,32,0)

PlayerTurn = 1
run= True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if pos[0] <= circle1.x + 32 and  pos[1] <= circle1.y + 32:
                if pos[0] >= circle1.x - 32 and pos[1] >= circle1.y - 32:
                    if PlayerTurn == 1 and circle1.color == blue:
                        circle1.color=white
                    elif PlayerTurn == -1 and circle1.color == red:
                        circle1.color=white
                    elif PlayerTurn == 1 and circle1.color== white:
                        circle1.color = blue
                        PlayerTurn= -1
                    elif PlayerTurn == -1 and circle1.color== white:
                        circle1.color = red
                        PlayerTurn = 1

            if pos[0] <= circle2.x + 32 and  pos[1] <= circle2.y + 32:
                if pos[0] >= circle2.x - 32 and pos[1] >= circle2.y - 32:
                    if PlayerTurn == 1 and circle2.color == blue:
                        circle2.color=white
                    elif PlayerTurn == -1 and circle2.color == red:
                        circle2.color=white
                    elif PlayerTurn == 1 and circle2.color== white:
                        circle2.color = blue
                        PlayerTurn= -1
                    elif PlayerTurn == -1 and circle2.color== white:
                        circle2.color = red
                        PlayerTurn = 1


            if pos[0] <= circle3.x + 32 and  pos[1] <= circle3.y + 32:
                if pos[0] >= circle3.x - 32 and pos[1] >= circle3.y - 32:
                    if PlayerTurn == 1 and circle3.color == blue:
                        circle3.color=white
                    elif PlayerTurn == -1 and circle3.color == red:
                        circle3.color=white
                    elif PlayerTurn == 1 and circle3.color== white:
                        circle3.color = blue
                        PlayerTurn= -1
                    elif PlayerTurn == -1 and circle3.color== white:
                        circle3.color = red
                        PlayerTurn = 1

            if pos[0] <= circle4.x + 32 and  pos[1] <= circle4.y + 32:
                if pos[0] >= circle4.x - 32 and pos[1] >= circle4.y - 32:
                    if PlayerTurn == -1 and circle4.color == red:
                        circle4.color=white
                    elif PlayerTurn == 1 and circle4.color == blue:
                        circle4.color=white
                    elif PlayerTurn == 1 and circle4.color== white:
                        circle4.color = blue
                        PlayerTurn= -1
                    elif PlayerTurn == -1 and circle4.color== white:
                        circle4.color = red
                        PlayerTurn = 1

            if pos[0] <= circle5.x + 32 and  pos[1] <= circle5.y + 32:
                if pos[0] >= circle5.x - 32 and pos[1] >= circle5.y - 32:
                    if PlayerTurn == -1 and circle5.color == red:
                        circle5.color=white
                    elif PlayerTurn == 1 and circle5.color == blue:
                        circle5.color=white
                    elif PlayerTurn == 1 and circle5.color== white:
                        circle5.color = blue
                        PlayerTurn= -1
                    elif PlayerTurn == -1 and circle5.color== white:
                        circle5.color = red
                        PlayerTurn = 1

            if pos[0] <= circle6.x + 32 and  pos[1] <= circle6.y + 32:
                if pos[0] >= circle6.x - 32 and pos[1] >= circle6.y - 32:
                    if PlayerTurn == -1 and circle6.color == red:
                        circle6.color=white
                    elif PlayerTurn == 1 and circle6.color == blue:
                        circle6.color=white
                    elif PlayerTurn == 1 and circle6.color== white:
                        circle6.color = blue
                        PlayerTurn= -1
                    elif PlayerTurn == -1 and circle6.color== white:
                        circle6.color = red
                        PlayerTurn = 1

            if pos[0] <= circle7.x + 32 and  pos[1] <= circle7.y + 32:
                if pos[0] >= circle7.x - 32 and pos[1] >= circle7.y - 32:
                    if PlayerTurn == 1 and circle7.color == white:
                        circle7.color=blue
                        PlayerTurn = -1
                    elif PlayerTurn == -1 and circle7.color == white:
                        circle7.color= red
                        PlayerTurn = 1
                    elif PlayerTurn == 1 and circle7.color == blue:
                        circle7.color=white
                    elif PlayerTurn == -1 and circle7.color == red:
                        circle7.color=white

            if pos[0] <= circle8.x + 32 and  pos[1] <= circle8.y + 32:
                if pos[0] >= circle8.x - 32 and pos[1] >= circle8.y - 32:
                    if PlayerTurn == 1 and circle8.color == white:
                        circle8.color=blue
                        PlayerTurn = -1
                    elif PlayerTurn == -1 and circle8.color == white:
                        circle8.color= red
                        PlayerTurn= 1
                    elif PlayerTurn == 1 and circle8.color == blue:
                        circle8.color=white
                    elif PlayerTurn == -1 and circle8.color == red:
                        circle8.color=white

            if pos[0] <= circle9.x + 32 and  pos[1] <= circle9.y + 32:
                if pos[0] >= circle9.x - 32 and pos[1] >= circle9.y - 32:
                    if PlayerTurn == 1 and circle9.color == white:
                        circle9.color=blue
                        PlayerTurn = -1
                    elif PlayerTurn == -1 and circle9.color == white:
                        circle9.color= red
                        PlayerTurn= 1
                    elif PlayerTurn == 1 and circle9.color == blue:
                        circle9.color=white
                    elif PlayerTurn == -1 and circle9.color == red:
                        circle9.color=white



    redrawGameWindow()

pygame.quit()





