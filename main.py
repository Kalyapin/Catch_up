from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Catch_up")
background = transform.scale(image.load("images/background.png"), (700, 500))

sprite1 = transform.scale(image.load("images/fly1.png"), (70, 70))

sprite2 = transform.scale(image.load("images/fly2.png"), (70, 70))

x1 = 0
y1 = 0
x2 = 630
y2 = 430

state = True

a = 70

timer = 0

clock = time.Clock()
FPS = 60


def hit_sprite():
    # x1, x1 + a, y1
    # y2, y2 + a, x2
    if (y2 <= y1 <= y2 + a) and (x1 <= x2 <= x1 + a):
        return True
    if (y2 <= y1 <= y2 + a) and (x1 <= x2 + a <= x1 + a):
        return True
    if (y2 <= y1 + a <= y2 + a) and (x1 <= x2 <= x1 + a):
        return True
    if (y2 <= y1 + a <= y2 + a) and (x1 <= x2 + a <= x1 + a):
        return True
    return False


game = True
while game:
    window.blit(background, (0, 0))
    if state:

        window.blit(sprite1, (x1, y1))
        window.blit(sprite2, (x2, y2))

        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and y1 > 5:
            y1 -= 10
        if key_pressed[K_DOWN] and y1 < 430:
            y1 += 10
        if key_pressed[K_LEFT] and x1 > 5:
            x1 -= 10
        if key_pressed[K_RIGHT] and x1 < 630:
            x1 += 10

        if key_pressed[K_w] and y2 > 5:
            y2 -= 10
        if key_pressed[K_s] and y2 < 430:
            y2 += 10
        if key_pressed[K_a] and x2 > 5:
            x2 -= 10
        if key_pressed[K_d] and x2 < 630:
            x2 += 10

        if hit_sprite():
            state = False

    else:
        if timer == 240:
            state = True
            x1 = 0
            y1 = 0
            x2 = 630
            y2 = 430
            timer = 0
        timer += 1

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()