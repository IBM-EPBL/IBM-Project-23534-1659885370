import random
import time

def CheckTemp(temperature):
    if temperature>70:
        print("Temperature is HIGH")
    else:
        print("Temperature Under Control")

while True:
    temp = random.randint(-40,100)
    humid = random.randint(0,100)
    print("Temperature = "+str(temp))
    print("Humidity = "+str(humid))
    CheckTemp(temp)
    time.sleep(2)