import random
from pico2d import *
# Game object class here


class Boy:

    def __init__(self):
        self.x, self.y = random.randint(0, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class BigBall:

    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.frame = random.randint(5, 10)
        self.image = load_image('ball41x41.png')

    def update(self):
        self.frame
        if self.y > 75:
            self.y -= self.frame
        else :
            self.y = 70

    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y)


class Ball:

    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.frame = random.randint(5, 10)
        self.image = load_image('ball21x21.png')

    def update(self):
        self.frame
        if self.y > 65:
            self.y -= self.frame
        else:
            self.y = 60

    def draw(self):
        self.image.clip_draw(0, 0, 21, 21, self.x, self.y)


class Grass:

    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


def handle_events():

    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()
Num = random.randint(1, 19)
# initialization code
team = [Boy() for i in range(11)]
balls = [Ball() for i in range(Num)]
bigballs = [BigBall() for i in range(20-Num)]
grass = Grass()
running = True

# game main loop code
while running:
    handle_events()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.update()
        boy.draw()

    for BigBall in bigballs:
        BigBall.update()
        BigBall.draw()





    update_canvas()
    delay(0.06)
# finalization code
close_canvas()