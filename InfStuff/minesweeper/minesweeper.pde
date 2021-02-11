int breite = 20;
int hoehe = 20;
float h_seite;
float b_seite;
float default_seite;
float anteil;
boolean ende = false;
Feld[][] Feld = new Feld[breite][hoehe];
restart restart = new restart(25, 25);
boolean first_click;


void setup() {
  
  size(1200, 900);

  //Instanzierung der Umgebung
  anteil = 0.2;

  //Setter der UMgebung
  feldSetter();
  wertSetter();
  first_click = true;
}

void draw() {
  if (!ende) {
    background(151);
    restart.show();
    translate((width - breite * default_seite)/2, (height - hoehe * default_seite)/2);
    for (int i = 0; i<breite; i++) {
      for (int j = 0; j<hoehe; j++) {
        Feld[i][j].right_pressed();
        Feld[i][j].left_pressed();
        Feld[i][j].update();
        Feld[i][j].show();
      }
    }
  }
}
