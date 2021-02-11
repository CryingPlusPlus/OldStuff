#include <stdio.h>
#include <iostream>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

int main() {
    // string str = "Mein Name ist Ben.";
    // cout << str << "\n" << str.length() << "\n";

    // str.insert(0, "Hallo, ");
    // str.erase(0, 2);

    // cout << str << "\n";

    // string::iterator i;

    // for(i = str.begin(); i < str.end(); i++){
    //     cout << *i;

    // }
    string abc = "42";
    istringstream stream(abc);

    int a;
    stream >> a;


    return 0;
}