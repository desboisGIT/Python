import pygame
import sys
import math

class Object:
    def __init__(self, velocity, mass, position, radius, screen_size):
        self.velocity = velocity
        self.mass = mass
        self.position = position
        self.radius = radius
        self.screen_width, self.screen_height = screen_size
        self.gravity = 0  

    def apply_force(self, force):
        acceleration_x = force[0] / self.mass
        acceleration_y = force[1] / self.mass

        acceleration_y += self.gravity

        self.velocity[0] += acceleration_x
        self.velocity[1] += acceleration_y

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def check_collisions(self, objects):

        for obj in objects:
            if obj != self:  #  self-collision check
                distance = math.sqrt((self.position[0] - obj.position[0]) ** 2 +
                                     (self.position[1] - obj.position[1]) ** 2)
                if distance <= self.radius + obj.radius:

                    self.handle_collision(obj)


        if self.position[0] - self.radius < 0 or self.position[0] + self.radius > self.screen_width:
            self.velocity[0] *= -1
        if self.position[1] - self.radius < 0 or self.position[1] + self.radius > self.screen_height:
            self.velocity[1] *= -1

    def handle_collision(self, obj):

        v1 = self.velocity
        v2 = obj.velocity
        m1 = self.mass
        m2 = obj.mass

        # c ca:
        new_v1 = [(2*m2*v2[0] + (m1 - m2)*v1[0]) / (m1 + m2),
                    (2*m2*v2[1] + (m1 - m2)*v1[1]) / (m1 + m2)]
        new_v2 = [(2*m1*v1[0] + (m2 - m1)*v2[0]) / (m1 + m2),
                    (2*m1*v1[1] + (m2 - m1)*v2[1]) / (m1 + m2)]

        self.velocity = new_v1
        obj.velocity = new_v2

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position[0]), int(self.position[1])), self.radius)

def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    ball1 = Object(velocity=[0, 0], mass=2, position=[width//2, height//2], radius=20, screen_size=(width, height))
    ball2 = Object(velocity=[0, 0], mass=1, position=[width//3, height//3], radius=15, screen_size=(width, height))
    ball3 = Object(velocity=[0, 0], mass=1, position=[width//3, height//4], radius=15, screen_size=(width, height))
    ball4 = Object(velocity=[0, 0], mass=1, position=[width//5, height//3], radius=15, screen_size=(width, height))
    ball5 = Object(velocity=[0, 0], mass=1, position=[width//1.5, height//3], radius=15, screen_size=(width, height))
    ball6 = Object(velocity=[0, 0], mass=1, position=[width//2, height//3], radius=15, screen_size=(width, height))
    ball7 = Object(velocity=[0, 0], mass=1, position=[width//1.5, height//7], radius=15, screen_size=(width, height))
    ball8 = Object(velocity=[0, 0], mass=1, position=[width//8, height//2], radius=15, screen_size=(width, height))
    objects = [ball1, ball2,ball3, ball4,ball5, ball6,ball7, ball8]
    ball1.apply_force([-2.1,-1.1])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        for obj in objects:
            obj.check_collisions(objects)
            obj.update()
            obj.draw(screen)

        pygame.display.flip()
        clock.tick(1000)

if __name__ == "__main__":
    main()