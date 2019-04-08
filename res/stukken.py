import pyglet

class GameObject(object):
    def __init__(self, board_w, board_h, x=None, y=None, image=None):
        self.board_w, self.board_h = board_w, board_h
        if (x == None) or (y == None):
            x, y = 0, 0
        self.x, self.y = x, y #abs location nodig voor de sprite te kunnen tekenen
    
        if image:
            img = pyglet.image.load(image) #mss op voorhand oproepen en stockeren in een dict-> performance
            self.sprite = pyglet.sprite.Sprite(img, self.x, self.y)
    
    def draw(self):
        self.sprite.draw()

class King(GameObject):
    def __init__(self):
        pass

class Switch(GameObject):
    pass

class Defender(GameObject):
    pass

class Deflector(GameObject):
    pass

class Laser(GameObject):
    pass
        