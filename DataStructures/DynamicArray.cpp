#include <iostream>

template<class T>
class DynamicArray
{
    private:
        unsigned int capacity = 0;

    public:
        unsigned int length = 0;
        T array[];
        DynamicArray(int size)
        {
            this -> array[size + 1];
            this -> capacity = size + 1;
        }
        ~DynamicArray(){}

        void push(T el)
        {
            if ( this->length >= this->capacity )
            {
                capacity *= 2;
                T newArray[capacity];
                for ( int i = 0; i < length; i++ )
                {
                    newArray[i] = array[i];
                }
                this->array = newArray;
            }
            this -> array[length] = el;
            length++;
        }
    

};

int main()
{
    DynamicArray<int> myDynArray(3);
    myDynArray.push(3);
    myDynArray.push(3);
    myDynArray.push(3);
    myDynArray.push(3);
    myDynArray.push(3);
    for ( int i = 0; i < myDynArray.length; i++ )
    {
        std::cout << myDynArray.array[i] << std::endl;
    }
}