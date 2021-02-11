#include <iostream>
#include <string>

int main()
{
    int input_number;
    std::string name;

    std::cout << "Number: ";
    std::cin >> input_number;

    std::cout << "Your Name: ";
    std::cin >> name;

    std::cout << "Your Name is ";
    std::cout << name;
    std::cout << " and you like the number ";
    std::cout << input_number; 
    std::cout << " very much!" << std::endl;

    return 0;
}
