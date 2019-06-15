// Skip M nodes and delete N nodes from a linked list alternately

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

void skip_m_delete_n(LinkedList* ll, int m, int n){
    Node *curr = ll->head, *del_ptr, *temp;

    while(curr != NULL){
        // Skip M nodes, reach to the mth node
        for(int i=0; i < m-1 && curr != NULL; i++){
            curr = curr->next;
        }
        if(curr == NULL) return;

        del_ptr = curr->next;

        // Delete N nodes, reach to the node and replace pointers
        for(int i=0; i < n && del_ptr != NULL; i++){
            temp = del_ptr;
            del_ptr = del_ptr->next;
            free(temp);
        }
        
        curr->next = del_ptr;
        curr = curr->next;
    }
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

    cout << "Linked list before removal: " << endl;
    ll->print_data();
    int k = 3;
    int m = 2, n = 3;
    skip_m_delete_n(ll, m, n);
    cout << "Linked list after skip "<< m << " delete " << n << ": "<< endl;
    ll->print_data();
    return 0;
}


