#-------------------------------------------------------------------------------
# Name:        Static funcs
# Purpose:
#
# Author:      I070890
#
# Created:     18/01/2015
# Copyright:   (c) I070890 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

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
