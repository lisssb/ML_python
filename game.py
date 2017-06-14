import pygame

pygame.init()

screen = pygame.display.set_mode((900, 700))

finished = False
x = 0
y = 50
playerImage = pygame.image.load("Player.png")
playerImage = pygame.transform.scale(playerImage, (30, 30))
playerImage = playerImage.convert()
frame = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()

    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[pygame.K_SPACE] == 1:
        y += 5
    #rectOne = pygame.Rect(x, y,30,30) #x,y,width,height
    color = (0,0,255)
    black = (0,0,0)
    screen.fill((black))
    screen.blit(playerImage, (x, y))
    #pygame.draw.rect(screen,color, rectOne)
    pygame.display.flip()
    frame.tick(30)
