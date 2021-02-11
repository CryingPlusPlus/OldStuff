#include <stdio.h>
#include <iostream>
#include <cmath>
#include <limits>


void print_array(int array[]) {

}

int main() {
    int guesses[] = {13,20,50,40,65};
    int size = sizeof(guesses) / sizeof(guesses[0]);

    for(int i = 0; i < size; i++){
        std::cout << guesses[i] << std::endl;
    }


    int arr[10];

    std::cout << "Array füllen!" << std::endl;
    for(int i = 0; i < 10; i++) {
        if(!(std::cin >> arr[i])){
            break;
        }
    } 
    std::cin.clear();
    std::cin.ignore((int) INFINITY, '\n');
    std::string test;
    std::cin >> test;
    std::cout << test << " Das hier ist der Test!" << std::endl;
    return 0;
}