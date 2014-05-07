from twisted.internet import reactor, task
import mosquitto
from datetime import datetime

messages = 0
client = mosquitto.Mosquitto("bfc_beaglebone")
l = task.LoopingCall(runEveryMinute)
rc = 0

def __main__():
    rc = client.connect("ec2-54-201-108-65.us-west-2.compute.amazonaws.com", port = 1883, keepalive = 60)
    l = task.LoopingCall(runEveryMinute)
    l.start(60.0)

def runEveryMinute():
    now = datetime.now()
    now = now.replace(microsecond = 0)
    print("sent message: " + str(messages))
    messages = messages + 1
    rc = client.publish("bfcanon_test/8111ANNA/OFFICE/TEMP", "BBB_TEMP" + "~" + str(now) + "~42", 1)
    if rc != 0:
        print("RC != 0, rc = " + str(rc))
        l.stop()



