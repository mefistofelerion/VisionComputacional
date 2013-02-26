import PIL
import Image
import sys

imageArgu=sys.argv[1]
def normalizacion(image):
    imagen=Image.open(image)
    pixeles=imagen.load()
    w,h=imagen.size
    for i in range(w):
        for j in range(h):
            if (i > 0 and i < w-1 and j > 0 and j < h-1):
                
                r,g,b=pixeles[i,j]
                rgb=r,g,b
                
                if(r>30 or g>30 or b>30):
                    rgb=((255,255,255))
                    pixeles[i,j]=rgb
                else:
                    rgb=((0,0,0))
                    pixeles[i,j]=rgb
                
            
            else:
                rgb=((0,0,0))
                pixeles[i,j]=rgb
    imagen.save("imagenNuevaNormalizada.png",format="PNG")
    imagen.show()

normalizacion(imageArgu)
    
