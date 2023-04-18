class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    #snake case
    def __init__(self, start):
        """Creates serial generating machine from start number"""
        self.start = start
        self.current_serial_num = start
        # print(type(self.currentSerialNum))

    def generate(self):
        """Creates new serial number by incrementing current serial number by 1"""
        self.current_serial_num += 1

        return self.current_serial_num - 1
        # return self.currentSerialNum += 1

    def reset(self):
        """Resets current serial number back to input start number - 1"""
        self.current_serial_num = self.start