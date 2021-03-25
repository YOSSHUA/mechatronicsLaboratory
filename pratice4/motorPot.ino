const int pot = A0;
const int EN = 10, a1 = 12, a2 = 11; 

void setup()
{
  pinMode(a1, OUTPUT);
  pinMode(a2, OUTPUT);
  pinMode(EN, OUTPUT);
  Serial.begin(9600);
  
}

double v;
void loop()
{
  v = map(analogRead(pot), 0, 1023, -255, 255);
 
  
  analogWrite(EN, abs(v));
  Serial.println(v);
  
  if(v > 0){
    digitalWrite(a1, LOW);
    digitalWrite(a2, HIGH);
  }
  if (v < 0){
    digitalWrite(a2, LOW);
    digitalWrite(a1, HIGH);
  }
 
  
}