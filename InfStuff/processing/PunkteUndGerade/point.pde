class punkt {
  public float x;
  public float y;

  punkt(float x, float y) {
    this.x = x;
    this.y = y;
  }

  float gerade(punkt pt, float n) {
    if (x - pt.x != 0) {
      float k = (y - pt.y)/(x - pt.x);
      float d = y - k * x;
      return k*n+d;
    } else {
      return 0;
    }
  }

  boolean onLine(punkt a, punkt b) {
    boolean line = true;
    float gb_0 = gerade(b, 0);
    float gb_1 = gerade(b, 1);

    float ga_0 = gerade(a, 0);
    float ga_1 = gerade(a, 1);

    if (gb_0 == ga_0 && gb_1 == ga_1) {
      line = false;
    }
    return line;
  }

  void show() {
    fill(0,0,0);
    ellipse(x, y, 12, 12);
  }
}
