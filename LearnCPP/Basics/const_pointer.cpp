#include <iostream>

int main()
{
    int integer = 13, int2 = 16;
    const int* Int_Pointer = &integer; // macht einen read only pointer

    std::cout << Int_Pointer << " " << *Int_Pointer << std::endl;
    Int_Pointer = &int2;
    std::cout << Int_Pointer << " " << *Int_Pointer << std::endl;
    //*Int_Pointer = 25; Illegal - read only pointer !!!
    std::cout << Int_Pointer << " " << *Int_Pointer << std::endl;
    return 0;
}
