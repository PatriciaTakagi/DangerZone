import pygame

#C
C_BLACK = (0,0,0)
C_WHITE = (255,255,255)
C_ORANGE = (255,165,0)
C_RED = (255,0,0)

#E

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Playerplane': 3,
    'PlayerplaneShot': 1,
    'Enemyplane1': 1,
    'Enemyplane1Shot': 5,
    'Enemyplane2': 1,
    'Enemyplane2Shot': 2,
}

EVENT_ENEMY = pygame.USEREVENT + 1

#M
MENU_OPTION = ('START NEW GAME',
                'SCORE',
                'EXIT')

# P
PLAYER_KEY_UP = {'Playerplane': pygame.K_UP}
PLAYER_KEY_DOWN = {'Playerplane': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Playerplane': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Playerplane': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Playerplane': pygame.K_RCTRL}

#S
SPAWN_TIME= 4000

#W
WIN_WIDTH = 576
WIN_HEIGHT = 324