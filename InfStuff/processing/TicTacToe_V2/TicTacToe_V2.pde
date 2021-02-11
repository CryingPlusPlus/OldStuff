public int nRaster = 4;
public feld[][] f =  new feld[nRaster][nRaster];
public int player;
public int gewonnen;

void winausgabe(int player) {
  gewonnen = player;
}

void winEcke(int i, int j, int player) {
  if (i == 0 && j == 0) { //links oben
    if (
      (f[i][j].owned == player && f[i+1][j].owned == player && f[i+2][j].owned == player)||
      (f[i][j].owned == player && f[i][j+1].owned == player && f[i][j+2].owned == player)||
      (f[i][j].owned == player && f[i+1][j+1].owned == player && f[i+2][j+2].owned == player)
      ) {
      winausgabe(player);
    }
  } else if (i==(nRaster-1) && j == 0) { //rechts oben
    if (
      (f[i][j].owned == player && f[i-1][j].owned == player && f[i-2][j].owned == player)||
      (f[i][j].owned == player && f[i][j+1].owned == player && f[i][j+2].owned == player)||
      (f[i][j].owned == player && f[i-1][j+1].owned == player && f[i-2][j+2].owned == player)

      ) {
      winausgabe(player);
    }
  } else if (i == (nRaster-1) && j == (nRaster-1)) {
    if (
      (f[i][j].owned == player && f[i-1][j].owned == player && f[i-2][j].owned == player)||
      (f[i][j].owned == player && f[i][j-2].owned == player && f[i][j-2].owned == player)||
      (f[i][j].owned == player && f[i-1][j-1].owned == player && f[i-2][j-2].owned == player)
      ) {
      winausgabe(player);
    }
  } else if (i == 0 && j == (nRaster-1)) {
    if (
      (f[i][j].owned == player && f[i+1][j].owned == player && f[i+2][j].owned == player)||
      (f[i][j].owned == player && f[i][j-1].owned == player && f[i][j-2].owned == player)||
      (f[i][j].owned == player && f[i+1][j-1].owned == player && f[i+2][j-2].owned == player)
      ) {
      winausgabe(player);
    }
  }
}
void winKanten4x4(int i, int j, int player) {
  if (j==0) { // kante oben
    if (i==1) {
      if (
        (f[i][j].owned == player && f[i+1][j].owned == player && f[i+2][j].owned == player)||
        (f[i][j].owned == player && f[i][j+1].owned == player && f[i][j+2].owned == player)||
        (f[i][j].owned == player && f[i+1][j+1].owned == player && f[i+2][j+2].owned == player)
        ) {
        winausgabe(player);
      }
    }
    if (i==2) {
      if (
        (f[i][j].owned == player && f[i-1][j].owned == player && f[i-2][j].owned == player)||
        (f[i][j].owned == player && f[i][j+1].owned == player && f[i][j+2].owned == player)||
        (f[i][j].owned == player && f[i-1][j+1].owned == player && f[i-2][j+2].owned == player)
        ) {
        winausgabe(player);
      }
    }
  } else if (i == 0) { //kante links
    if (j == 1) {
      if (
        (f[i][j].owned == player && f[i+1][j].owned == player && f[i+2][j].owned == player)||
        (f[i][j].owned == player && f[i][j+1].owned == player && f[i][j+2].owned == player)||
        (f[i][j].owned == player && f[i+1][j+1].owned == player && f[i+2][j+2].owned == player)
        ) {
        winausgabe(player);
      }
    } else if (j==2) {
      if (
        (f[i][j].owned == player && f[i+1][j].owned == player && f[i+2][j].owned == player)||
        (f[i][j].owned == player && f[i][j-1].owned == player && f[i][j-2].owned == player)||
        (f[i][j].owned == player && f[i+1][j-1].owned == player && f[i+2][j-2].owned == player)
        ) {
        winausgabe(player);
      }
    }
  } else if (j==(nRaster-1)) { // kante unten
    if (i == 1) {
      if (
        (f[i][j].owned == player && f[i+1][j].owned == player && f[i+2][j].owned == player)||
        (f[i][j].owned == player && f[i][j-1].owned == player && f[i][j-2].owned == player)||
        (f[i][j].owned == player && f[i+1][j-1].owned == player && f[i+2][j-2].owned == player)
        ) {
        winausgabe(player);
      }
    } else if (i == 2) {
      if (
        (f[i][j].owned == player && f[i-1][j].owned == player && f[i-2][j].owned == player)||
        (f[i][j].owned == player && f[i][j-1].owned == player && f[i][j-2].owned == player)||
        (f[i][j].owned == player && f[i-1][j-1].owned == player && f[i-2][j-2].owned == player)
        ) {
        winausgabe(player);
      }
    }
  } else if (i == (nRaster - 1)) { //kante rechts
    if (j == 1) {
      if (
        (f[i][j].owned == player && f[i-1][j].owned == player && f[i-2][j].owned == player)||
        (f[i][j].owned == player && f[i][j+1].owned == player && f[i][j+2].owned == player)||
        (f[i][j].owned == player && f[i-1][j+1].owned == player && f[i-2][j+2].owned == player)
        ) {
        winausgabe(player);
      }
    } else if (j == 2) {
      if (
        (f[i][j].owned == player && f[i-1][j].owned == player && f[i-2][j].owned == player)||
        (f[i][j].owned == player && f[i][j-1].owned == player && f[i][j-2].owned == player)||
        (f[i][j].owned == player && f[i-1][j-1].owned == player && f[i-2][j-2].owned == player)
        ) {
        winausgabe(player);
      }
    }
  }
}

public void coloring(int i, int j) {
  if (f[i][j].owned == 1) {
    f[i][j].farbe = color(0, 102, 255);
  } else if (f[i][j].owned == -1) {
    f[i][j].farbe = color(235, 52, 52 );
  }
}
ArrayList<int[]> allefreien() {
  ArrayList<int[]> a = new ArrayList<int[]>();
  int[] b = new int[2];
  for (int j = 0; j<nRaster; j++) {
    for (int i = 0; i<nRaster; i++) {
      if (f[i][j].owned == 0) {
        b[0] = i;
        b[1] = j;
        a.add(b);
      }
    }
  }
  return a;
}
void viktor() {
  ArrayList<int[]> a = allefreien();
  int[] b = new int[2];
  b = a.get(int(random(0, a.size())));
  f[b[0]][b[1]].owned = -1;
  println(b);
  println();
}

void currentplayer (int player) {
  textSize(32);
  fill(color(255, 255, 255));
  if (player == 1) {
    text(("Spieler Blau"), 50, 50);
  } else if (player == -1) {
    text(("Spieler Rot"), 50, 50);
  }
}



void setup() {
  gewonnen = 0;
  if (random(0, 1)<0.5) {
    player = 1;
  } else {
    player = -1;
  }

  for (int j = 0; j<nRaster; j++) {
    for (int i = 0; i<nRaster; i++) {
      f[i][j] = new feld(i, j);
      f[i][j].owned = 0;
    }
  }
  background(51);
  size(1000, 1000);
  frameRate = 20;
}
void draw() {
  currentplayer(player);
  //felder sachen machen
  if (mousePressed) {
    println(mouseX, mouseY);
    println();
  }
  if (gewonnen == 0) {
    for (int j = 0; j<nRaster; j++) {
      for (int i = 0; i<nRaster; i++) {
        winEcke(i, j, 1);
        winEcke(i, j, -1);
        winKanten4x4(i, j, 1);
        winKanten4x4(i, j, -1);
        f[i][j].show();
        coloring(i, j);
        if (player == 1) {
          f[i][j].pressed();
        } else if (player == -1) {
          viktor();
          player = 1;
        }
      }
    }
  } else {
    if (gewonnen == -1) {
      if (player == 1) {
        background(51);
        fill(255);
        textSize(50);
        text("Spieler Rot hat gewonnen", 100, 100);
      } else if (player == -1) {
        background(51);
        fill(255);
        textSize(50);
        text("Spieler Blau hat gewonnen", 100, 100);
      }
    }
  }
}
