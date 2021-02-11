#include <iostream>
#include <unordered_map>
#include <vector>

std::vector<int> Two_Sum (const std::vector<int> &vec, const int target)
{
    std::unordered_map<int, int> umap;
    int temp = 0;

    for ( int i = 0; i < vec.size(); ++i )
    {
        temp = target - vec[i];

        if ( umap.find(temp) != umap.end())
            return std::vector<int>{umap[temp], i};

        umap[vec[i]] = i;
    }
    return std::vector<int>{};
}

int main()
{
    return 0;
}
