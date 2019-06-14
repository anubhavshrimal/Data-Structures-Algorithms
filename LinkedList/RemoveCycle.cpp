// Find and remove cycle if present in a singly linked list

#include <iostream>

using namespace std;

class Node {
    public:
        int data;
        Node* next;

        Node() {
            this->next = NULL;
        }

        Node(int data) {
            this->data = data;
            this->next = NULL;
        }
};

class LinkedList {
    public:
        Node* head = NULL;

        void insert_at_beg(int data){
            Node* temp = new Node(data);
            temp->next = this->head;
            this->head = temp;
        }

        void print_data(){
            Node* itr = this->head;

            while(itr != NULL){
                cout << itr->data << " ";
                itr = itr->next;
            }
            cout << endl;
        }
};

bool remove_cycle(LinkedList* ll){
    Node *fast = ll->head, *slow = ll->head;
    
    // while the double speed pointer doesn't get to the end if loop doesn't exists
    // or does not meet with slow pointer again if loop exists
    while(fast != NULL){ 
        fast = fast->next;

        if(fast != NULL){
            fast = fast->next;
            slow = slow->next;
            if(fast == slow)
                break;
        }
    }

    // cycle doesn't exists
    if(fast == NULL) return false;
    else {
        // bring slow back to linked list head
        slow = ll->head;
        
        // move both pointers at same speed until they meet again
        while(slow->next != fast->next){
            fast = fast->next;
            slow = slow->next;
        }
    }
    
    // break the cycle
    fast->next = NULL;

    return true;
}

int main() {
    LinkedList* ll = new LinkedList();
    
    // Create Linked list
    ll->insert_at_beg(6);
    ll->insert_at_beg(5);
    ll->insert_at_beg(4);
    ll->insert_at_beg(3);
    ll->insert_at_beg(2);
    ll->insert_at_beg(1);

    // Add cycle in the linked list
    ll->head->next->next->next->next->next->next = ll->head->next->next->next;

    // remove cycle if any
    bool found = remove_cycle(ll);

    // print list after removing loop
    found ? cout << "After removing loop linked list is: " : cout << "Loop not found in list: ";
    ll->print_data();

    return 0;
}


