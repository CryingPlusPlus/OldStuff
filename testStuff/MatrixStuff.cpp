#include <iostream>
#include <vector>
#include <array>

std::vector<int> vec_one_liner(const std::vector<int> &a, const std::vector<std::vector<int>> &b)
{
    std::vector<int> end;
    end.reserve(a.size());
    int temp = 0;
    for(int j = 0; j < b[0].size(); ++j)
    {
        for(int i = 0; i < a.size(); ++i)
        {
            temp += a[i] * b[i][j];
        }
        end.push_back(temp);
        temp = 0;
    }
    return end;
}

std::vector<std::vector<int>> vec_full(const std::vector<std::vector<int>> &a, const std::vector<std::vector<int>> &b)
{
    std::vector<std::vector<int>> end;
    end.reserve(a.size());
    for(const auto &arr : a)
        end.push_back(vec_one_liner(arr, b));
    return end;

}

int main()
{
    std::vector<std::vector<int>> a{
        {4},
        {5},
        {6},
    };
    std::vector<std::vector<int>> b{
        {1, 2, 3}
    };
    auto end = vec_full(a, b);

    for(auto row : end)
    {
        for(auto el : row)
        {
            std::cout << el << " ";
        }
        std::cout << std::endl;
    }
    
    return 0;
}
