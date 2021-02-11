#ifndef MENSCH_H
#define MENSCH_H

#include <string>

class Mensch {
    protected:
        int alter;
    public:
        Mensch();
        Mensch(std::string, int);
        std::string name;
        virtual void WhoAmI();
        virtual void geburtstag();
        friend std::ostream& operator << (std::ostream&, Mensch&);

};

#endif
