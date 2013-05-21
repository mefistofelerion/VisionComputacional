#!/usr/bin/env python
import cv2.cv as cv
import numpy as np
import cv2

class AutoDetectTag:

    def run(self):#inicializa video
        cv.NamedWindow("captura", 1)
        self.capture=cv.CaptureFromCAM(0)
        frame_inicial=cv.QueryFrame(self.capture)#frame del video
        frame_size = cv.GetSize(frame_inicial)
	#se convierte a escala de grises para poder procesar la imagen
        grey_image = cv.CreateImage(frame_size, cv.IPL_DEPTH_8U,1)
	#creamos una imagen con diferente formato de 3 canales
        moving = cv.CreateImage(cv.GetSize(frame_inicial),cv.IPL_DEPTH_32F,3)
        difference = None
        control=0
	#aqui un loop para detectar movimiento en la camara
        while True:
	    #se obtiene el nuevo frame cada cierto tiempo
            imagen_tiempo_real = cv.QueryFrame(self.capture)
	    #se elimina el ruido de la imagen 
            cv.Smooth(imagen_tiempo_real, imagen_tiempo_real, cv.CV_GAUSSIAN, 3, 0)
            if not difference:
                difference = cv.CloneImage(imagen_tiempo_real)
                temp = cv.CloneImage(imagen_tiempo_real)
                cv.ConvertScale(imagen_tiempo_real, moving, 1.0, 0.0)
            else:
                cv.RunningAvg(imagen_tiempo_real, moving, 0.020, None)
            #se convierte a una imagen scalar
            cv.ConvertScale(moving, temp, 1.0, 0.0)
	    #se calcula la diferenciacion entre imagenes
            cv.AbsDiff(imagen_tiempo_real, temp, difference)
            #se hace una conversion a escala de grises
            cv.CvtColor(difference, grey_image, cv.CV_RGB2GRAY)
	    #se obtienen los bordes de la imagen
            cv.Threshold(grey_image,grey_image, 70, 255, cv.CV_THRESH_BINARY)
	    #se dilatan los bordes
            cv.Dilate(grey_image, grey_image, None, 18)
	    #se hace erosion en la imagen
            cv.Erode(grey_image, grey_image,None, 10)
	    
            storage = cv.CreateMemStorage(0)
            #se buscan los contornos en la imagen para ver si hay movimiento
            contour = cv.FindContours(grey_image, storage, cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)
            points = []
	    
            if not contour:
                print "no hay movimiento"
            else:
                print "si hay movimiento"
                
                self.detecta_gafet(imagen_tiempo_real)
            cv.ShowImage("captura", imagen_tiempo_real)
            #si se presiona la tecla ESC se cerrara la aplicacion
            if cv.WaitKey(20) == 27:
                break
        cv.DestroyAllWindows()



    def detecta_gafet(self, frame_inicial):
	'''se abre una imagen tomada en el instante que se detecta movimiento con la finalidad de procesarla'''
        from glob import glob
        cv.SaveImage("output.png", frame_inicial)
        for fn in glob('output.png'):
            img=cv2.imread(fn)
	    #se elimina ruido con blur
            img = cv2.GaussianBlur(img, (5, 5), 0)
            squares = []
	    '''si se encuentran contornos parecidos alos de un rectangulo es un gafet'''
            for gray in cv2.split(img):
                for thrs in xrange(0, 255, 26):
                    if thrs == 0:
			#se sacan los bordes y los dilata
                        bin = cv2.Canny(gray, 0, 50, apertureSize=5)
                        bin = cv2.dilate(bin, None)
                    else:
                        retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
                    contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                    for cnt in contours:
                        cnt_len = cv2.arcLength(cnt, True)
                        cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
                        if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
                            cnt = cnt.reshape(-1, 2)
                            max_cos = np.max([self.angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
			#si coincide la aproximacion es un rectangulo
                            if max_cos < 0.1:
                                squares.append(cnt)
        if squares:
            print "si hay gaffete"
        else:
            self.detect()
	#funcion para facilitar la deteccion de los angulos para saber si es un rectangulo-cuadrado
    def angle_cos(self,p0, p1, p2):
        d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
        return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

    def detect(self,frame):
        image_size=cv.GetSize(frame)
        grey=cv.CreateImage(image_size,8,1)
	#se transforma en escala de grises
        cv.CvtColor(frame, grey, cv.CV_BGR2GRAY)
	#el cascade para facilitar la deteccion de patrones
        cascade = cv.Load('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
	#la deteccion de haar 
        faces= cv.HaarDetectObjects(grey,cascade,cv.CreateMemStorage(),1.2,2,cv.CV_HAAR_DO_CANNY_PRUNING)
        if faces:
            for i in faces:
                cv.Rectangle(frame,(i[0][0], i[0][1]),
                         (i[0][0] + i[0][2], i[0][1] + i[0][3]),
                         (255, 0, 0),
                         3,
                         8,
                         0)
        if(control<2):
            cv.SaveImage("cara.png", frame)
            control+=1
            
        
if __name__=="__main__":
    demo=AutoDetectTag()
    demo.run()
