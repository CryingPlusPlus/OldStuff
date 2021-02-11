#include <iostream>
#include <array>
#include <string>
#include <vector>
#include <math.h>
#include <bits/stdc++.h>

using namespace std;

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


class InfPrecDouble
{
private:
    vector<int> vor_komma{0};
    vector<int> nach_komma;
    int vorzeichen = 1;
public:
    template<typename T>
    InfPrecDouble(T x) 
    {
        this->add(x);
    }

    template<typename T>
    void add(T x)
    {
        string temp = to_string(x);
        vector<string> vor_nach_komma;
        add_nachkomma(vor_nach_komma[1]);
        add_vor_komma(vor_nach_komma[0]);
    }
    void add_nachkomma(string x)
    {
        if ( x.length() > nach_komma.size() )
        {
            for ( int i = nach_komma.size(); i < x.length(); i++ )
            {
                this->nach_komma.push_back(0);
            }
        }
        for ( int i = x.length(); i < nach_komma.size(); i++ )
        {
            x += "0";
        }

        int sinn = 0;
        int temp;
        for ( int i = x.length(); i > 0; i-- )
        {
            temp = (int) x[i] + nach_komma[i] + sinn; 
            sinn = floor(temp/10); 
            nach_komma[i] = temp % 10;
        }
        temp = (int) x[0] + nach_komma[0] + sinn;
        sinn = floor(temp/10);
        nach_komma[0] = temp % 10;
        this->add_vor_komma(to_string(sinn)); 
    }
    void add_vor_komma(string x)
    {
        reverse(x.begin(), x.end());
        if ( x.length() > vor_komma.size() )
        {
            for ( int i = vor_komma.size(); i < x.length(); i++ )
            {
                vor_komma.push_back(0);
            }
        }
        for ( int i = x.length(); i < nach_komma.size(); i++ )
        {
            x+= "0";
        }
        int sinn = 0;
        int temp;

        for ( int i = 0; i < x.length(); i++ )
        {
            temp = (int) x[i] + vor_komma[i] + sinn;
            sinn = floor(temp/10);
            vor_komma[i] = temp % 10;
        }
        if ( sinn > 0 )
            vor_komma.push_back(sinn);
    }
    ~InfPrecDouble() {}
    friend ostream& operator << (ostream& output, InfPrecDouble& x);
};

ostream& operator << (ostream& output, InfPrecDouble& x)
{
    for ( auto i : x.vor_komma)
    {
        output << i;
    }
    output << ".";
    for ( auto i : x.nach_komma)
    {
        output << i;
    }
    return output;
}


int main()
{
    InfPrecDouble MyVar(3257.50125);
    cout << MyVar << endl;
    cout << "Hello" << endl;
    return 0;
}

