int breite = 20;
int hoehe = 20;
float seite = 25;
feld f;
void setup(){
  size(500,500);
  f = new feld(5,5,seite);
}

void draw(){
  background(255);
  f.show();
}
