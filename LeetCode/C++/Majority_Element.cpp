class Solution {
public:
    int majorityElement(vector<int>& nums) {
    unordered_map<int,int> number_count; 
    int temp;
    int max_element;
    int max_count =0;
    for(int i=0;i<nums.size();i++)
    {
        if(number_count.count(nums[i]))
        {
            temp = number_count[nums[i]];
            number_count[nums[i]]= temp+1;
            
        }
        else
        {   
            number_count[nums[i]]=1;
            temp = 0;
        }
        if((temp+1)>max_count){
            max_count = temp+1;
            max_element = nums[i];
        }
    }
    return max_element;    
    }
};
