#!/usr/bin/cgipython1
from motor import Motor
import RPi.GPIO as GPIO
import time

#Assign GPIO Pins
TRIG = 17
ECHO = 27
Buzzer = 22
D = 4

#Set GPIO pins as inputs/outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(Buzzer, GPIO.OUT)
GPIO.setup(D,GPIO.IN)

#Instantiate Motor Class
dc = Motor()
for i in range(0,4):
  dc.motors[i].start(0)

try:
  while True:
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)

    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
      sent = time.time()

    while GPIO.input(ECHO) == 1:
      received = time.time()

    timepassed = received - sent
    global distance
    distance = timepassed * (343/2) * 100

    print('Distance: %.2f' % distance)
    time.sleep(0.3)

    rain = GPIO.input(D)

    while distance > 10:
      GPIO.output(Buzzer, GPIO.LOW)
      with open('index.txt', 'r') as f:
        Dir = f.read()
      if Dir == 'L':
        dc.left()
        dc.forwards()

      elif Dir == 'R':
        dc.right()
        dc.forwards()

      elif Dir == "F":
        dc.forwards()
      
      else:
        pass
    
    dc.stop()
    if distance < 10:
      for i in range(0,5): 
        GPIO.output(Buzzer, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(Buzzer, GPIO.LOW)
        time.sleep(0.5)
    if rain == 0:
      dc.wiper()
    
    letter = 0;
    with open('index.txt', 'w') as f:
      f.write(str(letter))
except KeyboardInterrupt:
  print('shutting down')
  GPIO.cleanup()