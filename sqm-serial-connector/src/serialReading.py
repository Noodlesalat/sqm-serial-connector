import serial
import configparser
import io

class SerialReading:
    connection = None
    config = None

    def __init__(self):
        # load config file
        self.config = configparser.ConfigParser()
        self.config.read("../config.ini")

    def initializeConnection(self):
        # connect tono serial port
        self.connection = serial.Serial(self.config['sqm']['port'], self.config['sqm']['baudrate'])

    def getReading(self):
        # send command to SQM
        self.connection.write(b'Rx')
        # get reading
        return self.connection.readline()