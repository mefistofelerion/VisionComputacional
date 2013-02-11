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
            ''' #despues pasara por varios filtros
            for w in range(1):
            for i in range(width):
            for j in range(height):
            r,g,b=pixels[i,j]
            gray=int((r+g+b)/3)#saca el promedio de grises
            
            
            #primero checa todas las esquinas
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
            #despues checa todos los bordes
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
            #todo el resto de los pixeles 
            else:
            r,g,b=(gray,gray,gray)#toma el valor d grises del pixel actual
            r1,g1,b1=pixels[i+1,j]#toma cada uno de los pixeles vecinos
            r2,g2,b2=pixels[i-1,j]#y saca el promedio
            r3,g3,b3=pixels[i,j-1]
            r4,g4,b4=pixels[i,j+1]
            newPix=(((r+g+b)/3)+((r1+g1+b1)/3)+((r2+g2+b2)/3)+((r3+g3+b3)/3)+((r4+g4+b4)/3))/5#promediado del nuevo pixel
            if(newPix>255):#solo para asegurar que el pixel no se pase del RGB
            newPix=255
                        
            pixels[i,j]=(newPix,newPix,newPix)#se reemplaza'''

    aplicarMascara(imageLoaded)


def aplicarMascara(imagen):
    #mascaraX= [[0,1,0],[1,-4,1],[0,1,0]]
    mascaraX= [[-1,0,1], [-2,0,2],[-1,0,1]]
    pixels=imagen.load()
    im=Image.open(original)
    pix=im.load()
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
                
    im.show()
    
def main():
    load()
main()