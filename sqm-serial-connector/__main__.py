import time
from src.serialReading import SerialReading

# connect to SQM
serial = SerialReading()
serial.initializeConnection()

# get readings from SQM
while(True):
    print(serial.getReading())
    time.sleep(2)