import smbus 

class MCP4725:
    def __init__(self, dynamic_range, verbose = True):
        self.bus = smbus.SMBus(1)
        self.address = 0x4D
        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()
    
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, Старший байт: {upper_data_byte:x}, Младший байт: {lower_data_byte:x}, Число:{number}")
        return number

    def get_voltage(self):
        return self.dynamic_range * self.get_number() / 1024

if __name__ == "__main__":
    try:
        adc = MCP4725(5.2)
        while True:
            voltage = adc.get_voltage()
            print(f"Напряжение: {voltage}")
    finally:
        adc.deinit()