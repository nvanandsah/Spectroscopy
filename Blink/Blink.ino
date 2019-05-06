
int counter = 0;  int inp;

int code[] = {65,71,53,66,68,73,69,57,63,64,49,67,52,54,55,56,58,59,60};
void setup() {
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  Serial.begin(9600);
}
void loop() {

  if(Serial.available()>0 )
  {uint32_t ts1 = millis();
    inp = Serial.read()-48;
    
          if (inp == code[0])
          {
            analogWrite(10, 10);
            analogWrite(11, 10);
          }
          else if (inp == code[1])
          {
            analogWrite(10, 10);
            analogWrite(11, 20);
          }
          else if (inp == code[2])
          {
           analogWrite(10, 10);
           analogWrite(11, 30);
          }
          else if (inp == code[3])
          {
           analogWrite(10, 10);
           analogWrite(11, 50);
          }
         else if (inp == code[4])
          {
          analogWrite(10, 50);
          analogWrite(11, 10);
        }
        else if (inp == code[5])
          {
            analogWrite(10, 50);
            analogWrite(11, 20);
          }
          else if (inp == code[6])
          {
            analogWrite(10, 50);
            analogWrite(11, 30);
          }
          else if (inp == code[7])
          {
           analogWrite(10, 50);
           analogWrite(11, 50);
          }
         else if (inp == code[8])
          {
          analogWrite(10, 100);
          analogWrite(11, 10);
          }
          else if (inp == code[9])
          {
          analogWrite(10, 100);
          analogWrite(11, 20);
          }
         else if (inp == code[10])
         {
         analogWrite(10, 100);
         analogWrite(11, 30);
         }
         else if (inp == code[11])
         {  analogWrite(10, 100);
            analogWrite(11, 50);
        }
         else if (inp == code[12])
        {
         analogWrite(10, 70);
         analogWrite(11, 10);
          }
         else if (inp == code[13])
         {   analogWrite(10, 150);
            analogWrite(11, 20);
          }
          else if (inp == code[14])
          {
          analogWrite(10, 70);
            analogWrite(11, 30);
          }
          else if (inp == code[15])
          {
          analogWrite(10, 70);
            analogWrite(11, 50);
          }
           uint32_t ts2 = millis();
          Serial.print(inp);
          Serial.print(",");
          
  }
  
//  counter = counter + 1;
 // if (counter == 16)
//
//  {
//    counter=0;
//   Serial.println("done");
//  }
}
