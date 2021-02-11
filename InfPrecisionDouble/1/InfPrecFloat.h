#ifndef INFPRECFLOAT_H
#define INFPRECFLOAT_H

#include <string>
#include <iostream>
#include <math.h>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

class InfPrecFloat
{
private:
    vector<int> vor_komma{0};
    vector<int> nach_komma{0};
public:
    InfPrecFloat(string);
    ~InfPrecFloat();

    friend ostream& operator<<(ostream&, InfPrecFloat&);
    void add(string);
    void add_nach_komma(string);
    void add_vor_komma(string);
};

#endif