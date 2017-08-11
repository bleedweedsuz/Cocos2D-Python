from cocos.actions import Place, MoveBy, Repeat
from cocos.layer import Layer, director
from cocos.menu import Menu, CENTER, ImageMenuItem, LEFT, ToggleMenuItem, MenuItem, ColorMenuItem
from cocos.scene import Scene
import sceneGenerator
from cocos.sprite import Sprite
from app import gVariables


class MenuScene(Scene):
    def __init__(self, R):
        super(MenuScene, self).__init__()
        #ADD ALL TO MAIN LAYER
        self.add(_MenuBackground(R))
        self.add(_PlayerAnimation(R))
        self.M = _Menu(R, self)
        self.add(self.M)
#MENU LAYERS
class _MenuBackground(Layer):
    def __init__(self, R):
        super(_MenuBackground, self).__init__()
        self.R = R
        self.menuBackgroundSprite= self.R.BACKGROUND[0]
        self.menuBackgroundSprite.position = (director._window_virtual_width/2, director._window_virtual_height/2)
        self.add(self.menuBackgroundSprite)
class _PlayerAnimation(Layer):
    def __init__(self, R):
        super(_PlayerAnimation, self).__init__()
        self.R = R
        self.SamplePlayer = Sprite(self.R.PLAYERANIME[0])
        self.SamplePlayer.scale = 0.5
        self.size = director.get_window_size()
        #SIMPLE ANIMATION
        _WH = self.SamplePlayer.get_AABB()
        _place = (- _WH.width, self.size[1] - 120)
        _move = MoveBy((self.size[0] + (_WH.width *2) , 0), 3)
        self.SamplePlayer.do(Repeat(Place(_place) + _move))
        self.add(self.SamplePlayer)
class _Menu(Menu):
    def __init__(self, R, menuScene):
        super(_Menu, self).__init__()
        self.R = R
        self.menuScene = menuScene
        self.menu_valign = CENTER
        self.menu_halign = LEFT
        self.menu_hmargin = 4
        self.font_item['font_size'] = 40
        items = [
            (ImageMenuItem(self.R._BUTTON[0], self.onPlay)), # PLAY
            (ImageMenuItem(self.R._BUTTON[1], self.onOptions)), # Options
            (ImageMenuItem(self.R._BUTTON[2], self.onQuit)) # EXIT
        ]
        self.create_menu(items)
    def onPlay(self):
        sceneGenerator.SceneGenerator.ChangeScene(1) #Play Scene
    def onOptions(self):
        self.menuScene.add(_SubOptions(self.R,self.menuScene))
        self.menuScene.remove(self)
    def onQuit(self):
        sceneGenerator.SceneGenerator.ChangeScene(3)  # Quit Scene
class _SubOptions(Menu):
    def __init__(self, R, menuScene):
        super(_SubOptions, self).__init__()
        self.R = R
        self.menuScene = menuScene
        self.menu_valign = CENTER
        self.menu_halign = LEFT
        self.menu_hmargin = 4
        self.font_item['color'] = (189,216,178,255)
        self.font_item_selected['color'] = (140,161,132,255)
        self.create_menu([
            ColorMenuItem("Player Color ", self.onPlayerChoose, gVariables.g_player_color),
            ToggleMenuItem("Sound Effect ", self.onToggleFX, gVariables.g_IS_FX),
            ToggleMenuItem("Music        ", self.onToggleMusic, gVariables.g_IS_BACKMUSIC),
            MenuItem("Back", self.onBack)
        ])
    def onToggleFX(self, value):
        gVariables.g_IS_FX = value
    def onToggleMusic(self, value):
        if value:
            sceneGenerator.PLAYMUSIC.Play()
        else:
            sceneGenerator.PLAYMUSIC.Stop()
        gVariables.g_IS_BACKMUSIC = value
    def onPlayerChoose(self, color):
        gVariables.g_PlayerIndex = color
    def onBack(self):
        self.menuScene.add(_Menu(self.R, self.menuScene))
        self.menuScene.remove(self)