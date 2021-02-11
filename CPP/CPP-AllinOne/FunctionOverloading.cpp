#include <iostream>
#include <string>

void swap(std::string &a, std::string &b) {
    auto temp = a;
    a = b;
    b = temp;
}

void swap(int &a, int &b) {
    auto temp = a;
    a = b;
    b = temp;
}

int main() {
    std::string as, bs;
    as = "Hello";
    bs = "World";
    std::cout << as << bs << std::endl;
    swap(as, bs);
    std::cout << as << bs << std::endl;

    int a, b;
    a = 3;
    b = 5;
    std::cout << a << b << std::endl;
    swap(a, b);
    std::cout << a << b << std::endl;
    return 0;
}