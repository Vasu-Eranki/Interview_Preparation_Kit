/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
    if(!head)
    {
        return NULL;
    }
    else
    {
        unordered_map<Node*,Node*> dictionary;
        Node* deepcopy = new Node(0);
        Node* deepcopy_v1 = deepcopy;
        Node* deepcopy_v2 = deepcopy; 
        Node *headcopy = head;
        while(head)
        {
            deepcopy->val = head->val;
            if(head->next)
            {
                deepcopy->next = new Node(0);
            }
            dictionary[head]=deepcopy;
            deepcopy = deepcopy->next; 
            head = head->next;
        }
        while(deepcopy_v1)
        {
            deepcopy_v1->random = dictionary[headcopy->random];
            deepcopy_v1 = deepcopy_v1->next;
            headcopy = headcopy->next; 
        }
        return deepcopy_v2;
}
}};
