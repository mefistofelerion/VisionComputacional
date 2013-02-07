 
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
    howmany=raw_input("cuantos filtros quieres?: ")
    filtros=int(howmany)
    for w in range(filtros):
        for i in range(width):
            for j in range(height):
                r,g,b=pixels[i,j]
                gray=int((r+g+b)/3)
            

    
 

                if(i==0 and j==0):
                    r,g,b=(gray,gray,gray)
                    r1,g1,b1=pixels[i+1,j]
                    r2,g2,b2=pixels[i,j+1]
                    newPix=(((r+r1+r2)+(g+g1+g2)+(b+b1+b2))/3)
                    pixels[i,j]=(newPix,newPix,newPix)
                elif(i==0 and j== height-1):
                    r,g,b=(gray,gray,gray)
                    r1,g1,b1=pixels[i+1,j]
                    r2,g2,b2=pixels[i,j-1]       
                    newPix=(((r+r1+r2)+(g+g1+g2)+(b+b1+b2))/3)
                    pixels[i,j]=(newPix,newPix,newPix)
                elif(i==width-1 and j == 0):
                    r,g,b=(gray,gray,gray)
                    r1,g1,b1=pixels[i-1,j]
                    r2,g2,b2=pixels[i,j+1]
                    newPix=(((r+r1+r2)+(g+g1+g2)+(b+b1+b2))/3)
                    pixels[i,j]=(newPix,newPix,newPix)
                elif(i==width-1 and j == height-1):
                    r,g,b=(gray,gray,gray)
                    r1,g1,b1=pixels[i-1,j]
                    r2,g2,b2=pixels[i,j-1]
                    newPix=(((r+r1+r2)+(g+g1+g2)+(b+b1+b2))/3)
                    pixels[i,j]=(newPix,newPix,newPix)
                elif(j==0 and i>=1 and i < width-1):
                    r,g,b=(gray,gray,gray)
                    r1,g1,b1=pixels[i-1,j]
                    r2,g2,b2=pixels[i+1,j]
                    r3,g3,b3=pixels[i,j+1]
                    newPix=(((r+r1+r2+r3)+(g+g1+g2+g3)+(b+b1+b2+b3))/4)
                    pixels[i,j]=(newPix,newPix,newPix)
                elif(i==0 and j>=1 and j<height-1):
                    r,g,b=(gray,gray,gray)
                    r1,g1,b1=pixels[i,j-1]
                    r2,g2,b2=pixels[i,j+1]
                    r3,g3,b3=pixels[i+1,j]
                    newPix=(((r+r1+r2+r3)+(g+g1+g2+g3)+(b+b1+b2+b3))/4)
                    pixels[i,j]=(newPix,newPix,newPix)
                elif(i==width-1 and j>=1 and j < height-1):
                    r,g,b=(gray,gray,gray)
                    r1,g1,b1=pixels[i,j-1]
                    r2,g2,b2=pixels[i,j+1]
                    r3,g3,b3=pixels[i-1,j]
                    newPix=(((r+r1+r2+r3)+(g+g1+g2+g3)+(b+b1+b2+b3))/4)
                    pixels[i,j]=(newPix,newPix,newPix)
                elif(j==height-1 and i>=1 and i < width-1):
                    r,g,b=(gray,gray,gray)
                    r1,g1,b1=pixels[i+1,j]
                    r2,g2,b2=pixels[i-1,j]
                    r3,g3,b3=pixels[i,j-1]
                    newPix=(((r+r1+r2+r3)+(g+g1+g2+g3)+(b+b1+b2+b3))/4)
                    pixels[i,j]=(newPix,newPix,newPix)
                else:
                    r,g,b=(gray,gray,gray)
                    r1,g1,b1=pixels[i+1,j]
                    r2,g2,b2=pixels[i-1,j]
                    r3,g3,b3=pixels[i,j-1]
                    r4,g4,b4=pixels[i,j+1]
                    newPix=(((r+g+b)/3)+((r1+g1+b1)/3)+((r2+g2+b2)/3)+((r3+g3+b3)/3)+((r4+g4+b4)/3))/5
                    if(newPix>255):
                        newPix=255
                        
                    pixels[i,j]=(newPix,newPix,newPix)
                        
 
 

    imagen.show()
            
                

def main():
    load(imageArgu)
    
main()


        

