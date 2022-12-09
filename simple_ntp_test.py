import network
import socket
import time
import struct
from machine import Pin
import simple_ntp

led = Pin("LED", Pin.OUT)

ssid = 'your_ssid'
password = 'your_password'

hour_pins = [machine.Pin(0), machine.Pin(1), machine.Pin(2), machine.Pin(3), machine.Pin(4)]
minute_pins = [machine.Pin(5), machine.Pin(6), machine.Pin(7), machine.Pin(8), machine.Pin(9)]
second_pins = [machine.Pin(10), machine.Pin(11), machine.Pin(12), machine.Pin(13), machine.Pin(14)]

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

led.on()
simple_ntp.set_time()
print(time.localtime())
led.off()
