void WertSetter() {
  int danger;
  for (int i = 0; i<breite; i++) {
    for (int j = 0; j<hoehe; j++) {
      danger = 0;
      if (i - 1 >= 0 && j - 1 >= 0) {
        if (Feld[i-1][j-1].mine) {
          danger++;
        }
      }
      if (j - 1 >= 0) {
        if (Feld[i][j-1].mine) {
          danger++;
        }
      }
      if (i + 1 <= breite - 1 && j - 1 >= 0) {
        if (Feld[i+1][j-1].mine) {
          danger++;
        }
      }
      if (i - 1 >= 0) {
        if (Feld[i-1][j].mine) {
          danger++;
        }
      }
      if (i + 1 <= breite - 1) {
        if (Feld[i+1][j].mine) {
          danger++;
        }
      }
      if (i - 1 >= 0 && j + 1 <= hoehe - 1) {
        if (Feld[i-1][j+1].mine) {
          danger++;
        }
      }
      if (j + 1 <= hoehe - 1) {
        if (Feld[i][j+1].mine) {
          danger++;
        }
      }
      if (i + 1 <= breite - 1 && j + 1 <= hoehe - 1) {
        if (Feld[i+1][j+1].mine) {
          danger++;
        }
      }
      Feld[i][j].danger = danger;
    }
  }
}
