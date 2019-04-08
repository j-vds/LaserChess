from PIL import Image

a = Image.new('RGB', (50,50), color=(0,0,0))
b = Image.new('RGB', (48,48), color=(203,203,203))
a.paste(b, (1,1))

a.save("empty.png")


'''
final = Image.new('RGB', (500,500))
for i in range(10):
    for j in range(10):
        final.paste(a,(i*50, j*50))
final.save('veld.png')
'''