collatzkette ck = new collatzkette(50000);
import processing.serial.*;
import processing.pdf.*;

IntList collatz(int n) {
  IntList end = new IntList();
  while (n != 1) {
    end.append(n);
    if (n % 2 == 0) {
      n = n / 2;
    } else {
      n = n*3+1;
    }
  }
  end.append(1);
  return end;
}
void setup() {
  frameRate = 0;
  size(1920, 1080);
  beginRecord(PDF, "collatz.pdf");
}

void draw() {
  background(0);
  ck.show();
  endRecord();
}
