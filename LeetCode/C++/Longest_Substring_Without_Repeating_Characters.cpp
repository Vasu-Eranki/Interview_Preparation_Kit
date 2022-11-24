class Solution {
public:
    int lengthOfLongestSubstring(string s) {
       int lookahead_index = 0; 
       int string_length = s.size();
       int max_length = 0;
       for(int i=0;i<string_length;i++)
       {
            int temp_length = 0;
            unordered_map<char,int> dictionary; 
            dictionary[s[i]]=1;
            temp_length +=1;     
            for(lookahead_index=i+1;lookahead_index<string_length;lookahead_index++)
            {
                if(!dictionary.count(s[lookahead_index]))
                {
                    dictionary[s[lookahead_index]]=1;
                    temp_length+=1; 
                }
                else
                {
                    break;
                }
            }
            max_length = max(max_length,temp_length);
        }
        return max_length;
    }
};
