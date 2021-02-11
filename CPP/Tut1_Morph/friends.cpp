#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

class Tier {
    public:
        void wieMachtDasTier(){
            cout << "Guten Tag" << "\n";
        }
        virtual void lead(){
            cout << "Ich bib ein Tier" << endl;
        }
};

class Blindenfuehrer {
    public:
    virtual void lead(){
        cout << "follow me!" << endl;
    }
};

class Hund: public Tier, public Blindenfuehrer{
    private:
        string name;
    
    public:
        Hund(string name) {
            this -> name = name;
        }

        string getName(){
            return this -> name;
        }
        friend void adopt(Hund &H);

        void lead(){
            cout << "WUUUUFFF" << endl;
        }
};

void adopt(Hund &H){
    H.name = "Ceasar";
}

int main() {
    Hund Boo("Boo");
    cout << Boo.getName() << "\n";
    adopt(Boo);
    cout << Boo.getName() << "\n";

    Boo.wieMachtDasTier();
    Boo.lead();

    return 0;