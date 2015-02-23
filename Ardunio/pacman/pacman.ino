/* 
 SAP DKOM 2015 - Arduino pacman booth.
 
 For the Arduino Leonardo.
 
 Sends a text string when a button is pressed.
 
 The circuit:
 * 4 X Aligtors clips attached to your custom made arrows.
 * 4 X 10-kilohm resistor attached from pins 1,2,3,4  (analog) to ground.
 * See: https://raw.githubusercontent.com/idofishler/SAP-dokm-handson/master/Ardunio/resources/pacman-arduino-skatch.png for more details.
 
 created at: 25/01/2015
 by: Ido Fishler, Barak Kinarti, Daniel Turin
 
 This example code is made for SAP DKOM IL 2015
 */

 void setup() {
  // initialize control over the keyboard:
  Keyboard.begin();
}

void loop() {
  // read the input from your custom arrows a.k.a -> "sensors":
  int sensorRight = analogRead(A1); // "A1" - is the A1 analog input on the Arduino. you may chage this according to your wiering

  // more arrows reads goes here:
  // TODO: compleate me...
  // did you get all 4 directions?

  // if sensor get any current -> something must be touching it, right?
  if ((sensorRight > 20)) {
    // press the right arrow
    Keyboard.press(KEY_RIGHT_ARROW); 
    delay(10);
  }

  // TODO: add more arrows here

  // release the keyboard press press
  Keyboard.releaseAll();

}

