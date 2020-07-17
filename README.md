# Airtrik python

Airtrik is an IoT Cloud platform for managing communication between IoT devices and software platforms.
This is python sdk that can be used for communicating to both IoT device running python as a programming language like Raspberry Pi 
and software platform running python. This library can also be used for making realtime data pipeline for applying machine learning on the IoT devices.

## Summary

  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
    - [Connecting to your App's Network](#connecting-to-your-Apps-Network)
    - [Subscribe to device in App's Network](#subscribe-to-device-in-Apps-Network)
    - [Sending message to device](#sending-message-to-device)
    - [Receiving messages from device](#receiving-messages-from-device)
  - [Versioning](#versioning)
  - [Authors](#authors)
  - [License](#license)

## Getting Started

Follow the below instructions to get your device and application up and running within minutes. It is very easy to integrate airtrik into your project.

### Prerequisites

Before proceeding further you have the following software installed in your system or development system.

    python (Version > 3.5)
    pip (any recent version)

### Installing

Installing airtrik python library is straight forward, just install it with pip. Although it will work pretty well with your system python.
We recommend using the virtual environment for your project

```
pip install airtrik
```

### Connecting to your App's Network

```python

import airtrik.iot as iot

# create app in the panel to get the app key
iot.connect("__APP_KEY__")

```
### Subscribe to device in App's Network

```python

# you have to create device inside app from panel
device = "__DEVICE_ID__"
iot.subscribe(device)

```

### Sending message to device

```python

message = "YOUR MESSAGE TO DEVICE"
iot.send(device, message)

```

### Receiving messages from device

```python

# you can write your custom function handling the incoming message
def onReceive(deviceId, message):
	print(deviceId, message)

iot.onReceive = onReceive

iot.waitForMessage()

```

## Versioning



## Authors

  - **Vishal Pandey** - *Written Python Library* -
    [vishal-pandey](https://github.com/vishal-pandey)

See also the list of
[contributors](https://github.com/airtrik/python/contributors)
who participated in this project.

## License

This project is licensed under the [MIT](LICENSE)
Creative Commons License - see the [LICENSE](LICENSE) file for
details



