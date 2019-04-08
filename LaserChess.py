try:
    import time
    import pyglet

    class Window(pyglet.window.Window):
        def __init__(self, *args, **kwargs):
            #inintialiseer schermpje
            super().__init__(*args, **kwargs)

        def draw(self):
            self.clear()

        def update(self, dt):
            pass



    #start game
    if __name__ == "__main__":
        a = Window(height=500, width=500, resizable=False)
        pyglet.app.run()
except Exception as e:
    print(e)
    time.sleep(5)
        
