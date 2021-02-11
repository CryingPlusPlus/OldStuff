tropfen[] t = new tropfen[1000];
kreis k = new kreis(75);


void setup() {
  frameRate(60);
  size(1920, 1080);
  for (int i = 0; i < t.length; i++) {
    t[i] = new tropfen();
  }
}



void draw() {
  background(255);
  for (int i = 0; i<t.length; i++) {  
    t[i].fall();
    if (k.hitkreis(t[i].x, t[i].y)==true) {
      t[i].reset();
      if (k.r<250) {
        k.r = k.r * 1.0001;
      }
    }
    t[i].show();
  }
  k.show();
}
