# DHT11 - Sensor de Temperatura y Humedad

es un sensor digital que mide temperatura y humedad relativa del ambiente. Utiliza un termistor para detectar la temperatura y un sensor capacitivo para medir la humedad, enviando los datos a un microcontrolador a través de un solo pin de datos.  Mide temperaturas de 0°C a 50°C y humedades del 20% al 80%. Es ideal para la toma de datos de nuestro proyecto ya que permite monitorear condiciones ambientales de forma sencilla y practica.

# Uso aplicado en el LED SMD de Newton

Este sensor se encarga de medir la temperatura y la humedad del ambiente para registrar las variaciones que afectan al LED SMD. El objetivo es determinar por qué, después de cierto tiempo, las soldaduras tienden a despegarse, a pesar de que esto solo debería ocurrir a temperaturas muy elevadas, las cuales se considera poco probable que se alcancen en condiciones normales.

# Conexiones aplicadas para el uso 

| Conexiones | DHT11       | Raspberry Pi Pico |
|:------------|:-------------|:-----------------|
| Alimentación | VCC     | 3V3 (Pin 36)       |
| Datos        | DATA  | GP15 (Pin 21)      |
| Tierra       | GND    | GND (Pin 38)       |


# Imagen de las Conexiones

![](img/Conexiones%20Raspberry%20y%20DHT11.png)

# Especificaciones del DHT11

[DHT 11 Datasheet - Mouser Electronics](https://www.mouser.com/datasheet/2/758/DHT11-Technical-Data-Sheet-Translated-Version-1143054.pdf)