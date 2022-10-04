#Let us consider the leds are connected at :red -> 22, amber -> 25 , green -> 20

from gpiozero import LED
from time import sleep
red = LED(22)
yellow = LED(25)
green = LED(20)

while (1):
    red.on()
    print("STOP")
    sleep(5)
    red.off()

    yellow.on()
    print("READY")
    sleep(2)
    yellow.off()

    green.on()
    print("Go")
    sleep(5)
    green.off()
    
    
