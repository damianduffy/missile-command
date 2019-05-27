import pygame
#from pygame.locals import *

# Global configuration options
SCREENSIZE              = [800, 440]#[960, 540]
FPS                     = 30
TITLE                   = "Missile Defence"
SHOW_MOUSE              = True
CURRENT_GAME_STATE      = 0
GAME_STATE_SPLASH       = 10
GAME_STATE_MENU         = 20
GAME_STATE_RUNNING      = 30
GAME_STATE_NEW_LEVEL    = 40
GAME_STATE_OVER         = 50
SOUND                   = False
NUM_CITIES              = 6
SKY_LEVEL               = 35
GROUND_LEVEL            = 20

# Define colours
BACKGROUND              = (0, 0, 0)
GROUND                  = (69, 139, 81)         # 458b51
DEFENCE                 = (48, 117, 213)        # 3075D5
CITY                    = (255, 211, 24)        # FFD318
WARHEAD                 = (255, 0, 0)           # FF0000
WARHEAD_TRAIL           = (204, 39, 36)         # CC2724
INTERCEPTER             = (48, 117, 213)        # 3075D5
INTERCEPTER_TRAIL       = (255, 255, 255)       # ffffff
INTERFACE_PRI           = (69, 139, 116)        # 458b74
INTERFACE_SEC           = (69, 127, 139)        # 457f8b
NUKE_EXPLOSION          = (255, 0, 0)           # FF0000
INTERCEPT_EXPLOSION     = (255, 255, 255)       # ffffff

# define font
pygame.font.init()
game_font = pygame.font.Font('data/fnt/PressStart2P-Regular.ttf', 16)