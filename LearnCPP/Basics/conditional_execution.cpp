#include <iostream>

int main()
{
    int one, two, max;
    std::cout << "Ich gebe die größere Zahl zurück :)" << std::endl;
    std::cout << "Enter Nummer 1: ";
    std::cin >> one;
    std::cout << "Enter Nummer 2: ";
    std::cin >> two;

    max = ( one > two ) ? one : two;
    std::cout << std::endl << "This is the greater one: " << max << std::endl;
    return 0;
}
