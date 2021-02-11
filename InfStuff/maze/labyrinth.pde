class labyrinth {
  float feld_seite;
  float feld_hor;
  float feld_ver;
  int breite;
  int hoehe;
  feld[][] feld;
  ArrayList<String> gang = new ArrayList<String>();
  ArrayList<int[]> fertig_gang = new ArrayList<int[]>();

  labyrinth(int breite, int hoehe) {

    this.breite = breite;
    this.hoehe = hoehe;
    this.feld = new feld[breite][hoehe];
    for (int pos_x = 0; pos_x < breite; pos_x++) {
      for (int pos_y = 0; pos_y < hoehe; pos_y++) {
        feld[pos_x][pos_y] = new feld(pos_x, pos_y, (width * 0.75)/breite, (width * 0.25)/(breite + 1));
      }
    }
  }

  void show() {
    for (int pos_x = 0; pos_x < breite; pos_x++) {
      for (int pos_y = 0; pos_y < hoehe; pos_y++) {
        feld[pos_x][pos_y].show();
      }
    }
  }

  boolean contains(int[] pos) {
    int end = 0;
    for (int i = 0; i < this.fertig_gang.size(); i++) {
      if (fertig_gang.get(i) == pos) {
        end++;
      }
    }
    if (end != 0) {
      return true;
    } else {
      return false;
    }
  }

  void gangSetter() {
    int pos_x = 0;
    int pos_y = 0;
    float richtung;
    boolean step_done = false;
    int[] pos = new int[2];
    String step = new String();
    String last_step = new String();
    while (pos_x != breite - 1 || pos_y != hoehe - 1) {
      richtung = random(0, 1);
      if (richtung > 0 && richtung <= 0.25 && !last_step.equals("t") && pos_x != breite - 1) {
        pos[0] = pos_x;
        pos[1] = pos_y - 1;

        if (!contains(pos)) {
          step = "t";
          pos_y--;
          step_done = true;
          fertig_gang.add(pos);
        }
      }
      if (richtung > 0 && richtung <= 0.25 && !last_step.equals("r") && pos_y != 0) {
        pos[0] = pos_x + 1;
        pos[1] = pos_y;

        if (!contains(pos)) {
          step = "r";
          pos_x++;
          step_done = true;
          fertig_gang.add(pos);
        }
      }
      if (richtung > 0 && richtung <= 0.25 && !last_step.equals("d") && pos_y != hoehe - 1) {
        pos[0] = pos_x;
        pos[1] = pos_y + 1;

        if (!contains(pos)) {
          step = "d";
          pos_y++;
          step_done = true;
          fertig_gang.add(pos);
        }
      }
      if (richtung > 0 && richtung <= 0.25 && !last_step.equals("l") && pos_x != 0) {
        pos[0] = pos_x - 1;
        pos[1] = pos_y;

        if (!contains(pos)) {
          step = "l";
          pos_x--;
          step_done = true;
          fertig_gang.add(pos);
        }
      }
      if(step_done){
        gang.add(step);
        step_done = false;
      }
      
    }
    print(gang);
  }
}
