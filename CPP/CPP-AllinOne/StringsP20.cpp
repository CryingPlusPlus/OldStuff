#include <stdio.h>
#include <iostream>
#include <string>

int main() {
    // std::string kenobi = "Hello there!";

    // std::cout << kenobi << std::endl;
    // std::cout << kenobi[1] << std::endl;
    // std::cout << kenobi + " General Kenobi!" << std::endl;
    // std::cout << kenobi.length() << std::endl;


    // std::cout << "Was ist dein Satz?" << std::endl;
    // getline(std::cin, kenobi);
    // kenobi.insert(3, "                ");
    // kenobi.erase(0, 2);
    // std::cout << kenobi << std::endl;

    std::string bad_sentence = "What the fuck";
    std::cout << bad_sentence << std::endl;
    bad_sentence.replace(bad_sentence.find("fuck"), 4, "****");
    std::cout << bad_sentence << std::endl;

    return 0;
}