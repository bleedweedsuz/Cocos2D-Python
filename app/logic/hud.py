import cocos
from cocos.layer import Layer, director
from cocos.sprite import Sprite
from cocos.text import Label
from app import gVariables


class HUD(Layer):
    def __init__(self):
        super(HUD, self).__init__()
    def set(self, gScene):
        self.R = gScene.R
        self.batch = gScene.batch
        self.player = gScene.PLAYER

        # top bar
        self.topBar()

        # LivesImages
        self.livesImages()

        # Kill indicator
        self.initKillIndicator()

        # set control info
        self.setControlInfo(True)
        # Timer Loop
        self.initTimerLabel()

        # batch nodes
        self.add(self.batch)

        # Update Loop
        self.schedule(self.loop)
    def loop(self, dt):
        #update player lives
        #update kills
        self.updateKillIndicator(dt)
    def topBar(self):
        self.tBar = self.R.HUD[0]
        self.tBar.opacity = 10
        self.tBar.position = (director._window_virtual_width/2,
                              director._window_virtual_height - self.tBar.height/2)
        self.batch.add(self.tBar)
    def livesImages(self):
        self.sLists = [Sprite(self.R.PLAYERANIME[gVariables.g_PlayerIndex]) for s in range(0, self.player.total_lives)]
        i = 0
        padding = 6
        for s in self.sLists:
            s.scale = 0.3
            s.opacity = 255
            s.position = ((32 * i) + padding + s.width/2, director._window_virtual_height - (padding + s.height/2))
            self.batch.add(s)
            i += 1
    def initKillIndicator(self):
        padding = 20,10
        lSize = 14
        self.label = Label(
            "Total Kill: " + str(self.player.total_kill),
            font_size= lSize,
            color= self.R._TEXTCOLOR[gVariables.g_PlayerIndex],
            anchor_x = 'right',
            anchor_y = 'center'
        )
        self.label.position = director._window_virtual_width -15 , director._window_virtual_height - 15
        self.add(self.label)
    def updateKillIndicator(self, dt):
        self.label.element.text =  "Total Kill: " + str(self.player.total_kill)
        self.label.position = director._window_virtual_width - 15, director._window_virtual_height - 15
    def initTimerLabel(self):
        lSize = 18
        self.labelT2 = Label(
            "START IN " + str(self.player.start_timer),
            font_size=lSize,
            color= self.R._TEXTCOLOR[gVariables.g_PlayerIndex],
            anchor_x='center',
            anchor_y='center'
        )
        self.labelT2.position = (director._window_virtual_width / 2, director._window_virtual_height / 2)

        self.labelT1 = Label(
            "START IN " + str(self.player.start_timer),
            font_size=lSize,
            color= (153, 185, 197,255),
            anchor_x='center',
            anchor_y='center'
        )
        self.labelT1.position = (director._window_virtual_width / 2 + 2, director._window_virtual_height / 2 + 2)

        self.textBack = Sprite(self.R._HUD[2])
        self.textBack.position = (director._window_virtual_width / 2, director._window_virtual_height / 2)
        self.batch.add(self.textBack)

        self.add(self.labelT1)
        self.add(self.labelT2)
        self.schedule_interval(self.startTimer, 1)
    def startTimer(self, dt):
        if self.player.is_playing == False:
            if self.player.start_timer <=0:
                self.labelT2.visible = False
                self.labelT1.visible = False
                self.player.is_playing = True
                self.setControlInfo(False)
                self.textBack.visible = False
            else:
                self.labelT2.element.text = "START IN " + str(self.player.start_timer)
                self.labelT1.element.text = "START IN " + str(self.player.start_timer)
                self.player.start_timer -=1
        else:
            pass
    def setControlInfo(self, bool):
        if bool:
            self.controlInfo = Sprite(self.R._HUD[1])
            self.controlInfo.opacity = 255
            self.controlInfo.position = (director._window_virtual_width / 2,
                                         director._window_virtual_height/2 + 100)
            self.batch.add(self.controlInfo)
        else:
            self.controlInfo.visible = False