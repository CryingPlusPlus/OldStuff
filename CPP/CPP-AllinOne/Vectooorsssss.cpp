#include <stdio.h>
#include <array>
#include <iostream>
#include <vector>


void print_vector(std::vector<int> &vec) {
    for(int el : vec) {
        std::cout << el << " ";
    }
}

void change_vector(std::vector<int> &vec, int x) {
    for(int el : vec){
        el = x;
    }
}

int main() {
    std::vector<int> vektor = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    print_vector(vektor);
    change_vector(vektor, 3);
    std::cout << std::endl;
    print_vector(vektor);

    return 0;
}
