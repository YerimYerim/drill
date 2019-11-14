from pico2d import *
import game_framework

class Brick:
    def __init__(self):
        self.x, self.y = 1600 // 2, 200
        self.velocity = 200
        self.image = load_image('brick180x40.png')
        self.dir = 1
    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def draw(self):
        self.image.draw(self.x , self.y)

    def update(self):
        if self.x >= 1500:
            self.dir = 0
        if self.x <= 100:
            self.dir = 1
        if self.dir is 1:
            self.x += self.velocity * game_framework.frame_time
        elif self.dir is 0:
            self.x -= self.velocity * game_framework.frame_time


