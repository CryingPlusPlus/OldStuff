class Maze {
  int breite, hoehe;
  float seite;
  Feld[][] Feld;
  Maze(int breite, int hoehe, int seite) {
    this.breite = breite;
    this.hoehe = hoehe;
    this.seite = seite;
    Feld = new Feld[hoehe][breite];

    for (int pos_x = 0; pos_x < breite; pos_x++) {
      for (int pos_y = 0; pos_y < hoehe; pos_y++) {
        Feld[pos_x][pos_y] = new Feld(pos_x, pos_y, this.seite);
      }
    }
  }
  void update() {
    for (int pos_x = 0; pos_x < breite; pos_x++) {
      for (int pos_y = 0; pos_y < hoehe; pos_y++) {
        Feld[pos_x][pos_y].update();
      }
    }
  }

  void show() {
    for (int pos_x = 0; pos_x < breite; pos_x++) {
      for (int pos_y = 0; pos_y < hoehe; pos_y++) {
        Feld[pos_x][pos_y].show();
      }
    }
  }

  void mainGang(int d) {
    
    ArrayList<Feld> drehFelder = new ArrayList<Feld>();
    
    for(int i = 0; i < d; i++){
      drehFelder.add(Feld[round(random(1, breite - 1))][round(random(1, hoehe))]);
    }
    
    drehFelder = sort(drehFelder);
    
    for(int i = 0; i < drehFelder.size(); i++){
      print(drehFelder.get(i).pos_x + drehFelder.get(i).pos_y);
      print(" ");
    }
  }
}
