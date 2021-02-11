#include <stdio.h>
#include <math.h>
#include <iostream>

using namespace std;

class Kreis {
    private:
        float radius;

    public:
        void setRadius(float r){
            if(r >= 0){
                radius = r;
            }
        }

        Kreis() {
            radius = 0;
        }
        Kreis(float r) {
            radius = r;
        }

        float area() {
            return M_PI * radius * radius; 
        }
};

// Kreis::Kreis(float r) {
//     radius = r;
// } Konstruktoren außerhalb der Klasse

//Andere Methode Klassen zu schreiben
class Rechteck {
    public:
        float seite1;
        float seite2;

        Rechteck(float r1, float r2):seite1(r1), seite2(r2){
            //do Stuff here
        }

        float area() {
            return seite1 * seite2;
        }
};


int main() {
    Kreis frank(25);
    cout << frank.area() << "\n";

    // frank.radius = 25; geht nicht mehr weil radius Privat
    cout << frank.area() << "\n";

    Rechteck Hans = {12, 10};

    cout << Hans.area() << "\n";

    Kreis *pointerFrank = &frank;

    cout << pointerFrank -> area() << "\n";

    pointerFrank -> setRadius(500);

    cout << pointerFrank -> area() << "\n";


    return 0;
}