import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pwmPin = [12,16,20,21]
for i in range(0,4):
  GPIO.setup(pwmPin[i], GPIO.OUT)

class Motor:
  def __init__(self):
    self.f = 50
    self.motors = [self.motor1, self.motor2, self.motor3, self.motor4]
    self.motor1 = GPIO.PWM(pwmPin[0], self.f)
    self.motor2 = GPIO.PWM(pwmPin[1], self.f)
    self.motor3 = GPIO.PWM(pwmPin[2], self.f)
    self.motor4 = GPIO.PWM(pwmPin[3], self.f)

  
  
  def left(self):
    for i in range(0,2):
      self.motors[i].ChangeDutyCycle(25)
    for i in range(2,4):
      self.motors[i].ChangeDutyCycle(50)
    time.sleep(2)

  def right(self):
    for i in range(0,2):
      self.motors[i].ChangeDutyCycle(50)
    for i in range (2,4):
      self.motors[i].ChangeDutyCycle(25)
    time.sleep(2)
  
  def forwards(self):
    while time() < 3:
      for i in range(0,4):
        self.motors[i].ChangeDutyCycle(50)
      #if distance < 5:
        #buzzer
        #self.stop() 
      
  def backwards(self):
    while time() < 3:
      for i in range(0,4):
        self.motors[i].ChangeDutyCycle(-50)
  
  def stop(self):
    for i in range(0,4):
      self.motors[i].ChangeDutyCycle(0)