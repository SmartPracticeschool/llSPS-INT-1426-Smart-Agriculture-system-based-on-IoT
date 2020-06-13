import time
import sys
import ibmiotf.application
import ibmiotf.device
import requests

#Provide your IBM Watson Device Credentials
organization = "jour2i" # repalce it with organization ID
deviceType = "smart_agri" #replace it with device type
deviceId = "002-motor" #repalce with device id
authMethod = "token"
authToken = "Mahesh@123"#repalce with token
str="cmd"

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
        if cmd.data['command']=='motoron':
                print
                print("MOTOR ON")
        elif cmd.data['command'] == 'motoroff':
            print("MOTOR OFF")
        str=cmd.data['command']
        data={'command':str}
        success = deviceCli.publishEvent("event", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")


try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................

except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:

        #Send weather conditions from API to IBM Watson
        response=requests.get("http://api.openweathermap.org/data/2.5/weather?q=Mumbai, IN&appid=80a19d6af38283c126f2021f4145bfea")

        #print data
        def myOnPublishCallback():
            print(response.content)

        time.sleep(1)

        deviceCli.commandCallback = myCommandCallback


# Disconnect the device and application from the cloud
deviceCli.disconnect()
