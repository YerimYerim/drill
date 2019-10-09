from pico2d import *
import math
import random
i = 0
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
random_numX, random_numY = None, None
p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 = None, None, None, None, None, None, None, None, None, None
def makerandomPoint():
    global p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
    global random_numX
    global random_numY
    random_numX = [random.randint(100, 900) for n in range(10)]
    random_numY = [random.randint(100, 900) for n in range(10)]
    p1 = (random_numX[0], random_numY[0])
    p2 = (random_numX[1], random_numY[1])
    p3 = (random_numX[2], random_numY[2])
    p4 = (random_numX[3], random_numY[3])
    p5 = (random_numX[4], random_numY[4])
    p6 = (random_numX[5], random_numY[5])
    p7 = (random_numX[6], random_numY[6])
    p8 = (random_numX[7], random_numY[7])
    p9 = (random_numX[8], random_numY[8])
    p10 = (random_numX[9], random_numY[9])

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = None
# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
px, py = KPU_WIDTH // 2, KPU_HEIGHT // 2
case = 0
def move(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    global px, py
    global i
    global case
    #왼쪽이 디폴트
    if case == 0:
        t = i / 100
        px = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        py = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2
        if p1[0] > p2[0]:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, px, py)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, px, py)

        if i == 100:
            i = 0
            case += 1
        else:
            i += 2

    # draw p2-p3
    elif case == 1:
        t = i / 100
        px = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        py = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2

        if p2[0] > p3[0]:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, px, py)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, px, py)

        if i == 100:
            i = 0
            case += 1
        else:
            i += 2

    # draw p3-p4
    elif case == 2:
        t = i / 100
        px = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p5[0]) / 2
        py = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p5[1]) / 2

        if p3[0] > p4[0]:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, px, py)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, px, py)

        if i == 100:
            i = 0
            case += 1
        else:
            i += 2
    # draw p4-p5
    elif case == 3:
        t = i / 100
        px = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) / 2
        py = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p6[1]) / 2

        if p4[0] > p5[0]:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, px, py)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, px, py)
        if i == 100:
            i = 0
            case += 1
        else:
            i += 2

    #draw p5~p6
    elif case == 4:
        t = i / 100
        px = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[0] + (t ** 3 - t ** 2) * p7[0]) / 2
        py = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[1] + (t ** 3 - t ** 2) * p7[1]) / 2

        if p5[0] > p6[0]:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, px, py)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, px, py)

        if i == 100:
            i = 0
            case += 1
        else:
            i += 2
    # p6~p7

    elif case == 5:
        t = i / 100
        px = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p7[0] + (t ** 3 - t ** 2) * p8[0]) / 2
        py = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p7[1] + (t ** 3 - t ** 2) * p8[1]) / 2

        if p6[0] > p7[0]:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, px - 50, py)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, px - 50, py)
        if i == 100:
            i = 0
            case += 1
        else:
            i += 2
    # p7~p8
    elif case == 6:
        t = i / 100
        px = ((-t ** 3 + 2 * t ** 2 - t) * p6[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p8[0] + (t ** 3 - t ** 2) * p9[0]) / 2
        py = ((-t ** 3 + 2 * t ** 2 - t) * p6[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p8[1] + (t ** 3 - t ** 2) * p9[1]) / 2

        if p7[0] > p8[0]:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, px, py)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, px, py)
        if i == 100:
            i = 0
            case += 1
        else:
            i += 2
# p8~p9
    elif case == 7:
        t = i / 100
        px = ((-t ** 3 + 2 * t ** 2 - t) * p7[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[0] + (t ** 3 - t ** 2) * p10[0]) / 2
        py = ((-t ** 3 + 2 * t ** 2 - t) * p7[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[1] + (t ** 3 - t ** 2) * p10[1]) / 2

        if p8[0] > p9[0]:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, px, py)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, px, py)
        if i == 100:
            i = 0
            case += 1
        else:
            i += 2
    # p9~p10
    elif case == 8:
        t = i / 100
        px = ((-t ** 3 + 2 * t ** 2 - t) * p8[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p10[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        py = ((-t ** 3 + 2 * t ** 2 - t) * p8[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p10[1] + (t ** 3 - t ** 2) * p1[1]) / 2

        if p9[0] > p10[0]:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, px, py)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, px, py)
        if i == 100:
            i = 0
            case += 1
        else:
            i += 2
#10~1
    elif case == 9:
        t = i / 100
        px = ((-t ** 3 + 2 * t ** 2 - t) * p9[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) / 2
        py = ((-t ** 3 + 2 * t ** 2 - t) * p9[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) / 2

        if p10[0] > p1[0]:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, px, py)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, px, py)
        if i == 100:
            i = 0
            case += 1
        else:
            i += 2

    elif case == 10:
        case = 0


makerandomPoint()
while running:

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    move(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
    #character.clip_draw(frame * 100, 100 * 0, 100, 100, px - 50, py + 50)
    #elif dir is 1:
    #    character.clip_draw(frame * 100, 100 * 1, 100, 100, px - 50, py + 50)
    print(p1)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
#    handle_events()

close_canvas()




