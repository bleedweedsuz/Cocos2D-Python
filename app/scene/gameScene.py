from cocos.batch import BatchNode
from cocos.layer import Layer, director
from cocos.sprite import Sprite
import cocos.collision_model as CollisionModel
from app.logic.enemy import Enemy
from app.logic.hud import HUD
from app.logic.player import Player
from app.scene.parallaxBackground import ParallaxBackground

class GameScene(Layer):
    def __init__(self, R):
        super(GameScene, self).__init__()
        self.R = R
        self.batch = BatchNode()
        self.collisionManager = CollisionModel.CollisionManagerBruteForce()
        #Main Background
        mainBack = Sprite(R._BACKGROUND[4])
        mainBack.position = (director._window_virtual_width/2, director._window_virtual_height/2)
        self.add(mainBack)
        #Parallax-BackGround
        self.add(ParallaxBackground((0,0,800,600), [R._BACKGROUND[1],R._BACKGROUND[1]], 16, 10))
        self.add(ParallaxBackground((0, 0, 800, 600), [R._BACKGROUND[2], R._BACKGROUND[2]], 4, 10))
        self.add(ParallaxBackground((0, 0, 800, 600), [R._BACKGROUND[3], R._BACKGROUND[3]], 2, 10))

        #Add Player
        self.PLAYER = Player()
        self.ENEMY = Enemy()
        self.HUD = HUD()

        #set Data
        self.PLAYER.set(self)
        self.ENEMY.set(self)
        self.HUD.set(self)

        #Add layers
        self.add(self.PLAYER)
        self.add(self.ENEMY)
        self.add(self.HUD)

        #Adding Batch to Layer
        self.add(self.batch)