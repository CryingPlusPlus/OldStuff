#include <iostream>
#include <bitset>


int main()
{
    unsigned short number = 0, half, quarter, doubled, quad;
    std::bitset<8> bitwise_NOT, bitwise_AND, bitwise_OR, bitwise_XOR;

    std::cout << "Hello Bitwise Stuff" << std::endl;
    std::cout << "Input a Number between 0 - 255: ";
    std::cin >> number;

    bitwise_XOR = (number ^ number);
    bitwise_OR = (number | number);
    bitwise_AND = (number & number);
    bitwise_NOT = (~number);

    std::cout << "XOR: " << bitwise_XOR << std::endl;
    std::cout << "NOT: " << bitwise_NOT << std::endl;
    std::cout << "OR: " << bitwise_OR<< std::endl;
    std::cout << "AND: " << bitwise_AND<< std::endl;

    half = number >> 1;
    quarter = number >> 2;
    doubled = number << 1;
    quad = number << 2;

    std::cout << "Doubled: " << doubled << std::endl;
    std::cout << "Vervierfacht: " << quad << std::endl;
    std::cout << "Half: " << half << std::endl;
    std::cout << "Quarter: " << quarter << std::endl;
    return 0;
}
