class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low=0;
        int mid = 0; 
        int high = nums.size()-1;
        for(int i =0;i<nums.size();i++)
        {
            if(nums[mid]==2)
            {
                swap(nums[mid],nums[high]);
                high--;
            }
            else if (nums[mid]==1)
            {
                mid++;
            }
            else
            {
                swap(nums[low],nums[mid]);
                low++;
                mid++;
            }
        }
    }
};
