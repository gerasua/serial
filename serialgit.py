import serial
import sys
import glob

def infoSerial():

        try:
            ser = serial.Serial(port='/dev/tty', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                                timeout=1)
        except:

            if sys.platform.startswith('win'):
                ports = ['COM%s' % (i + 1) for i in range(256)]
            elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
                ports = glob.glob('/dev/tty[A-Za-z]*')
            elif sys.platform.startswith('darwin'):
                ports = glob.glob('/dev/tty.*')
            else:
                raise EnvironmentError('Unsoporte Plataform')
            result = []
            for port in ports:
                try:
                    ser = serial.Serial(port)
                    ser.close()
                    result.append(port)
                except (OSError, serial.SerialException):
                    pass
            if result == []:
                print("There are not open ports")
                exit()
            else:
                print("El puerto inicialmente configurado está cerrado\n")
                print("Open port(s):", result)
                exit()
        try:
            if (ser.isOpen()):
                print("Serial Port Open:", ser.port)
                ser_bytes = ser.readline()
                print(ser_bytes)
            else:
                print("Puerto Serial Cerrado")
        except:
            print("Error Except")

if __name__ == '__main__':
	infoSerial()