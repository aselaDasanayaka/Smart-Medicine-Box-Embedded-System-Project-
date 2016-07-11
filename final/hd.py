import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import threading
from threading import Thread, current_thread



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Initialize pins appropriately use physical numbering system of Raspberry pi
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
stcp = 12  # 7seg
shcp = 11  # 7seg
sin = 13   # 7seg

red = 29   # alert
green = 33 # alert
buz = 40   # alert

one = 38   # box
two = 37   # box
three = 36   # box
four = 35   # box
five = 32   # box

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Initialize pins output/input
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GPIO.setup(stcp,GPIO.OUT)
GPIO.setup(shcp,GPIO.OUT)
GPIO.setup(sin,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(buz,GPIO.OUT)
GPIO.setup(one,GPIO.IN)
GPIO.setup(two,GPIO.IN)
GPIO.setup(three,GPIO.IN)
GPIO.setup(four,GPIO.IN)
GPIO.setup(five,GPIO.IN)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Custom timer function
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Timer(p):
    GPIO.setup(p,GPIO.OUT)
    GPIO.output(p,0)
    time.sleep(0.001)
    GPIO.setup(p,GPIO.OUT)
    GPIO.output(p,1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           7-segment mapping 2D array
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
arr=[[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 0]]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Display 5 seven segment digits in this python function
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def display(a,b,c,d,e):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(stcp,GPIO.OUT)
    GPIO.setup(shcp,GPIO.OUT)
    GPIO.setup(sin,GPIO.OUT)
    
    ary = [e,d,c,b,a]
    for j in range (5):
        for i in range(8):
            print 'displaying'
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(sin,GPIO.OUT)
            GPIO.output(sin,arr[ary[j]][i])
            GPIO.setup(shcp,GPIO.OUT)
            Timer(shcp)
    for i in range (40):
        Timer(stcp)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Turn on green led
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def blinkG():
    GPIO.output(green,1)
    time.sleep(5)
    return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           blink red led
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def blinkR():
    GPIO.output(red,1)
    time.sleep(0.5)
    GPIO.output(red,0)
    time.sleep(0.5)
    return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Normal alert
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def alertN():
    print 'allertN'
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buz,GPIO.OUT)
    for i in range (2):
        GPIO.output(buz,1)
        time.sleep(0.5)
        GPIO.output(buz,0)
        time.sleep(0.5)
        
    return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Warning alert
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def alertW():
    for i in range (3):
        GPIO.output(buz,1)
        time.sleep(0.1)
        GPIO.output(buz,0)
        time.sleep(0.3)
    GPIO.output(buz,0)
    time.sleep(0.4)
    return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#          Check Open boxes function 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def openBoxes():
    op=""
    if GPIO.input(one):
        op=op+"1"
    else:
        op=op+"0"
    if GPIO.input(two):
        op=op+"1"
    else:
        op=op+"0"
    if GPIO.input(three):
        op=op+"1"
    else:
        op=op+"0"
    if GPIO.input(four):
        op=op+"1"
    else:
        op=op+"0"
    if GPIO.input(five):
        op=op+"1"
    else:
        op=op+"0"
    return op

def calldisplay(a,b,c,d,e):
    display(a,b,c,d,e)
    time.sleep(10)
    
       
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Testing functions in this script
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def opbox(boxes):
    if '1' in boxes:
        return boxes.index("1")+1
    else:
        return 0
        

   # print opbox(openBoxes())
#alertN()
#time.sleep(10)
t1=Thread(target=calldisplay,args=(0,1,0,2,3))
t1.start()
t2=Thread(target=alertN)
t2.start()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Clean used pins and clear variables
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GPIO.cleanup()