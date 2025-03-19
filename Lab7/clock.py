import pygame 
import datetime

pygame.init()

w = 800
d = 600

pygame.display.set_caption("Clock!")

clock = pygame.time.Clock()
screen =  pygame.display.set_mode((w, d))
bg = pygame.image.load("Lab7/clock.png")

min_hand = pygame.image.load("Lab7/min_hand.png")
sec_hand = pygame.image.load("Lab7/sec_hand.png")

def rotate(surf, img, times, angle):
    rot_img = pygame.transform.rotate(img, - (times % 60) * 6 + angle)
    new_img = rot_img.get_rect(center = img.get_rect(center = (400, 300)).center)
    print(new_img)
    surf.blit(rot_img, new_img)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    curtime = datetime.datetime.now()
    minuts = curtime.minute
    seconds = curtime.second
    print(minuts, seconds)
    screen.fill((0, 0, 0))
    
    screen.blit(bg, (0,0))
    
    rotate(screen, sec_hand, seconds, 60)
    rotate(screen, min_hand, minuts, -45)
    
    pygame.display.update()
    clock.tick(60)