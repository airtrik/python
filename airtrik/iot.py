import time
import paho.mqtt.client as mqtt
import ssl
import os
import requests

apiEndPoint = "https://airtrik.com/iot/"
client = mqtt.Client()
AIRTRIK_key = ""

IS_CONNECTED = False

def connect(key):
	global AIRTRIK_key
	global client

	AIRTRIK_key = key

	payload = {'key': key}
	try:
		res = requests.post(apiEndPoint, data=payload).json()
		username = res['username']
		password = res['password']
	except Exception as e:
		raise Exception("Ubable to connect please check app key")
		return
	
	
	client.on_connect = on_connect
	client.on_message = on_message
	# client.on_subscribe = on_subscribe

	client.tls_set()
	client.tls_insecure_set(True)
	client.username_pw_set(username, password)
	client.connect("airtrik.com", 8883, 60)


def onConnect():
	print("Connected")

def on_connect(client, userdata, flag, rc):
	if rc == 0:
		global IS_CONNECTED
		IS_CONNECTED = True
		onConnect()
	else:
		raise Exception("Ubable to connect please check app key")
		return

def onReceive(deviceId, msg):
	print("Device Id : ", deviceId)
	print("Message : ", msg)

def on_message(cleint, userdata, message):
	topic = message.topic
	deviceId = topic.split("/")[1]
	msg = str(message.payload.decode('utf-8'))
	onReceive(deviceId, msg)

def send(deviceId, msg):
	client.publish(AIRTRIK_key+"/"+deviceId, msg)

def subscribe(deviceId):
	client.subscribe(AIRTRIK_key+"/"+deviceId, 2)
	client.loop_start()




