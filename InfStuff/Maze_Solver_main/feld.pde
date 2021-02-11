class feld{
  int pos_x, pos_y, snake;
  float x, y, seite;
  boolean visited;
  boolean ways[] = {false, false, false, false};
  color feld_clr;
  
  feld(int pos_x, int pos_y, float seite){
    this.pos_x = pos_x;
    this.pos_y = pos_y;
    this.seite = seite;
    
    this.x = seite * this.pos_x;
    this.y = seite * this.pos_y;
  }
  
  void show(){
    noStroke();
    rect(x, y, seite, seite);
    if(!ways[0]){
      stroke(3);
      line(x, y, x + seite, y);
    }
    if(!ways[1]){
      stroke(3);
      line(x + seite, y, x + seite, y + seite);
    }
    if(!ways[2]){
      stroke(3);
      line(x + seite, y + seite, x, y + seite);
    }
    if(!ways[3]){
      stroke(3);
      line(x, y + seite, x, y);
    }
  }  
}
