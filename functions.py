import pygame
from pygame.locals import *
import os
import math
from config import *


# Define helper functions
def load_image(name, colorkey = None):
    fullname = os.path.join('data/img/', name)

    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if colorkey is not None:
        image = image.convert()
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    else:
        image = image.convert_alpha()

    return image # , image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer:
        return NoneSound()

    fullname = os.path.join('data/snd/', name)

    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound:', name)
        raise SystemExit(message)

    return sound


def exit_game(screen):
    pause = 0
    
    # pause music / sfx
    pygame.mixer.pause()

    # display message to confirm exit
    exit_msg = game_font.render('ABANDON YOUR POST?', False, INTERFACE_SEC)
    confirm_msg = game_font.render('(Y/N)', False, INTERFACE_SEC)
    exit_msg_pos = (SCREENSIZE[0] // 2 - (exit_msg.get_width() // 2),
                        SCREENSIZE[1] // 2 - (exit_msg.get_height() // 2))
    confirm_msg_pos = (SCREENSIZE[0] // 2 - (confirm_msg.get_width() // 2),
                        SCREENSIZE[1] // 2 - (confirm_msg.get_height() // 2) + exit_msg.get_height())
    screen.blit(exit_msg, exit_msg_pos)
    screen.blit(confirm_msg, confirm_msg_pos)
    pygame.display.update()

    # wait for player to confirm exit or not
    while pause == 0:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_y:
                    exit()
                if event.key == K_n:
                    pause = -1

    # resume music ifplayer not exiting
    pygame.mixer.unpause()


def pause_game(screen):
    pause = 0
    
    # pause music / sfx
    pygame.mixer.pause()

    # display message that game is paused
    pause_msg = game_font.render('GAME PAUSED', False, INTERFACE_SEC)
    confirm_msg = game_font.render('PRESS \'P\' TO RESUME', False, INTERFACE_SEC)
    pause_msg_pos = (SCREENSIZE[0] // 2 - (pause_msg.get_width() // 2),
                        SCREENSIZE[1] // 2 - (pause_msg.get_height() // 2))
    confirm_msg_pos = (SCREENSIZE[0] // 2 - (confirm_msg.get_width() // 2),
                        SCREENSIZE[1] // 2 - (confirm_msg.get_height() // 2) + pause_msg.get_height())
    screen.blit(pause_msg, pause_msg_pos)
    screen.blit(confirm_msg, confirm_msg_pos)
    pygame.display.update()

    # wait for player to un-pause
    while pause == 0:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_p:
                    pause = -1

    # resume music
    pygame.mixer.unpause()


def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def check_collisions(missile_list, explosion_list, city_list):
    score = 0

    for explosion in explosion_list:
        for missile in missile_list[:]:
            if explosion.get_radius() > distance(explosion.get_center(), missile.get_pos()):
                if missile.get_incoming() == 1:
                    score += 10
                missile_list.remove(missile)
        for city in city_list[:]:
            if explosion.get_radius() > distance(explosion.get_center(), city.get_pos()):
                city.set_destroyed(True)

    return score
