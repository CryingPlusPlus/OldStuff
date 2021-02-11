void FeldSetter(){
  boolean[] mines = new boolean[breite * hoehe];
  int k = 0;
  for(int i = 0; i < breite * hoehe; i++){
    if(random(0, 1) <= poss){
      mines[i] = true;
    }else{
      mines[i] = false;
    }
  }
  
  for(int i = 0; i < breite; i++){
    for(int j = 0; j < hoehe; j++){
      Feld[i][j] = new Feld(i, j, seite, mines[k]);
      k++;
    }
  }
}
