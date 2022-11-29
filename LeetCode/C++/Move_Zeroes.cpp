class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zero_indices =0;
        int next_counter = 0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]!=0)
            {
                nums[next_counter]= nums[i];
                next_counter+=1;
            }
            else
            {
                zero_indices++;
            }
        }
        for(int i=nums.size()-1;zero_indices!=0;i--)
        {
            zero_indices-=1;
            nums[i]=0;
        }
    }
};
