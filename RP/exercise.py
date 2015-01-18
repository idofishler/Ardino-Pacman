#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, os, subprocess, multiprocessing

from static_funcs import distance
from static_funcs import beep_func
from static_funcs import debug_print
from static_funcs import init_func
import Sound

# Which GPIO's are used (The ones you connected)
# ----------------------------------------------------------------------
# - STEP 1) define your  values
GPIO_ECHO = XXX
GPIO_TRIG = XXX

# A couple of variables
# ---------------------
EXIT = 0                        # Infinite loop
loop_sleep = 1                  # sleep period between loops
# Seperate process that play the bg music
sound = Sound()


# Go
# --
init_func()
beep_proc = multiprocessing.Process(target=beep_func, args=(False,))
beep_proc.start()


# Never ending loop
# -----------------
while EXIT == 0:

    # distance func prototype
    # def distance(GPIO_ECHO,GPIO_TRIG)
    # - STEP 2) Call to the distance function with your values
    mesured_distance = XXX
    print "Distance = " + str(mesured_distance) + "cm"
    alive = sound.isAlive()
    # - STEP 3) Set the threshold for the song to start playing
    if mesured_distance < XXX:
        print "Start me" + "alive is " + str(alive)
        if alive is not None:
            print "Start me" + "alive is " + str(alive)
            sound.play()
    elif alive is None:
            sound.kill()

    time.sleep(loop_sleep)

beep_proc.terminate()

