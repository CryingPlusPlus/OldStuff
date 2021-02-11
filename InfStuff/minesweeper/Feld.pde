class Feld {
  //Variablen
  float x, y, i, j, seite;
  color clr;
  boolean clicked;
  boolean mine;
  boolean marked;
  int umgebung;
  float mx;
  float my;

  //Konstruktor
  Feld(float i, float j, float seite, boolean mine) {
    this.marked = false;
    this.x = i * seite;
    this.y = j * seite;
    this.i = i;
    this.mine = mine;
    this.j = j;
    this.seite = seite;
    this.clicked = false;
    this.clr = color(51, 51, 51);
  }

  //Methoden
  void show() {
    textAlign(CENTER);
    fill(clr);
    if (!marked) {
      rect(x, y, seite, seite);
      if (clicked && !mine && umgebung != 0) {
        fill(35, 163, 6);
        textSize(seite);
        text(umgebung, x + seite/2, y + seite * 0.9);
      }
    } else {
      fill(0, 0, 255);
      rect(x, y, seite, seite);
      line(x, y, x + seite, y + seite);
      line(x, y + seite, x + seite, y);
    }
  }

  

  void right_pressed() {
    if (mousePressed && (mouseButton == RIGHT)) {
      mx = mouseX - (width - breite * default_seite)/2;
      my = mouseY - (height - hoehe * default_seite)/2;

      if (mx > x && mx < x + seite && my > y && my < y + seite) {
        if (marked) {
          this.marked = false;
          pause(100);
        } else {
          this.marked = true;
          pause(100);
        }
      }
    }
  }

  void left_pressed() {
    if (!marked) {
      mx = mouseX - (width - breite * default_seite)/2;
      my = mouseY - (height - hoehe * default_seite)/2;
      if (mousePressed && (mouseButton == LEFT) && !marked) {
        if (mx > x && mx < x + seite && my > y && my < y + seite) {
          this.clicked = true;
        }
      }
    }
  }

  void update() {
    if (clicked) {
      if (!mine) {
        this.clr = color(201);
      } else {
        this.clr = color(255, 0, 0);
        ende = true;
      }
    }
  }
}
