import pygame
import random
import math

pygame.init()

while 1:
    pygame.event.pump()
    w=650
    l=650
    box_w=w/2
    box_l=l/2
    box={
        "blue":pygame.Rect(0,0,box_w,box_l),
        "red":pygame.Rect(0,0,box_w, box_l),
    }
    window=pygame.display.set_mode()
    size=pygame.display.get_window_size()

    # pygame.draw.rect(window, "red", (0,600,600,1000))
    # pygame.display.flip()
    # pygame.draw.rect(window, "blue", (900, 1600, 1600, 1000))
    # pygame.display.flip()

    window.fill("black")
    pygame.display.flip()
    pygame.draw.circle(window, "white", [size[0]/2,size[1]/2], size[1]/2)
    pygame.draw.line(window, "black",(0,size[1]/2),(size[0],size[1]/2),5)
    pygame.draw.line(window, "black",(size[0]/2,0),(size[0]/2,size[1]),5)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.display.flip()

total_players=2
first_player=0
outcome=[0,0]
color_1=("green", "red")
color_2=("blue", "orange")



for i in range(10*total_players):
    x=random.randrange(0,size[0])
    y=random.randrange(0,size[1])
    distance_from_center=math.hypot(x-size[0]/2, y-size[1]/2)
    in_circle=(distance_from_center <= size[1]/2)
    if in_circle:
        pygame.draw.circle(window, color_1[first_player], (x,y),15)
        outcome[total_players]+=1
    else:
        pygame.draw.circle(window, color_2[first_player], (x,y), 15)
    pygame.display.flip()
    pygame.time.wait(1000)
    first_player=(first_player+1)%2

    print(outcome)

style=pygame.font.Font(None, 48)
if outcome[0]>outcome[1]:
    message=style.render("First Player Wins!", True, "black")
    window.blit(message,(0,0))
elif outcome[1]>outcome[0]:
    message=message= style.render("Second Player Wins!", True, "black")
    window.blit(style, (0,0))
else:
    message=style.render("Draw!", True, "black")
    window.blit(message, (0,0))
pygame.display.flip()
pygame.time.wait(3000)