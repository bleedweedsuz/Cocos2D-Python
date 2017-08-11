from cocos.layer import Layer, director
from cocos.menu import Menu, CENTER, ToggleMenuItem, MenuItem
from cocos.scene import Scene
from app import gVariables
import sceneGenerator

class CustomPauseScene(Scene):
    def __init__(self, gScene):
        super(CustomPauseScene, self).__init__()
        #ADD ALL TO MAIN LAYER
        self.add(_MenuBackground(gScene))
        self.add(_Menu(gScene))
#MENU LAYERS
class _MenuBackground(Layer):
    def __init__(self, gScene):
        super(_MenuBackground, self).__init__()
        self.R = gScene.R
        self.menuBackgroundSprite= self.R.BACKGROUND[0]
        self.menuBackgroundSprite.position = (director._window_virtual_width/2, director._window_virtual_height/2)
        self.add(self.menuBackgroundSprite)
class _Menu(Menu):
    def __init__(self, gScene):
        super(_Menu, self).__init__()
        self.gScene = gScene
        self.menu_valign = CENTER
        self.menu_halign = CENTER
        self.menu_hmargin = 4
        self.font_item['color'] = (189,216,178,255)
        self.font_item_selected['color'] = (140,161,132,255)
        self.create_menu([
            ToggleMenuItem("Sound Effect ", self.onToggleFX, gVariables.g_IS_FX),
            ToggleMenuItem("Music        ", self.onToggleMusic, gVariables.g_IS_BACKMUSIC),
            MenuItem("Resume", self.onBack)
        ])
    def onToggleFX(self, value):
        gVariables.g_IS_FX = value
    def onToggleMusic(self, value):
        if value:
            sceneGenerator.PLAYMUSIC.Play()
        else:
            sceneGenerator.PLAYMUSIC.Stop()
        gVariables.g_IS_BACKMUSIC = value
    def onBack(self):
        director.replace(Scene(self.gScene))
        self.gScene.PLAYER.is_playing = False