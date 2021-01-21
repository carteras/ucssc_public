#include <Wire.h>
#include <ZumoShield.h>

ZumoBuzzer buzzer;
ZumoReflectanceSensorArray reflectanceSensors;
ZumoMotors motors;
Pushbutton button(ZUMO_BUTTON);

void setup() {
  Serial.begin(115200);
  Serial.println("Robot working");
  unsigned int sensors[6];
  unsigned short count = 0;
  unsigned short last_status = 0;
  int turn_direction = 1;

  buzzer.play(">g32>>c32");

  reflectanceSensors.init();
  delay(500);
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);        // turn on LED to indicate we are in calibration mode

  button.waitForButton();

  int i;
  for (i = 0; i < 80; i++)
  {
    if ((i > 10 && i <= 30) || (i > 50 && i <= 70))
      motors.setSpeeds(-200, 200);
    else
      motors.setSpeeds(200, -200);
    reflectanceSensors.calibrate();

    // Since our counter runs to 80, the total delay will be
    // 80*20 = 1600 ms.
    delay(20);
  }
  motors.setSpeeds(0, 0);
  buzzer.play("L16 cdegreg4");
  while (buzzer.isPlaying());
  Serial.println("init complete");
}

void loop() {
  unsigned int sensors[6];
  int pos = reflectanceSensors.readLine(sensors);
  int error = pos - 2500;

  Serial.println(error);
}
