class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums,0,nums.size()-1);
        return nums;
    }
    void mergeSort(vector<int> &nums,int left,int right)
    {
        if(left>=right)
        {
            return;
        }
        else
        {
            int midpoint = left+(right-left)/2;
            mergeSort(nums,left,midpoint);
            mergeSort(nums,midpoint+1,right);
            merge(nums,left,midpoint,right);
            return; 
        }
    }
    void merge(vector<int> &nums,int left, int midpoint, int right)
    {
        if(left>=right)
        {
            return;
        }
        int pointer1 = midpoint-left+1;
        int pointer2 = right-midpoint;
        int indices_tracker = left;
        vector<int> left_array; 
        vector<int> right_array; 
        for(int i=0;i<pointer1;i++)
            {left_array.push_back(nums[i+left]);
            ;}
        for(int i=0;i<pointer2;i++)
            {right_array.push_back(nums[i+midpoint+1]);
            ;}
        int i =0;
        int j = 0; 
        while(i<pointer1 && j<pointer2)
        {
            if(left_array[i]<=right_array[j])
            {
                nums[indices_tracker]=left_array[i];
                i++;
            }
            else
            {
                nums[indices_tracker]=right_array[j];
                j++;
            }
            indices_tracker++;
        }
        while(i<pointer1)
        {
            nums[indices_tracker]= left_array[i];
            indices_tracker++;
            i++;
        }
        while(j<pointer2)
        {
            nums[indices_tracker]= right_array[j];
            indices_tracker++;
            j++;
        }
        return; 
    }

};
