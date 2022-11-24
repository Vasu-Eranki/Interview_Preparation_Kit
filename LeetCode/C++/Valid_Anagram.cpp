class Solution {
public:
    bool isAnagram(string s, string t) {
    unordered_map<char,int> counter;
    int dummy_sum = 0;
    if(s.size()!=t.size())
    {
        return false;
    }
    for(int i =0;i<s.size();i++)
    {
        hash_modifier(counter,s[i],1);
        hash_modifier(counter,t[i],-1);
    }
    for(int i=0;i<s.size();i++)
    {
        if(counter[s[i]]!=0)
        {
            return false;
        }
    }
    return true;
    }
    void hash_modifier(unordered_map<char,int> &temp,char character,int sign)
{
    int dummy_value;
    if(temp.count(character))
    {   
        dummy_value = temp[character];
        temp[character] = dummy_value+sign;
    }
    else
    {
        temp[character]=sign;
    }
}
};

