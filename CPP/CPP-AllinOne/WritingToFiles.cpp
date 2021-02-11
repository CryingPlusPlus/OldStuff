#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> names1 = {"Ben", "Luke", "Nick", "Jana", "Jan"};

    std::ofstream fh ("HelloWorld.txt");
    for(std::string name : names1) {
        fh << name << std::endl;
    }
    fh.close();

    std::vector<std::string> names2;
    std::string word;

    std::ifstream fh1 ("HelloWorld.txt");
    while(fh1 >> word) {
        names2.push_back(word);

    }
    for(std::string el : names2) {
        std::cout << el << std::endl;
    }
    fh.close();

    std::string line;

    std::ifstream fh2 ("HelloWorld.txt");

    getline(fh2, line);
    fh2.close();

    

    return 0;
}