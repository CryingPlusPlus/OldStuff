class Feld {
  int i;
  int j;
  float seite;
  boolean mine;
  boolean clicked;
  boolean marked;
  int danger;
  color clr;

  Feld(int i, int j, float seite, boolean mine) {
    this.i = i;
    this.j = j;
    this.seite = seite;
    this.mine = mine;
    this.clicked = false;
    this.marked = false;
    clr = color(51);
    this.danger = 0;
  }

 //<>//
  void show() {
    stroke(1);
    fill(clr);
    rect(i * seite, j * seite, seite, seite);
    if (clicked && danger > 0 && !mine) {
      textAlign(CENTER, TOP);
      fill(0, 200, 0);
      textSize(seite * 0.9);
      text(danger, i * seite + seite/2, j * seite);
    }
  }

  void update() {
    if (clicked) {
      if (mine) {
        clr = color(255, 0, 0);
        ende = true;
      } else {
        clr = color(201);
      }
    }
  }

  void pressed() {
    if (mousePressed) {
      if (inM(this.i * this.seite, this.j * this.seite, this.seite)) {
        if (mouseButton == LEFT && !this.marked) {
          this.clicked = true;
        }
        if (mouseButton == RIGHT) {
          if (this.marked) {
            this.marked = false;
            clr = color(51);
            pause(200);
          } else {
            this.marked = true;
            clr = color(0, 0, 255);
            pause(200);
          }
        }
      }
    }
  }
}
