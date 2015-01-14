#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, os, subprocess, multiprocessing
import RPi.GPIO as GPIO

##########################################
def debug_print(line,must_print = False):
    if debug or must_print:
        print line

def beep_func():
    while True:
        calc_dist = distance(GPIO_ECHO_BEEP,GPIO_TRIG_BEEP)
        print "BEEP dist is: " + str(calc_dist)
        if calc_dist < 60:
            cmd = "(speaker-test -t sine -f " + str(75*calc_dist) + " -l 1 -p 1024 -P 4 > /dev/null)& pid=$!; sleep 0.25s; kill -9 $pid"
            print cmd
            os.system(cmd)
        time.sleep(0.1)
        
    
def distance(GPIO_ECHO,GPIO_TRIG):
    debug_print ("GPIO_TRIG = " + str(GPIO_TRIG) + ",GPIO_ECHO = " + str(GPIO_ECHO))
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
    inttimeout = 1000               # Number of loop iterations before timeout called


    min_dist = 100

    # Never ending loop
    # -----------------
    while EXIT < 10:

        # Trigger high for 0.0001s then low
        GPIO.output(GPIO_TRIG, True)
        time.sleep(decpulsetrigger)
        GPIO.output(GPIO_TRIG, False)

        # Wait for echo to go high (or timeout)
        i_countdown = inttimeout

        while (GPIO.input(GPIO_ECHO) == 0 and i_countdown > 0):
            i_countdown -=  1

        # If echo is high than the i_countdown not zero
        if i_countdown > 0:

            # Start timer and init timeout countdown
            echostart = time.time()
            i_countdown = inttimeout

            # Wait for echo to go low (or timeout)
            while (GPIO.input(GPIO_ECHO) == 1 and i_countdown > 0):
                i_countdown -= 1

            # Stop timer
            echoend = time.time()


            # Echo duration
            echoduration = echoend - echostart

        # Display distance
        if i_countdown > 0:
            i_distance = (echoduration*1000000)/58
            debug_print("Distance = " + str(i_distance) + "cm")
            min_dist = min(min_dist,i_distance)
        else:
            debug_print("Distance - timeout")

            # Wait at least .01s before re trig (or in this case .1s)
            time.sleep(.1)

        EXIT +=1
        return min_dist
##########################################
    

# Which GPIO's are used [0]=BCM Port Number [1]=BCM Name [2]=Use [3]=Pin
# ----------------------------------------------------------------------
GPIO_ECHO = 17
GPIO_TRIG = 4
GPIO_ECHO_BEEP = 22
GPIO_TRIG_BEEP = 27
#arrgpio = [(17,"GPIO0","Echo",11),(4,"GPIO7","Trig",7)]




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
