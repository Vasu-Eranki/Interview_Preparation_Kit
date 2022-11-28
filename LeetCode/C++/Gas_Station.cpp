class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int gas_sum = accumulate(gas.begin(),gas.end(),0);
        int mileage_cost = accumulate(cost.begin(),cost.end(),0);
        int answer; 
        int gas_tank = 0;
        int previous_travelling_cost = 0;
        int next_starting_point=0;
        for(int i=0;i<gas.size();i++)
        {
            gas_tank+=gas[i]-cost[i];
            if(gas_tank<0)
            {
                next_starting_point = i+1;
                previous_travelling_cost+=gas_tank;
                gas_tank = 0;
            }
        
        }
        answer= (previous_travelling_cost+gas_tank>=0)?next_starting_point:-1;
        return answer;
    }
};
