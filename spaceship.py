import pygame
pygame.init()
pygame.mixer.init()
WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bluenightsky = pygame.image.load("images/bluenightsky.png")
bluenightsky = pygame.transform.scale(bluenightsky, (1000, 800))
redship = pygame.image.load("images/redship.png")
redship = pygame.transform.scale(redship, (200, 113))
redship = pygame.transform.rotate(redship, 90)
yellowship = pygame.image.load("images/yellowship.png")
yellowship = pygame.transform.scale(yellowship, (200, 113))
yellowship = pygame.transform.rotate(yellowship, 270)
grenade=pygame.mixer.Sound("images/Grenade+1.mp3")
gun=pygame.mixer.Sound("images/Gun+Silencer.mp3")

clock=pygame.time.Clock()

red_x = 200
red_y = 300
yellow_x = 700
yellow_y = 300
red_health=100
yellow_health=100
font=pygame.font.SysFont("Arial",36)

border = pygame.Rect(500, 0, 10, 800)
red = pygame.Rect(red_x, red_y, 113,200)
yellow = pygame.Rect(yellow_x, yellow_y, 200, 113)
yellow_bullet=[]
red_bullet=[]
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and yellow.y<HEIGHT-113:
                yellow.y += 30
            if event.key == pygame.K_w and yellow.y>50:
                yellow.y -= 30
            if event.key == pygame.K_d and yellow.x<WIDTH-200:
                yellow.x += 30
            if event.key == pygame.K_a and yellow.x>550:
                yellow.x -= 30
            if event.key == pygame.K_SPACE:
                bullet=pygame.Rect(red.x+100,red.y+100,10,5)
                red_bullet.append(bullet)
                gun.play()
            
            if event.key == pygame.K_DOWN and red.y<HEIGHT-113:
                red.y += 30
            if event.key == pygame.K_UP and red.y>50:
                red.y -= 30
            if event.key == pygame.K_RIGHT and red.x<380:
                red.x += 30
            if event.key == pygame.K_LEFT and red.x>50:
                red.x -= 30
            if event.key == pygame.K_RSHIFT:
                bullet=pygame.Rect(yellow.x-50,yellow.y+100,10,5)
                yellow_bullet.append(bullet)
                gun.play()
    screen.fill("sky blue")
    screen.blit(bluenightsky, (0, 0))
    pygame.draw.rect(screen, "White", border)
    screen.blit(redship, (red.x, red.y))
    screen.blit(yellowship, (yellow.x, yellow.y))
    red_text=font.render("Health:"+str(red_health),1,"Red")
    yellow_text=font.render("Health:"+str(yellow_health),1,"Yellow")
    screen.blit(red_text,(50,50))
    screen.blit(yellow_text,(600,50))
    for bullet in yellow_bullet:
        pygame.draw.rect(screen,"Yellow",bullet)
    for bullet in red_bullet:
        pygame.draw.rect(screen,"Red",bullet)
    for bullet in yellow_bullet:
        bullet.x-=5
        if red.colliderect(bullet):
            red_health-=1
            yellow_bullet.remove(bullet)
            grenade.play()
        if bullet.x<0:
            yellow_bullet.remove(bullet)
    for bullet in red_bullet:
        bullet.x+=5
        if bullet.x>HEIGHT:
            red_bullet.remove(bullet)

    
        if yellow.colliderect(bullet):
                yellow_health-=1
                grenade.play()
                red_bullet.remove(bullet)

   
    if red_health<=0:
        winnertext=font.render("Yellow Wins",True,"Yellow")
        screen.blit(winnertext,(550,350))
        run = False

    elif yellow_health<=0:
        winnertext=font.render("Red Wins",True,"Red")
        screen.blit(winnertext,(550,350))
        run = False
    pygame.display.update()

pygame.quit()
