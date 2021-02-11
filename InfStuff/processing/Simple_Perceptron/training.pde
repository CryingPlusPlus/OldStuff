float f(float x) {
  return 0.92 * x - 0.18;
}

class point {
  float x, y;
  int label;
  float bias;
  //konstruktoren
  point() {
    x = random(-1, 1);
    y = random(-1, 1);
    bias = 1;
    
    
    if (y > f(x)) {
      label = 1;
    } else {
      label = -1;
    }
  }
  
  point(float x, float y){
    this.x = x;
    this.y = y;
  }
  
  
  float pixelX() {
    return map(x, -1, 1, 0, width);
  }

  float pixelY() {
    return map(y, -1, 1, height, 0);
  }
  void show() {
    stroke(0);

    if (label == 1) {
      fill(255);
    } else {
      fill(0);
    }
    float px = pixelX();
    float py = pixelY();
    ellipse(px, py, 8, 8);
  }
}
