class Solution {
public:
    string countAndSay(int n) {
        string answer ;
        answer= recursive_solution(n);
        return answer;
    }
    string recursive_solution(int n)
    {
       string answer="";
       if(n==1)
       {
           answer="1";
       }
       else
       {
           string temp_answer;
           temp_answer = recursive_solution(n-1);
           int tracker = 1; 
           for(int i=1;i<temp_answer.size();i++)
           {
               if(temp_answer[i]!=temp_answer[i-1])
               {
                   answer+=(to_string(tracker));
                   answer+=(temp_answer[i-1]);
                   tracker = 1;
               }
               else
               {
                   tracker++;
               }
           }
           answer+=(to_string(tracker));
           answer+=(temp_answer[temp_answer.size()-1]);

       }
       return answer; 
    }
};
