import game_framework

from pico2d import *

from ball import Ball

import brick



import game_world

# Boy Run Speed

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Boy Action Speed

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Boy Event

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE = range(5)


key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE

}


class IdleState:

    @staticmethod

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS

        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS

        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS

        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS

        elif event == SPACE:
            boy.isJump = True
            boy.accel = RUN_SPEED_PPS * 5

    @staticmethod

    def exit(boy, event):
      pass

    @staticmethod

    def do(boy):

        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.y += boy.accel * game_framework.frame_time

        if boy.isJump or (boy.jump_direction != 0 and boy.isFall):
            boy.accel -= RUN_SPEED_PPS * game_framework.frame_time * 8
            if boy.y < 90:
                boy.y = 90
                boy.accel = 0
                boy.isJump = False



    @staticmethod

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 200, 100, 100, boy.x, boy.y)





class RunState:

    @staticmethod

    def enter(boy, event):

        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS

        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS

        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS

        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS

        elif event == SPACE:
            boy.isJump = True
            boy.accel = RUN_SPEED_PPS * 5

        boy.dir = clamp(-1, boy.velocity, 1)

    @staticmethod

    def exit(boy, event):
        pass

    @staticmethod

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)
        boy.y += boy.accel * game_framework.frame_time

        if boy.isJump or (boy.jump_direction != 0 and boy.isFall):
            boy.accel -= RUN_SPEED_PPS * game_framework.frame_time * 8
            if boy.y < 90:
                boy.y = 90
                boy.accel = 0
                boy.isJump = False

    @staticmethod

    def draw(boy):
        if boy.dir is 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)

        else:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState} }


class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1 #이동시 사용
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.isJump = False
        self.jump_direction = 0 #점프시 사용
        self.velocity = 0
        self.accel = 0
        self.isFall = False


    def get_bb(self):
        return self.x - 30, self.y - 35, self.x + 30, self. y + 40


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


    def brick_on(self, brick):
        if self.y > brick.y + 20:
            self.y = 260
            if brick.dir is 1:
                self.x += brick.velocity * game_framework.frame_time

            if brick.dir is 0:
                self.x -= brick.velocity * game_framework.frame_time

        else:
            self.accel = 0
            self.jump_direction = 0
            self.isFall = True
            self.isJump = False

