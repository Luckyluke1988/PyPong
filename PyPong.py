import pygame
import random


#RESOLUTION[0] = X Horizontal
#RESOLUTION[1] = Y Vertical 
#Top left is x and y = 0
resolution = (800,500)

white = (255,255,255)
black = (0,0,0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(resolution)

screen.fill(black) 

running = True

keyup = False
keydown = False
key8 = False 
key2 = False

InitDirection = False

movedright = False
'''
//////////////////////CLASS Circle///////////////////////////////////////////
'''
class Circle:
    def __init__(self,color=white, surface=screen ,centrex=200, centrey=200 ,radius=10, velx=5,  vely=5):
        self.color = color
        self.surface = surface
        self.radius = radius
        self.centrex = centrex
        self.centrey = centrey
        self.velx = velx
        self.vely = vely

    def MoveBall(self):
        self.centrex += self.velx





'''
//////////////////////CLASS Rectangle///////////////////////////////////////////
'''
class Rectangle:
    def __init__(self, posx=10, posy=10, hight=50, width=20):
        self.posx = posx
        self.posy = posy
        self.hight = hight
        self.width = width
    
    #Moving Rectangle Function
    def Move(self,up=False, down=False):
        if up == True:
            #Check if Padle is Still in Window Bottom
            if not self.posy < 10:
                self.posy = self.posy - 10

        elif down == True:
            #Check if padle is still in Window Top 
            if not self.posy > resolution[1] -60:
                self.posy = self.posy + 10 

        else:
            self.posy = self.posy 
            print('Error: Called Function Move Without Up or Down')



#Instanciate Circle
Circle = Circle(centrex=255,centrey=255)

#Instanciate Rectangles
RectangleLeft = Rectangle()
RectangleRight = Rectangle(resolution[0]-30)


while running == True:

    for event in pygame.event.get():
        #Button Down Press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()

            if event.key == pygame.K_UP:
                keyup = True
            if event.key == pygame.K_DOWN:
                keydown = True

            if event.key == pygame.K_KP8:
                key8 = True
            if event.key == pygame.K_KP2:
                key2 = True



        #Release Button UP
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keyup = False
            if event.key == pygame.K_DOWN:
                keydown = False

            if event.key == pygame.K_KP8:
                key8 = False
                print('released Key 8')
            if event.key == pygame.K_KP2:
                key2 = False
                print('released Key 2')


    #Move Left rectangles
    if keyup == True:
        RectangleLeft.Move(up=True)
    elif keydown == True:
        RectangleLeft.Move(down=True)

    #Move Right rectangles
    if key8 == True:
        RectangleRight.Move(up=True)
    elif key2 == True:
        RectangleRight.Move(down=True)



    #Clear window before Drawing new Items
    screen.fill(black)

   # if Circle.centrex > 799 or Circle.centrex < 1:
       # Circle.velx = -Circle.velx

    #Move Circle
    if Circle.centrey in range(RectangleRight.posy-50, RectangleRight.posy+50) and Circle.centrex > 799 or \
       Circle.centrey in range(RectangleLeft.posy-50, RectangleLeft.posy+50) and Circle.centrex <10 :
        Circle.velx = -Circle.velx

    #if Circle.centrex > 799 or Circle.centrex < 1:
        #Circle.velx = -Circle.velx
    #else:
       # Circle.centrex = 200
       # Circle.centrey = 200


    Circle.MoveBall()


    #Draw Circle
    pygame.draw.circle(Circle.surface,Circle.color,(Circle.centrex,Circle.centrey),Circle.radius)

    #Draw Padles 
    pygame.draw.rect( screen, white, [RectangleLeft.posx, RectangleLeft.posy, RectangleLeft.width, RectangleLeft.hight])
    pygame.draw.rect( screen, white, [RectangleRight.posx, RectangleRight.posy, RectangleRight.width, RectangleRight.hight])

    #Update Screen
    pygame.display.flip()

    #FPS
    clock.tick(60)




   