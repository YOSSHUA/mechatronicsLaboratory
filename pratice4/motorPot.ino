int EN = 10; 

void setup()
{
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(EN, OUTPUT);
  Serial.begin(9600);
  
}

double v;
void loop()
{
  v = analogRead(A0);
  v = map(v, 0, 1023, -255, 255);
  analogWrite(EN, abs(v));
  Serial.println(v);
  
  if(v > 0){
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
  }else if (v < 0){
    digitalWrite(11, LOW);
    digitalWrite(12, HIGH);
  }
  
}
