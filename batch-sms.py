import serial
import time
import datetime
from pprint import pprint


class TextMessage:
    def __init__(self, recipient="<your number starting with 63>",
                 message="<your text message>",
                 ):
        self.recipient = number
        self.content = message

    def setRecipient(self, number):
        self.recipient = number

    def setContent(self, message):
        self.content = message

    def connectPhone(self):
        #Timeout is needed for reading lines
        #COM4 is used on windows. still not sure what the naming conventions are on linux
        self.SerialPort = serial.Serial('COM4', 115200, timeout=1)
        time.sleep(1)

    def sendMessage(self):
        #serialport.write returns no. of bytes sent
        #\r\n is used to create a new lin in windows
        self.SerialPort.write('AT+CMFG=1\r\n')
        time.sleep(1)
        self.SerialPort.write('AT+CMGS="'+self.recipient'"\r\n')
        time.sleep(1)
        self.SerialPort.write(self.content+"\x1A")
        time.sleep(1)
        #\x1A is the same as chr(26) which is an escape sequence like CTRL+Z
        #self.SerialPort.write(chr(26))
        #time.sleep(1)
        print "message sent"

    def readMessages(self):
        print "\nPrinting all the messages stored in the current inbox:"
        self.SerialPort.write('AT+CMGL="ALL"\r\n')
        time.sleep(1)
        x = self.SerialPort.readlines(1)
        for line in x:
            print line.strip('\r\n')

    def disconnectPhone(self):
        self.SerialPort.close()

if __name__ == "__main__":
    #The modem usually timeouts.
    sms = TextMessage("<number to send>", str(datetime.datetime.now())+" :hello!")
    sms.connectPhone()
    sms.readMessages()