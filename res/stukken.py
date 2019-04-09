import pyglet

class GameObject(object):
    def __init__(self, x=None, y=None, vakje_w=50, vakje_h=50, image=None):
        ''' vakje_w: width van 1 vakje hier 50
            vakje_h: height van 1 vakje hier 50
            x: abs x locatie
            y: abs y locatie
            image: afbeelding, mss afbeeldingenset
        '''
        self.vakje_w, self.vakje_h = vakje_w, vakje_h
        if (x == None) or (y == None):
            x, y = 0, 0
        self.x, self.y = x, y #abs location nodig voor de sprite te kunnen tekenen
    
        if image:
            img = pyglet.image.load(image) #mss op voorhand oproepen en stockeren in een dict-> performance
            self.sprite = pyglet.sprite.Sprite(img, self.x, self.y)

        self.rotation = 0
        self.maxrot = 1
    
    def draw(self):
        self.sprite.draw()

    def move(self, new_x, new_y):
        pass

class King(GameObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    

class Switch(GameObject):
    pass

class Defender(GameObject):
    pass

class Deflector(GameObject):
    pass

class Laser(GameObject):
    pass
        