import pygame
import random
import math

pygame.init()

window=pygame.display.set_mode()
pygame.display.flip()
size=pygame.display.get_window_size()
print(size)

window.fill("blue")
pygame.draw.circle(window, "pink", [700,450], 450)
pygame.draw.line(window, "black",(0,size[1]/2),(size[0],size[1]/2),5)
pygame.draw.line(window, "black",(size[0]/2,0),(size[0]/2,size[1]),5)
pygame.display.flip()
pygame.time.wait(3000)
pygame.display.flip()

for i in range(10):
    x1=random.randrange(0,size[0])
    y1=random.randrange(0,size[1])
    distance_from_center=math.hypot(x1-size[0]/2, y1-size[1]/2)
    in_circle=(distance_from_center <= size[1]/2)
    if in_circle:
        pygame.draw.circle(window, "green", (x1,y1),15)
    else:
        pygame.draw.circle(window, "red", (x1,y1), 15)
    pygame.display.flip()
    pygame.time.wait(1000)
pygame.time.wait(3000)
pygame.display.flip()
