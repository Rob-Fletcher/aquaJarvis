import serial
import sys


def write(cmd):
    try:
        port = serial.Serial("/dev/tty.usbserial-AK06K32C",
                             #bauderate=9600,
                             #bytesize=serial.EIGHTBITS,
                             #parity=serial.PARITY_NONE,
                             #stopbits=serial.STOPBITS_ONE
                             )
    except:
        print("Could not open serial port.")
    res = ""
    print("Response: {}".format(res))




if __name__ == '__main__':

    cmd = sys.argv[1]
    write(cmd)
