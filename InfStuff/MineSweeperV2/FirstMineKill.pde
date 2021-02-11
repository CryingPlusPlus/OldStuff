void check() {
  if (mousePressed && first_click) {
    float mx = getM()[0];
    float my = getM()[1];
    int r_i = 0, r_j = 0;
    for (int i = 0; i < breite; i++) {
      if (mx > i * seite && mx < i * seite + seite) {
        r_i = i;
      }
    }
    for (int j = 0; j < hoehe; j++) {
      if (my > j * seite && my < j * seite + seite) {
        r_j = j;
      }
    }
    FirstMineKill(r_i, r_j);
    first_click = false;
  }
}

void FirstMineKill(int i, int j) {
  Feld[i][j].mine = false;

  if (j - 1 >= 0) {
    Feld[i][j-1].mine = false;
    if (i - 1 >= 0) {
      Feld[i-1][j-1].mine = false;
    }
    if (i + 1 <= breite - 1) {
      Feld[i+1][j-1].mine = false;
    }
  }
  if (j + 1 <= hoehe - 1) {
    Feld[i][j+1].mine = false;
    if (i - 1 >= 0) {
      Feld[i-1][j+1].mine = false;
    }
    if (i + 1 <= breite - 1) {
      Feld[i+1][j+1].mine = false;
    }
  }
  if (i - 1 >= 0) {
    Feld[i-1][j].mine = false;
  }
  if (i + 1 <= breite - 1) {
    Feld[i+1][j].mine = false;
  }

  WertSetter();
}
