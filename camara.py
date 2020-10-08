import picamera
import numpy as np
import paho.mqtt.client as mqtt
import imutils
from imutils.video import VideoStream
from time import sleep
from lib.color import *
from lib.progress import *

# Set up MQTT client
client = mqtt.Client()
client.connect("128.199.208.181", 1883, 60)
console("info","connecting to MQTT broker...")
sleep(2)
client.loop_start()

# Open camera
resolution = (1024, 768)
vs = VideoStream(                   \
    usePiCamera = True,                 \
    resolution = resolution,             \
    framerate = 2                       \
).start()
console("info","Opening Camera...")
startProgress("Opening Camera")
for _ in range(10):
    sleep(1)
    progress(10*_)
endProgress()
sleep(1)

# Capture frames
console("info","Capturing frames")
newwidth = 600
newheight = 400
while True:
    frame = imutils.resize(vs.read(), width=newwidth, height=newheight)
    client.publish("camera",frame)
    sleep(0.5)