import PIL
import Tkinter
fro Tkinter import *
import Image,ImageTk

imageLoaded=Image.open("/imagenes/convex.png")
BLANCO=((255,255,255))

def load():
    
    show=Tkinter.Tk()
    show.title("convex hull")
    tkimage=ImageTk.PhotoImage(imageLoaded)
    Tkinter.Label(show,image=tkimage).pack()
    b=Button(show,text="Convex Hull",command=convexHull)
    b.pack(fill=BOTH)
    show.mainloop()

def convexHull():
    pixel=imageLoaded.load()
    w,h=imageLoaded.size
    nuevaImagen.imageLoaded.load()
    for i in range (w):
        for j in range(h):
            if pixel[i,j]==BLANCO:
                nuevaImagen=bfs(pixel,(i,j),((255,0,0)))
    
    
                

def bfs(ima,pizelOrigen,color):
    pix=ima.load()
    w,h=ima.size

    colar=list()
    pixelOriginal = pix[w,h]
    cola.append(pixelOrigen)

    while len(cola) > 0:
        (wid,hei)=cola.pop(0)
        pixelActual=pix[wid,hei]
        if pixelActual == pixelOriginal or pixelActual == color:
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    i,j=(wid+dx,hei+dy)
                    if i >= 0 and i < w and j >=0 and j<h:
                        aux=pix[i,j]
                        if aux==original:
                            pix[i,j]=color
                            cola.append((i,j))
    return ima
                        
    
