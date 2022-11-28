class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int index = modified_binary_search(nums,0);
        return index; 
    }
    int modified_binary_search(vector<int>&nums,int historical_midpoint)
    {
        int midpoint = ceil(nums.size()/2);

        int index;
        if(nums.size()==1)
        {
            index= 0;
        }
        else if(nums.size()<3)
        {
            if(nums[0]>nums[1])
            {
                index = 0+historical_midpoint;
            }
            else
            {
                index= 1+historical_midpoint;
            }
        }
        else
        {
            int left = nums[midpoint-1];
            int center = nums[midpoint];
            int right = nums[midpoint+1];
            if((left<center)&& (center>right))
            {
                index = historical_midpoint+midpoint;
                
            }
            else if(center<left)
            {
                vector<int> temp(nums.begin(),nums.begin()+midpoint);
                index= modified_binary_search(temp,historical_midpoint);
            }
            else
            {
                vector<int> temp(nums.begin()+midpoint,nums.end());
                index = modified_binary_search(temp,midpoint+historical_midpoint);
            }
        }
        return index;
    }
};
