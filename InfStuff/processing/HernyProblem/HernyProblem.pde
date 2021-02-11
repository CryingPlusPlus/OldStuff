//objekte und variablen
ArrayList<point> points = new ArrayList<point>();
sorter sort = new sorter();
henry henry = new henry();

//------------------------------------------------------------------------------------
// setup und draw
void setup() {
  size(800, 800);

  for (int i = 0; i<100; i++) {
    points.add(new point(random(-width/3, width/3), random(-height/3, height/3)));
  }
}

void draw() {
  background(255);
  translate(width/2, height/2);
  henry.updateHenryListe(points);
  henry.show();
  for (int i = 0; i<points.size(); i++) {
    points.get(i).show();
  }
}
