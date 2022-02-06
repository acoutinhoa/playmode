modulor='/Users/alien/x3/x/qdd/playmode/img/escala1.png'
imgw,imgh=imageSize(modulor)

e=226/imgh

humano=BezierPath()
humano.traceImage(modulor,threshold=0.6, blur=None, invert=False, turd=2, tolerance=0.2, offset=None)

size(imgw*e,imgh*e)
print(height())
scale(e)
fill(0,0,1)
drawPath(humano)