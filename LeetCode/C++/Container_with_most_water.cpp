class Solution {
public:
    int maxArea(vector<int>& height) {
        int pointer1 = 0,pointer2 = height.size()-1;
        int max_water = 0;
        while(pointer2>pointer1)
        {
            int temp_water = (pointer2-pointer1)*min(height[pointer1],height[pointer2]);
            max_water = max(temp_water,max_water);
            if(height[pointer1]>height[pointer2])
            {
                pointer2--;
            }
            else if (height[pointer2]>height[pointer1])
            {
                pointer1++;
            }
            else
            {
                pointer1++;
                pointer2--;
            }
        }
        return max_water;  
        }
};
