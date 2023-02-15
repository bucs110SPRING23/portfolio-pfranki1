import pygame

pygame.init()

screen=pygame.display.set_mode()
screen.fill("white")
pygame.display.flip()

dimensions= screen.get_size()
print(dimensions)

pygame.draw.circle(screen,"black", [700,200], 80)
pygame.draw.circle(screen,"black", [700,400], 125)
pygame.draw.circle(screen,"black", [700,680], 170)
pygame.draw.circle(screen,"white", [700,200], 70)
pygame.draw.circle(screen,"white", [700,400], 115)
pygame.draw.circle(screen,"white", [700,680], 160)
pygame.display.flip()
pygame.time.wait(2000)