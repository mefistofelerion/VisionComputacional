import PIL
import Tkinter
from Tkinter import*
import Image,ImageTk
import sys,random

original=sys.argv[1]
imageLoaded=Image.open(original)
show=Tkinter.Tk()


def load(): #se carga la imagen original
    # show=Tkinter.Tk()

    show.title("Imagen")
    tkimage=ImageTk.PhotoImage(imageLoaded)
    Tkinter.Label(show,image=tkimage).pack()
    b=Button(show,text="Detectar Figura", command=detectarFigura)
    b.pack(fill=BOTH)
    show.mainloop()

def detectarFigura():
    
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
    imagenConMascara.save("starBordes.png")
    imagenProcesar(imagenConMascara)
            
        

def aplicarMascara(imagen):
    
    mascaraX=[[0,1,0],[1,-4,1],[0,1,0]]
    pixels=imagen.load()
    nuevaImagen=Image.open(original)#nueva imagen con los bordes resaltados
    pix=nuevaImagen.load()
    wid,hei=imagen.size 
    for i in range(wid):
        for j in range(hei):#tomo los valores de cada pixel
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
                matrizDePixeles=[[ra,rb,rc],[rd,re,rf],[rg,rh,ri]]#los valores de los pixeles vecinos los pongo adentro de una matriz
                #saco el promedio del nuevo pixel
                newPix = (ra*mascaraX[0][0])+(rb*mascaraX[0][1])+(rc*mascaraX[0][2])+(rd*mascaraX[1][0])+(re*mascaraX[1][1])+(rf*mascaraX[1][2])+(rg*mascaraX[2][0])+(rh*mascaraX[2][1])+(ri*mascaraX[2][2])
                #el nuevo pixel lo ingreso en la nueva imagen
                pix[i,j] = (newPix,newPix,newPix)
                
                            

    return nuevaImagen
    
def imagenProcesar(imagenConMascara):#Aqui es donde la imagen es procesada pixel por pixel
    w, h = imagenConMascara.size
    pix = imagenConMascara.load()
    for i in range( w ):
        for j in range( h ):
            color = ( random.randint( 0, 255 ), random.randint( 0, 255 ), random.randint( 0, 255 ) )#genera color aleatorio en RGB
            if pix[ i, j ] == ( 255, 255, 255  ):#si es un borde blanco
                imagenConMascara = bfs( imagenConMascara, ( i, j ), color )# llamara al bfs
                                
    imagenConMascara.show()#al finalizar mostrara la imagen
                
def bfs(ima,pixelOrigen,color):#funcion del BFS
    pix = ima.load()
    w, h = ima.size
    
    cola=list()
    pixelOriginal = pix[ pixelOrigen ]#el pixel de donde vengo al momento de entrar al BFS
    cola.append( pixelOrigen )# almaceno el pixel de origen 

    while len( cola ) > 0: # Algoritmo de BFS
        ( wid, hei ) = cola.pop( 0 )
        pixelActual = pix[wid, hei]
        if pixelActual == pixelOriginal or pixelActual == color:
            for dx in [ -1, 0, 1 ]:
                for dy in [ -1, 0, 1 ]:
                    i, j = ( wid + dx, hei + dy )
                    if i >= 0 and i < w and j >= 0 and j < h:
                        variableAuxiliar = pix[ i, j ]
                        if variableAuxiliar == original:
                            pix[ i, j ] = color
                            cola.append( ( i, j ) )
    return ima



    
                       
def main():

    load()

main()
