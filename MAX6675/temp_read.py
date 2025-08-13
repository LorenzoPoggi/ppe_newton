import time
from machine import Pin

class MAX6675:
    MEASUREMENT_PERIOD_MS = 220

    def __init__(self, sck, cs, so):
        self._sck = sck
        self._sck.low()

        self._cs = cs
        self._cs.high()

        self._so = so
        self._so.low()

        self._last_measurement_start = 0
        self._last_read_temp = 0
        self._error = 0

    def _cycle_sck(self):
        self._sck.high()
        time.sleep_us(1)
        self._sck.low()
        time.sleep_us(1)

    def refresh(self):
        self._cs.low()
        time.sleep_us(10)
        self._cs.high()
        self._last_measurement_start = time.ticks_ms()

    def ready(self):
        return time.ticks_ms() - self._last_measurement_start > MAX6675.MEASUREMENT_PERIOD_MS

    def error(self):
        return self._error

    def read(self):
        if self.ready():
            self._cs.low()
            time.sleep_us(10)

            value = 0
            for i in range(12):
                self._cycle_sck()
                value += self._so.value() << (11 - i)

            self._cycle_sck()
            self._error = self._so.value()

            for i in range(2):
                self._cycle_sck()

            self._cs.high()
            self._last_measurement_start = time.ticks_ms()

            self._last_read_temp = value * 0.25

        return self._last_read_temp