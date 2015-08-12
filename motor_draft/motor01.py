import RPi.GPIO as GPIO
import time

print '#' * 20
print 'HELLO WORLD'
print '#' * 20

GPIO.setmode(GPIO.BOARD)

# Front left
GPIO.setup(15,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
# Front right
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

RUN_TIME = raw_input('RUN TIME: ')

def reset():
    GPIO.output(15, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)


def front_left_forward():
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)

def front_left_backward():
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)

def front_right_forward():
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)

def front_right_backward():
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)

def stop():
    reset()

def main():
    reset()
    # Front left operation
    print 'Front left wheel runing forward'
    front_left_forward()
    time.sleep(int(RUN_TIME))
    stop()
    time.sleep(2)
    print 'Front left wheel runing backward'
    front_left_backward()
    time.sleep(int(RUN_TIME))
    stop()
    # Front right operation
    print 'Front right wheel runing forward'
    front_right_forward()
    time.sleep(int(RUN_TIME))
    stop()
    time.sleep(2)
    print 'Front right wheel runing backward'
    front_right_backward()
    time.sleep(int(RUN_TIME))
    stop()
    GPIO.cleanup()

if __name__ == '__main__':
    main()
