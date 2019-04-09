import glob, random
import pyglet
from res.stukken import GameObject, King

#global vars
IMAGES = "res/images/"

#https://www.youtube.com/watch?v=vpMgbCsKviU&t=202s
class Scherm(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        #inintialiseer schermpje
        super().__init__(*args, **kwargs)

        self.images = self.load_images(IMAGES)
        self.veld = self.create_veld()
        
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
        

    #pyglet functions:
    def on_draw(self):
        self.clear()
        for i in self.vakjes:
            i.draw()


    def update(self, dt):
        pass
    
    #game functions:
    def load_images(self, PATH):
        pngs = [i.split("\\") for i in glob.glob(PATH+'*.png')]
        print(pngs)
        imgs = {}
        for i in pngs:
            imgs[i[1]] = pyglet.image.load(f"{i[0]}/{i[1]}")
        print(imgs)
        return imgs

        

    def create_veld(self, rows=10, columns=10): #, name=None):
        #read from file
        #TODO
        pass
        return 0





#start game
if __name__ == "__main__":
    a = Scherm(height=500, width=500, resizable=True)
    pyglet.clock.schedule_interval(a.update, 1/60.0) #update 60fps, maar we kunnen ook VSYNC gebruiken
    pyglet.app.run()

