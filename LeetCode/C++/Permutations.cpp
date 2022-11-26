class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> answer;
    recursive_solution(nums,answer,0); 
    return answer; 
    }
    void recursive_solution(vector<int> &nums,vector<vector<int>> &tracker,int indices)
    {
        if(indices==nums.size()-1)
        {
            tracker.push_back(nums);
        }
        else{
        for(int i=indices;i<nums.size();i++)
        {
            vector<int> safecopy = nums;
            swap(safecopy[indices],safecopy[i]);
            recursive_solution(safecopy,tracker,indices+1);
        }
        }
    };
};
