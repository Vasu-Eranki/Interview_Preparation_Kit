class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> max; 
        deque<int> k_window;
        for(int i=0;i<nums.size();i++)
        {
            while(!k_window.empty()&& nums[i]>nums[k_window.back()])
            {
                k_window.pop_back();
            }
            k_window.push_back(i);
            if(i>=k-1)
            {
                if(k_window.front()<=i-k)
                {
                    k_window.pop_front();
                }            
                max.push_back(nums[k_window.front()]);
            }

        }
        return max; 
    }
};
