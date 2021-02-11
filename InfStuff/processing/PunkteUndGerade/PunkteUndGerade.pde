punkt[] pt = new punkt[30];
punkt test;
punkt dz;
punkt rp;

float rpx;
float rpy;
//------------------------------------------------------------
void gerade(){
  if(rpx <= dz.x && rpy <= dz.y){
    line(dz.x, dz.y, rpx + 800, rpy - 800);
  }else if(rpx >= dz.x && rpy <= dz.y){
    line(dz.x, dz.y, rpx + 800, rpy + 800);
  }else if(rpx >= dz.x && rpy >= dz.y){
    line(dz.x, dz.y, rpx - 800, rpy + 800);
  }else if(rpx <= dz.x && rpy >= dz.y){
    line(dz.x, dz.y, rpx - 800, rpy - 800);
  }
}

void updateRPXRPY() {
  if (rpx <= dz.x && rpy <= dz.y) {
    rpx++;
    rpy--;
  } else if (rpx >= dz.x && rpy <= dz.y) {
    rpx++;
    rpy++;
  } else if (rpx >= dz.x && rpy >= dz.y) {
    rpx--;
    rpy++;
  } else if (rpx <= dz.x && rpy >= dz.y) {
    rpx--;
    rpy--;
  }
}
//-------------------------------------------------------------
void setup() {
  frameRate(120);
  size(800, 800);

  pt[0] = new punkt(width/2, height/2);
  pt[1] = new punkt(width/2+12, height/2+12);

  for (int i = 2; i < pt.length; i++) {

    float x = random(100, width-100);
    float y = random(100, height-100);

    test = new punkt(x, y);

    if (test.onLine(pt[i-2], pt[i-1])) {
      pt[i] = test;
    } else {
      i--;
    }
  }
  dz = pt[pt.length/2];
  rp = new punkt(200, height/2);
  rpx = 200;
  rpy = height/2;
}

void draw() {

  updateRPXRPY();

  background(255, 255, 255);
  for (int i = 0; i<pt.length; i++) {
    pt[i].show();
  }
  gerade();
  
}
