Arduino pacman exercise
=======================

General
-------

The goal of this exercise is to create a pacman controller using a pencil and paper.

How? We will use the electricity in our fingers. You will use fruit as your four arrows: <-, ^, ->, v. You may actually use anything you like (be creative) as long as it’s a semi-conductor. When you press on an arrow, detect it with the Arduino controller and fake the keyboard button accordingly.

Steps
-----

1. Draw / Create your arrows (use pencil and paper, vegetables or plasteline). Make sure you can reach each arrow with a cable.
2. Connect the Arduino as described in the following [diagram](resources/pacman-arduino-skatch.png)
	* What we want to do is use the semi-conductors and keys for our keyboard.
3. Complete the code in the Arduino IDE
	* Arduino comes with a build in framework that runs C/C++ code.
	* Any Arduino program has a `setup()` and `loop()` functions. `setup()` is called once and `loop()` is called all the time (like a `while(true)` loop).
	* What your code needs to do is:
		1. detect the inputs form your arrows (semi-conductors)
		2. Press the required key using the `Keyboard` API
		3. See more instructions and examples in the code.
4. Upload the code to the Arduino controller by pressing the *upload* button
5.	Play pacman [pacman](http://files.widgetbox.com/widgets/neave/neave_pacman_widgetbox.swf) :)

