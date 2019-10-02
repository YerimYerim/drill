from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

x = 0

# 여기를 채우세요.
frame = 0
while True:
    if x < 800:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame+1) % 8
        x += 10
        delay(0.04)
        get_events()
        
    elif x >= 800:
        if x > 1600:
            x = 0
        clear_canvas()
        grass.draw(400, 30)
        ##character.clip_draw(frame * 100, 0, 100, 100, 800 - x + 800, 90)
        character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', 800 - x + 800, 90, 100, 100)
        update_canvas()
        frame = (frame+1) % 8
        x += 10
        delay(0.04)
        get_events()

close_canvas()

