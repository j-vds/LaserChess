import copy
import pyglet
from pyglet.sprite import Sprite


V = '|'
H = '-'
T1 = '\\'
T2 = '/'

class LaserVeld(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

        self.veld = [['.' for _ in range(w)] for _ in range(h)]

    def draw(self):
        #pyglet bazaar
        pass
    
    def set_veld(self, veld):
        self.veld = veld
        print(veld)
        self.w = len(veld[0])
        self.h = len(veld)

    def set_laserpos(self, x, y, rot):
        self.veld[y][x] = 'L'
        self.rot = rot #L, R, U, D

    def send_laser(self, laserpos=None):
        for y in range(self.h):
            for x in range(self.w):
                if self.veld[y][x] == 'L':
                    laserpos = (x,y)
                    break
        print(laserpos)
        
        (l_x, l_y) = laserpos
        rot = copy.deepcopy(self.rot)
        veld = copy.deepcopy(self.veld)

        while True:
            if rot == 'U':
                l_y -= 1
            elif rot == 'D':
                l_y += 1
            elif rot == 'R':
                l_x += 1
            else: #rot = 'L'
                l_x -= 1
            ret = self.stuck(l_x, l_y, rot)
            if ret == False:
                break
            elif ret == True:
                veld[l_y][l_x] = V if (rot in 'UD') else H
            else:
                rot = ret
        print(self.print(veld))
        return veld
            
            
    
    def stuck(self, x, y, r):
        if (x < 0) or (x == self.w) or (y == self.h) or (y<0):
            return False
        elif self.veld[y][x] == '.':
            return True
        elif self.veld[y][x] == '\\':
            if r == 'U':
                return 'L'
            elif r == 'D':
                return 'R'
            elif r == 'L':
                return 'U'
            else:
               return 'D'
        elif self.veld[y][x] == '/':
            if r == 'U':
                return 'R'
            elif r == 'D':
                return 'L'
            elif r == 'L':
                return 'D'
            else:
                return 'U'
        else:
            False
    

    def __str__(self):
        return self.print(self.veld)
    
    def print(self, veld):
        string = (self.w+2)*'#'+'\n'
        for i in veld:
            string += '#'+''.join(i)+'#\n'

        string += (self.w+2)*'#'+'\n'
        return string



#testing purposes
if __name__ == '__main__':
    a = LaserVeld(10, 10)
    print(a)
    v1 = [
        ['.','.','.','.','.','.','.','.','/','.'],
        ['.','.','/','.','.','\\','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.'],
        ['.','.','\\','.','.','.','.','/','.','.'],
        ['.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','\\','.','.'],
        ['.','.','.','/','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','\\','.','.'],
        ['.','/','.','.','.','.','.','.','.','.'],
        ['\\','.','.','.','.','.','.','.','.','.'],
       
    ]
    '''
     '../..\\....',
        '..........',
        '..\\..../..',
        '..........',
        '.......\\..',
        '.../......',
        '.......\\..'
    '''
    a.set_veld(v1)
    a.set_laserpos(5,4,'U')
    print(a)
    
    a.send_laser()

