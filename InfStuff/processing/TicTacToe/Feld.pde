class feld {
  //Variablen
  public float x;
  public float y;
  float raster;
  public int gefaerbt;
  public int gehoert = 2;
  public float i;
  public float j;
  float seite;
  color normal = color(255, 255, 255);
  //Konstruktor
  feld(float r, float i, float j) {
    raster = r;
    this.i = i;
    this.j = j;
    seite = 800/r;
    x = 100+(seite*i);
    y = 100 + (seite*j);  
}
  void show() {
    fill(normal);
    rect(x, y, seite, seite);
  }
  //gepressedte felder einfärben
  void pressed(int p) {
    if (mousePressed) {
      if (normal == color(255, 255, 255)) {
        if ((mouseX > x) && (mouseX < (x+seite)) && (mouseY > y) && (mouseY < (y+seite))) {
          if (p == 0) {
            normal = color(235, 52, 52);
            player =1;
            gehoert = 0;
            gefaerbt = 1;
          } else if (p == 1) {
            normal = color(0, 102, 255);
            gehoert = 1;
            player = 0;
            gefaerbt = 1;
          }
        }
      }
    }
  }

  //feld gepresst
}
