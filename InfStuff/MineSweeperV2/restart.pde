class Restart {
  float x;
  float y;
  float r;

  Restart(float x, float y, float r) {
    this.x = x;
    this.y = y;
    this.r = r;
  }

  void show() {
    noStroke();
    fill(220, 140, 222);
    rect(x, y, r, r);
  }
  void pressed() {
    if (mousePressed && (mouseButton == LEFT)) {
      if (mouseX >  this.x && mouseX < this.x + r && mouseY >  this.y && mouseY < this.y + r) {
        setup();
      }
    }
  }
}
