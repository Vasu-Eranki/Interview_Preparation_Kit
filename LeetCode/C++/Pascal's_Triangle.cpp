class Solution {
public:
    vector<vector<int>> generate(int numRows) {
    vector<vector<int>> answer;
    vector<int> scratchpad;
    scratchpad.push_back(1);
    answer.push_back(scratchpad);
    for(int i=1;i<=numRows-1;i++)
    {
        vector<int> scratchpad;
        for(int j=0;j<=i;j++)
        {   
            int factor,factor1;
            factor = (j-1<0)?0:answer[i-1][j-1];
            factor1 = (j>i-1)?0:answer[i-1][j];
            scratchpad.push_back(factor+factor1);
        }
        answer.push_back(scratchpad);
    }
    return answer;
    }
};
