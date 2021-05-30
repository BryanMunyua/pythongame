import pygame
import math
import random
import time
from threading import Timer



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

chip_image = pygame.image.load('chip4.png')
class circle():
    def __init__(self,color,x,y,radius,width,number):
        self.color=color
        self.x=x
        self.y=y
        self.radius=radius
        self.width=width
        self.number = number

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

    circle1.draw()
    circle2.draw()
    circle3.draw()
    circle4.draw()
    circle5.draw()
    circle6.draw()
    circle7.draw()
    circle8.draw()
    circle9.draw()

    # For the red wins
    # The first vertical line win
    if circle1.color == red and circle7.color == red:
        if circle4.color == red:
            text = font.render('Red won!', 0, red)
            win.blit(text, (270, 200))

    # The second vertical line win
    if circle2.color == red and circle8.color == red:
        if circle5.color == red:
            text = font.render('Red won!', 0, red)
            win.blit(text, (270, 200))

    # The third vertical line
    if circle3.color == red and circle9.color == red:
        if circle6.color == red:
            text = font.render('Red won!', 0, red)
            win.blit(text, (270, 200))

    # The horizontal line
    if circle7.color == red and circle8.color == red:
        if circle9.color == red:
            text = font.render('Red won!', 0, red)
            win.blit(text, (270, 200))

    # The first diagonal
    if circle1.color == red and circle8.color == red:
        if circle6.color == red:
            text = font.render('Red won!', 0, red)
            win.blit(text, (270, 200))

    # The second diagonal
    if circle3.color == red and circle8.color == red:
        if circle4.color == red:
            text = font.render('Red won!', 0, red)
            win.blit(text, (270, 200))

    # For the blue wins
    # The first vertical line win
    if circle1.color == blue and circle7.color == blue:
        if circle4.color == blue:
            text = font.render('Blue won!', 0, blue)
            win.blit(text, (270, 200))

    # The second vertical line win
    if circle2.color == blue and circle8.color == blue:
        if circle5.color == blue:
            text = font.render('Blue won!', 0, blue)
            win.blit(text, (270, 200))

    # The third vertical line
    if circle3.color == blue and circle9.color == blue:
        if circle6.color == blue:
            text = font.render('Blue won!', 0, blue)
            win.blit(text, (270, 200))

    # The horizontal line
    if circle7.color == blue and circle8.color == blue:
        if circle9.color == blue:
            text = font.render('Blue won!', 0, blue)
            win.blit(text, (270, 200))

    # The first diagonal
    if circle1.color == blue and circle8.color == blue:
        if circle6.color == blue:
            text = font.render('Blue won!', 0, blue)
            win.blit(text, (270, 200))

    # The second diagonal
    if circle3.color == blue and circle8.color == blue:
        if circle4.color == blue:
            text = font.render('Blue won!', 0, blue)
            win.blit(text, (270, 200))



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

circle1 = circle(blue,45,45,32,0,1)
circle2 = circle(blue,350,45,32,0,2)
circle3 = circle(blue,655,45,32,0,3)
circle4 = circle(red,45,535,32,0,4)
circle5 = circle(red,350,535,32,0,5)
circle6 = circle(red,655,535,32,0,6)
circle7 = circle(white,45,290,32,0,7)
circle8 = circle(white,350,290,32,0,8)
circle9 = circle(white,655,290,32,0,9)


close_to_one = [ 2 , 7 ,8]
close_to_two = [ 1 , 3 ,8]
close_to_three = [ 2 , 9 , 8]
close_to_four = [ 7 , 5 ,8]
close_to_five = [ 4 , 6 , 8]
close_to_six = [ 5 , 9 ,8]
close_to_seven = [ 1 , 8 , 4]
close_to_eight = [ 1 , 2,3 , 4,5 , 6,7 , 9]
close_to_nine = [ 3 , 8 , 6]

previous_to_circle1 = [2,7,8]
previous_to_circle2 = [1,3,8]
previous_to_circle3 = [2,9,8]
previous_to_circle4 = [7,5,8]
previous_to_circle5 = [4,6,8]
previous_to_circle6 = [5,9,8]
previous_to_circle7 = [1,8,4]
previous_to_circle8 = [1,2,3,4,5,6,7,9]
previous_to_circle9 = [3,6,8]



PlayerTurn = 1
run= True
previous_blue_circle = 0
previous_red_circle = 0
close_to_one_whitelist = []

Those_that_can_be_selected = 0

while run:
    speed = 54
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if pos[0] <= circle1.x + 32 and  pos[1] <= circle1.y + 32:
                if pos[0] >= circle1.x - 32 and pos[1] >= circle1.y - 32:
                    if PlayerTurn == 1 and circle1.color == blue:
                        circle1.color=white
                        previous_blue_circle = 1
                    elif PlayerTurn == -1 and circle1.color == red:
                        circle1.color=white
                        previous_red_circle = 1
                    elif PlayerTurn == 1 and circle1.color== white:
                        if previous_blue_circle in previous_to_circle1:
                            circle1.color = blue
                            PlayerTurn= -1
                    elif PlayerTurn == -1 and circle1.color== white:
                        if previous_red_circle in previous_to_circle1:
                            circle1.color = red
                            PlayerTurn = 1

            if pos[0] <= circle2.x + 32 and  pos[1] <= circle2.y + 32:
                if pos[0] >= circle2.x - 32 and pos[1] >= circle2.y - 32:
                    if PlayerTurn == 1 and circle2.color == blue:
                        circle2.color=white
                        previous_blue_circle = 2
                    elif PlayerTurn == -1 and circle2.color == red:
                        circle2.color=white
                        previous_red_circle = 2
                    elif PlayerTurn == 1 and circle2.color== white:
                        if previous_blue_circle in previous_to_circle2:
                            circle2.color = blue
                            PlayerTurn= -1
                    elif PlayerTurn == -1 and circle2.color== white:
                        if previous_red_circle in previous_to_circle2:
                            circle2.color = red
                            PlayerTurn = 1


            if pos[0] <= circle3.x + 32 and  pos[1] <= circle3.y + 32:
                if pos[0] >= circle3.x - 32 and pos[1] >= circle3.y - 32:
                    if PlayerTurn == 1 and circle3.color == blue:
                        circle3.color=white
                        previous_blue_circle = 3
                    elif PlayerTurn == -1 and circle3.color == red:
                        circle3.color=white
                        previous_red_circle = 3
                    elif PlayerTurn == 1 and circle3.color== white:
                        if previous_blue_circle in previous_to_circle3:
                            circle3.color = blue
                            PlayerTurn= -1
                    elif PlayerTurn == -1 and circle3.color== white:
                        if previous_red_circle in previous_to_circle3:
                            circle3.color = red
                            PlayerTurn = 1

            if pos[0] <= circle4.x + 32 and  pos[1] <= circle4.y + 32:
                if pos[0] >= circle4.x - 32 and pos[1] >= circle4.y - 32:
                    if PlayerTurn == -1 and circle4.color == red:
                        circle4.color=white
                        previous_red_circle = 4
                    elif PlayerTurn == 1 and circle4.color == blue:
                        circle4.color=white
                        previous_blue_circle = 4
                    elif PlayerTurn == 1 and circle4.color== white:
                        if previous_blue_circle in previous_to_circle4:
                            circle4.color = blue
                            PlayerTurn= -1
                    elif PlayerTurn == -1 and circle4.color== white:
                        if previous_red_circle in previous_to_circle4:
                            circle4.color = red
                            PlayerTurn = 1

            if pos[0] <= circle5.x + 32 and  pos[1] <= circle5.y + 32:
                if pos[0] >= circle5.x - 32 and pos[1] >= circle5.y - 32:
                    if PlayerTurn == -1 and circle5.color == red:
                        circle5.color=white
                        previous_red_circle = 5
                    elif PlayerTurn == 1 and circle5.color == blue:
                        circle5.color= white
                        previous_blue_circle = 5
                    elif PlayerTurn == 1 and circle5.color== white:
                        if previous_blue_circle in previous_to_circle5:
                            circle5.color = blue
                            PlayerTurn= -1
                    elif PlayerTurn == -1 and circle5.color== white:
                        if previous_red_circle in previous_to_circle5:
                            circle5.color = red
                            PlayerTurn = 1

            if pos[0] <= circle6.x + 32 and  pos[1] <= circle6.y + 32:
                if pos[0] >= circle6.x - 32 and pos[1] >= circle6.y - 32:
                    if PlayerTurn == -1 and circle6.color == red:
                        circle6.color=white
                        previous_red_circle = 6
                    elif PlayerTurn == 1 and circle6.color == blue:
                        circle6.color=white
                        previous_blue_circle = 6
                    elif PlayerTurn == 1 and circle6.color== white:
                        if previous_blue_circle in previous_to_circle6:
                            circle6.color = blue
                            PlayerTurn= -1
                    elif PlayerTurn == -1 and circle6.color== white:
                        if previous_red_circle in previous_to_circle6:
                            circle6.color = red
                            PlayerTurn = 1

            if pos[0] <= circle7.x + 32 and  pos[1] <= circle7.y + 32:
                if pos[0] >= circle7.x - 32 and pos[1] >= circle7.y - 32:
                    if PlayerTurn == 1 and circle7.color == white:
                        if previous_blue_circle in previous_to_circle7:
                            circle7.color=blue
                            PlayerTurn = -1
                    elif PlayerTurn == -1 and circle7.color == white:
                        if previous_red_circle in previous_to_circle7:
                            circle7.color= red
                            PlayerTurn = 1
                    elif PlayerTurn == 1 and circle7.color == blue:
                        circle7.color=white
                        previous_blue_circle = 7
                    elif PlayerTurn == -1 and circle7.color == red:
                        circle7.color= white
                        previous_red_circle = 7

            if pos[0] <= circle8.x + 32 and  pos[1] <= circle8.y + 32:
                if pos[0] >= circle8.x - 32 and pos[1] >= circle8.y - 32:
                    if PlayerTurn == 1 and circle8.color == white:
                        if previous_blue_circle in previous_to_circle8:
                            circle8.color=blue
                            PlayerTurn = -1
                    elif PlayerTurn == -1 and circle8.color == white:
                        if previous_red_circle in previous_to_circle8:
                            circle8.color= red
                            PlayerTurn= 1
                    elif PlayerTurn == 1 and circle8.color == blue:
                        circle8.color=white
                        previous_blue_circle = 8
                    elif PlayerTurn == -1 and circle8.color == red:
                        circle8.color= white
                        previous_red_circle = 8

            if pos[0] <= circle9.x + 32 and  pos[1] <= circle9.y + 32:
                if pos[0] >= circle9.x - 32 and pos[1] >= circle9.y - 32:
                    if PlayerTurn == 1 and circle9.color == white:
                        if previous_blue_circle in previous_to_circle9:
                            circle9.color=blue
                            PlayerTurn = -1
                    elif PlayerTurn == -1 and circle9.color == white:
                        if previous_red_circle in previous_to_circle9:
                            circle9.color= red
                            PlayerTurn= 1
                    elif PlayerTurn == 1 and circle9.color == blue:
                        circle9.color=white
                        previous_blue_circle = 9
                    elif PlayerTurn == -1 and circle9.color == red:
                        circle9.color=white
                        previous_red_circle = 9

        bluelist = []
        redlist = []
        whitelist = []

        if circle1.color == blue:
            bluelist.append(circle1)
        elif circle1.color == red:
            redlist.append(circle1)
        elif circle1.color == white:
            whitelist.append(circle1)

        if circle2.color == blue:
            bluelist.append(circle2)
        elif circle2.color == red:
            redlist.append(circle2)
        elif circle2.color == white:
            whitelist.append(circle2)

        if circle3.color == blue:
            bluelist.append(circle3)
        elif circle3.color == red:
            redlist.append(circle3)
        elif circle3.color == white:
            whitelist.append(circle3)

        if circle4.color == blue:
            bluelist.append(circle4)
        elif circle4.color == red:
            redlist.append(circle4)
        elif circle4.color == white:
            whitelist.append(circle4)

        if circle5.color == blue:
            bluelist.append(circle5)
        elif circle5.color == red:
            redlist.append(circle5)
        elif circle5.color == white:
            whitelist.append(circle5)

        if circle6.color == blue:
            bluelist.append(circle6)
        elif circle6.color == red:
            redlist.append(circle6)
        elif circle6.color == white:
            whitelist.append(circle6)

        if circle7.color == blue:
            bluelist.append(circle7)
        elif circle7.color == red:
            redlist.append(circle7)
        elif circle7.color == white:
            whitelist.append(circle7)

        if circle8.color == blue:
            bluelist.append(circle8)
        elif circle8.color == red:
            redlist.append(circle8)
        elif circle8.color == white:
            whitelist.append(circle8)

        if circle9.color == blue:
            bluelist.append(circle9)
        elif circle9.color == red:
            redlist.append(circle9)
        elif circle9.color == white:
            whitelist.append(circle9)


        if PlayerTurn == 1:
            selected = random.choice(bluelist)



            if selected.number == 1:
                colornext = random.choice(whitelist)

                while colornext.number not in close_to_one:
                    colornext = random.choice(whitelist)


            elif selected.number == 2:
                colornext = random.choice(whitelist)

                while colornext.number not in close_to_two:
                    colornext = random.choice(whitelist)

            elif selected.number == 3:
                colornext = random.choice(whitelist)

                while colornext.number not in close_to_three:
                    colornext = random.choice(whitelist)

            elif selected.number == 4:
                colornext = random.choice(whitelist)

                while colornext.number not in close_to_four:
                    colornext = random.choice(whitelist)

            elif selected.number == 5:
                colornext = random.choice(whitelist)

                while colornext.number not in close_to_five:
                    colornext = random.choice(whitelist)

            elif selected.number == 6:
                colornext = random.choice(whitelist)

                while colornext.number not in close_to_six:
                    colornext = random.choice(whitelist)

            elif selected.number == 7:
                colornext = random.choice(whitelist)

                while colornext.number not in close_to_seven:
                    colornext = random.choice(whitelist)

            elif selected.number == 8:
                colornext = random.choice(whitelist)

                while colornext.number not in close_to_eight:
                    colornext = random.choice(whitelist)

            elif selected.number == 9:
                colornext = random.choice(whitelist)

                while colornext.number not in close_to_nine:
                    colornext = random.choice(whitelist)



            def colorchanger():
                selected.color = white
                colornext.color = blue



            timer = Timer(2.0, colorchanger)

            timer.start()

            PlayerTurn = -1


    redrawGameWindow()

pygame.quit()

# The error that it is bringing is because of the circles that can be selected



