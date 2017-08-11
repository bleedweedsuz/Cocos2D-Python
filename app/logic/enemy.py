import random
from cocos.actions import Move, CallFunc, Delay
from cocos.layer import Layer, director
from cocos.sprite import Sprite
import cocos.collision_model as CollisionModel
from app import gVariables
from app.audioManager import SFX


class Enemy(Layer):
    def __init__(self):
        super(Enemy, self).__init__()
    def set(self, gScene):
        self.gScene = gScene
        self.R = gScene.R  # adding resources
        self.batch = gScene.batch  # batch object
        self.player = gScene.PLAYER  # player sprite
        self.collisionManager = gScene.collisionManager
        # Enemy Lists
        self.enemy_lists = set()
        # Schedule Timer
        self.schedule_interval(self.generateEnemyLists, 1)  # Generate enemy every 2 second
        self.schedule(self.checkForCollision)
    def generateEnemyLists(self, dt):
        if self.player.is_playing:
            index = random.randint(0, 3)
            EO = EnemyObject((self, index))
            self.collisionManager.add(EO)
            self.batch.add(EO)
            self.enemy_lists.add(EO)
    def checkForCollision(self, dt):
        eOBJ = set()
        for enemyObj in self.enemy_lists:
            if enemyObj.isDead == False:
                enemyObj.cshape.center = enemyObj.position
                collisions = self.collisionManager.objs_colliding(enemyObj)
                if collisions:
                    if self.player.PLAYER in collisions:
                        enemyObj.die(True)
                        self.player.getHit()

            if enemyObj.position[0] < 0 - enemyObj.width:
                enemyObj.visible = False

            if enemyObj.visible == False:
                eOBJ.add(enemyObj)

        #delete the set obj
        for obj in eOBJ:
            self.enemy_lists.remove(obj)
class EnemyObject(Sprite):
    def __init__(self, e):
        super(EnemyObject, self).__init__(e[0].R.ENEMY[e[1]])
        #X(axis)-Location for enemy
        self.e = e
        self.isDead = False
        self.scale = 0.7
        self.position = (director._window_virtual_width,
                         random.randint(30,director._window_virtual_height - 34 - self.height/2))
        self.velocity = (-100, 0)
        self.deadtemplate = Delay(0.5) + CallFunc(self.destroy)
        self.do(Move())
        #Collision Shape
        self.cshape = CollisionModel.AARectShape(self.position, self.width/2, self.height/2)
    def die(self, collidewithplayer=False):
        try:
            if gVariables.g_IS_FX:
                SFX(self.e[0].R._SFX[1])
            if collidewithplayer:
                self.e[0].gScene.HUD.sLists[self.e[0].gScene.PLAYER.total_lives - 1].visible = False
            self.e[0].gScene.collisionManager.remove_tricky(self)
            self.e[0].player.total_kill +=1
            self.image = self.e[0].R.EFFECT[0]
            self.isDead = True
            self.velocity = (0, 0)
            self.do(self.deadtemplate)
        except:
            print "ERR"
    def destroy(self):
        self.visible = False