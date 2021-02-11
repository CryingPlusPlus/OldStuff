#include <iostream>
#include <vector>

int get_highest_jump(const std::vector<int> &moves, int index)
{
    int temp, highest = 0, highest_index;
    for(int i = 0; i <= moves[index]; ++i)
    {
        if(index + i >= moves.size() - 1)
            return index + i;
        temp = index + i + moves[index + i];
        if(temp > highest)
        {
            highest = temp;
            highest_index = index + i;
        }
    }
    return highest_index;
}

int jump(const std::vector<int> &moves, int index, int njumps)
{
    if(index >= moves.size() - 1)
        return njumps;
    return jump(moves, get_highest_jump(moves, index), njumps + 1);
}

int main()
{
    std::vector<int> moves{2, 3, 0, 1, 4};
    std::cout << jump(moves, 0, 0) << std::endl;
    return 0;
}
