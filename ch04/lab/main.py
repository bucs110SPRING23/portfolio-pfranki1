import pygame
import random
import math

pygame.init()
total_players=2
first_player=0
outcome=[0,0]
colors=("green", "red")
other_colors=("blue", "orange")


#Cannot get Part B to work
#while 1:
    #pygame.event.pump()
    #width=600
    #height=600
    #hit_box_width=width/2
    #hit_box_height=height/2

    #hitboxes={
     #   "red":pygame.rect(0,0,hit_box_width,hit_box_height),
      #  "blue": pygame.rect(0,0, hit_box_width, hit_box_height),
    #}

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
    x=random.randrange(0,size[0])
    y=random.randrange(0,size[1])
    distance_from_center=math.hypot(x-size[0]/2, y-size[1]/2)
    in_circle=(distance_from_center <= size[1]/2)
    if in_circle:
        pygame.draw.circle(window, colors[total_players], (x,y),15)
        outcome[total_players]+=1
    else:
        pygame.draw.circle(window, other_colors[total_players], (x,y), 15)
    pygame.display.flip()
    pygame.time.wait(1000)
    total_players=(total_players+1)%2
pygame.time.wait(3000)
pygame.display.flip()

print(outcome)