import serial


uintId = 0
RS232Baud = 9600

class SerialUI():
    """Handle all serial communications

    """
    def __init__(self, pool):
        self.pool = pool

        
