class wall {
  float x;
  float y;
  float w;

  wall(float x, float y, float w) {
    this.x = x;
    this.y = y;
    this.w = w;
  }
  
  void show(){
    rect (x,y, w, 1200);
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
}
