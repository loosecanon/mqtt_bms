import mosquitto
import boto
from boto import dynamodb2
from boto.dynamodb2 import table, types, fields
from datetime import datetime


def on_message(mosq, obj, msg):
	#print(msg.topic + ": " + msg.payload)
	top = msg.topic.split("/")
	print(top)
	loc = top[2]
	typ = top[3]
	pld = msg.payload.split("~")
	print("Payload: " + str(pld))
	dev = pld[0]
	stamp = pld[1]
	dat = pld[2]
	id = dev + "/" + stamp
	bo = dynamodb2.connect_to_region('us-west-2')
	tabl = dynamodb2.table.Table(table_name = top[1],
		schema = [fields.HashKey('id', data_type=fields.STRING), 
			fields.RangeKey('timestamp', data_type=fields.STRING), ],
		connection=bo)
	tabl.put_item(data = {
		'id': id,
		'timestamp': stamp,
		'location': loc,
		'type': typ,
		'data': dat
	})
	
	
client = mosquitto.Mosquitto("bfc_aws")
rc = client.connect("127.0.0.1", port = 1883)
client.on_message = on_message
topic = "bfcanon_test/#"
client.subscribe(topic)
while(1):
	client.loop()
