class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
    vector<int> indexes={-1,-1};
    binary_search(indexes,nums,target);
    return indexes;
    }
    void binary_search(vector<int> &indexes,vector<int> &nums,int target)
    {
    int low = 0; 
    int high = nums.size()-1;
    while(low<=high)
    {   
        int midpoint =low+(high-low)/2;
        if(nums[midpoint]==target)
        {
            int low_point = midpoint;
            int high_point = midpoint;
            while(low_point>=0 && nums[low_point]==target)
            {    
                low_point-=1;
            }
            while(high_point<nums.size()&& nums[high_point]==target)
                {
                    high_point+=1;
                }
            
            indexes[0]=low_point+1;
            indexes[1]=high_point-1;
            return;
        }
        else if(nums[midpoint]>target)
        {
            
            high = midpoint-1;
        }
        else
        {
            low = midpoint+1;
        }   
   }
   return;
   }
};
