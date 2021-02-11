#include <iostream>

int main()
{
    int ints[] = {0, 1, 2, 3, 4, 5};

    int panel[3][3] = {0, 1, 2, 3, 4, 5, 6, 7, 8};

    for ( auto i = 0; i < 3; i++ )
    {
        for (auto j = 0; j < 3; j++ )
            std::cout << "panel[" << i << "][" << j << "]" << " = " << panel[i][j] << std::endl;
    }

    return 0;
}
