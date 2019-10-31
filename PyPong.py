import pygame

resolution = (500,500)

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
            else:
                print('already at the Top')

        elif down == True:
            #Check if padle is still in Window Top 
            if not self.posy > resolution[1] -60:
                self.posy = self.posy + 10 
            else:
                print('already at the Bottom')

        else:
            self.posy = self.posy 
            print('Error: Called Function Move Without Up or Down')


#Instanciate Rectangles
RectangleLeft = Rectangle()
RectangleRight = Rectangle(posx=400)


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
                print('pressed Key 8')
            if event.key == pygame.K_KP2:
                key2 = True
                print('pressed Key 2')



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
        print('Call Move')
    elif key2 == True:
        print('Call Move')
        RectangleRight.Move(down=True)


    #Clear window before Drawing new Items
    screen.fill(black)

    #Draw Padles 
    pygame.draw.rect( screen, white, [RectangleLeft.posx, RectangleLeft.posy, RectangleLeft.width, RectangleLeft.hight])
    pygame.draw.rect( screen, white, [RectangleRight.posx, RectangleRight.posy, RectangleRight.width, RectangleRight.hight])

    #Update Screen
    pygame.display.flip()

    #FPS
    clock.tick(60)




   