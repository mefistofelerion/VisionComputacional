import PIL
import Tkinter
from Tkinter import *
import Image,ImageTk
import sys,random,time

imageArgument=sys.argv[1]

def load(imagen):
    imageLoaded=Image.open(imagen)
    show=Tkinter.Tk()
    show.title("Imagen")
    tkimage=ImageTk.PhotoImage(imageLoaded)
    Tkinter.Label(show,image=tkimage).pack()
    b=Button(show,text="Ponerle \" sal pimienta\"",command=ponerPimienta)
    b2=Button(show,text="Quitarle manchas",command=eliminarManchas)
    b.pack(fill=BOTH)
    b2.pack(fill=BOTH)
    show.mainloop()

def ponerPimienta(imagen=imageArgument):
    imagenParaProcesar=Image.open(imagen)
    pixels=imagenParaProcesar.load()
    width,height=imagenParaProcesar.size
    print width, height
    for i in range (width):
        for j in range(height):
            
            valorPimienta=random.randint(1,500)
            if(valorPimienta==350):
                negro=random.randint(0,10)
                pixels[i,j] = (0,0,0)
                
            if(valorPimienta==123):
                blanco=random.randint(200,255)
                pixels[i,j]=(255,255,255)
                
                

    rp,gp,bp=pixels[199,299]=((0,10,20))
    
    imagenParaProcesar.show()
    imagenParaProcesar.save("imagenConManchas.jpg")
    eliminarManchas(imagenParaProcesar)

def eliminarManchas(imagenManchada):
    #imagenManchada=Image.open("imagenConManchas.png")
    pix=imagenManchada.load()
    w,h= imagenManchada.size
    print w,h
    for i in range(w):
        for j in range(h):
            if(i>0 and i < w-1 and j>0 and j < h-1):
                r,g,b=pix[i,j]#toma el valor d grises del pixel actual
                rgb=(r,g,b)

                if (r,g,b) >= 0 or   or rgb == (255,255,255)):
                    r1,g1,b1=pix[i+1,j]#toma cada uno de los pixeles vecinos                                                                         
                    r2,g2,b2=pix[i-1,j]#y saca el promedio                                                                                           
                    r3,g3,b3=pix[i,j-1]
                    r4,g4,b4=pix[i,j+1]
                    newPix=(((r1+g1+b1)/3)+((r2+g2+b2)/3)+((r3+g3+b3)/3)+((r4+g4+b4)/3))/4

                    pix[i,j]=(newPix,newPix,newPix)
    imagenManchada.show()

def main():
    load(imageArgument)

main()
