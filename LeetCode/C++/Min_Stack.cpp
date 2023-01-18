class MinStack {
public:
    vector<int> numbers;
    MinStack() {
        
    }
    
    void push(int val) {
        numbers.push_back(val);
    }
    
    void pop() {
        numbers.pop_back();
    }
    
    int top() {
        return numbers.back();
    }
    
    int getMin() {
        int min=numbers[0]; 
        for(int i=1;i<numbers.size();i++)
            min = (numbers[i]<min)?numbers[i]:min;
        return min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
