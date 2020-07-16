import airtrik.iot as iot

device = "bulb"

def onConnect():
	print("Connected To Network")
	# print(iot.logs())

def onReceive(deviceId, message):
	print(device, message)


iot.onConnect = onConnect
iot.onReceive = onReceive

iot.connect("__APP_KEY__")
iot.subscribe(device)

# print(iot.logs())
iot.waitForMessage()


# while True:
# 	msg = input("Enter The Message to send\n")
# 	iot.send(device, msg)
