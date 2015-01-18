#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, os, subprocess, multiprocessing
import RPi.GPIO as GPIO

from static_funcs import distance
from static_funcs import beep_func
from static_funcs import debug_print


# Which GPIO's are used [0]=BCM Port Number [1]=BCM Name [2]=Use [3]=Pin
# ----------------------------------------------------------------------
GPIO_ECHO = 17
GPIO_TRIG = 4
GPIO_ECHO_BEEP = 22
GPIO_TRIG_BEEP = 27
#arrgpio = [(17,"GPIO0","Echo",11),(4,"GPIO7","Trig",7)]



#################### TDS #################################
# Set GPIO Channels
# -----------------
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(GPIO_ECHO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(GPIO_TRIG, GPIO.OUT)
#GPIO.output(GPIO_TRIG, False)
#################### TDE #################################


# A couple of variables
# ---------------------
EXIT = 0                        # Infinite loop
decpulsetrigger = 0.0001        # Trigger duration
inttimeout = 2000               # Number of loop iterations before timeout called
debug = False                   # debug mode for console output
loop_sleep = 1                  # sleep period between loops
# Seperate process that play the bg music
proc = subprocess.Popen("echo")


# Wait for 2 seconds to allow the ultrasonics to settle (probably not needed)
# ---------------------------------------------------------------------------
print "Waiting for 2 seconds....."
time.sleep(2)


# Go
# --
print "Running...."
print "Start Beep process...."
beep_proc = multiprocessing.Process(target=beep_func)
beep_proc.start()


# Never ending loop
# -----------------
while EXIT == 0:

    # Display distance


    intdistance = distance(GPIO_ECHO,GPIO_TRIG)
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

    time.sleep(loop_sleep)

beep_proc.terminate()
