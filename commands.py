from motor import Motor
import RPi.GPIO as GPIO
import time

dc = Motor()
for i in range(0,4):
  dc.motors.start(0)

while True:
  dc.forwards()
'''
data = ['Data']
if data[0] = 'Left':
  dc.left()
  dc.forwards()

elif data[0] = 'Right':
  dc.right()
  dc.forwards()

elif data[0] = "Forward":
  dc.forwards()

elif data[0] = "Backward":
  dc.backwards()
  '''