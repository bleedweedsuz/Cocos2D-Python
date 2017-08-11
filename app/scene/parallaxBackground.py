import cocos
from cocos.actions import MoveBy, Repeat, Place
from cocos.layer import Layer
from cocos.sprite import Sprite


class ParallaxBackground(Layer):
    def __init__(self, box, sprites, time, delay):
        super(ParallaxBackground, self).__init__()
        self.batch = cocos.batch.BatchNode()
        self.imgA = Sprite(sprites[0])      #Sprite A
        self.imgB = Sprite(sprites[1])      #Sprite B
        self.box = box          #(X, Y, W, H) Window Box (0 = X, 1 = Y, 2 = W, 3 = H)
        self.time = time        #in second

        w = box[2]
        h = box[3]

        self.imgA.position = (w/2, h/2)
        self.imgB.position = (w + (w /2), h/2)

        #point A to point B for image A
        A = MoveBy((-w, 0),time) + Place((w + w/2 ,h/2)) + MoveBy((-w, 0),time)
        B = MoveBy(( -w - w  , 0), time *2) + Place((w + (w /2), h/2))
        #IMAGE ANIMATION
        self.imgA.do(Repeat(A))
        self.imgB.do(Repeat(B))

        self.batch.add(self.imgA)
        self.batch.add(self.imgB)

        self.add(self.batch)