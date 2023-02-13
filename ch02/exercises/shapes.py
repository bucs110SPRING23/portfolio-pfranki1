import pygame

pygame.init()

screen=pygame.display.set_mode()
screen.fill("white")
pygame.display.flip()
pygame.draw.circle(screen,"blue", [700,200], 80)
pygame.draw.circle(screen,"blue", [700,400], 125)
pygame.draw.circle(screen,"blue", [700,650], 170)
pygame.display.flip()
pygame.time.wait(2000)


