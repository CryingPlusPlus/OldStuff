class feld{
  float x;
  float y;
  float seite;
  float pos_x;
  float pos_y;
  boolean[] richtungen = new boolean[4];
  float l, b;
  float wall;
  
  feld(float pos_x, float pos_y, float seite, float wall){
    this.pos_x = pos_x;
    this.pos_y = pos_y;
    this.seite = seite;
    this.x = pos_x * seite + (pos_x + 1) * wall;
    this.y = pos_y * seite + (pos_y + 1) * wall;
    this.l = seite;
    this.b = seite;
    this.wall = wall;
    
    for(int i = 0; i<4; i++){
      richtungen[i] = false;
    }
  }
  
  void show(){
    fill(255);
    if(richtungen[1] == true){
      b += this.wall;
    }
    if(richtungen[3] == true){
      l += this.wall;
    }
    rect(x, y, l, b);
  }
}
