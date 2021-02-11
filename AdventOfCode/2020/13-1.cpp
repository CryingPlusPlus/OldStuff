#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <bits/stdc++.h>

using namespace std;

vector<int> split_bus_IDs(string bus_IDs)
{
    vector<int> raw;
    string temp = "";

    for ( const auto& c : bus_IDs )
    {
        if ( c == ',' )
        {
            if ( temp != "x" )
                raw.push_back( stoi( temp ) );
            temp = "";
        }
        else
        {
           temp += c; 
        }
    }
    if ( temp != "x" )
        raw.push_back( stoi( temp ) );

    return raw;
}

int find_index(int min_time, vector<int> bus_IDs)
{
    int index = 0;
    int temp = 0;
    vector<int> temp_list;
    for ( auto bus : bus_IDs )
    {
        temp = 0;
        while ( temp < min_time)
        {
            temp += bus;
        }
        temp_list.push_back(temp);
    }
    for ( int i = 0; i < temp_list.size(); i++ )
    {
        if ( temp_list[i] < temp_list[index] )
            index = i;
    }
    return index;
}

void handler(int min_time, string raw_bus_IDs)
{
    vector<int> bus_IDs = split_bus_IDs(raw_bus_IDs);
    for ( auto i : bus_IDs )
        cout << i << endl;
    
    int index = find_index(min_time, bus_IDs);
    cout << index;

    int temp = 0;
    while (temp < min_time)
        temp += bus_IDs[index];
    
    cout << endl << endl << "Erg: " << (temp - min_time) * bus_IDs[index];
}

int main(int argc, char const *argv[])
{
    handler(1000511, "29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,409,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,13,19,x,x,x,23,x,x,x,x,x,x,x,353,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41");
}
