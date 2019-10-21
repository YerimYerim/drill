from pico2d import *

import game_framework
import main_state

def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del image


def update():
    global image
    delay(0.05)

def draw():
    global pause
    clear_canvas()
    main_state.draw()
    image.draw(400, 300, 500, 500)
    delay(0.05)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def pause():
    pass


def resume():
    pass