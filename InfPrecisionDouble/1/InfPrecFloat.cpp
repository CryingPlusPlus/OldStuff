#include "InfPrecFloat.h"

vector<string> split(string str, char c)
{
    vector<string> end;
    string temp = "";

    for ( auto&& i : str)
    {
        if ( i != c )
            temp += i;
        else
        {
            end.push_back(temp);
            temp = "";
        }
        
    }
    end.push_back(temp);

    return end;
}

InfPrecFloat::InfPrecFloat(string str)
{
    this->add(str);
}

void InfPrecFloat::add(string x)
{
    vector<string> temp = split(x, '.'); 
    this->add_vor_komma(temp[0]);
    this->add_nach_komma(temp[1]);
    
}

void InfPrecFloat::add_nach_komma(string x)
{
    cout << "1\n";
    for ( int i = 0; i < x.length() - nach_komma.size(); i++ )
    {
        nach_komma.push_back(0);
    }
    cout << "2\n";
    cout << nach_komma.size() << " " << x.length() << endl;
    for ( int i = 0; i < nach_komma.size() - x.length(); i++ )
    {
        x += "0";
    }
    cout << "3\n";
    int temp;
    int sinn = 0;
    for ( int i = x.length() - 1; i >= 0; i-- )
    {
        cout << i << endl;
        temp = (int) x[i] + nach_komma[i] + sinn;
        sinn = floor(temp/10);
        nach_komma[i] = temp % 10;
    }

    this->add_vor_komma(to_string(sinn));
}

void InfPrecFloat::add_vor_komma(string x)
{
    cout << "Adde Vorkomma " << x << endl;
}

InfPrecFloat::~InfPrecFloat(){}

std::ostream& operator << (std::ostream &output, InfPrecFloat &m){
    for ( int i = m.vor_komma.size() - 1; i >= 0; i-- )
        output << m.vor_komma[i];
    output << ".";
    for ( auto i : m.nach_komma )
        output << i;
    return output;
}