// Find the middle node of a singly linked list

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

Node* middle_node(LinkedList* ll){
    Node *fast = ll->head, *slow = ll->head;
    
    // if list is empty or only 1 node is present
    if(fast == NULL || fast->next == NULL)
        return fast;
    
    // while the double speed pointer doesn't get to the end
    // keep updating both slow and fast pointers
    while(fast != NULL){
        fast = fast->next;

        if(fast != NULL){
            fast = fast->next;
            slow = slow->next;
        }
    }

    return slow;
}

int main() {
    LinkedList* ll = new LinkedList();

    // Create Linked list
    ll->insert_at_beg(7);
    ll->insert_at_beg(6);
    ll->insert_at_beg(5);
    ll->insert_at_beg(4);
    ll->insert_at_beg(3);
    ll->insert_at_beg(2);
    ll->insert_at_beg(1);

    cout<<"Linked List data:\n";
    ll->print_data();
    
    cout << "Middle of the linked list is: " << middle_node(ll)->data << endl;
    
    ll->insert_at_beg(0);

    cout<<"Linked List data:\n";
    ll->print_data();
    
    cout << "Middle of the linked list is: " << middle_node(ll)->data << endl;
    return 0;
}


