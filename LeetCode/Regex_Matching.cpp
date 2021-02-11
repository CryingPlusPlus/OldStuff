#include <iostream>
#include <vector>
#include <string>

struct Rule
{
    char c;
    bool star;
    Rule(char c, bool star)
    {
        this->c = c;
        this->star = star;
    }
    ~Rule(){}
};

std::vector<Rule> parse_rules(const std::string &rule_string)
{
    std::vector<Rule> end;
    const char *p_char, *p_end;
    p_char = &rule_string[0];
    p_end = &rule_string.back();
    Rule temp_rule{*p_char, false};
    ++p_char;
    while(p_char <= p_end)
    {
        if(*p_char == '*')
        {
            temp_rule.star = true;
            ++p_char;
        }
        end.push_back(temp_rule);
        temp_rule = {*p_char, false};
        ++p_char;
    }
    if(*p_char != '*')
        end.push_back(temp_rule);
    return end;
}

bool is_Match(const std::vector<Rule> &rules, const std::string str)
{
    const Rule *p_rule, *end_rule;
    const char *p_str, *end_str;
    p_rule = &rules[0];
    end_rule = &rules.back();
    p_str = &str[0];
    end_str = &str.back();
    bool valid;

    while(p_rule <= end_rule && p_str <= end_str)
    {
        valid = p_rule->c == *p_str || p_rule->c == '.';
        if(p_rule->star)
        {
            if(valid)
                ++p_str;
            else
                ++p_rule;
        }
        else
        {
            if(!valid)
                return false;
            ++p_str;
            ++p_rule;
        }
    }
    return true;
}

int main()
{
    std::string rule_string = "abc*g.";
    std::vector<std::string> inputs{
        "abccgH",
        "abgH",
        "accawd"
    };
    std::vector<Rule> rules = parse_rules(rule_string);
    std::cout << rule_string << std::endl;

    for(auto str : inputs)
    {
        std::cout << str << std::endl;
        std::cout << is_Match(rules, str) << std::endl;
    }
    return 0;
}
