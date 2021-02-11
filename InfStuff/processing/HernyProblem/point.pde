class point {
  public float x;
  public float y;

  point(float x, float y) {
    this.x = x;
    this.y = y;
  }

  void show() {
    fill(0);
    ellipse(x, y, 8, 8);
  }
}
