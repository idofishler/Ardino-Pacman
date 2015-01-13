#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, os, subprocess, multiprocessing
import RPi.GPIO as GPIO

def bgMusic():
    os.system("/home/pi/VC/bg-music.sh")
    

# Which GPIO's are used [0]=BCM Port Number [1]=BCM Name [2]=Use [3]=Pin
# ----------------------------------------------------------------------
GPIO_ECHO = 17
GPIO_TRIG = 4
arrgpio = [(17,"GPIO0","Echo",11),(4,"GPIO7","Trig",7)]




# Set GPIO Channels
# -----------------
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_ECHO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.output(GPIO_TRIG, False)


# A couple of variables
# ---------------------
EXIT = 0                        # Infinite loop
decpulsetrigger = 0.0001        # Trigger duration
inttimeout = 2000               # Number of loop iterations before timeout called
# Seperate process that play the bg music
proc = subprocess.Popen("echo")
            

# Wait for 2 seconds to allow the ultrasonics to settle (probably not needed)
# ---------------------------------------------------------------------------
print "Waiting for 2 seconds....."
time.sleep(2)


# Go
# --
print "Running...."


# Never ending loop
# -----------------
while EXIT == 0:

        # Trigger high for 0.0001s then low
        
    GPIO.output(GPIO_TRIG, True)
    time.sleep(decpulsetrigger)
    GPIO.output(GPIO_TRIG, False)

    # Wait for echo to go high (or timeout)

    intcountdown = inttimeout

    while (GPIO.input(GPIO_ECHO) == 0 and intcountdown > 0):
        intcountdown = intcountdown - 1

    # If echo is high

    if intcountdown > 0:

        # Start timer and init timeout countdown

        echostart = time.time()
        intcountdown = inttimeout

        # Wait for echo to go low (or timeout)

        while (GPIO.input(GPIO_ECHO) == 1 and intcountdown > 0):
            intcountdown = intcountdown - 1

        # Stop timer

        echoend = time.time()


        # Echo duration

        echoduration = echoend - echostart

    # Display distance

    if intcountdown > 0:
        intdistance = (echoduration*1000000)/58
        print "Distance = " + str(intdistance) + "cm"
        alive = proc.poll()
        if intdistance < 20:
            print "Start me" + "alive is " + str(alive)
            if alive is not None:
                print "Start me" + "alive is " + str(alive)
                proc = subprocess.Popen(["/usr/bin/aplay", "/home/pi/VC/CSH6XuazmB8.wav"])
                time.sleep(0.5)
        elif alive is None:
                print "Walla??"
                subprocess.Popen.kill(proc)
    else:
        print "Distance - timeout"

        # Wait at least .01s before re trig (or in this case .1s)

        time.sleep(.1)
    time.sleep(0.2)

