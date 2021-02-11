boolean inM(float x, float y, float seite){
  float mx = mouseX - (width - seite * breite)/2;
  float my = mouseY - (height - seite * hoehe)/2;
  if(mx > x && mx < x + seite && my > y && my < y + seite){
    return true;
  }else{
    return false;
  }
}

float[] getM(){
  float mx = mouseX - (width - seite * breite)/2;
  float my = mouseY - (height - seite * hoehe)/2;
  float[] ende = new float[2];
  ende[0] = mx;
  ende[1] = my;
  return ende;
}
