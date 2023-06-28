from tkinter import *
import RPi.GPIO as GPIO
import time

pin1 = 5  # 1nd finger(hand in)
pin2 = 6   # 1nd finger     max 160
pin3 = 13  # 2nd finger     max 160
pin4 = 19  # 3nd finger     max 160
pin5 = 26 # 4nd,5nd finger  max 140
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin1, GPIO.OUT)
p1 = GPIO.PWM(pin1,50)
p1.start(4)

GPIO.setup(pin2, GPIO.OUT)
p2 = GPIO.PWM(pin2,50)
p2.start(4)

GPIO.setup(pin3, GPIO.OUT)
p3 = GPIO.PWM(pin3,50)
p3.start(4)

GPIO.setup(pin4, GPIO.OUT)
p4 = GPIO.PWM(pin4,50)
p4.start(4)

GPIO.setup(pin5, GPIO.OUT)
p5 = GPIO.PWM(pin5,50)
p5.start(4)

SERVO_MAX_DUTY    = 12   # 서보의 최대(180도) 위치의 주기
SERVO_MIN_DUTY    = 3    # 서보의 최소(0도) 위치의 주기
def setServoPos(pin,degree):
  if degree > 170:
    degree = 170
  elif degree < 10:
    degree = 10  
  duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
  pin.ChangeDutyCycle(duty)

def Position_1():
    setServoPos(p1,10)
    setServoPos(p2,120)
    setServoPos(p3,10)
    setServoPos(p4,160)
    setServoPos(p5,140)
    
def Position_2():
    setServoPos(p1,10)
    setServoPos(p2,120)
    setServoPos(p3,10)
    setServoPos(p4,10)
    setServoPos(p5,140)
    
def Position_3():
    setServoPos(p1,10)
    setServoPos(p2,10)
    setServoPos(p3,10)
    setServoPos(p4,10)
    setServoPos(p5,140)
    
def Position_4():
    setServoPos(p1,10)
    setServoPos(p2,120)
    setServoPos(p3,10)
    setServoPos(p4,10)
    setServoPos(p5,10)

def Position_5():
    setServoPos(p1,10)
    setServoPos(p2,10)
    setServoPos(p3,10)
    setServoPos(p4,10)
    setServoPos(p5,10)

def Position_S():
    setServoPos(p1,10)
    setServoPos(p2,10)
    setServoPos(p3,10)
    setServoPos(p4,160)
    setServoPos(p5,140)
    
def Position_R():
    setServoPos(p1,10)
    setServoPos(p2,120)
    setServoPos(p3,160)
    setServoPos(p4,160)
    setServoPos(p5,140)
    
def Position_G():
    setServoPos(p1,10)
    setServoPos(p2,10)
    setServoPos(p3,160)
    setServoPos(p4,160)
    setServoPos(p5,140)
    
def Position_F():
    setServoPos(p1,10)
    setServoPos(p2,60)
    setServoPos(p3,140)
    setServoPos(p4,130)
    setServoPos(p5,100)
    
def Position_F2():
    setServoPos(p1,10)
    setServoPos(p2,60)
    setServoPos(p3,170)
    setServoPos(p4,130)
    setServoPos(p5,100)

BUTTON_0 = 4
BUTTON_1 = 5
BUTTON_PRESSED = 0
ON = 1
OFF = 0
GPIO.setup(BUTTON_0, GPIO.IN)
GPIO.setup(BUTTON_1, GPIO.IN)

root = Tk()
root.minsize(400,500)
root.maxsize(800,500)
frame = Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)


button1 = Button(root,font=('Helvetica bold',16), text='Position_1', command = Position_1)
button2 = Button(root,font=('Helvetica bold',16), text='Position_2', command = Position_2)
button3 = Button(root,font=('Helvetica bold',16), text='Position_3', command = Position_3)
button4 = Button(root,font=('Helvetica bold',16), text='Position_4', command = Position_4)
button5 = Button(root,font=('Helvetica bold',16), text='Position_5', command = Position_5)
button6 = Button(root,font=('Helvetica bold',16), text='Position_Rock', command = Position_R)
button7 = Button(root,font=('Helvetica bold',16), text='Position_Scissor', command = Position_S)
button8 = Button(root,font=('Helvetica bold',16), text='Position_Good', command = Position_G)
button9 = Button(root,font=('Helvetica bold',16), text='Position_F', command = Position_F)
button10 = Button(root,font=('Helvetica bold',16), text='Position_F', command = Position_F2)

button1.grid(row=3,column=1, sticky = N+S+E+W)
button2.grid(row=3,column=2, sticky = N+S+E+W)
button3.grid(row=3,column=3, sticky = N+S+E+W)
button4.grid(row=4,column=1, sticky = N+S+E+W)
button5.grid(row=4,column=2, sticky = N+S+E+W)
button6.grid(row=4,column=3, sticky = N+S+E+W)
button7.grid(row=5,column=1, sticky = N+S+E+W)
button8.grid(row=5,column=2, sticky = N+S+E+W)
button9.grid(row=5,column=3, sticky = N+S+E+W)
button10.grid(row=6,column=2, sticky = N+S+E+W)

frame.pack()

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()

root.mainloop()
