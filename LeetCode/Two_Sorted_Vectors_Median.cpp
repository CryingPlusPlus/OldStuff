#include <iostream>
#include <vector>

void fillup(std::vector<int> &to_fill, const int *p_vec, const int *end_vec)
{
    while(p_vec <= end_vec)
    {
        to_fill.push_back(*p_vec);
        ++p_vec;
    }
}

std::vector<int> pointer_merge(const std::vector<int> &one, const std::vector<int> &two)
{
    const int *p_one, *p_two, *one_end, *two_end;
    std::vector<int> merged;
    merged.reserve(one.size() + two.size());
    p_one = &one[0];
    p_two = &two[0];
    one_end = &one.back();
    two_end = &two.back();

    while(p_one <= one_end && p_two <= two_end)
    {
        if(*p_one < *p_two)
        {
            merged.push_back(*p_one);
            ++p_one;
        }
        else
        {
            merged.push_back(*p_two);
            ++p_two;
        }
    }
    fillup(merged, p_one, one_end);
    fillup(merged, p_two, two_end);
    return merged;
}

double get_median(const std::vector<int> &one, const std::vector<int> &two)
{
    std::vector<int> merged = pointer_merge(one, two);
    int size = merged.size();
    int half = size / 2;
    if(size % 2 == 0)
    {
        return (merged[half] + merged[half - 1]) / 2.0;
    }
    return merged[half];
}

int main()
{
    std::vector<int> one{1, 2}, two{3, 4};
    std::cout << get_median(one, two) << std::endl;
    return 0;
}
