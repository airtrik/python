import time
import paho.mqtt.client as mqtt
import ssl
import os
import requests



welcome_message = """

 █████╗ ██╗██████╗ ████████╗██████╗ ██╗██╗  ██╗    ██╗ ██████╗ ████████╗     ██████╗██╗      ██████╗ ██╗   ██╗██████╗ 
██╔══██╗██║██╔══██╗╚══██╔══╝██╔══██╗██║██║ ██╔╝    ██║██╔═══██╗╚══██╔══╝    ██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗
███████║██║██████╔╝   ██║   ██████╔╝██║█████╔╝     ██║██║   ██║   ██║       ██║     ██║     ██║   ██║██║   ██║██║  ██║
██╔══██║██║██╔══██╗   ██║   ██╔══██╗██║██╔═██╗     ██║██║   ██║   ██║       ██║     ██║     ██║   ██║██║   ██║██║  ██║
██║  ██║██║██║  ██║   ██║   ██║  ██║██║██║  ██╗    ██║╚██████╔╝   ██║       ╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝    ╚═╝ ╚═════╝    ╚═╝        ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ 

"""


apiEndPoint = "https://airtrik.com/iot/"
logsEndPoint = "https://airtrik.com/api/logs/"
client = mqtt.Client()
AIRTRIK_key = ""
AIRTRIK_APP_name = ""

IS_CONNECTED = False

def connect(key):
	global AIRTRIK_key
	global client
	global IS_CONNECTED
	global AIRTRIK_APP_name
	if IS_CONNECTED:
		return

	AIRTRIK_key = key

	payload = {'key': key}
	try:
		res = requests.post(apiEndPoint, data=payload).json()
		username = res['username']
		password = res['password']
		AIRTRIK_APP_name = res['name']

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
	IS_CONNECTED = True


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


def logs(key=0):
	if key == 0:
		key = AIRTRIK_key
	payload = {'key': key}
	res = requests.post(logsEndPoint, data=payload)
	f = open(AIRTRIK_APP_name+".csv", "w")
	f.write(res.text)
	f.close()
	return AIRTRIK_APP_name+".csv"


def waitForMessage():
	try:
		print(welcome_message)
		# print("Waiting for message.")
		while True:
			pass
	except KeyboardInterrupt:
		print()
		print("Disconnecting...")
		print("Good Luck !!")
		return