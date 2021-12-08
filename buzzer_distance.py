import RPi.GPIO as GPIO
import time

TRIG = 21
ECHO = 20

Buzzer = 16


GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(Buzzer, GPIO.OUT)

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
    distance = timepassed * (343/2) * 100

    print('Distance: %.2f' % distance)
    time.sleep(0.3)

    if distance > 10:
      GPIO.output(Buzzer, GPIO.LOW)

    if distance < 10:
      GPIO.output(Buzzer, GPIO.HIGH)
      time.sleep(0.5)
      GPIO.output(Buzzer, GPIO.LOW)
      time.sleep(0.5)


except KeyboardInterrupt:
  print('Bye')
  GPIO.cleanup()




