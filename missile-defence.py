import pygame
#from pygame.locals import *
#import os
import random
#import math
import time

from config import *
from functions import *
from city import City
from missile import Missile
from explosion import Explosion
from defence import Defence
from director import Director


# Initialize game engine, screen and clock
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.mouse.set_visible(SHOW_MOUSE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


def main():
    global current_game_state

    # set the random seed - produces more random trajectories
    random.seed()

    # start music
    if SOUND == True:
        background_track.play(-1)

    # list of all active explosions
    explosion_list = []
    # list of all active missiles
    missile_list = []
    # TBC - generate the cities
    # need to be replaced with working cities
    city_list = []
    for i in range(1, 8):   # 8 == Max num cities plus defence plus one
        if i == 8 // 2:     # find centre point for gun
            pass
        else:
            city_list.append(City(i, 7))   # 7 == max num cities plus guns
    # Intercepter gun
    defence = Defence()

    # setup the AI director
    director = Director()

    while True:
        # write event handlers here
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    # primary mouse button
                    defence.shoot(missile_list)
                if event.button == 2:
                    # middle mouse button
                    pass
                if event.button == 3:
                    # right mouse button
                    pass
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit_game(screen)
                if event.key == K_SPACE:
                    defence.shoot(missile_list)
                if event.key == K_p:
                    pause_game(screen)
            if event.type == KEYUP:
                pass

        # clear the screen before drawing
        screen.fill(BACKGROUND)

        # Game logic and draws
        
        # --- cities
        for city in city_list:
            city.draw(screen)
        
        # --- interceptor turret
        defence.update()
        defence.draw(screen)
        
        # --- missiles
        for missile in missile_list[:]:
            missile.update(explosion_list)
            missile.draw(screen)
            if missile.detonated:
                missile_list.remove(missile)
        
        # --- explosions
        for explosion in explosion_list[:]:
            explosion.update()
            explosion.draw(screen)
            if explosion.complete:
                explosion_list.remove(explosion)

        # --- Draw the interface 
        director.draw(screen)

        # --- update game director
        current_game_state = director.update(missile_list, explosion_list, city_list)

        # load a message and set new game values for start new level
        if current_game_state == GAME_STATE_NEW_LEVEL:
            director.new_level(screen)
        
        # Update the display
        pygame.display.update()

        # hold for few seconds before starting new level
        if current_game_state == GAME_STATE_NEW_LEVEL:
            time.sleep(3)
            
        # run at pre-set fps
        clock.tick(FPS)


if __name__ == '__main__':
    main()
