#include <iostream>
using namespace std;

// creat the User Define Data Type Of Node 
struct Node
{
    int data;
    Node *next;
};
Node *head; // we declare head to store the address the first node
int main()
{
//  first node created
    Node *new_node;
    new_node = new Node();
    head = new_node;
    new_node->data = 20;

    // node2
    Node *new_node2;
    new_node2 = new Node();
    new_node->next = new_node2; // we link node1 to node2
    new_node2->data = 21;
// node3
    Node *node3 = new Node();
    node3->data = 30;
    new_node2->next = node3;
// node4
    Node *node4 = new Node();
    node4->data = 43;
    node3->next = node4;







// the method to inter the given element to given position
     int pos = 3, index = 1;

    Node *temp2 = head;
    while (index < pos - 1)
    {
        temp2 = temp2->next;
        index++;
    }
    Node *Created = new Node();
    Created->data = 32;
    Created->next = temp2->next;
    temp2->next = Created;









// add element into the last position
    Node *temp3 = head;
    while (temp3->next != NULL)
    {
        temp3 = temp3->next;
    }
    Node *node6 = new Node();
    node6->data = 54;
    temp3->next = node6;
    node6->next = NULL;










 // this code works to remove the spacifc data
    Node *temp4 = head;
    while (temp4->next != NULL)
    {
        if (temp4->next->data == 32)
        {
            Node *del = temp4->next;
            temp4->next = del->next;
            delete del;
            temp4 = temp4->next;
        }
        else
        {
            temp4 = temp4->next;
        }
    } 





    // to remove the first Node
    Node *Dele = head;
    head = Dele->next;
    delete Dele;




    // to remove the last element
    Node *temp5 = head;
    while (temp5->next->next != NULL)
    {
        temp5 = temp5->next;
    }
    temp5->next = NULL;








    // to itrate the whole list
    Node *temp = head;
    while (temp != NULL)
    {
        cout << temp->data << "->";
        temp = temp->next;
    }
}
