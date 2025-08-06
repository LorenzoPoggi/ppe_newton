# ------- Codigo DHT11 con MicroPython -------
# Este código lee la temperatura y humedad de un sensor DHT11 conectado a una Raspberry Pi
import dht
from machine import Pin
import time

sensor = dht.DHT11(Pin(15))  # Usás GP15 o el que quieras

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    
    print("Temperatura: {} grados".format(temp))
    print("Humedad: {}%".format(hum))
    time.sleep(2)