class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
    map<int,int> ordered_numbers; 
    vector<int> k_frequent;
    for(auto i:nums)
    {
        ordered_numbers[i]++;
    } 
    priority_queue<pair<int,int>> sorted_map;
    for(auto i:ordered_numbers)
    {
        sorted_map.push({i.second,i.first});
    }
    for(int j=0;j<k;j++)
    {   
           k_frequent.push_back(sorted_map.top().second);
           sorted_map.pop();           
    }
     return k_frequent;       
    }
};
