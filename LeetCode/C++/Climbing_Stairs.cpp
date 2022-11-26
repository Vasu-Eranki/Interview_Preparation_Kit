class Solution {
public:
    int climbStairs(int n) {
    int val1=1;
    int val2=1;
    if (n==1)
    {
        return 1;
    }
    else
    {   
        int temp;
        for(int i=2;i<n+1;i++)
        {
            temp = val1+val2;
            val1=val2;  
            val2 = temp;
        }
        return temp;
    }
    }
};
