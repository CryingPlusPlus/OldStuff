#include <iostream>
#include <string>

int main()
{
    std::string greeting {"Hello std::string!"};
    std::cout << greeting << std::endl;

    std::cout << "Enter a line of text: " << std::endl;
    std::string first_line;
    std::getline(std::cin, first_line);

    std::cout << "Enter another" << std::endl;
    std::string another_line;
    std::getline(std::cin, another_line);

    std::string cat_string = first_line + " " + another_line;
    std::cout << "catted string = " \
        << cat_string \
        << " and this is its length: " \
        << cat_string.length() \
        << std::endl;

    return 0;
}
