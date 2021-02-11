#include <iostream>
#include <cmath>

// struct Point {
//     int x, y;

//     double get_Abs() {
//         return sqrt(x * x + y * y);
//     }
// };

class Point {
    public:
        int x, y;
        Point(int x, int y) {
            this -> x = x;
            this -> y = y;
        }
        Point operator + (Point &b) {
            Point newP(this -> x + b.x, this -> y + b.y);
            return newP;
        }
};

std::ostream& operator << (std::ostream &output, Point &p) {
    output << p.x << " " << p.y;
    return output;
}

int main() {
    Point a = {1, 3};
    Point b = {5, 6};
    Point c = a + b;

    std::cout << c << std::endl;
    return 0;
}