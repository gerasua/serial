import serial
import sys
import glob
import logging

#Loggin de errores y consola
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(funcName)s:%(message)s')
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def infoSerial():

        try:
            ser = serial.Serial(port='/dev/tty.Bluetooth-Incoming-Port', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                                timeout=1)
        except:

            if sys.platform.startswith('win'):
                ports = ['COM%s' % (i + 1) for i in range(256)]
            elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
                ports = glob.glob('/dev/tty[A-Za-z]*')
            elif sys.platform.startswith('darwin'):
                ports = glob.glob('/dev/tty.*')
            else:
                raise EnvironmentError('Unsoported Plataform')
            result = []
            for port in ports:
                try:
                    ser = serial.Serial(port)
                    ser.close()
                    result.append(port)
                except Exception as e:
                    logger.exception("Ports Error: %s" % e)
                    pass
            if result == []:
                logger.exception("There are not open ports")
                exit()
            else:
                logger.exception("The initially configured port is closed")
                logger.debug("Open port(s): %s" % result)
                exit()
        try:
            if (ser.isOpen()):
                logger.debug("Serial Port Open: %s" % ser.port)
                ser_bytes = ser.readline()
                logger.debug("%s" % ser_bytes)
            else:
                logger.exception("Puerto Serial Cerrado")
        except Exception as e:
            logger.exception("Error: %s" % e)

if __name__ == '__main__':
	infoSerial()