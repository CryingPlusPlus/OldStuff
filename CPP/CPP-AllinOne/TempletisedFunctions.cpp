#include <iostream>
#include <string>
#include <stdio.h>

template<typename T>
void swap(T &a, T &b) {
    T temp = a;
    a = b;
    b = temp;
}

template<typename T>
void print(T &a, T &b) {
    std::cout << a << " " << b << std::endl;
}

int main() {
    std::string as, bs;
    as = "Hello";
    bs = "World";

    int a, b;
    a = 8;
    b = 16;
    print(a, b);
    swap(a, b);
    print(a, b);
    print(as, bs);
    swap(as, bs);
    print(as, bs);

}