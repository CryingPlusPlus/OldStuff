perceptron brain;

point[] pt = new point[5000];

void setup() {
  frameRate = 120;
  size(800, 800);
  brain = new perceptron(3);

  for (int i = 0; i<pt.length; i++) {
    pt[i] = new point();
  }
}

void draw() {
  background(255);
  stroke(0);
  //line(width, 0, 0, height);
  point p1 = new point(1,f(1));
  point p2 = new point(-1, f(-1));
  stroke(0);
  line(p1.pixelX(), p1.pixelY(), p2.pixelX(), p2.pixelY());

  //showing loop
  for (int i = 0; i<pt.length; i++) {
    pt[i].show();
  }



  //training loop
  for (int i = 0; i<pt.length; i++) {

    float[] inputs = {pt[i].x, pt[i].y, pt[i].bias}; 

    brain.train(inputs, pt[i].label);

    int guess = brain.guess(inputs);

    if (guess == pt[i].label) {
      fill(0, 255, 0);
    } else {
      fill(255, 0, 0);
    }
    stroke(0);
    ellipse(pt[i].pixelX(), pt[i].pixelY(), 10, 10);
  }

  for (int i = 0; i<3; i++) {
    println(brain.weights[i]);
  }
}
