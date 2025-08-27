# Tabla de Conexiones de todos los Sensores 

| Conexiones     | ACS712  | Raspberry Pi Pico |
| :------------- | :------ | :---------------- |
| Alimentación   | VCC     | 3V (Pin 36)       |
| Tierra         | GND     | GND (Pin 23)      |
| Salida analógica | OUT   | GP26 (ADC0) (Pin 31)       |

| Conexiones | MAX6675       | Raspberry Pi Pico |
|:------------|:-------------|:-----------------|
| Tierra | GND    | GND (Pin 38)       |
| Alimentacion       | VCC | VSYS (Pin 39)      |
| Clock      | SCK  | GPIO 14 (SCK) (Pin 19)       |
| Chip Select |CS   | GPIO 13 (CSn) (Pin  17)      | 
| SPI SO      | SO |  GPIO 12 (Rx)   (Pin 16)  |

| Conexiones        | MicroSD  | Raspberry Pi Pico |
| :---------------- | :------- | :---------------- |
| Alimentación      | VCC      | VSYS (Pin 39)       |
| Tierra            | GND      | GND (Pin 38)      |
| Datos de salida   | MISO     | GP4 (SPI0 RX) (Pin 6)   |
| Datos de entrada  | MOSI     | GP3 (SPI0 TX) (Pin 5)   |
| Reloj SPI         | SCK      | GP2 (SPI0 SCK) (Pin 4) |
| Selección de chip | CS       | GP5 (SPI0 CSn)  (Pin 7) |

| Conexiones       | DS1302 | Raspberry Pi Pico |
| :--------------- | :----- | :---------------- |
| Alimentación     | VCC    | VSYS (Pin 39)     |
| Tierra           | GND    | GND (Pin 38)      |
| Reloj (CLK)     | CLK     | GPIO 18 (Pin 24)  |
| Datos (DAT)     | DAT     | GPIO 17 (Pin 22)  |
| RST              | RST    | GPIO  16 (Pin 21)  |

| Conexiones | DHT11       | Raspberry Pi Pico |
|:------------|:-------------|:-----------------|
| Alimentación | VCC     | VSYS (Pin 39)       |
| Datos        | DATA  | GP15 (Pin 20)      |
| Tierra       | GND    | GND (Pin 38)       |

Esta tabla tiene el fin de poder hacer más fácil y comodo el trabajo al hacer las conexiones de todos los sensores a la Raspberry Pi Pico.