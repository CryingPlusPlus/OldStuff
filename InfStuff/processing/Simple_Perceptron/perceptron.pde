class perceptron {
  float[] weights;
  float lernRate = 0.1;

  //konstruktor
  perceptron(int n) {
    weights = new float[n];
    for (int i = 0; i<weights.length; i++) {
      weights[i] = random(-1, 1);
    }
  }

  //activation function
  int sign(float n) {
    if (n >= 0) {
      return 1;
    } else {
      return -1;
    }
  }

  
  int guess(float[] inputs) {
    float sum = 0;
    for (int i = 0; i<weights.length; i++) {
      sum = sum + inputs[i]*weights[i];
    }
    int output = sign(sum);
    return output;
  }
  
  void train(float[] inputs, int target){
    int guess = guess(inputs);
    int error = target - guess;
    
    for(int i = 0; i<weights.length; i++){
      weights[i] +=(error * inputs[i] * lernRate);
    }
  }
}
