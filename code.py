from adafruit_circuitplayground.express import cpx
import time

blueval = 200
orange = (34,100,100)
purple = (5,512,12)
off = (0,0,0)


 while True:   
    for i in range(0,100):
        cpx.pixels[i] =purple
        print (i)
        time sleep (0.5)
        
    cpx.pixels.fill(off)
    
    




