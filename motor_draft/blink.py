import RPi.GPIO as GPIO
import time

def active(times):
     GPIO.setmode(GPIO.BOARD)
     GPIO.setup(11, GPIO.OUT)

     while times>0:
          GPIO.output(11, GPIO.HIGH) #or output(11, GPIO.True)
          print 'run {} seconds'.format(times)
          time.sleep(times)
          GPIO.output(11, GPIO.LOW)
          times = 0
     return

if __name__ == '__main__':
     active(5)