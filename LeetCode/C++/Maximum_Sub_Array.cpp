class Solution {
public:
    int maxSubArray(vector<int>& nums) {
    int max_final_array = INT_MIN;
    int total_sum = 0;
    for(int i=0;i<nums.size();i++)
    {
        total_sum+=nums[i];
        max_final_array = (max_final_array<total_sum)?total_sum:max_final_array;
        total_sum = (total_sum<0)?0:total_sum;
    }
    return max_final_array;
}};
