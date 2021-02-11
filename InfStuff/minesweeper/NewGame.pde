class restart{
  float x;
  float y;
  float seite;
  
  restart(float x, float y){
    this.x = x;
    this.y = y;
    this.seite = 20;
  }
  void show(){
    stroke(1);
    fill(206,14,91);
    ellipse(x, y, seite, seite);
  }
  void pressed(){
    if(mousePressed && (mouseButton == LEFT)){
      if(mouseX > this.x && mouseY > this.y && mouseX < this.x + seite && mouseY < this.y + seite){
        setup();
      }
    }
  }
}
