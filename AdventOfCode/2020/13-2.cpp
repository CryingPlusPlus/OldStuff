#include <iostream>
#include <vector>
#include <array>
#include <math.h>
#include <string>

using namespace std;

vector<array<int, 2>> get_IDs(string str)
{
    vector<string> str_temp;
    string temp = "";

    for (const auto& c : str )
    {
        if (c == ',')
        {
            str_temp.push_back(temp);
            temp = "";
        }
        else
        {
            temp += c;
        }
        
    }
    str_temp.push_back(temp);

    vector<array<int, 2>> end;
    for ( int i = 0; i < str_temp.size(); i++ )
    {
        if ( str_temp[i] != "x" )
        {
            end.push_back(array<int, 2>{i, stoi(str_temp[i])});
        }
    }
    return end;

}

bool valid(int offset, int id, int time)
{
    return (time + offset) % id == 0;
}

bool valid_for_all(vector<array<int, 2>> IDs, int time)
{
    for ( auto& bus : IDs )
    {
        if (!valid(bus[0], bus[1], time))
            return false;
    }
    return true;
}

auto get_max(vector<array<int, 2>> IDs)
{
   array<int, 2> end {0, 500000}; 

   for ( const auto& bus : IDs )
   {
       if ( bus[1] < end[1] )
       {
           end = bus;
       }
   }
   return end;
}

int looper(vector<array<int, 2>> IDs)
{
    auto bus = get_max(IDs);
    int time, index = 1;

    while (true)
    {
        time = index * bus[1] - bus[0];
        if ( valid_for_all(IDs, time) )
            return time;
        index++;
    }
}

int main(int argc, char const *argv[])
{
    cout << "Starting" << endl;
    auto IDs = get_IDs("29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,409,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,13,19,x,x,x,23,x,x,x,x,x,x,x,353,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41");
    cout << looper(IDs) << endl;
}
