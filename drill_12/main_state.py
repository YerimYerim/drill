import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from ground import Ground
from zombie import Zombie
from zombie import Ball

name = "MainState"

boy = None
zombie = None
balls = None
font = None

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True



def get_boy():
    return boy
def get_balls():
    return balls

def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global zombie
    zombie = Zombie()
    game_world.add_object(zombie, 1)

    global balls
    balls = [Ball() for i in range(10)]
    game_world.add_objects(balls, 1)

    ground = Ground()
    game_world.add_object(ground, 0)

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    global  font
    if font is None:
        font = load_font('ENCR10B.TTF', 100)
    for game_object in game_world.all_objects():
        game_object.update()
    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)
            boy.hp += 100
            game_world.remove_object(ball)
        if collide(zombie, ball):
            balls.remove(ball)
            zombie.hp += 100
            game_world.remove_object(ball)



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    if collide(zombie, boy):
        if (zombie.hp > boy.hp):
            quit(0)
            pass
        if (zombie.hp < boy.hp):
            game_world.remove_object(zombie)
            pass
    update_canvas()






