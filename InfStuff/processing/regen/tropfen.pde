class tropfen {
  float x = random(0, width);
  float y = random(-600, 0);
  float z = random(0, 20);
  float yspeed = map(z, 0, 20, 1, 20);
  float len = map(z, 0, 20, 2, 10);
  float grav = map(z, 0, 20, 0.01, 0.2);
  float thick = map(z, 0, 20, 1, 3);


  tropfen() {
  }


  void reset() {
    y= random(-600, 0);
    z = random(0, 20);
    x=random(0, width);
    yspeed = map(z, 0, 20, 1, 20);
    len = map(z, 0, 20, 2, 10);
    grav = map(z, 0, 20, 0.01, 0.2);
    thick = map(z, 0, 20, 1, 3);
  }

  void fall() {
    y = y + yspeed;
    yspeed = yspeed + grav;

    if (y>height+500) {
      reset();
    }
  }

  void show() {
    stroke(3, 57, 252);
    strokeWeight(thick);
    line(x, y, x, y+len);
  }
}
