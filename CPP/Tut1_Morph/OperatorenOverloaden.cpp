#include <stdio.h>
#include <iostream>
#include "Vector.h"

using namespace std; 


int main() {
    Vector n(5, 5, 5);
    Vector m(9, 1, 1);
    Vector *pm = &m; 
    Vector name(4, 4, 4);
    Vector *pname = &name; 

    m.printMe();
    n.printMe();

    Vector x = m + n;
    x.printMe();

    return 0;
}
