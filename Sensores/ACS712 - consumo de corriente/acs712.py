from machine import Pin, ADC
import time

class ACS712:
    def __init__(self, pin, sensitivity=0.185):
        self.adc = ADC(Pin(pin))        
        self.max_adc_value = 4095        
        self.vcc_voltage = 3.3
        self.sensitivity = sensitivity
        self.offset_adc = 0
        self.calibrate()

    def calibrate(self, num_samples=1000):
        sum_adc = 0
        for _ in range(num_samples):
            sum_adc += self.adc.read_u16() if hasattr(self.adc, 'read_u16') else self.adc.read()
            time.sleep_us(100) 
        self.offset_adc = sum_adc // num_samples

    def read_current(self):
        adc_value = self.adc.read_u16() if hasattr(self.adc, 'read_u16') else self.adc.read()        
        voltage = (adc_value - self.offset_adc) * (self.vcc_voltage / self.max_adc_value)
        current = voltage / self.sensitivity        
        return current