#include <iostream>
#include <vector>
#include <unordered_set>
#include <cmath>

int calc(const std::vector<int> &vec)
{
    bool inf = true;
    int smol;
    std::unordered_set<int> mem;

    for(const auto el : vec)
    {
        mem.insert(el);
        if(smol == el)
            inf = true;
        if(mem.find(el + 1) == mem.end() and (inf or el + 1 < smol))
        {
            inf = false;
            smol = el + 1;
        }
    }
    return smol;
}

int main()
{
    std::vector<int> input{-2, 1, 2, 3, 4, 6, 7, 8};
    std::cout << calc(input) << std::endl;
    return 0;
}
