#include <LiquidCrystal.h> // include the library code:
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // initialize the interface pins
void setup() {
lcd.begin(16, 2); // set up the LCD's number of columns and rows:
}
void loop() {
  char nom[] = "Yosshua Eli     ";
  char ap[] = "Cisneros        ";
  ///lcd.setCursor(Col,row);
  for(int i =0; i < 16; i++){
    /// en blanco
    for(int j = 0; j < 16-i; j++){
      lcd.setCursor(j,0);
      lcd.print(" ");
      lcd.setCursor(j,1);
      lcd.print(" ");
    }
    for(int j = 16-i; j < 16; j++){
      lcd.setCursor(j,0);
      lcd.print(nom[j-16+i]);
      lcd.setCursor(j,1);
      lcd.print(ap[j-16+i]);
    }
    delay(200);
  }  
  delay("400");
  lcd.setCursor(0,0);
  lcd.write("                ");
  lcd.setCursor(0,1);
  lcd.write("                ");
  

}
