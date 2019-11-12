import game_framework
import game_world
from pico2d import *



PIXEL_PER_METER = (1.0 / 0.01) # 1pixel 1cm
RUN_SPEED_KMPH = 10.0 #km/hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
TIME_PER_ACTION = 1.0 #시간당 액션 1번
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    image = None
    def __init__(self):
        self.x, self.y = 1600 / 2, 150
        if self.image is None:
            self.image = load_image('bird_animation.png')
        self.dir = "Right"
        self.velocity = RUN_SPEED_PPS
        self.frame = 0
        self.frame_x = 0
        self.frame_y = 0


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.frame_x = int(self.frame) % 5

        if int(self.frame) % 14 is 0:
            self.frame_y = 2

        elif int(self.frame) % 14 is 5:
            self.frame_y = 1

        elif int(self.frame) % 14 is 10:
            self.frame_y = 0


        if self.x >= 1450:
            self.velocity = -RUN_SPEED_PPS
            self.dir = "Left"

        if self.x <= 100:
            self.velocity = RUN_SPEED_PPS
            self.dir = "Right"
        self.x += self.velocity * game_framework.frame_time
    def draw(self):
        if self.dir is "Left":
            self.image.clip_composite_draw(int(self.frame_x) * 182, int(self.frame_y) * 168, 182, 168, 0.0, 'h', self.x, self.y, 182, 167)

        elif self.dir is "Right":
            self.image.clip_draw(int(self.frame_x) * 182, int(self.frame_y) * 168, 182, 168, self.x, self.y, 182, 167)