// Implementation of Singly linked list

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

        void insert_at_end(int data){
            Node* itr = this->head;
            if (itr == NULL){
                this->insert_at_beg(data);
                return;
            }
            
            Node* temp = new Node(data);

            while(itr->next != NULL){
                itr = itr->next;
            }
            
            itr->next = temp;
        }
        

        void delete_from_beg(){
            if (this->head == NULL) return;

            Node* temp = this->head;
            this->head = this->head->next;
            free(temp);
        }

        void delete_from_end(){
            Node* itr = this->head;
            if (itr == NULL){
                return;
            }
            else if (itr->next == NULL){
                this->head = NULL;
                free(itr);
            }

            while(itr->next->next != NULL){
                itr = itr->next;
            }
            
            Node* temp = itr->next;
            itr->next = NULL;
            free(temp);
        }

        int size() {      
            Node* itr = this->head;
            int length = 0;

            while(itr != NULL){
                length += 1;
                itr = itr->next;
            }

            return length;
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

int main() {
    LinkedList* ll = new LinkedList();
    
    ll->delete_from_beg();
    ll->delete_from_end();
    // Insert at the beginning 3, 2, 1
    ll->insert_at_beg(3);
    ll->insert_at_beg(2);
    ll->insert_at_beg(1);
    cout<<"After insertion at the beginning:\n";
    ll->print_data();

    // Insert at the end of the list 4, 5
    ll->insert_at_end(4);
    ll->insert_at_end(5);
    cout<<"After insertion at the end:\n";
    ll->print_data();

    // Delete 1 from the beginning
    cout<<"After deletion at the beginning:\n";
    ll->delete_from_beg();
    ll->print_data();

    // Delete 5 from the end
    cout<<"After deletion at the end:\n";
    ll->delete_from_end();
    ll->print_data();

    // print size of the list
    cout << "Size of the linked list: " << ll->size() << endl;
    return 0;
}



