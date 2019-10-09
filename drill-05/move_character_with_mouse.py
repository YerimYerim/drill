from pico2d import *
import math
dir = 0
i = 0
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
ismove = False
goal_x , goal_y = 0, 0
start_x, start_y = 0, 0
def handle_events():
    # fill here
    global ismove
    global running
    global x, y, dir
    global px, py
    global goal_x, goal_y, i
    global start_x, start_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            goal_x, goal_y = event.x, KPU_HEIGHT - 1 - event.y
            start_x, start_y = px, py
            i = 0
            ismove = True
            if px > goal_x:
                dir = 0
            elif px < goal_x:
                dir = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = None
# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cusor = load_image('hand_arrow.png')
point = list()

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
px, py = KPU_WIDTH // 2, KPU_HEIGHT // 2
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[0] - p2[0]) ** 2)

def move(p1,p2):
    global px, py
    global i
    i += distance(p1, p2) / 15
    t = i / distance(p1, p2)
    px = (1-t)*p1[0]+t*p2[0]
    py = (1-t)*p1[1]+t*p2[1]

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if ismove:
        move((start_x, start_y), (goal_x, goal_y))
        if px == goal_x or py == goal_y:
            ismove = False
    if dir is 0:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, px - 50, py + 50)
    elif dir is 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, px - 50, py + 50)
    print(px, py)
    cusor.clip_draw(0, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()

close_canvas()




