# MAX6675 - Thermocouple 

El MAX6675 es un módulo que se utiliza principalmente en entornos donde se requieren mediciones de temperaturas elevadas gracias a su amplio rango y precisión. Convierte la pequeña señal eléctrica generada por la termocupla, proporcional a la temperatura medida, en un valor digital que puede ser interpretado fácilmente por el sistema. Este dispositivo permite medir temperaturas que van desde 0°C hasta 1024°C, con una resolución de 0,25°C, e incluye compensación interna de temperatura ambiente para mejorar la precisión de la lectura. 

# Uso aplicado en el LED SMD de Newton

El módulo DS1302 se utiliza para registrar con precisión la fecha y hora exactas en las que comienzan a observarse anomalías en el comportamiento del LED SMD, como fallos en la soldadura, parpadeos anómalos o funcionamiento errático. Esta información temporal se correlaciona con datos físicos obtenidos del entorno, con el objetivo de analizar las posibles causas de deterioro del LED.

En este contexto, el sensor de temperatura MAX6675, conectado a una termocupla tipo K, juega un rol fundamental, ya que permite medir con alta precisión la temperatura real y localizada en la zona del LED. A diferencia del DHT11 —que solo brinda valores generales de temperatura y humedad ambiente— el MAX6675 proporciona datos térmicos exactos del punto crítico, permitiendo detectar calentamientos excesivos que podrían causar daños directos en la soldadura o afectar el rendimiento del LED.

Registrar esta temperatura directamente sobre o cerca del LED resulta crucial para establecer relaciones claras entre el aumento térmico localizado y los fallos observados. Así, se pueden validar hipótesis como la degradación del LED por exceso de calor, errores de disipación térmica, o condiciones extremas de operación.

# Conexiones aplicadas para el uso 

| Conexiones | MAX6675       | Raspberry Pi Pico |
|:------------|:-------------|:-----------------|
| Tierra | VCC     | GND (Pin 36)       |
| Alimentacion       | VCC | GP15 (Pin 21)      |
| Clock      | Clock  | GND (Pin 38)       |
| Chip Select | 
| Data Out | SPI SO |

# Imagen de las Conexiones

![](img/Conexiones%20Raspberry%20y%20MAX6675.png)

# Especificaciones del DHT11

[MAX6675 Datasheet - Maxim Integrated Products ](https://www.alldatasheet.com/datasheet-pdf/view/73692/MAXIM/MAX6675.html)