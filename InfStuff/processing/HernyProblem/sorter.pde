class sorter {


  public point Y(ArrayList<point> points, int b) {
    point endpoint = points.get(0);
    if (b < 0) {
      for (int i = 1; i< points.size(); i++) {
        if (endpoint.y > points.get(i).y) {
          endpoint = points.get(i);
        }
      }
    } else {
      for (int i = 1; i< points.size(); i++) {
        if (endpoint.y < points.get(i).y) {
          endpoint = points.get(i);
        }
      }
    }  
    return endpoint;
  }

  public point X(ArrayList<point> points, int b) {
    point endpoint = points.get(0);
    if (b < 0) {
      for (int i = 1; i< points.size(); i++) {
        if (endpoint.x > points.get(i).x) {
          endpoint = points.get(i);
        }
      }
    } else {
      for (int i = 1; i< points.size(); i++) {
        if (endpoint.x < points.get(i).x) {
          endpoint = points.get(i);
        }
      }
    }  
    return endpoint;
  }
}
