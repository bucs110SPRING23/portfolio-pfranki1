import pygame

def threenp1(n):
    while n > 1.0:
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return None

def threenp1range(upper_limit):
    objects_in_sequence={}
    for i in range(2, upper_limit):
            varry=threenp1(i)
            objects_in_sequence[i]=varry
    return objects_in_sequence

