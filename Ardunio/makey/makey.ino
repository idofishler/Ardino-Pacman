#include <USBKeyboard.h>

void setup() {
  // make pin 2 an input and turn on the 
  // pullup resistor so it goes high unless
  // connected to ground:
  pinMode(2, INPUT_PULLUP);
  // initialize control over the keyboard:
  Keyboard.init();
}

void loop() {
  while (digitalRead(2) == HIGH) {
    // do nothing until pin 2 goes low
    delay(500);
  }
  delay(1000);
  Keyboard.sendKeyStroke(KEY_A);
  digitalWrite(13, HIGH);
  delay(100);
  digitalWrite(13, LOW);
}
