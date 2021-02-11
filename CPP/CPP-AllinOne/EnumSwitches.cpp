#include <stdio.h>
#include <iostream>

int main() {
    enum season {winter, sommer, fruehling, herbst};
    season now = herbst;

    switch (now) {
        case winter:
            std::cout << "Muetze anziehen" << std::endl;
            break;
        case sommer:
            std::cout << "Bdehose anziehen" << std::endl;
            break;
        case fruehling:
            std::cout << "Blumen anschauen" << std::endl;
            break;
        case herbst:
            std::cout << "Lange Hose anziehen" << std::endl;
            break;
    }

    enum class Season {winter, sommer, fruehling, herbst};
    Season Now = Season::winter;

    switch (Now) {
        case Season::winter:
            std::cout << "Muetze anziehen" << std::endl;
            break;
        case Season::sommer:
            std::cout << "Bdehose anziehen" << std::endl;
            break;
        case Season::fruehling:
            std::cout << "Blumen anschauen" << std::endl;
            break;
        case Season::herbst:
            std::cout << "Lange Hose anziehen" << std::endl;
            break;
    }
    return 0;
}