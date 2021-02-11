#include <iostream>
#include <vector>
#include "mensch.h"
#include "schueler.h"
#include <array>
#include "lehrer.h"

int main(){
    Mensch Hans("Hans Meier", 48);
    std::cout << Hans << std::endl;
    Hans.geburtstag();
    Hans.WhoAmI();
    std::cout << Hans << std::endl;


    Lehrer Hagmann("Stefan Hagmann", 34);
    std::cout << Hagmann << std::endl;
    Hagmann.WhoAmI();

    Schueler Ben("Ben Wernicke", 17);
    std::cout << Ben << std::endl;
    Ben.WhoAmI();

    Mensch &BW = Ben;
    Mensch &SH = Hagmann;
    Mensch &HM = Hans;

    Mensch Personen[] = {BW, SH, HM};
    for(auto p : Personen){
        std::cout << p << std::endl;
        p.WhoAmI();
    }


    return 0;

}