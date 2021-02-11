int breite;
int hoehe;
int seite;
float poss;
boolean ende;
boolean first_click;

Feld[][] Feld;
Restart Restart;

void setup() {
  //fullScreen();
  size(1200, 900);
  breite = 20;
  hoehe = 20;
  poss = 0.3;

  Feld = new Feld[breite][hoehe];
  Restart = new Restart(25, 25, 20);
  ende = false;
  first_click = true;
  //seite definieren
  if (width / breite < height / hoehe) {
    seite = width / breite;
  } else {
    seite =  height / hoehe;
  }
  //Felder
  FeldSetter();
}

void draw() {
  Restart.show();
  Restart.pressed();
  if (!ende) {
    background(230);
    Restart.show();
    Restart.pressed();
    translate((width - seite * breite)/2, (height - seite * hoehe)/2);

    //Felder
    for (int i = 0; i < breite; i++) {
      for (int j = 0; j < hoehe; j++) {
        check();
        Feld[i][j].pressed();
        Feld[i][j].show();
        Feld[i][j].update();
      }
    }
  } else {
    Restart.show();
    Restart.pressed();
    translate((width - seite * breite)/2, (height - seite * hoehe)/2);
    for (int i = 0; i < breite; i++) {
      for (int j = 0; j < hoehe; j++) {
        Feld[i][j].show();
        Feld[i][j].update();
      }
    }
  }
}
