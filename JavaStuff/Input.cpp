#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int main()
{
    int zahl;
    do
    {
        cout << "Deine Zahl: " << endl;
        cin >> zahl;
    } 
    while (!(0 < zahl && zahl <= 10));

    cout << "Deine Zahl ist: " << zahl << endl;
}
