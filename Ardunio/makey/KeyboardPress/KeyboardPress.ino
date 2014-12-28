/* 
 Keyboard Message test
 
 For the Arduino Leonardo and Micro.
 
 Sends a text string when a button is pressed.
 
 The circuit:
 * pushbutton attached from pin 4 to +5V
 * 10-kilohm resistor attached from pin 4 to ground
 
 created 24 Oct 2011
 modified 27 Mar 2012
 by Tom Igoe
 modified 11 Nov 2013
 by Scott Fitzgerald
 
 This example code is in the public domain.
 
 http://www.arduino.cc/en/Tutorial/KeyboardMessage
 */

void setup() {
  // make the pushButton pin an input:
  // initialize control over the keyboard:
  Keyboard.begin();
}

void loop() {
  // read the pushbutton:
  int sensorValue = analogRead(A2);
  // if the button state has changed, 
  if ((sensorValue > 0)) {
    // increment the button counter
    // type out a message
    Keyboard.press('a');
    delay(10);
    Keyboard.releaseAll();
  }
}

