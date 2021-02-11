void feldSetter() {

  boolean[] mine = new boolean[breite * hoehe];
  for (int i = 0; i<breite*hoehe; i++) {
    if(random(0,1) <= anteil){
      mine[i] = true;
    }else{
      mine[i] = false;
    }
  }
  h_seite = height / hoehe;
  b_seite = width / breite;

  if (h_seite <= b_seite) {
    default_seite = h_seite;
  } else {
    default_seite = b_seite;
  }

  //felder generieren
  int mines = 0;
  for (int i = 0; i<breite; i++) {
    for (int j = 0; j<hoehe; j++) {
      Feld[i][j] = new Feld(i, j, default_seite, mine[mines]);
      mines++;
    }
  }
}
