from cocos.audio.pygame.mixer import Sound


class AudioManager(Sound):
    def __init__(self, audioFile):
        super(AudioManager, self).__init__(audioFile)

class PlayMusic:
    def __init__(self, R):
        self.Music = AudioManager(R._MUSIC[0])
        self.Music.set_volume(0.5)
        self.Music.play(-1)
    def Stop(self):
        self.Music.stop()
    def Play(self):
        self.Music.play(-1)
class SFX:
    def __init__(self, effect):
        self.sfx = AudioManager(effect)
        self.sfx.set_volume(0.5)
        self.sfx.play()