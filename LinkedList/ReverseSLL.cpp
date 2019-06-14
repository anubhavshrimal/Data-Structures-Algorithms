// Reverse a singly linked list

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

void reverse(LinkedList *ll){
    // if linked list is empty or has only 1 node
    if(ll->head == NULL || ll->head->next == NULL) return;

    Node *curr_ptr = ll->head, *next_ptr, *prev_ptr = NULL;

    while(curr_ptr != NULL){
        next_ptr = curr_ptr->next;
        curr_ptr->next = prev_ptr;
        prev_ptr = curr_ptr;
        curr_ptr = next_ptr;
    }

    // update to the new head
    ll->head = prev_ptr;
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

    cout << "Linked list before reverse: " << endl;
    ll->print_data();

    reverse(ll);
    cout << "Linked list after reverse: " << endl;
    ll->print_data();
    return 0;
}


