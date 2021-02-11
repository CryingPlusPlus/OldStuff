#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <bits/stdc++.h>
#include <math.h>

using namespace std;

template< typename T >
bool element_in_vector( const vector<T>& vec, const unsigned char& el )
{
    int low = 0, high = vec.size(), mid;

    while ( true )
    {
        if ( low == high )
            break;
        
        mid = ( low + high ) / 2;

        if ( el > vec[mid] )
            low = mid + 1;
        else
            high = mid;
        
    }
    
    if ( el == vec[low] )
        return true;
    else
        return false;
}

vector<unsigned char> reader()
{
    vector<unsigned char> end;
    fstream fh;

    fh.open("data.txt", ios::in);
    
    if ( fh.is_open() )
    {
        string temp;
        while ( getline(fh, temp) )
        {
            end.push_back( stoi(temp) );
        }
    }

    fh.close();
    end.push_back(0);
    sort( end.begin(), end.end() );
    end.push_back( end[ end.size() - 1 ] + 3 );
    return end;
}

bool all_the_same( const vector<int> vec, int same )
{
    bool result = true;
    for (const auto el : vec )
    {
        if ( el != same )
        {
            result = false;
            break;
        }
    }
    return result;
}

int num_of_arrangements(const vector<unsigned char>& vec, vector<unsigned char>& temp, unsigned char& ziel, unsigned char length)
{
    vector<unsigned char> end;
    bool change = false;
    
    for ( const auto& el : temp )
    {
        if ( el == ziel )
        {
            length++;
        }
        else
        {
            for ( unsigned char i = 1; i < 4; i++ )
            {
                if (element_in_vector( vec, el + i))
                    end.push_back( el + i );
                    change = true;
            }
        }
        
    }

    if ( !change )
        return length;
    else
        temp = end;
        return num_of_arrangements(vec, temp, ziel, length);
    
}

int main(int argc, char const *argv[])
{
    auto jolts = reader();
    vector<unsigned char> temp{0};
    cout << num_of_arrangements( jolts, temp, jolts[ jolts.size() - 1 ], 0) << endl;
}
