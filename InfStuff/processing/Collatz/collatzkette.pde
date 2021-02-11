class collatzkette {
  ArrayList<IntList> kettenListe = new ArrayList<IntList>();
  float gerade = -PI/24;
  float ungerade = PI/24;
  float len = 10;
  float r = 51;
  float g = 150;
  float b = 51;
  float w = 10;
  IntList kette;
  color[] colors = {
    color(150, 250, 150), color(104, 252, 90), color(21, 237, 111), color(42, 209, 247), color(49, 83, 249), color(159, 12, 209)  
  };
  collatzkette(int n) {


    for (int i = 1; i <= n; i++) {

      kette = collatz(i);
      kette.reverse();
      kettenListe.add(kette);
    }
  }
  void show() {
    translate(850, 600);
    rotate(PI*3/2);
    strokeWeight(w);
    for (int i = 0; i<kettenListe.size(); i++) {
      push();
      //stroke(colors[int(random(0,colors.length-1))]);
      stroke(255);
        for (int j = 0; j<kettenListe.get(i).size(); j++) {
        if (kettenListe.get(i).get(j) % 2 == 0) {
          rotate(gerade);
        } else {
          rotate(ungerade);
        }
        strokeWeight(1);
        line(0, 0, 0, len);
        translate(0, len);
      }

      pop();
    }
  }
}
