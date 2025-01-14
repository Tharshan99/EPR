int red = 2;
int green = 3;
int yellow = 4;
int button = 5;

void setup()
{
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(button, INPUT);

}

void loop()
{
   //sequence 1
  if (digitalRead(button) == HIGH){

    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(2, LOW);
    delay(3000); // Wait for 1000 millisecond(s)


    digitalWrite(2,LOW);
    digitalWrite(3,HIGH);
    digitalWrite(4, LOW);
    delay(3000); 

    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, HIGH);
    delay(2000); // Wait for 1000 millisecond(s)
  }



//sequence 2
    else if (digitalRead(button) == LOW){

        //sec 1
       digitalWrite(2,HIGH);
        digitalWrite(3,LOW);
         digitalWrite(4, LOW);
        delay(500);   
        digitalWrite(2,LOW);
        digitalWrite(3,HIGH);
         digitalWrite(4, LOW);
        delay(500);  

        //sec 2
      digitalWrite(2,HIGH);
        digitalWrite(3,LOW);
         digitalWrite(4, LOW);
        delay(500);   
      digitalWrite(2,LOW);
        digitalWrite(3,HIGH);
         digitalWrite(4, LOW);
        delay(500);   

      // sec 3
        digitalWrite(2,HIGH);
        digitalWrite(3,LOW);
         digitalWrite(4, LOW);
        delay(500);   
      digitalWrite(2,LOW);
        digitalWrite(3,HIGH);
         digitalWrite(4, LOW);
        delay(500);   

        //sec 4
        digitalWrite(2,HIGH);
        digitalWrite(3,LOW);
         digitalWrite(4, LOW);
        delay(500);   
      digitalWrite(2,LOW);
        digitalWrite(3,HIGH);
         digitalWrite(4, LOW);
        delay(500);

      // sec 5
        digitalWrite(2,HIGH);
        digitalWrite(3,LOW);
         digitalWrite(4, LOW);
        delay(500);   
      digitalWrite(2,LOW);
        digitalWrite(3,HIGH);
         digitalWrite(4, LOW);
        delay(500);   

      //follow by yellow
        digitalWrite(2, LOW);
        digitalWrite(3, LOW);
         digitalWrite(4, HIGH);
        delay(5000); 

}

  //sequence 3
   else if (digitalRead(button) == LOW){


      digitalWrite(2, HIGH);
      digitalWrite(3, LOW);
       digitalWrite(4, LOW);
      delay(3000); 

     //sec 1   
    digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250); 
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   

      // sec 2
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   

      //sec 3
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250); 
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   

      //sec 4
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   

      //sec 5
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
       digitalWrite(4, HIGH);
      delay(250);   
      }
//sequence 4
  else{
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
   digitalWrite(4, HIGH);
  delay(500);
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
   digitalWrite(4, HIGH);
  delay(500);
  
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
   digitalWrite(4, HIGH);
  delay(500);
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
   digitalWrite(4, HIGH);
  delay(500);
  
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
   digitalWrite(4, HIGH);
  delay(500);
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
   digitalWrite(4, HIGH);
  delay(500);
  
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
   digitalWrite(4, HIGH);
  delay(500);
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
   digitalWrite(4, HIGH);
  delay(500);
  
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
   digitalWrite(4, HIGH);
  delay(500);
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
   digitalWrite(4, HIGH);
  delay(500);
  
  
  
//follow by green
  digitalWrite(2, LOW);
  digitalWrite(3, HIGH);
   digitalWrite(4, LOW);
  delay(3000); 
}
}