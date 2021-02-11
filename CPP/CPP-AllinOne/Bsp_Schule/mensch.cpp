#include "mensch.h"
#include <iostream>

Mensch::Mensch(std::string name, int alter) {
    this -> name = name;
    this -> alter = alter;
}
void Mensch::WhoAmI(){
    std::cout << "Ich bin ein Mensch" << std::endl;
}
void Mensch::geburtstag(){
    this -> alter++;
    std::cout << "Ich bin ein Jahr aelter geworden!" << std::endl;
}
std::ostream& operator << (std::ostream &output, Mensch &m){
    output << "Meine name ist " << m.name << " und ich bin " << m.alter << " Jahre alt.";
    return output;
}
Mensch::Mensch(){}
