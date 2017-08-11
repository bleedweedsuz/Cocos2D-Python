import pyglet
from cocos.sprite import Sprite
from pyglet.resource import animation
from app.audioManager import AudioManager


class Resources:
    """Used for to collect all the resources in single class so other class can easily used it."""
    #Sprites with animation [BLUE = [0] , GREEN = [2] , RED = [3] , YELLOW = [4]]
    _PLAYER = [
        "assets/sprites/player/player_blue.gif",
        "assets/sprites/player/player_green.gif",
        "assets/sprites/player/player_red.gif",
        "assets/sprites/player/player_yellow.gif",
    ]
    _ENEMY = [
        "assets/sprites/enemy/enemyBlue.gif",
        "assets/sprites/enemy/enemyGreen.gif",
        "assets/sprites/enemy/enemyRed.gif",
        "assets/sprites/enemy/enemyLYellow.gif",
    ]
    _TEXTCOLOR = [
        (210, 67, 67, 255),
        (210, 67, 67, 255),
        (210,67,67,255),
        (210, 67, 67, 255)
    ]
    _BACKGROUND = [
        "assets/sprites/background/MenuBackground.png",
        "assets/sprites/background/P_Back.png",
        "assets/sprites/background/P_Mid.png",
        "assets/sprites/background/P_Front.png",
        "assets/sprites/background/P_Sky.png"
    ]
    _BULLET = [
        "assets/sprites/bullet/bulletBlue.png",
        "assets/sprites/bullet/bulletGreen.png",
        "assets/sprites/bullet/bulletRed.png",
        "assets/sprites/bullet/bulletYellow.png"
    ]
    _BUTTON = [
        "assets/sprites/buttons/btnPlay.png",
        "assets/sprites/buttons/btnOptions.png",
        "assets/sprites/buttons/btnExit.png",
        "assets/sprites/buttons/btnFx_ON.png",
        "assets/sprites/buttons/btnFx_OFF.png",
        "assets/sprites/buttons/btnMusic_ON.png",
        "assets/sprites/buttons/btnMusic_OFF.png",
        "assets/sprites/buttons/btnBack.png"
    ]
    _EFFECT = [
        "assets/sprites/effects/boom.gif",
    ]
    _MUSIC = [
        "assets/media/music/menuMusic.ogg"
    ]
    _SFX =[
        "assets/media/sfx/shoot.ogg",
        "assets/media/sfx/explode.ogg",
    ]
    _HUD = [
        "assets/sprites/hud/topBar.png",
        "assets/sprites/hud/controlInfo.png",
        "assets/sprites/hud/textBack.png"
    ]

    PLAYERANIME = None
    ENEMY = None
    BACKGROUND = None
    BULLET = None
    HUD = None
    TEXTFONT = None
    EFFECT = None

    def __init__(self):
        self.PLAYERANIME = [animation(self._PLAYER[sprite]) for sprite in range(len(self._PLAYER))]
        self.ENEMY = [animation(self._ENEMY[sprite]) for sprite in range(len(self._ENEMY))]
        self.BACKGROUND = [Sprite(self._BACKGROUND[sprite]) for sprite in range(len(self._BACKGROUND))]
        self.HUD = [Sprite(self._HUD[sprite]) for sprite in range(len(self._HUD))]
        self.EFFECT = [animation(self._EFFECT[sprite]) for sprite in range(len(self._EFFECT))]