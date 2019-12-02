
import random
from pico2d import *
class Ball:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(0,1837) , random.randint(0,1109)
        self.size = 20
        if self.image is None:
            self.image = load_image("ball21x21.png")
    def draw(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
    #    self.image.draw(self.x , self.y , self.size , self.size)
        self.image.clip_draw(0, 0, 40, 40, cx, cy)
        draw_rectangle(cx - self.size, cy - self.size, cx + self.size, cy +self.size)
        print (cx , cy , self.x , self.y)
    def delete(self):
        del self
    def update(self):
        pass
    def get_bb(self):
        return self.x - self.size, self.y - self.size, self.x + self.size, self.y +self.size

    def set_background(self, bg):
        self.bg = bg