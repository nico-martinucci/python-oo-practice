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

    def __init__(self, start):
        """Create a serial generator starting at start"""
        self.start = self.current = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} current={self.current}>"

    def generate(self):
        """Increments current number by 1"""
        self.current += 1
        return self.current - 1

    def reset(self):
        """Resets current number to start number"""
        self.current = self.start
