
const int motorPin = 9;

void setup() {
  pinMode(motorPin, OUTPUT);

   // Open serial port, set data rate to 9600 bps
  Serial.begin(9600);
}

int incomingByte = 0;   

// Letters to send over serial and numbers that are received here:
// Start motor
const int q = 113;
// Stop motor
const int w = 119;
// Reserved, unassigned
const int e = 101;
// Reserved, unassigned
const int r = 114;

void loop() {

  if (Serial.available() > 0) {
      // read the incoming byte:
      incomingByte = Serial.read();

      Serial.println(incomingByte, DEC);
      digitalWrite(motorPin, HIGH);
      
      if (incomingByte == q) {
        digitalWrite(motorPin, HIGH);    
      } else if (incomingByte == w) {
        digitalWrite(motorPin, LOW);
      } else if (incomingByte == e) {
        
      } else if (incomingByte == r) {
        
      }
  }
}


