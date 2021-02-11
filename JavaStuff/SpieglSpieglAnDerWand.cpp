#include <iostream>
#include <string>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    string str;

    // while ( str != "tiuq" )
    // {
    //     getline(cin, str);
        
    //     if ( str == "" )
    //         str = "Spieglein Spieglein an der Wand";
        
    //     reverse(str.begin(), str.end());
    //     cout << str << endl;
    // }
    while ( true )
    {
        getline(cin, str);

        if ( str == "quit" )
            break;
        if ( str == "" )
            str = "Spieglein Spieglein an der Wand";
        
        reverse(str.begin(), str.end());
        cout << str << endl;
    }
}