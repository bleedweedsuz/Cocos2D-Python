from cocos.layer import Layer, director
from cocos.menu import Menu, ImageMenuItem, LEFT, BOTTOM
from cocos.scene import Scene
from cocos.scenes import FadeTransition
from cocos.text import Label


class FinishScene(Scene):
    def __init__(self, gScene):
        super(FinishScene, self).__init__()
        #ADD ALL TO MAIN LAYER
        self.add(_MenuBackground(gScene))
        self.add(_Menu(gScene))
        self.add(_Score(gScene))
class _Score(Layer):
    def __init__(self, gScene):
        super(_Score, self).__init__()
        l = Label("You Kill " + str(gScene.PLAYER.total_kill), color = (0,0,0,255), font_size = 30, anchor_x ='center')
        l.position = (director._window_virtual_width/2 , director._window_virtual_height - 200)
        self.add(l)
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
        self.R = gScene.R
        self.menu_valign = BOTTOM
        self.menu_halign = LEFT
        self.menu_hmargin = 4
        self.font_item['font_size'] = 40
        items = [
            (ImageMenuItem(self.R._BUTTON[7], self.goMainMenu) ) #BACK
        ]
        self.create_menu(items)
    def goMainMenu(self):
        from app.scene.menuScene import MenuScene
        director.replace(FadeTransition(Scene(MenuScene(self.R))))


