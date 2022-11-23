#include <map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indices;
        map<int,int> has_sum;
        int desired_value; 
        for(int i =0;i<=nums.size();i++)
        {
            desired_value = target-nums[i];
            if(has_sum.count(desired_value))
            {
                indices.push_back(i);
                indices.push_back(has_sum[desired_value]);
                return indices;
            }
            else
            {
                has_sum[nums[i]]=i;
            }
        }
    return indices;
    }
};
