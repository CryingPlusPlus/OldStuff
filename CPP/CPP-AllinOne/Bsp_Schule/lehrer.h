#ifndef LEHRER_H
#define LEHRER_H

#include "mensch.h"
#include <iostream>

class Lehrer: public Mensch {
    using Mensch::Mensch;
    public:
        void WhoAmI();
};

#endif