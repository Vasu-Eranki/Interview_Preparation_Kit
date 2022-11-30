class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> answer;
        sort(intervals.begin(),intervals.end()); 
        int low_interval = intervals[0][0];
        int high_interval = intervals[0][1]; 
        vector<int> interval; 
        for(int i=1;i<intervals.size();i++)
        {
            vector<int> interval;
            int temp_low_interval = intervals[i][0];
            int temp_high_interval = intervals[i][1];
            if(temp_low_interval<=high_interval)
            {
                low_interval = min(low_interval,temp_low_interval);
                high_interval = max(high_interval,temp_high_interval);
            }
            else{
                interval.push_back(low_interval);
                interval.push_back(high_interval);
                answer.push_back(interval);
                low_interval = temp_low_interval;
                high_interval = temp_high_interval;
            }
            
        }
        interval.push_back(low_interval);
        interval.push_back(high_interval);
        answer.push_back(interval);
        return answer;
    }
};
