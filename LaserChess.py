import glob
import pyglet
from pyglet.window import FPSDisplay
from res.stukken import GameObject, King



#ok cava ik zie hoe het werkt ik ben niet helemaal ok met hoe het werkt tho
#ikke u huidige code apart opgeslagen en dan deze is mijn aangepaste versie



#global vars
IMAGES = "res/images/"

#https://www.youtube.com/watch?v=vpMgbCsKviU&t=202s
class Scherm(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        #inintialiseer schermpje
        super().__init__(*args, **kwargs)

        #fps
        
        self.fps = FPSDisplay(self)

        self.images = self.load_images(IMAGES)
        self.veld = self.create_veld() #todo verander de afbeeldingen zodat ze een achtergrond hebben
        self.objlist_1 = {}  #{(1,1)=obj op deze plaats} dit zou de cirkels kunnen bevatten
        self.objlist_2 = {}
        '''
        #test het is:
        img = "res/images/empty.png"
        self.vakjes = []
        for i in range(10):
            for j in range(10):
                self.vakjes.append(GameObject(i*50,j*50, image=img))
        #self.vakje = GameObject(10, 10, image=img)
        #self.vakje2 = GameObject(10, 10, 50, 50, image=img)
        self.vakjes.append(King(image="res/images/king.png"))
        
        #via een menu kan men het veld kiezen, dit wordt ingelezen uit een bepaalde file
        '''

    #pyglet functions:
    def on_draw(self):
        self.clear()

        #teken layer 1 veld
        self.draw_veld(self.veld)
        
        #teken layer 2 pionnen
        for q in self.objlist_1.values():
            q.draw()

        #teken layer 3 witte bollen als nodig
        for q in self.objlist_2.values():
            q.draw()


        #draw fps counter
        self.fps.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        vak_x = x//50
        vak_y = y//50
        if button == pyglet.window.mouse.RIGHT:
            self.objlist_1[(vak_x, vak_y)] = King(vak_x*50, vak_y*50, image=self.images['king.png'])
        elif button == pyglet.window.mouse.LEFT:
            if self.objlist_2.get((vak_x,vak_y), None) != None:
                self.objlist_2[(vak_x, vak_y)].click(self.objlist_1, self.images['circle.png'])
                self.objlist_2 = {}
            elif self.objlist_1.get((vak_x,vak_y), None) != None: #vermijd zo keyerror
                self.objlist_1[(vak_x, vak_y)].click(self.objlist_2, self.images['circle.png'])
            #self.objlist[(vak_x, vak_y)].click(self.objlist, self.images['circle.png'])

        #self.draw_list.append(GameObject(vak_x*50, vak_y*50, image=self.images['circle.png']))


    def update(self, dt):
        pass
    
    #game functions:
    def load_images(self, PATH):
        pngs = [i.split("\\") for i in glob.glob(PATH+'*.png')]
        imgs = {}
        for i in pngs:
            imgs[i[1]] = pyglet.image.load(f"{i[0]}/{i[1]}")
        return imgs


    def create_veld(self, rows=10, columns=10): #, name=None):
        #read from file
        #TODO
        veld = [[GameObject(i*50, j*50, image=self.images['empty.png']) for i in range(columns)] for j in range(rows)]
        return veld
    

    def draw_veld(self, veld):
        for rij in veld:
            for obj in rij:
                obj.draw()


#start game
if __name__ == "__main__":
    a = Scherm(height=500, width=500, resizable=True)
    pyglet.clock.schedule_interval(a.update, 1/60.0) #update 60fps, maar we kunnen ook VSYNC gebruiken
    pyglet.app.run()

