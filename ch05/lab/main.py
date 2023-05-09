import pygame

def threenp1(n):
    number=0
    while n > 1.0:
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
        number +=1
    return number

def threenp1range(upper_limit):
    obj_in_sequence={}
    for i in range(2, upper_limit+1):
            varry=threenp1(i)
            obj_in_sequence[i]=varry
    return obj_in_sequence

def graph_coordinates(threenplus1_iters_dict):
    point=list(threenplus1_iters_dict.items())
    print(point)
    screen=pygame.display.set_mode(size=(600,500))
    screen.fill("black")
    pygame.draw.lines(screen, "white", True, location=point)
    next_display=pygame.transform.flip(screen, False, True)
    screen.blit(next_display, (0,0))

    width, height=next_display.get_size()
    multiplier=2
    print((width*multiplier, height*multiplier))
    next_display=pygame.transform.scale(next_display, (width*multiplier, height*multiplier))
    screen.blit(next_display, (width*multiplier, height*multiplier))
    pygame.display.flip()

def main():
    diction=threenp1range(100)
    print(diction)
    graph_coordinates(diction)

pygame.init()
while 1:
    pygame.event.pump()
    main()
    pygame.time.wait(4000)
    break
