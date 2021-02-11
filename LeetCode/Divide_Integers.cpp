#include <iostream>

int divide(const int dividend, const int divisor, int current, int index)
{
    if(dividend - 1> current)
        return divide(dividend, divisor, current + divisor, ++index);
    return index;
}

int main()
{
    std::cout << divide(8, 2, 0, 0) << std::endl;
    return 0;
}
