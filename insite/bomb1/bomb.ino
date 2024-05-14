#include <LiquidCrystal.h>

#define PIN_RS 0
#define PIN_EN 1
#define PIN_D4 2
#define PIN_D5 3
#define PIN_D6 4
#define PIN_D7 5


unsigned long initTime, time;

uint16_t frequenzy = 600;
uint16_t waitTime = 1000;
uint16_t countTime = 300;

LiquidCrystal lcd(PIN_RS,PIN_EN,PIN_D4,PIN_D5,PIN_D6,PIN_D7);

void actualizarLCD() {
  uint8_t minutos = countTime /60;
  uint8_t segundos = countTime % 60;
  
  lcd.setCursor(0,0);
  lcd.print(minutos);
  lcd.print(":");

  if (segundos < 10)
  	lcd.print("0");
  lcd.print(segundos);
}

void mensajeVictoria() {
  lcd.setCursor(0,0);
  lcd.print("DESACTIVADO");
  lcd.setCursor(0,1);
  // Flag: ETSIIT_CTF{flag}
  lcd.print("flag");
  while(true);
}

void mensajeDerrota() {
  lcd.setCursor(0,0);
  lcd.print("ESTALLÓ");
  lcd.setCursor(0,1);
  lcd.print("LA BOMBA!!!");
  while(true);
}


void setup() {
  
  // Set up Pins
  pinMode(8, INPUT);  // RED
  pinMode(9, INPUT);  // YELLOW
  pinMode(10, INPUT); // GREEN
  pinMode(11, INPUT); // Im BLUE dabidabadabudiba
  
  // Set up LCD
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  
  // Set up Piezo
  pinMode(6,OUTPUT);
  
  // Start clock
  initTime = millis();
}

void loop() {
  time = millis() - initTime;
  
  // Piezo Beep
  frequenzy = (frequenzy +600) % 1200;
  if (frequenzy == 0)
    noTone(6);
  else
  	tone(6, frequenzy);
  
  if (digitalRead(8)&& digitalRead(9) && digitalRead (10) && countTime) {
    if (time >= 1000){
  		actualizarLCD();
    	initTime = millis();
      	if (countTime == 60){
    	  waitTime = 500;
      	}
    	// LCD print number
    	countTime--;
    	if (digitalRead(11) == LOW) {
    		// Deactivated
      		mensajeVictoria();
    	}
    }
  } else {
  	// LCD Kaboom
    mensajeDerrota();
  }
  delay(waitTime); // Wait for 1000 millisecond(s)
}