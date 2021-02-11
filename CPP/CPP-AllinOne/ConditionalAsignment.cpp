
#include <stdio.h>
#include <iostream>

int main() {
int a = 11;
int guess;

std::cout << "Welche nummer: ";
std::cin >> guess;

int point = guess == a ? 10 : 0;

std::cout << point << std::endl;

guess == a ? std::cout << "Nice!" << std::endl : std::cout << "Not noice!" << std::endl;

return 0;
}