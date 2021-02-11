#include <iostream>
#include <stdio.h>
#include <string>

namespace Ben {
    void print(std::string msg) {
        std::cout << msg << std::endl;
    }
}

int main() {
    Ben::print("Hello World");
    return 0;
}