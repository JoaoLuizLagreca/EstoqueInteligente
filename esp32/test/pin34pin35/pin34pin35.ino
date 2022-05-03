
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(1000);
  Serial.print("34 - ");
  Serial.println(analogRead(34));
   Serial.print("35 - ");
  Serial.println(analogRead(35));
}
