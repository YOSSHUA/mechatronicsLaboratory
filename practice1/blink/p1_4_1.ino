void setup()
{
  pinMode(13, OUTPUT);
  pinMode(12, INPUT);
}
// Cada 0.5Hz -> 2 por seg
//Cada 1Hz -> 1 por seg
void loop()
{
  int stateButton = digitalRead(12); //read the state of the button
  if(stateButton == 1) { //LOW
     digitalWrite(13, HIGH); 
   delay(400);
     digitalWrite(13,LOW);
     delay(400);
  }else{// HIGH
     digitalWrite(13, HIGH); 
   delay(800);
     digitalWrite(13,LOW);
     delay(800);
  }
}
