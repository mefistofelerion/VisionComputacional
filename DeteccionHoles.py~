import PIL
import Tkinter
import Image
import numpy as nump
import random
import ImageDraw
from sys import argv


def encuentraAgujeros(imagen,vertical,horizontal):
  w,h=imagen.size
  ori=Image.open(argv[1])
  d=ImageDraw.Draw(ori)
  pixeles=ori.load()
  for x in horizontal:
    for y in vertical:
      (x1, y1), (x2, y2) = (y-(8), x-(8)), (y+(8), x+(8))
      comienzo=area(imagen,(x1,y1),(x2,y2))
      lon,coords=bfs(imagen,comienzo)
      sumatoria=[sum(n) for n in zip(*coords)]
      centro=(sumatoria[0]/len(coords), sumatoria[1]/len(coords))
      pixeles[centro]=(255,0,0)
      draw.ellipse(((centro[0]-8,centro[1]-8),(centro[0]+8,centro[1]+8)),outline=((120,50,120)),fill=((160,140,175)))
      
def area(imagen,(x1,y1),(x2,y2)):
  w,h=imagen
  pixeles=imagen.load()
  area=abs(x2-x1)* abs(y2-y1)
  c=0
  for x in range (x1,x2):
    for y in range(y1,y2):
      if x>0 and x<w and y >0 and y < h:
        if pixeles[x,y]==(0,0,0):
          i,j=x,y
          c+=1
  if c > area * 0.2:
    return (i,j)
  

def binarizar(ima):
  w,h = ima.size
  pix = ima.load()
  newIma = Image.new('RGB',(w,h))
  pixeles = newIma.load()

  for i in range(w):
    for j in range(h):
      r,g,b = pix[i,j]
      if r > 30 or g > 30 or b>30:
        pixeles[i,j]= ((255,255,255))
      else:
        pixeles[i,j]=((0,0,0))
  return newIma

def bfs(im,origen,color=((255,255,0))):
  pix = im.load()
  w, h = im.size
  q = []
  coords = []
  q.append(origen)
  original = pix[origen]
  while len(q) > 0:
    (x, y) = q.pop(0)
    actual = pix[x, y]
    if actual == original or actual == color:
      for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
          i, j = (x + dx, y + dy)
          if i >= 0 and i < w and j >= 0 and j < h:
            contenido = pix[i, j]
            if contenido == original:
              pix[i, j] = color
              coords.append((i, j))
              q.append((i, j))
  return len(coords), coords

def histograma_vertical(ima):
  imagen2=ima.copy()
  pixeles=nump.array(imagen2.convert('L'))
  return [sum(x) for x in zip(*pixeles)]

def histograma_horizontal(ima):
  imagen2=ima.copy()
  pixeles=nump.array(imagen2.convert('L'))
  return [sum(y) for y in zip(*pixeles)]

def obtienePuntos(ori,orienta):
  puntos=[]
  maximo=max(ori)
  minimo=min(ori)
  media=(maximo+minimo)/2
  for i in range(1,len(ori)-1):
    if orienta==1:
      if(ori[i] > ori[i-1]) and (ori[i] > ori[i+1]):
        puntos.append(i)
        if ori[i] > media:
          puntos.append(i)
    if orienta==2:
      if(ori[i] < ori[i-1]) and (ori[i] < ori[i+1]):
        puntos.append(i)
        if ori[i]>media:
          puntos.append(i)
                                   


def main():
  image=Image.open(argv[1]).convert('RGB')
  imagebin=binarizar(image)
  histogramaVertical=histograma_vertical(imagebin)
  histogramaHorizontal=histograma_horizontal(imagebin)
  vertical=obtienePuntos(histogramaVertical,1)
  horizontal=obtienePuntos(histogramaHorizontal,2)
  encuentraAgujeros(imagebin,vertical,horizontal)

main()
