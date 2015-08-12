#!/usr/bin/env python
#coding=utf-8
"""
泥色线-> ENA -> pin#15
红色线-> IN1 -> pin#11
橙色线-> IN2 -> pin#13


白色线-> ENB -> pin#23
灰色线-> IN4 -> pin#19
紫色线-> IN3 -> pin#21
"""
import RPi.GPIO as GPIO
import time
import sys

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


def reset():
    GPIO.output(15, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)


def right_forward():
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)

def right_backward():
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)

def left_forward():
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(21, GPIO.LOW)

def left_backward():
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(21, GPIO.HIGH)

def stop():
    reset()

def run(command):
    """
    rf = Right wheel go forward
    lf = Left wheel go forward
    rb = Right wheel go backward
    lb = Left wheel go backward
    bf = Both wheels go forward
    bb = Both wheels go backward
    st = stop()
    """
    if command == 'rf':
        right_forward()
    if command == 'lf':
        left_forward()
    if command == 'rb':
        right_backward()
    if command == 'lb':
        left_backward()
    if command == 'bf':
        right_forward()
        left_forward()
    if command == 'bb':
        right_backward()
        left_backward()
    if command == 'st':
        stop()
    if command == 'q':
        stop()
        sys.exit(0)


def main():
    reset()
    while True:
        command = raw_input("OP: ")
        run(command)

if __name__ == '__main__':
    main()