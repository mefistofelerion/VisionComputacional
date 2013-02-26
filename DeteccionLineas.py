import PIL 
import Tkinter
from Tkinter import *
import Image,ImageTk
import sys
from math import sqrt,sin,cos,atan,fabs,floor,ceil

imageArgu=sys.argv[1]
def load():#cargo la imagen dentro dela ventana
    imagen=Image.open(imageArgu)
    show=Tkinter.Tk()
    show.title("deteccion de lineas")
    tkimage=ImageTk.PhotoImage(imagen)
    Tkinter.Label(show,image=tkimage).pack()
    b=Button(show,text="Mostrar Lineas", command=detectarLineas)
    b.pack(fill=BOTH)
    show.mainloop()
    

def detectarLineas():
    imagenOriginal=Image.open("ecuadrado.png")#utilizo la imagen original para sacar las gradientes
    imagenBinaria=Image.open("imagenBuena.png")#utilizo la imagen ya binarizada anteriormente
    lineas=deteccion(imagenOriginal,imagenBinaria,10)
    print 'terminado'
    

def deteccion(original,image,umbral):
    mascaraX=[[-1,0,1],[-2,0,2],[-1,0,1]]
    mascaraY=[[1,2,1],[0,0,0],[-1,-2,-1]]
    gradx = convolucion(original, mascaraX)
    grady = convolucion(original, mascaraY)
    gx = gradx.load()
    gy = grady.load()
    w,h = image.size
    combin = {}
    pixels = original.load()
    matriz = list()

    for x in range(w):
        listaFila = list()
        for y in range(h):
            horiz = gx[x,y][0]
            verti = gy[x,y][0]

            if fabs(horiz) + fabs(verti) <= 0.0:#nada en ninguna direccion
                theta = None
            elif horiz == 0 and verti == 255:
                theta = 90
            elif fabs(horiz) > 0.0:
                theta = atan(fabs(verti/horiz))
            if theta is not None:
                rho = fabs( x * cos(theta) + y * sin(theta))
                
                if x > 0 and x < w-1 and y > 0 and y < h-1:
                    if (rho, theta) in combin:
                        combin[ (rho, theta) ] += 1
                    else:
                        combin[ (rho, theta) ] = 1
                listaFila.append( (rho, theta) )
            else:
                listaFila.append((None,None))
        matriz.append(listaFila)

    incluir = int(ceil (len(combin) * umbral))
    
    frec = frecuentes(combin, incluir)

    for x in range(w):
        for y in range(h):
            if x > 0 and x< w-1 and y > 0 and y < h-1:
                rho, theta = matriz[x][y]
                    
                if (rho, theta) in frec:
                    if theta == 0:
                        pixels[x,y] = (255,0,0)
                    elif theta == 90:
                        pixels [x,y] = (0,0,255)
    original.save('deteccionDeLineas.png',format="PNG")

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
    

def frecuentes(histo, cantidad):
    frec = list()
    for valor in histo:
        if valor is None:
            continue
        frecuencia = histo[valor]
        acepta = False
        if len(frec) <= cantidad:
            acepta = True
        if not acepta:
            for (v, f) in frec:
                if frecuencia > f:
                    acepta = True
                    break
        if acepta:
            frec.append((valor, frecuencia))
            frec = sorted(frec, key = lambda tupla: tupla[1])
            if len(frec) > cantidad:
                frec.pop(0)
    incluidos = list()
    for (valor, frecuencia) in frec:
        incluidos.append(valor)
    return incluidos

def main():
    load()
main()
