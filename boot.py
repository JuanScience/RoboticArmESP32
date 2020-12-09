try:
  import usocket as socket
except:
  import socket

from machine import Pin, PWM
import network
import time

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'USUARIO'
password = 'PASSWORD'

estacion = network.WLAN(network.STA_IF)

estacion.active(True)
estacion.connect(ssid, password)

while estacion.isconnected() == False:
  pass

print('Connection successful')

pwmMiddle = PWM(Pin(15), freq = 50, duty = 70)
pwmLeft = PWM(Pin(2), freq = 50, duty = 70)
pwmRight = PWM(Pin(16), freq = 50, duty = 70)
pwmClaw = PWM(Pin(4), freq = 50, duty = 70)
