import pygame
import random as rnd
import math

pygame.init()

width, height = 1024, 620
surface = pygame.display.set_mode((width, height))
color2 = (0, 90, 0)
running = True

force = 13  # Adjust this value to control the force

class Balls:
    def __init__(self, nb):
        self.position = [[rnd.randint(0, width), rnd.randint(0, height)] for _ in range(nb)]
        self.base_position = [[rnd.randint(0, width), rnd.randint(0, height)] for _ in range(nb)]
        self.speeds = [0 for _ in range(nb)]  # Initialize speeds to zero
        self.color = pygame.Color(0, 0, 0)  # Initialize color

    def update(self):
        for index, ball in enumerate(self.position):
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Calculate distance between ball and mouse
            distance = math.sqrt((mouse_x - ball[0]) ** 2 + (mouse_y - ball[1]) ** 2)

            # Calculate repulsive force
            force_repulsion = force * math.pow(distance, -2)

            # Calculate direction vector
            direction = [mouse_x - ball[0], mouse_y - ball[1]]

            # Apply force to ball's position
            ball[0] += direction[0] * force_repulsion
            ball[1] += direction[1] * force_repulsion

            # Calculate attractive force
            force_attraction = force * math.pow(distance, -2)
            attract_direction = [self.base_position[index][0] - ball[0], self.base_position[index][1] - ball[1]]

            # Apply force to ball's position
            ball[0] += attract_direction[0] * force_attraction
            ball[1] += attract_direction[1] * force_attraction

            # Calculate speed
            speed = math.sqrt((ball[0] - self.base_position[index][0]) ** 2 +
                              (ball[1] - self.base_position[index][1]) ** 2)

            # Update speed in the list
            self.speeds[index] = speed

            # Set color based on speed
            red = int(speed * 2.55)
            self.color.r = min(255, red)

            # Restrict ball to within screen boundaries
            if ball[0] < 0:
                ball[0] = 0
            elif ball[0] > width:
                ball[0] = width

            if ball[1] < 0:
                ball[1] = 0
            elif ball[1] > height:
                ball[1] = height

    def draw(self):
        for index, ball in enumerate(self.position):
            pygame.draw.circle(surface, self.color, (int(ball[0]), int(ball[1])), 3)

balls = Balls(1000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.fill(color2)
    balls.update()
    balls.draw()

    pygame.display.flip()
