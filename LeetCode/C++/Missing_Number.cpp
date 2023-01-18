class Solution {
public:
    int missingNumber(vector<int>& nums) {
        priority_queue<int> max_heap; 
        int length = nums.size();
        for(int i=0;i<length;i++)
        {
            max_heap.push(nums[i]);    
        }
        for(int i=0;i<length;i++)
        {
            if(max_heap.top()==length-i)
            {
                max_heap.pop();
            }
            else
            {
                return length-i;
            }
        }
        return 0;
}};
