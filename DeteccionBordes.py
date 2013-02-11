import PIL
import Tkinter
from Tkinter import*
import Image,ImageTk
import sys

original=sys.argv[1]
imageLoaded=Image.open(original)
show=Tkinter.Tk()
#imageLoaded = imageLoaded.resize((1024, 600))

def load(): 
   # show=Tkinter.Tk()
    show.title("Imagen de Bordes")
    tkimage=ImageTk.PhotoImage(imageLoaded)
    Tkinter.Label(show,image=tkimage).pack()
    b=Button(show,text="Mostrar Bordes", command=detectarBordes)
    b.pack(fill=BOTH)
    show.mainloop()
    
def detectarBordes():
#primero lo paso a grises
    pixels=imageLoaded.load()
    width,height=imageLoaded.size
    for i in range(width):
        for j in range(height):
            r,g,b=pixels[i,j]#toma el valor del pixel actual
            gray=int((r+g+b)/3)#saca el promedio para la escala de grises
            pixels[i,j]=(gray,gray,gray)#lo reemplaza
          
            r,g,b=pixels[i,j]
            gray=int((r+g+b)/3)#saca el promedio de grises
            
    imagenConMascara=aplicarMascara(imageLoaded)
    imagenConMascara.show()

def aplicarMascara(imagen):
    #mascaraX= [[0,1,0],[1,-4,1],[0,1,0]]
    mascaraX= [[-1,0,1], [-2,0,2],[-1,0,1]]
    pixels=imagen.load()
    nuevaImagen=Image.open(original)
    pix=nuevaImagen.load()
    wid,hei=imagen.size 
    for i in range(wid):
        for j in range(hei):
            if (i > 0 and i < wid-1 and j > 0 and j < hei-1):
                ra,ga,ba=pixels[i-1,j-1]
                rb,gb,bb=pixels[i-1,j]
                rc,gc,bc=pixels[i-1,j+1]
                rd,gd,bd=pixels[i,j-1]
                re,ge,be=pixels[i,j]
                rf,gf,bf=pixels[i,j+1]
                rg,gg,bg=pixels[i+1,j-1]
                rh,gh,bh=pixels[i+1,j]
                ri,gi,bi=pixels[i+1,j+1]
                matrizDePixeles=[[ra,rb,rc],[rd,re,rf],[rg,rh,ri]]
                newPix = (ra*mascaraX[0][0])+(rb*mascaraX[0][1])+(rc*mascaraX[0][2])+(rd*mascaraX[1][0])+(re*mascaraX[1][1])+(rf*mascaraX[1][2])+(rg*mascaraX[2][0])+(rh*mascaraX[2][1])+(ri*mascaraX[2][2])
                
                pix[i,j] = (newPix,newPix,newPix)
                
            else:
                None
                
    return nuevaImagen
    
def main():
    load()
main()
