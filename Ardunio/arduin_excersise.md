Arduin pacman excersise
=======================

General
-------
The goal of this excercise is to create a pacman controller using a pancil and paper.

How? We will use the the electricity in our fingures. You will draw four arrows: <-, ^, ->, v.
The lead from the pencil is a semi-conductor. When you press on an arrow, detect it with the Ardino controller and fake the keybord button acoordingly.

Steps
-----
1. Draw / Create your arrows (use pencil and papar, vegtibles or palsteline). Make sure you can reach each arrow with a cable.
2. Connect the Arduino as discibed in the following [diagram](resources/pacman-arduino-skatch.png)
	1. What we want to do is use the semi-conductors and keys for our keyboard.
3. Compleate the code in the Ardino IDE
	1. Arduion comes with a build in framework that runs C/C++ code.
	2. Any arduino program has a `setup()` and `loop()` functions. `setup()` is called once and `loop()` is called all the time (like a `while(true)` loop).
	3. What your code needs to do is:
		1. detect the inputs form your arrows (semi-conductors)
		2. Press the required key usignd the `Keyboard` API
		3. See more instructions and examples in the code.
4. Upload the code to the Arduino controller by pressing the *upload* button
5. Play [pacman](http://www.play-pacman-online.com/) :)