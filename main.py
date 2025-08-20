from machine import Pin, SPI
import os
import sdcard 
import time
import dht
import temp_read
import ds1302
import acs712

# Configuracion DHT11
sensor_dht11 = dht.DHT11(Pin(15))

# Configuracion MAX6675
sck = Pin(2, Pin.OUT)
cs = Pin(3, Pin.OUT)
so = Pin(4, Pin.IN)
sensor_max6675 = temp_read.MAX6675(sck, cs , so)

# Configuracion DS1302
ds_rtc = ds1302.DS1302(Pin(0), Pin(1), Pin(5))

# Configuracion ASC712
sensor_acs712 = acs712.ACS712(pin=28, sensitivity=0.185)

# Configuracion tarjeta SD
cs = Pin(13, Pin.OUT) 
sck = Pin(10)         
mosi = Pin(11)      
miso = Pin(12)        
spi = SPI(1, baudrate=1000000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)

try:
    # Inicializaxion de la tarjeta SD y del sistema de archivos
    sd = sdcard.SDCard(spi, cs)
    os.mount(sd, '/sd')

    # Ruta del archivo en la tarjeta SD
    file_path = '/sd/data_logger.csv'

    # Abre el archivo en modo de añadir ('a') para no sobrescribir datos viejos
    # y añade el encabezado si el archivo no existe.
    if 'data_logger.csv' not in os.listdir('/sd'):
        with open(file_path, 'w') as f:
            f.write("Fecha,Hora,Temperatura_DHT11,Humedad_DHT11,Temperatura_MAX6675,Error_MAX6675,Corriente_ACS712\n")

    print("Tarjeta SD montada y lista. Se iniciará el registro de datos.")
    
    while True:
        dt = ds_rtc.date_time()
        fecha = "{:04d}-{:02d}-{:02d}".format(dt[0], dt[1], dt[2])
        hora = "{:02d}:{:02d}:{:02d}".format(dt[4], dt[5], dt[6])

        sensor_dht11.measure()
        temp_dht = sensor_dht11.temperature()
        hum_dht = sensor_dht11.humidity()

        temp_max = sensor_max6675.read()
        error_max = sensor_max6675.error()

        current_acs = sensor_acs712.read_current()

        # Formato para la consola
        print("--- Nueva Lectura ---")
        print(f"Fecha: {fecha}")
        print(f"Hora de Lectura: {hora}")
        print(f"Temperatura (DHT11): {temp_dht} grados C")
        print(f"Humedad (DHT11): {hum_dht}%")
        print(f"Temperatura (MAX6675): {temp_max} grados C")
        print(f"Error (MAX6675): {error_max}")
        print(f"Corriente (ACS712): {current_acs} A")
        
        linea_de_datos = "{},{},{},{},{},{},{}\n".format(
            fecha,
            hora,
            temp_dht,
            hum_dht,
            temp_max,
            error_max,
            current_acs
        )
        
        with open(file_path, 'a') as registro_sd:
            registro_sd.write(linea_de_datos)
        
        time.sleep(10)
        
except KeyboardInterrupt:
    print("Finalizando el data logger...")
    os.umount('/sd')
    print("Tarjeta SD desmontada.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
    try:
        os.umount('/sd')
    except:
        pass