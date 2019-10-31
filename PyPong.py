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
                print(self.posy)

        elif down == True:
            #Check if padle is still in Window Top 
            if not self.posy > resolution[1] -60:
                self.posy = self.posy + 10 
                print(self.posy)

        else:
            self.posy = self.posy 
            print('Error: Called Function Move Without Up or Down')


#Instanciate Rectangles
RectangleLeft = Rectangle()
RectangleRight = Rectangle()


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

        #Release Button UP
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keyup = False
            if event.key == pygame.K_DOWN:
                keydown = False

    #Move Left rectangles
    if keyup == True:
        RectangleLeft.Move(up=True)
    if keydown == True:
        RectangleLeft.Move(down=True)



    screen.fill(black)

    pygame.draw.rect( screen, white, [RectangleLeft.posx, RectangleLeft.posy, RectangleLeft.width, RectangleLeft.hight])
    
    #Update Screen
    pygame.display.flip()

    #FPS
    clock.tick(60)




   