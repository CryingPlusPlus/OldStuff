#include <iostream>
#include <string>

class Human
{
    private:
        int age;
        std::string name;

    public:
        Human(const int con_Age = 18, const std::string con_Name = "Ben")
            : age(con_Age), name(con_Name)
        {
            std::cout << "Hello i'm " << name << " and I'm " << age << " Jahre alt." << std::endl;
        } // Ich brauche die geschwungenen Dinger 

        Human(const Human& source)
            : age(source.age), name(source.name)
        {
            std::cout << "Hello i'm " << name << " and I'm " << age << " Jahre alt." << std::endl;
        }

        ~Human()
        {
            std::cout << name << " wurde kaputt gemacht" << std::endl;
        }
};

Human copy_Human(const Human& src)
{
    return Human{src};
}

int main()
{
    Human ape{3, "Ape"};
    {
        Human ben;
        Human Papa{48, "Jan"};
    } //wenn Sache aus Scope geht geht Sache kaputt

    std::cout << "Hello World!" << std::endl;
    auto ape2 = copy_Human(ape);

    return 0;
}
