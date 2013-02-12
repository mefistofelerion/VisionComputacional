import PIL
import Tkinter
from Tkinter import*
import Image,ImageTk
import sys,time

original=sys.argv[1]
imageLoaded=Image.open(original)
show=Tkinter.Tk()
#imageLoaded = imageLoaded.resize((1024, 650)) lo ocupo para redimensionar imagenes muy grandes

def load(): #se carga la imagen original
   # show=Tkinter.Tk()
    show.title("Imagen de Bordes")
    tkimage=ImageTk.PhotoImage(imageLoaded)
    Tkinter.Label(show,image=tkimage).pack()
    b=Button(show,text="Mostrar Bordes", command=detectarBordes)
    b.pack(fill=BOTH)
    show.mainloop()
    
def detectarBordes():
#primero lo paso a grises
    
    inicio=time.time()#para tomar el tiempo de inicio
    pixels=imageLoaded.load()
    width,height=imageLoaded.size
    for i in range(width):
        for j in range(height):
            r,g,b=pixels[i,j]#toma el valor del pixel actual
            gray=int((r+g+b)/3)#saca el promedio para la escala de grises
            pixels[i,j]=(gray,gray,gray)#lo reemplaza
          
            r,g,b=pixels[i,j]
            gray=int((r+g+b)/3)#saca el promedio de grises
            
    imagenConMascara=aplicarMascara(imageLoaded) #despues se pasa a que se le aplique la mascara
    final= time.time()#el tiempo al final de la ejecucion
    tiempoEjecucion=final-inicio #una simple resta para saber el tiempo total de ejecucion
    print tiempoEjecucion
    imagenConMascara.show()
    imagenConMascara.save("imagenBordes.jpg")

def aplicarMascara(imagen):

    #pregunto cual mascara utilizar
    mascara=int(raw_input("Elige la mascara\n1.-Sobel\n2.-Prewitt\n3.-Kirsch\n4.-Robinson 3-level\n5.-Robinson 5-level\nopcion: "))
    #utilizo diferentes mascaras dependiendo de la opcion
    if(mascara==1):
        mascaraX=[[-1,0,1],[-2,0,2],[-1,0,1]]
    if(mascara==2):
        mascaraX=[[-1,0,1],[-1,0,1],[-1,0,1]]
    if(mascara==3):
        mascaraX=[[-3,-3,5],[-3,0,5],[-3,-3,5]]
    if(mascara==4):
        mascaraX=[[1,1,1],[-1,-2,1],[-1,-1,1]]
    if(mascara==5):
        mascaraX=[[-1,0,1],[-2,0,2],[-1,0,1]]
    if(mascara==6):
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
                #hago la suma para el nuevo pixel
                newPix = (ra*mascaraX[0][0])+(rb*mascaraX[0][1])+(rc*mascaraX[0][2])+(rd*mascaraX[1][0])+(re*mascaraX[1][1])+(rf*mascaraX[1][2])+(rg*mascaraX[2][0])+(rh*mascaraX[2][1])+(ri*mascaraX[2][2])
                #el nuevo pixel lo ingreso en la nueva imagen
                pix[i,j] = (newPix,newPix,newPix)
                
            else:#detecta todo los bordes
                if(i == 0 and j>0):
                    ra,ga,ba=pixels[i,j-1]
                    rb,gb,bb=pixels[i,j]
                    rc,gc,bc=pixels[i,j+1]
                    rd,gd,bd=pixels[i+1,j-1]
                    re,ge,be=pixels[i+1,j]
                    rf,gf,bf=pixels[i+1,j+1]
                    matrizDePixeles=[[0,ra,rd],[0,rb,re],[0,rc,rf]]
                    newPix = (ra*mascaraX[0][1])+(rb*mascaraX[1][1])+(rc*mascaraX[2][1])+(rd*mascaraX[0][2])+(re*mascaraX[1][2])+(rf*mascaraX[2][2])
                    pix[i,j]=(newPix,newPix,newPix)
                if(i== wid and j>0):
                    ra,ga,ba=pixels[i,j-1]
                    rb,gb,bb=pixels[i,j]
                    rc,gc,bc=pixels[i,j+1]
                    rd,gd,bd=pixels[i-1,j-1]
                    re,ge,be=pixels[i-1,j]
                    rf,gf,bf=pixels[i-1,j+1]
                    matrizDePixeles=[[rd,ra,0],[re,rb,0],[rf,rc,0]]
                    newPix = (ra*mascaraX[0][1])+(rb*mascaraX[1][1])+(rc*mascaraX[2][1])+(rd*mascaraX[0][0])+(re*mascaraX[1][0])+(rf*mascaraX[2][0])
                    pix[i,j]=(newPix,newPix,newPix)
                if(j==0 and i>0):
                    ra,ga,ba=pixels[i-1,j]
                    rb,gb,bb=pixels[i,j]
                    rc,gc,bc=pixels[i+1,j]
                    rd,gd,bd=pixels[i-1,j+1]
                    re,ge,be=pixels[i-1,j+1]
                    rf,gf,bf=pixels[i-1,j+1]
                    matrizDePixeles=[[0,0,0],[ra,rb,rc],[rd,re,rf]]
                    newPix = (ra*mascaraX[1][0])+(rb*mascaraX[1][1])+(rc*mascaraX[1][2])+(rd*mascaraX[2][0])+(re*mascaraX[2][1])+(rf*mascaraX[2][2])
                    pix[i,j]=(newPix,newPix,newPix)

                if(j==hei and i>0):
                    ra,ga,ba=pixels[i-1,j]
                    rb,gb,bb=pixels[i,j]
                    rc,gc,bc=pixels[i+1,j]
                    rd,gd,bd=pixels[i-1,j-1]
                    re,ge,be=pixels[i-1,j-1]
                    rf,gf,bf=pixels[i-1,j-1]
                    matrizDePixeles=[[rd,re,rf],[ra,rb,rc],[0,0,0]]
                    newPix = (ra*mascaraX[1][0])+(rb*mascaraX[1][1])+(rc*mascaraX[1][2])+(rd*mascaraX[0][0])+(re*mascaraX[0][1])+(rf*mascaraX[0][2])
                    pix[i,j]=(newPix,newPix,newPix)
                    



    return nuevaImagen
    
def main():
    load()
main()
