void setup() {
  // put your setup code here, to run once:
  //SEMAFORO 1
  pinMode(13,OUTPUT); // ROJO
  pinMode(12,OUTPUT); // AMAR
  pinMode(11,OUTPUT); // VERDE
  //SEMAFORO 2
  pinMode(19,OUTPUT); // ROJO
  pinMode(20,OUTPUT); // AMAR
  pinMode(21,OUTPUT); // VERDE
}

void loop() {
    // -------
    // 1
    digitalWrite(13,HIGH );
    digitalWrite(12,LOW );
    digitalWrite(11,LOW );
    //2
    digitalWrite(19,LOW );
    digitalWrite(20,LOW );
    digitalWrite(21,HIGH );
    delay(3000);  

    // ---------
    // 1
    digitalWrite(13,HIGH );
    digitalWrite(12,LOW );
    digitalWrite(11,LOW );
    //2
    digitalWrite(19,LOW );
    digitalWrite(20,HIGH );
    digitalWrite(21,LOW );
    delay(800);
    //---------
    // 1
    digitalWrite(13,LOW );
    digitalWrite(12,LOW );
    digitalWrite(11,HIGH );
    //2
    digitalWrite(19,HIGH );
    digitalWrite(20,LOW );
    digitalWrite(21,LOW );
    delay(3000);
    //-----------
    // 1
    digitalWrite(13,LOW );
    digitalWrite(12,HIGH );
    digitalWrite(11,LOW );
    //2
    digitalWrite(19,HIGH );
    digitalWrite(20,LOW );
    digitalWrite(21,LOW );
    delay(800);
}
