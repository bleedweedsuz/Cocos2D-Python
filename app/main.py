from cocos.director import director
import sceneGenerator

__APPNAME__ = "Endless Shooter"
__AUTHORNAME__ = "Sujan Thapa"

__WINDOW__ = (800, 600)

if __name__ == "__main__":
    director.init(caption=__APPNAME__, width=__WINDOW__[0], height=__WINDOW__[1])
    #director.show_FPS = True
    sGenerator = sceneGenerator.SceneGenerator()
    sGenerator.MainScene()
