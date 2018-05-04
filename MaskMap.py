__author__ = 'Brandon Funk'

from PIL import Image, ImageFilter, ImageOps
import os, sys
import subprocess

from tkinter.filedialog import askopenfilename, askdirectory

textures=[]
size_int=int(input("Target texture Size>"),10)
size=(size_int,size_int)
texture_type = ""
outputPath = askdirectory()

def getTexture():
    if len(textures) is 0:
        texture_type = "Metallic"
    elif len(textures) is 1:
        texture_type = "Ambient Occlusion"
    elif len(textures) is 2:
        texture_type = "Detail"
    elif len(textures) is 3:
        texture_type = "Smoothness"
    print("{0} map".format(texture_type))
    inputPath = askopenfilename(initialdir = outputPath, title = "Choose {0} Texture".format(texture_type), filetypes = (("PNG", "*.png"),("JPEG","*.jpg"),("TIFF", ".tif"),("all files", "*")))
    if texture_type == "Smoothness":
        cmd = int(input("1: Roughness  |  2: Smoothness >"),10)
        if cmd == 1:
            img = Image.open(inputPath)
            img = ImageOps.invert(img)
            img = img.convert("L")
            textures.append(img.resize(size))
            
        elif cmd == 2:
            textures.append(Image.open(inputPath).convert('L').resize(size))
           
        else:
            print("Try Again!")
    else:
        textures.append(Image.open(inputPath).convert('L').resize(size))
   
    

def getColor():
    if len(textures) is 0:
        texture_type = "Metallic"
    elif len(textures) is 1:
        texture_type = "Ambient Occlusion"
    elif len(textures) is 2:
        texture_type = "Detail"
    elif len(textures) is 3:
        texture_type = "Smoothness"
    color = int(input("Color (0-255) for {0} map>".format(texture_type)))
    textures.append(Image.new('L', size, color))
                    



def make_texture():
    for texture in textures:
        texture.resize(size)
    Image.merge("RGBA",tuple(textures) ).save("{0}/MaskMap.png".format(outputPath))

def main():           
    while True:
        if len(textures) > 3:
            make_texture()
            break
        try:
            cmd = int(input("1: Texture  |  2: Color >"),10)
            if cmd == 1:
                getTexture()
            elif cmd == 2:
                getColor()
            else:
                print ("Number must be one or two")
        except Exception:
            print ("Please enter a real number")


if __name__ == '__main__':
    main()
