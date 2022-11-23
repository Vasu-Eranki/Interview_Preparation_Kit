class Solution {
public:
    void reverseString(vector<char>& s) {
        int total_length = s.size();
        int half_length = int(total_length/2);
        char temp; 
        for(int i=0;i<half_length;i++)
        {
            temp = s[total_length-i-1];
            s[total_length-i-1] = s[i];
            s[i]=temp;
        }
    }
};
