class feld {
  //variablen
  public int i, j; 
  public float seite, x, y; 
  public color farbe = color(255, 255, 255);
  public int owned = 0;
  //konstruktor
  feld(int i, int j) {
    this.i = i;
    this.j = j;
    seite = 800/nRaster;
    x = 100 + (seite*i);
    y = 100 + (seite*j);
  }

  void show() {
    strokeWeight(1);
    fill(farbe);
    rect(x, y, seite, seite);
  }

  void pressed() {
    if (mousePressed) {
      if ((mouseX > x) && (mouseX < (x+seite)) && (mouseY > y) && (mouseY < (y+seite))) {
        if (owned == 0) {
          owned = 1;
          player = -1;
        }
      }
    }
  }
}
