#include <iostream>
#include <vector>

class Smart_Iterator
{
    private:
        std::vector<int>::const_iterator p_val, p_end;
    public:
        Smart_Iterator(const std::vector<int> &vec)
        {
            p_val = vec.begin();
            p_end = vec.end();
        }

        ~Smart_Iterator(){}

        int operator *()
        {
            return *p_val;
        }

        void operator ++()
        {
            ++p_val;
        }

        bool valid()
        {
            return p_val < p_end;
        }

};

void append_speicher(int &speicher, Smart_Iterator &p_val)
{
    speicher += *p_val;
    ++p_val;
}

float calc_from_both(Smart_Iterator &p_one, Smart_Iterator &p_two, const bool gerade)
{
    if(gerade)
    {
        int speicher = 0;
        append_speicher(speicher, (*p_one < *p_two) ? p_one : p_two);

        if(p_one.valid() && p_two.valid())
            append_speicher(speicher, (*p_one < *p_two) ? p_one : p_two);
        else if(p_one.valid())
            append_speicher(speicher, p_one);
        else
            append_speicher(speicher, p_two);

        return speicher / 2.0;
    }
    else
        return (*p_one < *p_two) ? *p_one : *p_two;
}

float calc_from_one(Smart_Iterator &p_two, const bool gerade)
{
    int speicher = *p_two;
    if(gerade)
        return speicher;
    else
    {
        ++p_two;
        return (speicher + *p_two) / 2.0;
    }
}


float calc_Median(Smart_Iterator &p_one, Smart_Iterator &p_two, const bool gerade)
{
    if(p_one.valid() && p_two.valid())
        return calc_from_both(p_one, p_two, gerade);
    else if(p_one.valid())
        return calc_from_one(p_one, gerade);
    else
        return calc_from_one(p_two, gerade);
}

float Median(const std::vector<int> &one, const std::vector<int> &two)
{
    int stop = ((one.size() + two.size()) / 2 + (one.size() + two.size()) % 2) - 2;
    bool gerade = stop % 2 == 0;
    Smart_Iterator p_one{one}, p_two{two};

    for(; stop >= 0; --stop)
    {
        if(p_one.valid() && p_two.valid())
            (*p_one < *p_two) ? ++p_one : ++p_two;
        else if(p_one.valid())
            ++p_one;
        else
            ++p_two;
    }
    return calc_Median(p_one, p_two, gerade);
}

int main()
{
    std::vector<int> one{1, 2};
    std::vector<int> two{3, 4};
    std::cout << Median(one, two) << std::endl;
    return 0;
}
