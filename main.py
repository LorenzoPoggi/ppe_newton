from machine import Pin
import time
import dht
import temp_read 
import ds1302 
import dht11

# DHT11 pines
dht11 = dht.DHT11(Pin(15))

# MAX6675 pines
sck = Pin(2, Pin.OUT)
cs = Pin(3, Pin.OUT)
so = Pin(4, Pin.IN)
max6675 = MAX6675(sck, cs , so)

# DS1302 registros
DS1302_REG_SECOND = (0x80)
DS1302_REG_MINUTE = (0x82)
DS1302_REG_HOUR   = (0x84)
DS1302_REG_DAY    = (0x86)
DS1302_REG_MONTH  = (0x88)
DS1302_REG_WEEKDAY= (0x8A)
DS1302_REG_YEAR   = (0x8C)
DS1302_REG_WP     = (0x8E)
DS1302_REG_CTRL   = (0x90)
DS1302_REG_RAM    = (0xC0)

registro = open ("Users/lorenzo.poggi/Documents/GitHub/ppe_newton/data_logger.txt", "w+")

while True:
    