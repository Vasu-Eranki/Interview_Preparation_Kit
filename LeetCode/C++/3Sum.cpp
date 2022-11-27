class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> answers; 
        sort(nums.begin(),nums.end());
        if((nums[0]>0)||(nums.size()<3))
        {
            return answers;
        }
        else
        {
            for(int i=0;i<nums.size();i++)
            {
                if(nums[i]>0)
                {
                    break;
                }
                else if((i>0) && (nums[i]==nums[i-1]))
                {
                    continue;
                }
                else
                {
                    int high_pointer = nums.size()-1;
                    map<vector<int>,int> dictionary; 
                    
                    int low_pointer = i+1;
                    int total_sum; 
                    while(low_pointer<high_pointer)
                    {
                        total_sum = nums[i]+nums[low_pointer]+nums[high_pointer];
                        if(total_sum==0)
                        {
                            vector<int> scratchpad; 
                            scratchpad.push_back(nums[i]);
                            scratchpad.push_back(nums[low_pointer]);
                            scratchpad.push_back(nums[high_pointer]);
                            if(!dictionary.count(scratchpad))
                            {
                                dictionary[scratchpad]=0;
                                answers.push_back(scratchpad);
                            }
                            low_pointer+=1;
                            high_pointer-=1;; 
                        }
                        else if(total_sum>0)
                        {
                            high_pointer-=1;;
                        }
                        else
                        {
                            low_pointer+=1;
                        }
                    }

                }
            }

        }
        return answers;
    }
};
