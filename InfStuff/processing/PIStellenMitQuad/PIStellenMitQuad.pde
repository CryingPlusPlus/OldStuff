float m = 10000;
klotz big = new klotz(0, 200, m, m, -1, 100);
klotz smol = new klotz(-100, 250, 50, 1, 0, 50);
wall wall = new wall(-400-m, -400, m+100);
int c = 0;
//-----------------------------------------------------



void updateV() {
  float bigV, smolV;
  bigV = (big.m-smol.m)/(big.m+smol.m)*big.v + 2*smol.m/(big.m+smol.m)*smol.v;
  smolV = (2 * big.m/(big.m+smol.m)*big.v) + ((smol.m - big.m)/(big.m + smol.m)*smol.v);
  big.v = bigV;
  smol.v = smolV;
}


//---------------------------------------------------
void setup() {
  frameRate(6000);
  size(800, 800);
}

void draw() {
  //-----------------------------------------------
  //Setup stuff
  background(71, 71, 71);
  translate(width/2, height/2);
  fill(51, 51, 51);
  rect(-400, 300, 1200, 1200);
  wall.show();
  //-------------------------------------------------
  //Block Stuff
  if (big.collide(smol)) {
    updateV();
    c++;
  }
  if (wall.collide(smol)) {
    smol.v = smol.v * -1;
    c++;
  }

  fill(255);
  textSize(32);
  text(c, -300, -300);
  smol.update();
  big.update();

  //smol.show();
  //big.show();

  if (abs(smol.v) < 15) {
    big.show();
    smol.show();
  } else {
    rect(-300+smol.drawW, big.y, big.drawW, big.drawW);
    rect(-300, smol.y, smol.drawW, smol.drawW);
  }
}
