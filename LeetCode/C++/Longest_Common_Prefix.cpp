class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix;
        bool flag = 1;
        int length = find_smallest_length(strs);
        for(int i=0;i<length;i++)
        {
            for(int j=1;j<strs.size();j++)
            {
                if(strs[j][i]!=strs[j-1][i])
                {
                    flag = 0;
                    break;
                }
            }
            if(flag==false)
            {
                break;
            }
            prefix = (isalpha(strs[0][i]))?(prefix+strs[0][i]):prefix;
        }
        return prefix; 
    }
    int find_smallest_length(vector<string> &strs)
    {
        int length = strs[0].size();
        for(int i=1;i<strs.size();i++)
            length = (strs[i].size()<length)?strs[i].size():length;
        return length;
    }
};
