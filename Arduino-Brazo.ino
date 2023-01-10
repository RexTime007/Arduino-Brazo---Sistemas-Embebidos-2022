#include <Servo.h>
#include <SoftwareSerial.h>
#define SER3 3 //Pin para el servo
#define SER4 4 //Pin para el servo
#define SER5 5 //Pin para el servo
#define SER6 6 //Pin para el servo
#define SER7 7 //Pin para el servo
#define SER8 8 //Pin para el servo

SoftwareSerial serialESP32(9, 10); // RX, TX
String readString;
 
Servo servo3; //Objeto servo
Servo servo4; //Objeto servo
Servo servo5; //Objeto servo
Servo servo6; //Objeto servo
Servo servo7; //Objeto servo
Servo servo8; //Objeto servo
int mssg; //Variable para guardar el mensaje recibido por serial
int servo3Pos, servo4Pos, servo5Pos, servo6Pos, servo7Pos, servo8Pos; // current position
int servo3PPos, servo4PPos, servo5PPos, servo6PPos, servo7PPos, servo8PPos; // previous position
int p3 = 0, p4 = 0, p5 = 0, p6 = 0, p7 = 0, p8 = 0;
void setup()
{
    //Inicializamos el servo y el Serial:
    servo3.attach(SER3);
    servo4.attach(SER4);
    servo5.attach(SER5);
    servo6.attach(SER6);
    servo7.attach(SER7);
    servo8.attach(SER8);
    servo3PPos = 90;
    servo4PPos = 40;
    servo5PPos = 30;
    servo6PPos = 90;
    servo7PPos = 115;
    servo8PPos = 30;
    servo3.write(servo3PPos);
    servo4.write(servo4PPos);
    servo5.write(servo5PPos);
    servo6.write(servo6PPos);
    servo7.write(servo7PPos);
    servo8.write(servo8PPos);
    Serial.begin(9600);
    Serial.begin(115200); // Antes era 9600
    while(!Serial) {
       ; // Espera a establecer la conexión con el serial.
    }

    serialESP32.begin(115200);

    delay(20);
}

String readSerials() {
    int esp32AvailableBytes = serialESP32.available();
    int serialAvailableBytes = Serial.available();
    String cad;

    if (serialAvailableBytes > 0) {
        cad = Serial.readString();
    } else if (esp32AvailableBytes > 0) {
        cad = serialESP32.readString();
    } else {
        cad = "";
    }

    return cad;
}
  
void loop()
{
   if (Serial.available() > 0)
  {
    String cad = readSerials();
    String cad = Serial.readString(); 
    int pos = cad.indexOf(',');
    int cad1= (cad.substring(0,pos)).toInt();
    int cad2= (cad.substring(pos+1)).toInt();
    if (cad1 == 3){
      servo3Pos = cad2;
      if(servo3PPos > servo3Pos)
      for(int j = servo3PPos; j >= servo3Pos; j--){
        servo3.write(j);
        delay(20);  
      }
      if(servo3PPos < servo3Pos){
        for(int j = servo3PPos; j <= servo3Pos; j++){
          servo3.write(j);
          delay(20);
        }  
      }
      servo3PPos = servo3Pos;
    }
    if (cad1 == 4){
      servo4Pos = cad2;
      if(servo4PPos > servo4Pos)
      for(int j = servo4PPos; j >= servo4Pos; j--){
        servo4.write(j);
        delay(20);  
      }
      if(servo4PPos < servo4Pos){
        for(int j = servo4PPos; j <= servo4Pos; j++){
          servo4.write(j);
          delay(20);
        }  
      }
      servo4PPos = servo4Pos;
    }
    if (cad1 == 5){
       servo5Pos = cad2;
      if(servo5PPos > servo5Pos)
      for(int j = servo5PPos; j >= servo5Pos; j--){
        servo5.write(j);
        delay(20);  
      }
      if(servo5PPos < servo5Pos){
        for(int j = servo5PPos; j <= servo5Pos; j++){
          servo5.write(j);
          delay(20);
        }  
      }
      servo5PPos = servo5Pos;
    }
    if (cad1 == 6){
       servo6Pos = cad2;
      if(servo6PPos > servo4Pos)
      for(int j = servo6PPos; j >= servo6Pos; j--){
        servo6.write(j);
        delay(20);  
      }
      if(servo6PPos < servo6Pos){
        for(int j = servo6PPos; j <= servo6Pos; j++){
          servo6.write(j);
          delay(20);
        }  
      }
      servo6PPos = servo6Pos;
    }
    if (cad1 == 7){
       servo7Pos = cad2;
      if(servo7PPos > servo7Pos)
      for(int j = servo7PPos; j >= servo7Pos; j--){
        servo7.write(j);
        delay(20);  
      }
      if(servo7PPos < servo7Pos){
        for(int j = servo7PPos; j <= servo7Pos; j++){
          servo7.write(j);
          delay(20);
        }  
      }
      servo7PPos = servo7Pos;
    }
    if (cad1 == 8){
      servo8Pos = cad2;
      if(servo8PPos > servo8Pos)
      for(int j = servo8PPos; j >= servo8Pos; j--){
        servo8.write(j);
        delay(20);  
      }
      if(servo8PPos < servo8Pos){
        for(int j = servo8PPos; j <= servo8Pos; j++){
          servo8.write(j);
          delay(20);
        }  
      }
      servo8PPos = servo8Pos;
    }

     //mssg = Serial.parseInt(); //Leemos el serial
     //servo.write(mssg); //Movemos el servo
     //delay(50);
   //}
}
