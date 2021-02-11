#include <iostream>
#include <array>

template<typename T, size_t X, size_t Y>
void print(const std::array<std::array<T, X>, Y> &arr)
{
    for(auto row : arr)
    {
        for(auto el : row)
            std::cout << el << " ";
        std::cout << std::endl;
    }
}

template<typename T, size_t M, size_t N, size_t P>
std::array<std::array<T, P>, M> dot_product(
        const std::array<std::array<T, N>, M> &a,
        const std::array<std::array<T, P>, N> &b
        )
{
    std::array<std::array<T, P>, M> end;
    T temp = 0;
    for(int m = 0; m < M; ++m)
    {
        for(int p = 0; p < P; ++p)
        {
            for(int n = 0; n < N; ++n)
            {
                temp += a[m][n] * b[n][p];
            }
            end[m][p] = temp;
            temp = 0;
        }
    }
    return end;
}

int main()
{
    std::array<std::array<int, 3>, 2> a{
        3, 4, 2,
        3, 4, 2
    };
    std::array<std::array<int, 4>, 3> b{
        13, 9, 7, 15,
        8, 7, 4, 6,
        6, 4, 0, 3,
    };
    auto end = dot_product(a, b);
    print(end);
    return 0;
}
