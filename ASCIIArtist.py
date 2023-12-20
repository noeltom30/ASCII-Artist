from PIL import Image, ImageOps
from math import ceil
from colorama import Fore, Style
from cameraCapture import capture

capture()#takes photo with webcam, otherwise remove this function and just change image source in the next line

with Image.open("image.png") as im:    
    im = im.transpose(Image.ROTATE_270)#image is flipped by default? or i'm doing somn wrong
    im = ImageOps.mirror(im)   
    #im.resize((50,50))#in case you want to fit it terminal, adjust to screen size
    px = im.load()
    width = im.width
    height = im.height
    
print(width," ", height)
brightMatrix = [[0 for j in range(height)] for i in range(width)]
for i in range(width):#stores the averaged rgb value of the pixel and normalizes it to a scale of 90
    for j in range(height):
        sum = 0.21 *px[i,j][0] + 0.72 *px[i,j][1] + 0.07*px[i,j][2]
        brightMatrix[i][j] = sum//3        
        normalized = (brightMatrix[i][j]-0)/255
        normalized *= 90
        brightMatrix[i][j] = ceil(normalized)        
        
charaPixels = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
print(len(charaPixels))
for i in range(width):
    for j in range(height):
        index = +brightMatrix[i][j]   #change + to - to toggle inversion 
        print(Fore.GREEN+charaPixels[index]*2,end="")#*2 prints twice
        #Fore changes terminal font colour
    print()
print(Style.RESET_ALL)#resets colour to white

with open("result.txt", "w") as text:#writes the ascii art to a txt file
    for i in range(width):
        for j in range(height):
            index = +brightMatrix[i][j]   #change + to - to toggle inversion 
            text.write("%s"%(charaPixels[index]*2))
        text.write("\n")

    
