labyrinth labyrinth;

void setup() {
  size(800, 800);
  labyrinth = new labyrinth(20, 20);
  labyrinth.gangSetter();
}

void draw() {
  background(0);
  labyrinth.show();
}
