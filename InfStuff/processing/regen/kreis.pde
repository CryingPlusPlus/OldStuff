class kreis {
  float r; 

  kreis(float radius) {
    r = radius;
  }

  void show() {
    strokeWeight(r);
    stroke(51);
    fill(51);
    circle(mouseX, mouseY, r);
  }
  boolean hitkreis(float x, float y) {
    if (((x-mouseX)*(x-mouseX))+((y-mouseY)*(y-mouseY)) < r*r) {
      return true;
    } else {
      return false;
    }
  }
}
