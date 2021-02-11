class henry {
  ArrayList<point> henryListe;

  henry() {
    henryListe = new ArrayList<point>();
    henryListe.add(new point(0, 0));
  }
  ArrayList<point> outerpoints(ArrayList<point> points, ArrayList<point> control) {
    ArrayList<point> outerpoints = new ArrayList<point>();

    for (int i = 0; i<points.size(); i++) {
      if (points.get(i).x  >= control.get(0).x && 
          points.get(i).x <= control.get(2).x && 
          points.get(i).y >= control.get(1).y &&
          points.get(i).y <= control.get(3).y
        ){}else{
          outerpoints.add(points.get(i));
        }
      }

      return outerpoints;
  }

  ArrayList<point> breakpoints(ArrayList<point> points){
    ArrayList<point> breakpoints = new ArrayList<point>();
    breakpoints.add(sort.X(points, -1));
    breakpoints.add(sort.Y(points, -1));
    breakpoints.add(sort.X(points, 1));
    breakpoints.add(sort.Y(points, 1));
    
    return breakpoints;
  }
  void updateHenryListe(ArrayList<point> points) {
      ArrayList<point> control = new ArrayList<point>();
      henryListe = breakpoints(points);
      control = henryListe;
  
    }

  void show() {
    println(henryListe.get(2).x, henryListe.get(2).y);
    for (int i = 1; i < henryListe.size(); i++) {
      stroke(0);
      line(henryListe.get(i-1).x, henryListe.get(i-1).y, henryListe.get(i).x, henryListe.get(i).y);
    }
    line(henryListe.get(henryListe.size()-1).x, henryListe.get(henryListe.size()-1).y, henryListe.get(0).x, henryListe.get(0).y);
  }
}
