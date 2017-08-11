from cocos.actions import Move, MoveBy, Delay, CallFunc, Blink, Place
from cocos.layer import Layer, director
from cocos.scene import Scene
from cocos.scenes import FadeTransition
from cocos.sprite import Sprite
from pyglet.window import key as KEY
from app import gVariables
import cocos.collision_model as CollisionModel

from app.audioManager import SFX
from app.scene.customPauseScene import CustomPauseScene
from app.scene.finishScene import FinishScene


class Player(Layer):
    is_playing = False
    is_dead = False
    is_shield = False
    total_lives = 4
    total_kill = 0
    is_event_handler = True
    start_timer = 3
    bullet_speed = 800
    bulletZ = 1
    bullet_Lists = set()
    is_dead_scene_Playing = False
    _lastVelocity = None
    def __init__(self):
        super(Player, self).__init__()
    def set(self, gScene):
        self.gScene = gScene
        self.R = gScene.R
        self.enemy = gScene.ENEMY
        self.batch = gScene.batch
        self.collisionManager = gScene.collisionManager
        self.startLocation = (50, director._window_virtual_height - 120)
        self.PLAYER = Sprite(self.R.PLAYERANIME[gVariables.g_PlayerIndex])
        self.PLAYER.position = self.startLocation
        self.PLAYER.scale = 0.5
        self.PLAYER.velocity = (0, 0)
        self.PLAYER.speed = 200
        self.collisionManager.add(self.PLAYER)
        self.PLAYER.do(Move())
        self.PLAYER.do(MoveBy((400, 0), 2) + MoveBy((-400, 0), 2))
        self.batch.add(self.PLAYER)
        self.PLAYER.cshape = CollisionModel.AARectShape(self.PLAYER.position, self.PLAYER.width / 2,
                                                        self.PLAYER.height / 2)
        self.schedule(self.update)
    def on_key_press(self, Key, modifier):
        if self.is_playing == True and self.is_dead_scene_Playing == False:
            K = Key
            if K == KEY.UP:
                self.PLAYER.velocity = 0, self.PLAYER.speed
            elif K == KEY.DOWN:
                self.PLAYER.velocity = 0, -self.PLAYER.speed
            if K == KEY.RIGHT:
                self.PLAYER.velocity = self.PLAYER.speed, 0
            elif K == KEY.LEFT:
                self.PLAYER.velocity = -self.PLAYER.speed, 0
            elif K == KEY.SPACE:
                self.shootBullet()
            elif K == KEY.ENTER:
                director.replace(Scene(CustomPauseScene(self.gScene)))
    def update(self, dt):
        if self.is_playing:
            #BoundingBox Collision
            self.playerCollision()
            #check bullet Collision
            self.checkBulletCollision()
    def playerCollision(self):
        #update Player cShape center
        self.PLAYER.cshape.center = self.PLAYER.position

        #update player boundry
        size =  director.get_window_size()
        w = size[0]
        h= size[1]
        TOP = h - 34 #bar image height/2  because of image position
        LEFT = 0
        RIGHT = w
        BOTTOM = 0
        if self.PLAYER.position[0] - self.PLAYER.width/2  <= LEFT:
            self.PLAYER.position = (LEFT + self.PLAYER.width/2, self.PLAYER.position[1])
        if self.PLAYER.position[0] + self.PLAYER.width/2 >= RIGHT:
            self.PLAYER.position = (RIGHT - self.PLAYER.width/2, self.PLAYER.position[1])
        if self.PLAYER.position[1] - self.PLAYER.height/2 <= BOTTOM:
            self.PLAYER.position = (self.PLAYER.position[0], BOTTOM + self.PLAYER.height/2)
        if self.PLAYER.position[1] + self.PLAYER.height/2>= TOP:
            self.PLAYER.position = (self.PLAYER.position[0], TOP - self.PLAYER.height/2)
    def shootBullet(self):
        if gVariables.g_IS_FX:
            SFX(self.R._SFX[0])
        bullet = Sprite(self.R._BULLET[gVariables.g_PlayerIndex])
        bullet.position = (self.PLAYER.position[0] + bullet.width/2,self.PLAYER.position[1])
        bullet.cshape = CollisionModel.AARectShape(bullet.position, bullet.width/2, bullet.height/2)
        bullet.scale = 0.8
        bullet.velocity = (self.bullet_speed,0)
        bullet.do(Move())
        self.bullet_Lists.add(bullet)
        self.collisionManager.add(bullet)
        self.batch.add(bullet, self.bulletZ)
    def checkBulletCollision(self):
        if len(self.bullet_Lists) > 0:
            hitbullet = set()
            for bullet in self.bullet_Lists:
                #check if bullet collides with enemy
                bullet.cshape.center = bullet.position
                for enemy in self.enemy.enemy_lists:
                    collision = self.collisionManager.objs_colliding(bullet)
                    if enemy in collision:
                        bullet.visible = False
                        hitbullet.add(bullet)
                        enemy.die()
                #check if it is far beyond the window
                if bullet.visible:
                    RBound = director._window_virtual_width + bullet.width /2
                    if bullet.position[0] >= RBound:
                        bullet.visible  = False
                        hitbullet.add(bullet)
            #Remove all the hit bullet from hitbulletLists
            if len(hitbullet) > 0:
                for bullet in hitbullet:
                    self.bullet_Lists.remove(bullet)
                    del bullet
    def getHit(self):
        if self.is_dead_scene_Playing == False and self.is_shield == False:
            self.total_lives -=1
            self.revive_Pattern = Place(self.startLocation)  + CallFunc(self.revive)+ Blink(4, 2) + CallFunc(self.shieldoff)
            self.deadtemplate = Delay(0.5) + CallFunc(self.destroy)
            self.die()
            if self.total_lives <= 0:
                director.replace(FadeTransition(FinishScene(self.gScene)))
    def die(self):
        if gVariables.g_IS_FX:
            SFX(self.R._SFX[1])
        self.is_dead_scene_Playing = True
        self.PLAYER.image = self.R.EFFECT[0]
        self.PLAYER.velocity = (0, 0)
        self.PLAYER.do(self.deadtemplate)
    def destroy(self):
        self.PLAYER.image = self.R.PLAYERANIME[gVariables.g_PlayerIndex]
        self.PLAYER.do(self.revive_Pattern)
    def revive(self):
        self.is_shield =True
        self.is_dead_scene_Playing = False
    def shieldoff(self):
        self.is_shield = False