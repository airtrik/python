import airtrik.iot as iot

device1 = "bulb"
device2 = "fan"

def onConnect():
	print("Connected To Network")

def onReceive(deviceId, message):
	if deviceId == device1:
		print(device1, message)
	if deviceId == device2:
		print(device2, message)


iot.onConnect = onConnect
iot.onReceive = onReceive

iot.connect("__APP_KEY__")
iot.subscribe(device1)
iot.subscribe(device2)

# iot.waitForMessage()


while True:
	msg = input("Enter The Message to send\n")
	iot.send(device1, msg)
