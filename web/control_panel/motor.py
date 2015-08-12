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


class motor:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        # Front left
        GPIO.setup(15,GPIO.OUT)
        GPIO.setup(11,GPIO.OUT)
        GPIO.setup(13,GPIO.OUT)
        # Front right
        GPIO.setup(19,GPIO.OUT)
        GPIO.setup(21,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)

    def reset(self):
        GPIO.output(15, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)


    def right_forward(self):
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)

    def right_backward(self):
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)

    def left_forward(self):
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(21, GPIO.LOW)

    def left_backward(self):
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(21, GPIO.HIGH)

    def stop(self):
        self.reset()