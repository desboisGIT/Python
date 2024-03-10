import pygame
import random
import time

pygame.init()


WIDTH = 1800
HEIGHT = 600
GROUND_MID = HEIGHT // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Map Renderer")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)

def generateMap(width, groundMid, contrast):
    heightList = []
    ht = groundMid
    for i in range(width):
        ht += random.randint(-contrast, contrast)
        heightList.append(ht)
    return heightList

def renderMap(heightMap):
    column_width = WIDTH // len(heightMap)
    for x, height in enumerate(heightMap):
        column_height = HEIGHT - height
        pygame.draw.rect(screen, BROWN, (x * column_width, height, column_width, column_height))


def smooth(heightMap):
    smoothedMap = heightMap.copy()
    for i in range(1, len(heightMap) - 1):
        smoothedMap[i] = (heightMap[i-1] + heightMap[i] + heightMap[i+1]) // 3
    return smoothedMap

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    heightMap = generateMap(WIDTH, GROUND_MID, 1)
    renderMap(heightMap)
    pygame.display.flip()
    time.sleep(1)
    for i in range(10):
        screen.fill(WHITE)
        heightMap = smooth(heightMap)
        renderMap(heightMap)
        pygame.display.flip()
        time.sleep(0.1)

pygame.quit()