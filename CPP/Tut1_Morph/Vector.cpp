#include "Vector.h"
#include <stdio.h>
#include <iostream>

using namespace std;

Vector::Vector(double x, double y, double z){
    this -> x = x;
    this -> y = y;
    this -> z = z;
}
    
void Vector::printMe() {
            cout << this -> x << " " << this -> y << " " << this -> z << "\n";
        }

Vector Vector::operator +(Vector &b) {
            return Vector(this -> x + b.x, this -> y + b.y, this -> z + b.z); 
        }