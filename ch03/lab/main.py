import pygame
import random
import math

window=pygame.display.set_mode()
size=pygame.display.get_window_size()

window.fill("black")
pygame.display.flip()
pygame.draw.circle(window, "white", [size[0]/2,size[1]/2], size[1]/2)
pygame.draw.line(window, "black",(0,size[1]/2),(size[0],size[1]/2),5)
pygame.draw.line(window, "black",(size[0]/2,0),(size[0]/2,size[1]),5)
pygame.display.flip()
pygame.time.wait(3000)
pygame.display.flip()

for i in range(10):
    y=random.randrange(0,size[1])
    x=random.randrange(0,size[0])
    distance_from_center=math.hypot(x-size[0]/2, y-size[1]/2)
    in_circle=(distance_from_center <= size[1]/2)
    if in_circle:
        pygame.draw.circle(window, "green", (x,y),10)
    else:
        pygame.draw.circle(window, "red", (x,y), 10)
    pygame.display.flip()
    pygame.time.wait(1000)
pygame.time.wait(3000)
pygame.display.flip()
