from cocos.audio.pygame import mixer
from cocos.director import director
from cocos.scene import Scene
from cocos.scenes import FadeTransition

from app.audioManager import PlayMusic
from scene.menuScene import MenuScene
from scene.finishScene import FinishScene
from scene.gameScene import GameScene
import gVariables
import gameResources


class SceneGenerator:

    def __init__(self):
        #INITILIZE ALL RESOURCES HERE
        mixer.init()
        gVariables.g_RESOURCES = gameResources.Resources()

        #INIT MUSIC
        global PLAYMUSIC
        PLAYMUSIC = PlayMusic(gVariables.g_RESOURCES)

    def MainScene(self):
        director.run(Scene(MenuScene(gVariables.g_RESOURCES)))  # redirect to MenuScene
    @staticmethod
    def ChangeScene(index):
        gVariables.g_scene = index
        if index == 0:
            director.replace(FadeTransition(Scene(MenuScene(gVariables.g_RESOURCES))))
        elif index == 1:
            director.replace(FadeTransition(Scene(GameScene(gVariables.g_RESOURCES))))
        else:
            exit(0)