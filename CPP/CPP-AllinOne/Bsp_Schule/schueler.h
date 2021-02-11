#ifndef SCHUELER_H
#define SCHUELER_H

#include <iostream>
#include "mensch.h"

class Schueler: public Mensch {
    using Mensch::Mensch;
    public:
        void WhoAmI();
};

#endif