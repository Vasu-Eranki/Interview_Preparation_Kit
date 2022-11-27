class Solution {
public:
    bool isPalindrome(string s) {
    string corrected_s = char_stripper(s);
    bool answer = palindrome_checker(corrected_s);
    return answer;
    }
    string char_stripper(string s)
    {
        string strippeds;
        for(int i=0;i<s.size();i++)
        {
            if((isalpha(s[i]))||(isdigit(s[i])))
            {
                 if(isupper(s[i]))
                {
                    strippeds+= tolower(s[i]);
                }
                else
                {
                    strippeds+=s[i];
                }
            }
        }
        return strippeds;
    }
    bool palindrome_checker(string s)
    {
        for(int i=0;i<ceil(s.size()/2);i++)
        {
            if(s[i]!=s[s.size()-1-i])
            {
                return false;
            }
        }
        return true; 
    }
};
