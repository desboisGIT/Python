import pygame
import sys
import random
import time

pygame.init()

width, height = 1600, 400
surface = pygame.display.set_mode((width, height))

color = (255, 0, 0)

running = True

towers = [random.randint(0, 200) for i in range(1600)]

def tri_rapide(liste, left, right):
    time.sleep(0.005)
    if left < right:
        pivot_index = partition(liste, left, right)
        tri_rapide(liste, left, pivot_index - 1)
        tri_rapide(liste, pivot_index + 1, right)

def partition(liste, left, right):
    pivot_value = liste[right]
    index = left - 1

    for i in range(left, right):
        if liste[i] <= pivot_value:
            index += 1
            liste[index], liste[i] = liste[i], liste[index]

    liste[index + 1], liste[right] = liste[right], liste[index + 1]

    draw_towers(liste)
    return index + 1

def draw_towers(tower_list):
    pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, width, height))
    for x, tower in enumerate(tower_list):
        pygame.draw.rect(surface, color, pygame.Rect(x * width / len(tower_list), 0, width / len(tower_list), tower))
    pygame.display.flip()

print(towers)
print(len(towers))

draw_towers(towers)
time.sleep(2)
tri_rapide(towers, 0, len(towers) - 1)
time.sleep(2)

pygame.quit()
sys.exit()
