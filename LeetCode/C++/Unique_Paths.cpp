class Solution {
public:
    int uniquePaths(int m, int n) {
    if(m==1||n==1)
    {
        return 1;
    }
    vector<vector<int>> answer(m,vector<int>(n,0));
    for(int i=1;i<m;i++)
        {answer[i][0] = 1;}
    for(int i=1;i<n;i++)
        {answer[0][i] = 1;}
    for(int i=1;i<m;i++)
       { for(int j=1;j<n;j++)
        {    answer[i][j] = answer[i-1][j]+answer[i][j-1];}}
    return answer[m-1][n-1];
    }
};
