import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pwmPin = 16
pin2 = 20
GPIO.setup(pwmPin, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

dcMin = 0
dcMax = 100
pwm = GPIO.PWM(pwmPin, 50) # PWM object at 50 Hz (20 ms period)
pwm2 = GPIO.PWM(pin2, 50)
pwm.start(0)
pin2.start(0)
try:
  while True:
    pwm.ChangeDutyCycle(50)
    pin2.ChangeDutyCycle(10)
    time.sleep(0.02)
except KeyboardInterrupt:
  print("bye")
  GPIO.cleanup()