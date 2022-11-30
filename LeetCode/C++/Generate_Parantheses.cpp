class Solution {
public:
    vector<string> generateParenthesis(int n) {
    vector<string> answer;
    recursive_solution(n,0,0,"",answer);
    return answer;  
    }
    void recursive_solution(int n,int left, int right,string s,vector<string> &results)
    {
        if(s.size()==2*n)
        {
            results.push_back(s);
        }
        if(left<n)
        {
            recursive_solution(n,left+1,right,s+"(",results);
        }
        if(right<left)
        {
            recursive_solution(n,left,right+1,s+")",results);
        }
    }
};
