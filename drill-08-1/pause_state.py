from pico2d import *
import game_framework

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global pause


def update():
    delay(0.1)

def draw():
    global image
    clear_canvas()
    image.draw(400, 300, 500, 500)
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