class klotz{
  public float x;
  public float y;
  public float w;
  public float m;
  public float v;
  public color farbe = color(255,255,255);
  public float drawW;
  
  klotz(float x, float y, float w,float m, float v, float drawW){
    this.x = x;
    this.y = y;
    this.w = w;
    this.m = m;
    this.v = v;
    this.drawW = drawW;
  }
  boolean collide(klotz other){
    boolean collision = false;
    
    if(
    (other.x < (x+w) && other.x > x)||
    ((other.x+other.w) < (x+w) && (other.x+other.w) > x)
    ){
      collision = true;
    }
    
    return collision;
  }
  
  void update(){
    x += v;
  }
  
  
  void show(){
    noStroke();
    fill(farbe);
    rect(x,y,drawW,drawW);
  }
}
