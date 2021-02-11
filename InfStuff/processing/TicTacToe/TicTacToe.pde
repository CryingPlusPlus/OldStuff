int nRaster = 4;
public boolean gewonnen;
public int win = 0;
feld[][] f = new feld[nRaster][nRaster];
public int player;
float startTimer;



void winausgabe() {
  gewonnen = true;
}


void winEcke(int i, int j, int player) {
  if (i == 0 && j == 0) { //links oben
    if (
      (f[i][j].gehoert == player && f[i+1][j].gehoert == player && f[i+2][j].gehoert == player)||
      (f[i][j].gehoert == player && f[i][j+1].gehoert == player && f[i][j+2].gehoert == player)||
      (f[i][j].gehoert == player && f[i+1][j+1].gehoert == player && f[i+2][j+2].gehoert == player)
      ) {
      winausgabe();
    }
  } else if (i==(nRaster-1) && j == 0) { //rechts oben
    if (
      (f[i][j].gehoert == player && f[i-1][j].gehoert == player && f[i-2][j].gehoert == player)||
      (f[i][j].gehoert == player && f[i][j+1].gehoert == player && f[i][j+2].gehoert == player)||
      (f[i][j].gehoert == player && f[i-1][j+1].gehoert == player && f[i-2][j+2].gehoert == player)

      ) {
      winausgabe();
    }
  } else if (i == (nRaster-1) && j == (nRaster-1)) {
    if (
      (f[i][j].gehoert == player && f[i-1][j].gehoert == player && f[i-2][j].gehoert == player)||
      (f[i][j].gehoert == player && f[i][j-2].gehoert == player && f[i][j-2].gehoert == player)||
      (f[i][j].gehoert == player && f[i-1][j-1].gehoert == player && f[i-2][j-2].gehoert == player)
      ) {
      winausgabe();
    }
  } else if (i == 0 && j == (nRaster-1)) {
    if (
      (f[i][j].gehoert == player && f[i+1][j].gehoert == player && f[i+2][j].gehoert == player)||
      (f[i][j].gehoert == player && f[i][j-1].gehoert == player && f[i][j-2].gehoert == player)||
      (f[i][j].gehoert == player && f[i+1][j-1].gehoert == player && f[i+2][j-2].gehoert == player)
      ) {
      winausgabe();
    }
  }
}


void winKanten3x3(int i, int j, int player) {
  if (i== 1 && j == 0) {
    if (
      (f[i][j].gehoert == player && f[i][j+1].gehoert == player && f[i][j+2].gehoert == player)
      ) {
      winausgabe();
    }
  } else if (i == 0 && j == 1) {
    if (
      (f[i][j].gehoert == player && f[i+1][j].gehoert == player && f[i+2][j].gehoert == player)
      ) {
      winausgabe();
    }
  }
}


void winKanten4x4(int i, int j, int player) {
  if (j==0) { // kante oben
    if (i==1) {
      if (
        (f[i][j].gehoert == player && f[i+1][j].gehoert == player && f[i+2][j].gehoert == player)||
        (f[i][j].gehoert == player && f[i][j+1].gehoert == player && f[i][j+2].gehoert == player)||
        (f[i][j].gehoert == player && f[i+1][j+1].gehoert == player && f[i+2][j+2].gehoert == player)
        ) {
        winausgabe();
      }
    }
    if (i==2) {
      if (
        (f[i][j].gehoert == player && f[i-1][j].gehoert == player && f[i-2][j].gehoert == player)||
        (f[i][j].gehoert == player && f[i][j+1].gehoert == player && f[i][j+2].gehoert == player)||
        (f[i][j].gehoert == player && f[i-1][j+1].gehoert == player && f[i-2][j+2].gehoert == player)
        ) {
        winausgabe();
      }
    }
  } else if (i == 0) { //kante links
    if (j == 1) {
      if (
        (f[i][j].gehoert == player && f[i+1][j].gehoert == player && f[i+2][j].gehoert == player)||
        (f[i][j].gehoert == player && f[i][j+1].gehoert == player && f[i][j+2].gehoert == player)||
        (f[i][j].gehoert == player && f[i+1][j+1].gehoert == player && f[i+2][j+2].gehoert == player)
        ) {
        winausgabe();
      }
    } else if (j==2) {
      if (
        (f[i][j].gehoert == player && f[i+1][j].gehoert == player && f[i+2][j].gehoert == player)||
        (f[i][j].gehoert == player && f[i][j-1].gehoert == player && f[i][j-2].gehoert == player)||
        (f[i][j].gehoert == player && f[i+1][j-1].gehoert == player && f[i+2][j-2].gehoert == player)
        ) {
        winausgabe();
      }
    }
  } else if (j==(nRaster-1)) { // kante unten
    if (i == 1) {
      if (
        (f[i][j].gehoert == player && f[i+1][j].gehoert == player && f[i+2][j].gehoert == player)||
        (f[i][j].gehoert == player && f[i][j-1].gehoert == player && f[i][j-2].gehoert == player)||
        (f[i][j].gehoert == player && f[i+1][j-1].gehoert == player && f[i+2][j-2].gehoert == player)
        ) {
        winausgabe();
      }
    } else if (i == 2) {
      if (
        (f[i][j].gehoert == player && f[i-1][j].gehoert == player && f[i-2][j].gehoert == player)||
        (f[i][j].gehoert == player && f[i][j-1].gehoert == player && f[i][j-2].gehoert == player)||
        (f[i][j].gehoert == player && f[i-1][j-1].gehoert == player && f[i-2][j-2].gehoert == player)
        ) {
        winausgabe();
      }
    }
  } else if (i == (nRaster - 1)) { //kante rechts
    if (j == 1) {
      if (
        (f[i][j].gehoert == player && f[i-1][j].gehoert == player && f[i-2][j].gehoert == player)||
        (f[i][j].gehoert == player && f[i][j+1].gehoert == player && f[i][j+2].gehoert == player)||
        (f[i][j].gehoert == player && f[i-1][j+1].gehoert == player && f[i-2][j+2].gehoert == player)
        ) {
        winausgabe();
      }
    } else if (j == 2) {
      if (
        (f[i][j].gehoert == player && f[i-1][j].gehoert == player && f[i-2][j].gehoert == player)||
        (f[i][j].gehoert == player && f[i][j-1].gehoert == player && f[i][j-2].gehoert == player)||
        (f[i][j].gehoert == player && f[i-1][j-1].gehoert == player && f[i-2][j-2].gehoert == player)
        ) {
        winausgabe();
      }
    }
  }
}


void currentplayer() {
  background(51);
  textSize(32);
  fill(color(255, 255, 255));
  text(("Player: " + player), 50, 50);
}


void setup() {

  size(1000, 1000);
  gewonnen = false;
  //felder einfügen
  for (int j = 0; j<nRaster; j++) {
    for (int i = 0; i<nRaster; i++) {
      f[i][j] = new feld(nRaster, i, j);
      f[i][j].normal = color(255, 255, 255);
    }
  }
  //spieler
  if (random(0, 1)<0.5) {
    player =0;
  } else {
    player = 1;
  }
}

void draw() {
  background(51);
  //currentplayer();

  //felder ansteuern und zeichnen
  if (!gewonnen) {
    startTimer = millis();
    for (int j = 0; j<nRaster; j++) {
      for (int i = 0; i<nRaster; i++) {
        f[i][j].pressed(player);

        winEcke(i, j, 1);
        winEcke(i, j, 0);
        if (nRaster == 3) {
          winKanten3x3(i, j, 0);
          winKanten3x3(i, j, 1);
        } else if (nRaster == 4) {
          winKanten4x4(i, j, 0);
          winKanten4x4(i, j, 1);
        }
        f[i][j].show();
      }
    }
  } else if (player == 1) {
    //while ((millis() - startTimer) < 10000) {
      background(51);
      fill(color(255, 255, 255));
      textSize(50);
      text(("Spieler 0 Rot hat gewonnen"), 100, 100, 900, 900);
    //}
    setup();
  } else if (player == 0) {
    //while ((millis() - startTimer) < 10000) {
      background(51);
      textSize(50);
      fill(color(255, 255, 255));
      text(("Spieler 1 Blau hat gewonnen"), 100, 100, 900, 900);
      setup();
    //}
  }
}
