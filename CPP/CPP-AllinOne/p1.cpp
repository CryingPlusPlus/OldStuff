#include <stdio.h>
#include <iostream>
#include <cmath>

double power(double base, int exponent) {
    double output = 1;

    for(int i = 0; i < exponent; i++) {
        output *= base;
    }
    return output;
}

int main() {
    // std::cout << "Hello World!" << std::endl;
    // std::cout << pow(2, 10) << std::endl;

    // double base, exponent;
    // std::cout << "Base: ";
    // std::cin >> base;
    // std::cout << std::endl << "Exponent: ";
    // std::cin >> exponent;

    // std::cout << std::endl << "Erg: " << power(base, exponent) << std::endl;

    char x = 'A';
    short a;
    int b;
    long c;
    long long d;
    unsigned short aa;
    unsigned int bb;
    unsigned long cc;
    unsigned long long dd;
    
    return 0;
}