const int sprinkler1 = 2;
const int sprinkler2 = 4;
const int light = 7;
const int lightSensorPin = A0;

int lightValue;
int minLightValue;
int maxLightValue;
int adjustedLightValue;

void setup() {
  pinMode(sprinkler1, OUTPUT);
  pinMode(sprinkler2, OUTPUT);
  pinMode(light, OUTPUT);
  
  lightValue = analogRead(lightSensorPin);
  minLightValue = lightValue - 10;
  maxLightValue = lightValue + 10;
  
  Serial.begin(9600); //initialize port at 9600 bauds

}

void loop() {
  if (Serial.available()) {
      char instruction = Serial.read();
      if (instruction == 'a') { //If it is an 'a', switch sprinkler 1 ON
         digitalWrite(sprinkler1, HIGH);        
      }else if (instruction == 'b') { //If it is a 'b', switch sprinkler 1 OFF
         digitalWrite(sprinkler1, LOW);
      }else if (instruction == 'c') { //If it is a 'c', switch sprinkler 2 ON
         digitalWrite(sprinkler2, HIGH);
      }else if (instruction == 'd') { //If it is a 'd', switch sprinkler 2 OFF
         digitalWrite(sprinkler2, LOW);
      }else if (instruction == 'e') { //If it is an 'e', return day/night
         Serial.write(getIsNight());
      }else if (instruction == 'f') { //If it is a 'g', switch light ON
         digitalWrite(light, HIGH);
      }else if (instruction == 'g') { //If it is a 'b', switch light OFF
         digitalWrite(light, LOW);
      }
   }
}

char getIsNight(){
  lightValue = analogRead(lightSensorPin);
  //Adjust minimum and maximum limits 
  if(minLightValue > lightValue){
    minLightValue = lightValue;
  }
  if(maxLightValue < lightValue){
    maxLightValue = lightValue;
  }
  //Set the result between 0-100
  adjustedLightValue = map(lightValue, minLightValue, maxLightValue, 0, 100);
  if (adjustedLightValue <= 5){
    return 'z'; //it is night
  }else{
    return 'y'; // it is day
  }
}
