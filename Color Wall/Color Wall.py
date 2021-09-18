import pygame, random, time

# Window Setup
windowWidth = 800
windowHeight = 600
pygame.init()
win = pygame.display.set_mode((windowWidth, windowHeight))

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

stickForwardImage = pygame.image.load("Color Wall\FinnStick.png").convert_alpha()

class Stickman:
    def __init__(self, pos):
        self.sprite = stickForwardImage
        self.dead = False
        self.score = 0
        self.pos = pos
        self.sprite = pygame.transform.scale(self.sprite, (75, 75))

    def draw(self):
        win.blit(self.sprite, self.pos)

class colorWall:
    def __init__(self, color, pos):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.colorChange = colorChange
        self.color = color
        self.pos = pos


running = True

squares = []
deletedSquares = []

stickman = Stickman((20,230))
changeRectColor = (255,255,255)
changeWallColor = (255, 255, 255)

while running:
    #Window stuff
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((135,206,235))

    #Drawing
    stickman.draw()

    #Change player color
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        #Orange
        changeRectColor = (255, 165, 0)
    elif keys[pygame.K_2]:
        #Purple
        changeRectColor = (138,43,226)
    elif keys[pygame.K_3]:
        #Red
        changeRectColor = (255, 0, 0)
    elif keys[pygame.K_4]:
        #Chartruese
        changeRectColor = (127,255,0)

    pygame.draw.rect(win, (changeRectColor), (20, 300, 75, 300))
    pygame.draw.rect(win, (changeWallColor), (725, 0, 75, 600))
    pygame.display.update()



pygame.quit()
