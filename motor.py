import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

global distance 
#Assign pins and set as output
pwmPin = [12,16,20,21]
for i in range(0,4):
  GPIO.setup(pwmPin[i], GPIO.OUT)
TRIG = 17
ECHO = 27
Buzzer = 22
servo = 24
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(Buzzer, GPIO.OUT)

class Motor:
  def __init__(self):
    #Set up PWM for each motor
    self.f = 50
    self.motor1 = GPIO.PWM(pwmPin[0], self.f)
    self.motor2 = GPIO.PWM(pwmPin[1], self.f)
    self.motor3 = GPIO.PWM(pwmPin[2], self.f)
    self.motor4 = GPIO.PWM(pwmPin[3], self.f)
    self.motors = [self.motor1, self.motor2, self.motor3, self.motor4]
    self.servom = GPIO.PWM(servo, self.f)
    

  def stop(self):
    for i in range(0,4):
      self.motors[i].ChangeDutyCycle(0) #stop motors
  
  def left(self):
    for i in range(0,2):
      self.motors[i].ChangeDutyCycle(50)
    for i in range(2,4):
      self.motors[i].ChangeDutyCycle(75)
    time.sleep(2)

  def right(self):
    for i in range(0,2):
      self.motors[i].ChangeDutyCycle(75)
    for i in range (2,4):
      self.motors[i].ChangeDutyCycle(50)
    time.sleep(2)
  
  def forwards(self):
    while time.time() < 5 and distance > 10:
      for i in range(0,4):
        self.motors[i].ChangeDutyCycle(100)
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
    self.stop() 
  
  def wiper(self):
    self.servo.start(0)
    dcMin = 5
    dcMax = 10
    for i in range(0,3):
      self.servo.ChangeDutyCycle(dcMax)
      time.sleep(.5)
      self.servo.ChangeDutyCycle(dcMin)
      time.sleep(.5)
