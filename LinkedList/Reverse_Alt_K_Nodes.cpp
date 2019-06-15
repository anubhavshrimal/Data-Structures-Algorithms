// Reverse a singly linked list alternately in groups of size k

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

Node* reverse_alt_k_nodes_util(Node* head, int k) {
    // if linked list is empty or has only 1 node
    if(head == NULL || head->next == NULL) return head;

    Node *curr_ptr = head, *next_ptr, *prev_ptr = NULL;
    int count = 0;

    while(curr_ptr != NULL && count < k){
        count += 1;
        next_ptr = curr_ptr->next;
        curr_ptr->next = prev_ptr;
        prev_ptr = curr_ptr;
        curr_ptr = next_ptr;
    }
    
    head->next = curr_ptr;

    count  = 0;
    while(curr_ptr != NULL && count < k-1) {
        curr_ptr = curr_ptr->next;
        count += 1;
    }
    if (curr_ptr != NULL)    
        curr_ptr->next = reverse_alt_k_nodes_util(curr_ptr->next, k);

    // update to the new head
    return prev_ptr;
}

void reverse_alt_k_nodes(LinkedList *ll, int k){
    ll->head = reverse_alt_k_nodes_util(ll->head, k);
}

int main() {
    LinkedList* ll = new LinkedList();
    
    // Create Linked list
    ll->insert_at_beg(8);
    ll->insert_at_beg(7);
    ll->insert_at_beg(6);
    ll->insert_at_beg(5);
    ll->insert_at_beg(4);
    ll->insert_at_beg(3);
    ll->insert_at_beg(2);
    ll->insert_at_beg(1);

    cout << "Linked list before reverse: " << endl;
    ll->print_data();
    int k = 3;
    reverse_alt_k_nodes(ll, k);
    cout << "Linked list after reversing in groups of " << k << ": " << endl;
    ll->print_data();
    return 0;
}


