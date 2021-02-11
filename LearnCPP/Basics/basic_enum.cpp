#include <iostream>

int main()
{
    enum himmels_richtungen {
        Norden = 100, //int value beginnt hier zu zählen -> rauf 
        Osten,
        Westen,
        Sueden
    };

    std::cout << "Norden: " << Norden << std::endl;
    std::cout << "Osten: " << Osten << std::endl;
    std::cout << "Sueden: " << Sueden << std::endl;
    std::cout << "Westen: " << Westen<< std::endl;

    himmels_richtungen windrichtung = Sueden;
    std::cout << "Windrichtung: " << windrichtung << std::endl;

    return 0;
}
