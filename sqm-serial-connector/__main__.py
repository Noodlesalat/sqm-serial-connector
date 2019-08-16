import time
import logging
from src.serialReading import SerialReading
from src.TCP_Connection import TCP_Connection
import configparser
import io

# enable logging
logging.basicConfig(level=logging.DEBUG)

# read config file
config = configparser.ConfigParser()
config.read("../config.ini")

# connect to SQM
serial = SerialReading()
serial.initializeConnection()

# setup tcp connection to server
connection = TCP_Connection()

# get readings from SQM
while(True):
    reading = serial.getReading()

    logging.debug(reading)

    connection.sendReading(reading)

    time.sleep(int(config['sqm']['interval']))