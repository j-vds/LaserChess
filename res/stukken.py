import pyglet

class GameObject(object):
    def __init__(self, x=None, y=None, vakje_w=50, vakje_h=50, image=None, team=0, movable=True):
        ''' vakje_w: width van 1 vakje hier 50
            vakje_h: height van 1 vakje hier 50
            x: abs x locatie
            y: abs y locatie
            image: afbeelding, mss afbeeldingenset
        '''
        self.vakje_w = vakje_w
        self.vakje_h = vakje_h
        if (x == None) or (y == None):
            x, y = 0, 0
        self.x, self.y = x, y #abs location nodig voor de sprite te kunnen tekenen
    
        if isinstance(image, pyglet.image.ImageData):
            #image = pyglet.image.load(image) #mss op voorhand oproepen en stockeren in een dict-> performance
            self.sprite = pyglet.sprite.Sprite(image, self.x, self.y)

        self.rotation = 0
        self.maxrot = 1
        self.team = team #0 or 1
        self.movable = movable
        self.clicked = False

    def draw(self):
        self.sprite.draw()
    
    def delete(self):
        self.sprite.delete()

    def location(self, tuple=True):
        if tuple:
            return (self.x//self.vakje_w, self.y//self.vakje_h)
        else:
            return self.x//self.vakje_w, self.y//self.vakje_h

    def move(self, new_x, new_y):
        pass
    
    def click(self, objlist, img_circle):
        pass

class Circle(GameObject):
    def __init__(self, stuk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = stuk
    
    def click(self, objlist, img_circle):
        #verwijder cirkels en verschuiv pion
        del objlist[self.parent.location(False)]
        self.parent.click(objlist, img_circle)
        self.parent>>(self.x-10, self.y-10)
        objlist[(self.x//50, self.y//50)] = self.parent
        


class King(GameObject):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    #operatoren
    def __rshift__(self, other):
        (self.x, self.y) = other
        self.sprite.position = (self.x, self.y) #vaste methode in pyglet --> los op via update!!!
        return self
    
    
    def click(self, objlist, img_circle):
        if self.clicked:
            self.clicked = False
        
        else:
            vak_x = self.x/50
            vak_y = self.y/50
            #teken cirkels
            for i in range(-1,2):
                for j in range(-1,2):
                    if (i==0)*(j==0):
                        continue
                    else:
                        objlist[(vak_x+i, vak_y+j)] = Circle(self, x=50*(vak_x+i)+10, y=50*(vak_y+j)+10, image=img_circle)
            self.clicked = True

        

class Switch(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Defender(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Deflector(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class Laser(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                