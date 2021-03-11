int xPin = A1;
int yPin = A0;

void setup() {
  // inicializar las comunicaciones en serie a 9600 bps:
  Serial.begin(9600);
  
  pinMode(xPin, INPUT);
  pinMode(yPin, INPUT);
  
}

void loop() {
  int x = analogRead(A0);
  int y = analogRead(A1);
  float xMap = map(x, 0, 1023, -1000, 1000);
  float yMap = map(y, 0, 1023, -1000, 1000);
  float xV = xMap/1000;
  float yV = yMap/1000;
  Serial.print(xV);
  Serial.print(",");
  Serial.println(yV);

  delay(100); // añadir un poco de retraso entre lecturas
}
