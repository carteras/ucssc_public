int led = 13;
bool is_on = true;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(115200);
  Serial.println("Hey, this thing is rocken!");
}

void loop() {
  if (is_on) {
    digitalWrite(led, LOW);
    is_on = false;
    Serial.println("LED is OFF");
  } else {
    digitalWrite(led, HIGH);
    is_on = true;
    Serial.println("LED is ON!");
  }
  
  delay(500);
}
