int analogPin = A0; // potentiometer wiper (middle terminal) connected to analog pin 3
// outside leads to ground and +5V
int val = 0; // variable to store the value read
float tot;
void setup() {
Serial.begin(9600); // setup serial
pinMode(13, OUTPUT);
}
void loop() {
val = analogRead(analogPin); // read the input pin
tot = 5.0*(float)val/1023.0;

if(tot > 3.0000){
  analogWrite(13, val/4);
}else{
  digitalWrite(13,LOW);
}
Serial.print ("Conversi´on anal´ogico-digital: ");
Serial.println(tot); // debug value
}
