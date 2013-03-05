import PIL
import Tkinter
from Tkinter import *
import Image, ImageTk
import sys
from random import randint, random
from math import sqrt, ceil1, floor, fabs,atan2


original=sys.argv[1]#imagen tomada como argumento, la original
imageLoaded=Image.open(original)
show=Tkinter.Tk()

def load():# carga la imagen en la ventana
    show.title("Deteccion Circulos")
    tkimage=ImageTk.PhotoImage(imageLoaded)
    Tkinter.Label(show,image=tkimage).pack()
    b=Button(show,text="Mostrar circulos", command=detectarCirculos)
    b.pack(fill=BOTH)
    show.mainloop()


def detectarCirculos():#parte donde detecta los ciruclos
    mascarax=[[-1,0,1],[-2,0,2],[-1,0,1]]#mascara para gradiente x
    mascaray=[[1,2,1],[0,0,0],[-1,-2,-1]]#mascara para gradiente y
    gradientex=convolucion(imageLoaded, mascarax)#obtiene la gradiente
    print 'obtuvo gx'
    gradientey=convolucion(imageLoaded, mascaray)#obtiene la otra gradiente
    print 'obtuvo gy'
    imagen=Image.open(imageLoaded)
    
    cm,freq=centros(gradientex,gradientey,imagen)#encuentra los centros *aunque todavia con muchos errores
    
    for i in freq.keys():
        if freq[i]<30*8:
            freq.pop(i)
    
    marcarCirculos(imagen,freq,cm)#ya cuando se encuentran los circulos, los remarca
    imagen.show()
    imagen.save("CirculosDetectados.png",format"PNG")
        

def centros(x,y,imagen)#para encontrar los centros, aunque todavia tiene errores
    frq=dict()
    matriz=dict()
    w,h=imagen.size
    for i in range(w):
        for j in range(h):
            r,g,b=x[i,j]
            r2,g2,b2=y[i,j]

            gx=float(r+g+b)/3
            gy=float(r2+g2+b2)/3

            gradiente=sqrt(gx ** 2 +  gy ** 2)#gradiente total
            if gradiente < -1 * 10 or gradientes > 10:
                cosTheta=(gx/gradiente)#saco cos
                sinTheta=(gy/gradiente)#saco seno
                theta=atan2(gy,gx)#y saco teta
                radio=50

                centro=(int(i-radio*math.cos(theta+math.randians(90.0))),int(j-radio*math.sin(theta+math.radians(90.0))))#calculo los centros
                centro=((centro[0]/30)*10,(centro[1]/30)*30)
                matriz[i,j]=centro
                if not centro in frq:
                    frq[centro]=1
                else:
                    frq[centro]+=1
            else:
                matriz[i,j]=None
    return matriz,frq

def marcarCirculos(imagenls,freq,matriz):#para los circulos encontrados remarca los circulos
    imagen=imagenls.load()
    fuente=ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 10)
    draw=ImageDraw.Draw(imagen)
    con=1
    color=dict()
    for i in freq.keys():
        color[i]=((255),randint(150,255),randint(0,30))#solo para dar diferentes colores de amarillo
        r=2
        draw.ellipse((i[0]-r, i[1]-r, i[0]+r, i[1]+r), fill=(0, 255, 0))
        draw.text((i[0]+r+3, i[1]), ('Fig'+str(counter)), fill=(0, 255, 0),font=fuente)
        con+=1
    w,h=imagen.size
    for i in range(w):
        for j in range(h):
            if matriz[i,j] in freq:
                imagen[i,j]=color[matriz[i,j]]

    return image



                
def convolucion(imagen,mascara):#con la convolucion se obtienen las gradientes
    w, h = imagen.size
    pixels = imagen.load()
    imagenConMascara = Image.new('RGB', (w,h))
    pix = imagenConMascara.load()

    for x in range(w):
        for y in range(h):
            suma = 0
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    try:
                        suma += g[i - (x-1)][j - (y-1)] * pixels[i,j][1]
                    except:
                        pass
            pix[x,y] = (suma,suma,suma)
    return imagenConMascara











def main():
    load()

main()
    



