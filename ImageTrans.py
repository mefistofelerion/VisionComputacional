import PIL 
import Tkinter
from Tkinter import *
import Image, ImageTk
import sys

imageArgu= sys.argv[1]

def load( imagen):    
    imageLoaded=Image.open(imagen)
    show=Tkinter.Tk()
    show.title("Imagen")
    tkimage=ImageTk.PhotoImage(imageLoaded)
    Tkinter.Label(show, image=tkimage).pack()
    b=Button(show, text="Grises",command=convertGray)
    b2=Button(show,text="Binarizacion",command=convertBin)
    b3=Button(show,text="blur",command=vecinity)
    b.pack(fill=BOTH)
    b2.pack(fill=BOTH)
    b3.pack(fill=BOTH)
    show.mainloop()

def convertGray(imagen=imageArgu):
    imagen2=Image.open(imagen)
    pixels=imagen2.load()
    width,height=imagen2.size
    for i in range(width):
        for j in range(height):
            r,g,b=pixels[i,j]
            gray=int((r+g+b)/3)
            pixels[i,j]=(gray,gray,gray)
    imagen2.show()
    #show2=Tkinter.Tk()
    #show2.title("Imagen en escala de grises")
    #tkimage=ImageTk.PhotoImage(imagen2)
    #Tkinter.Label(show2, image= tkimage).pack()
    #show2.mainloop()

def convertBin(image=imageArgu):
    imagen=Image.open(image)
    pixels=imagen.load()
    width,height=imagen.size
    for i in range(width):
        for j in range(height):
            r,g,b=pixels[i,j]
            gray=int((r+g+b)/3)
            if(gray<127):
                pixels[i,j]=(0,0,0)
            else:
                pixels[i,j]=(255,255,255)
    imagen.show()

def vecinity(image=imageArgu):
    imagen=Image.open(image)
    pixels=imagen.load()
    width,height=imagen.size
    for i in range(width):
        for j in range(height):
            if(i==0 and j==0):
                r,g,b=pixels[i,j]
                r1,g1,b1=pixels[i+1,j]
                r2,g2,b2=pixels[i,j+1]
                newPix=(((r+r1+r2)+(g+g1+g2)+(b+b1+b2))/3)
                pixels[i,j]=newPix
            elif(i==0 and j== height):
                r,g,b=pixels[i,j]
                r1,g1,b1=pixels[i+1,j]
                r2,g2,b2=pixels[i,j+1]
                r3,g3,b3=pixels[i-1,j]
                r4,g4,b4=pixels[i,j-1]
                newPix=(((r+r1+r2+r3+r4)+(g+g1+g2+g3+g4)+(b+b1+b2+b3+b4))/5)


    imagen.show()
            
                

def main():
    load(imageArgu)
    
main()


        

