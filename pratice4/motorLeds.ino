int LED0 = 4;
int LED1 = 3;
int BUT0 = 2;
int BUT1 = 1;
int val0 = 0;
int val1 = 0;
void setup()
{
  pinMode(13, OUTPUT); // Enable
  pinMode(12, OUTPUT); // Puente H
  pinMode(11, OUTPUT); // Puente H
  pinMode(LED0, OUTPUT); // LED 0
  pinMode(LED1, OUTPUT); // LED 1
  pinMode(BUT0, INPUT); // Button 0
  pinMode(BUT1, INPUT); // Button 1  
}

void loop()
{  
  digitalWrite(13, HIGH);
  val0 = digitalRead(BUT0);  // read input value    
  if (val0 == HIGH){         // check if the input is HIGH (button released)
    digitalWrite(LED0, HIGH);// turn LED OFF
   	digitalWrite(11, HIGH);
  } else {
    digitalWrite(LED0, LOW);  // turn LED ON    
    digitalWrite(11, LOW);
  }
  val1 = digitalRead(BUT1);
  if (val1 == HIGH){         // check if the input is HIGH (button released)
    digitalWrite(LED1, HIGH);// turn LED OFF
    digitalWrite(12, HIGH);
  } else {
    digitalWrite(LED1, LOW);  // turn LED ON   
    digitalWrite(12, LOW);
  }
  
  
}