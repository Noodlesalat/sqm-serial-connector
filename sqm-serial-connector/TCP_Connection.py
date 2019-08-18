import socket
import configparser
import io


class TCP_Connection:
    sock = None
    config = None

    def __init__(self):
        # load config file
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    def sendReading(self, reading):
        # initialize connection
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.config['server']['ip'], int(self.config['server']['port'])))

        self.sock.send(reading)
        self.sock.close()
        self.sock = None