class Feld {
  float x, y, seite;
  int pos_x, pos_y;
  boolean[] ways = new boolean[4];
  color[] ways_clr = new color[4];

  Feld(int pos_x, int pos_y, float seite) {
    this.pos_x = pos_x;
    this.pos_y = pos_y;
    this.seite = seite;
    this.x = pos_x * seite;
    this.y = pos_y * seite;
    
    for (int i = 0; i < ways.length; i++) {
      this.ways[i] = false;
      this.ways_clr[i] = color(0, 0, 0);
    }
  }

  void update() {
    for (int i = 0; i < ways.length; i++) {
      if (ways[i]) {
        ways_clr[i] = color(255, 255, 255);
      }
    }
  }

  void show() {

    stroke(ways_clr[0]);
    line(x, y, x + seite, y);

    stroke(ways_clr[1]);
    line(x + seite, y, x + seite, y + seite);

    stroke(ways_clr[2]);
    line(x + seite, y + seite, x, y + seite);

    stroke(ways_clr[3]);
    line(x, y + seite, x, y);
  }
}
