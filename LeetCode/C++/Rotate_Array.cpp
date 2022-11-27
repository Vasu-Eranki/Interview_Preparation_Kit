class Solution {
public:
    void rotate(vector<int>& nums, int k) {
    int actual_rotation = k%nums.size();
    right_one_rotation(nums,actual_rotation);
    }
    void right_one_rotation(vector<int> &nums,int k)
    {    
        vector<int> answer;
        answer.resize(nums.size());
        for(int i=0;i<nums.size();i++)
            answer[(i+k)%nums.size()] =nums[i] ;
        nums = answer;
    }
};
