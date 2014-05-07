from twisted.internet import reactor, task
import mosquitto
from datetime import datetime

def runEverySecond():


client = mosquitto.Mosquitto("bfc_beaglebone")
rc = client.connect("ec2-54-201-108-65.us-west-2.compute.amazonaws.com", port = 1883, keepalive = 60)
messages = 0
last_min = datetime.now().minute
while rc == 0:
	now = datetime.now().minute
	if(now > last_min):
		print("sent message: " + str(messages))
		now = datetime.now()
		now = now.replace(microsecond = 0)
		rc = client.publish("bfcanon_test/8111ANNA/OFFICE/TEMP", "BBB_TEMP" + "~" + str(now) + "~42", 1)
		last_min = datetime.now().minute
	rc = client.loop()
	messages += 1
	
