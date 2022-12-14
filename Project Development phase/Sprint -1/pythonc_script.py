
import time
import sys
import random
import ibmiot.application
import ibmiot.device
organization = "8lpjde"
deviceType = "Ultrasonic"
deviceId = "123654"
authMethod = "use-token-auth"
authToken = "qwerty1234"
try:
    deviceOptions = {"org": organization, "type": deviceType,"id": deviceId, "auth-method": authMethod, "auth-token":authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()
deviceCli.connect()
while True:
    temp=random.randint(0,100)
    Humid=random.randint(0,100)
    Gas=random.randint(0,100)

    data = { 'temp' : temp, 'Humid': Humid, 'Gas':gas }

    def myOnPublishCallback():
        print ("Published Temperature = %s C" % temp, "Humidity = %s %%" %Humid, "Gas Concentration = %s" %Gas )
    success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
    if not success:
        print("Not connected to IoTF")
    time.sleep(10)
    deviceCli.commandCallback = myCommandCallback
    
deviceCli.disconnect()

