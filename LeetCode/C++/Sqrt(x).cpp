class Solution {
public:
    int mySqrt(int x) {
     long difference = 0;
     long iterator = 1;
     while(difference>=0)
    {
        difference = x-iterator*iterator;
        iterator = iterator+1;
    }
    return (int)iterator -2; 
    }
};
