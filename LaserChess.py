import pyglet
from res.stukken import GameObject


#https://www.youtube.com/watch?v=vpMgbCsKviU&t=202s
class Scherm(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        #inintialiseer schermpje
        super().__init__(*args, **kwargs)

        #test het is:
        img = "res/images/empty.png"
        self.vakjes = []
        for i in range(10):
            for j in range(10):
                self.vakjes.append(GameObject(10,10,i*50,j*50, image=img))
        #self.vakje = GameObject(10, 10, image=img)
        #self.vakje2 = GameObject(10, 10, 50, 50, image=img)



    def on_draw(self):
        self.clear()
        for i in self.vakjes:
            i.draw()


    def update(self, dt):
        pass



#start game
if __name__ == "__main__":
    a = Scherm(height=500, width=500, resizable=True)
    pyglet.clock.schedule_interval(a.update, 1/60.0) #update 60fps, maar we kunnen ook VSYNC gebruiken
    pyglet.app.run()

