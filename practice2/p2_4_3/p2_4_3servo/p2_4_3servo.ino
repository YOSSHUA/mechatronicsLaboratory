#include <Servo.h>
#include <LiquidCrystal.h> // include the library code:
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // initialize the interface pins
int analogPin = A0;
Servo myservo; // create servo object to control a servo
int val = 0; // variable to read the value from the analog pin
float tot;
void setup() {
  lcd.begin(16, 2); // set up the LCD's number of columns and rows:
  myservo.attach(9); // attaches the servo on pin 9 to the servo object
}
void loop() {

  val = analogRead(analogPin); // read the input pin
  tot = 5.0*float(val)/1023.0;
  
  float ang = tot*180/5 ;
  
  myservo.write(int(ang));
  
  lcd.setCursor(0,0);
  lcd.write("A'ngulo");
  String num = String(ang,4);
  lcd.setCursor(0,1);
  lcd.print(num);   
}
