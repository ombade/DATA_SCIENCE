#include <iostream>
using namespace std;

class BT
{
public:
    int data;
    BT *LC, *RC;
    static int cnt;
    static int cntl;
    static int cntr;
    static BT *st[10];

    BT()
    {
        LC = NULL;
        RC = NULL;
    }

    static void create(BT *&root);
    void insert(BT *next);
    void height();
    void leafnode();
    void mirror();
    void inorder();
};

int BT::cnt = 0;
int BT::cntl = 0;
int BT::cntr = 0;
BT *BT::st[10];

void BT::create(BT *&root)
{
    int ch;
    BT *next;
    root = new BT;
    cout << "Enter the root data: ";
    cin >> root->data;
    BT::cnt++;
    BT::cntl = BT::cntr = 0;

    do
    {
        cout << "Do you want to enter more data? (1 for yes): ";
        cin >> ch;

        if (ch == 1)
        {
            next = new BT;
            cout << "Enter new data: ";
            cin >> next->data;
            root->insert(next);
            if (BT::cntl > BT::cnt)
                BT::cnt = BT::cntl;
            else
                BT::cnt = BT::cntr;
        }
    } while (ch == 1);
}

void BT::insert(BT *next)
{
    if (data > next->data)
    {
        if (LC == NULL)
        {
            LC = next;
            BT::cntl++;
        }
        else
        {
            LC->insert(next);
        }
    }
    else if (data < next->data)
    {
        if (RC == NULL)
        {
            RC = next;
            BT::cntr++;
        }
        else
        {
            RC->insert(next);
        }
    }
}

void BT::inorder()
{
    int top = -1;
    BT *temp;
    temp = this;

    if (this != NULL)
    {
        do
        {
            while (temp != NULL)
            {
                top++;
                BT::st[top] = temp;
                temp = temp->LC;
            }

            if (top != -1)
            {
                temp = BT::st[top];
                cout << temp->data << "\t";
                temp = temp->RC;
                top--;
            }
        } while (temp != NULL || top != -1);
    }
}

void BT::leafnode()
{
    int top = -1;
    BT *temp;
    temp = this;
    int lcount = 0;

    if (this != NULL)
    {
        cout << "Leaf nodes are: ";
        do
        {
            while (temp != NULL)
            {
                top++;
                BT::st[top] = temp;
                temp = temp->LC;
            }

            if (top != -1)
            {
                temp = BT::st[top];

                if (temp->LC == NULL && temp->RC == NULL)
                {
                    cout << temp->data << "\t";
                    lcount++;
                }

                temp = temp->RC;
                top--;
            }
        } while (temp != NULL || top != -1);
    }

    cout << "\nTotal number of leaf nodes: " << lcount;
}

void BT::mirror()
{
    if (this != NULL)
    {
        LC->mirror();
        RC->mirror();

        BT *temp = LC;
        LC = RC;
        RC = temp;
    }
}

void BT::height()
{
    cout << "Height of the tree is: " << BT::cnt;
}

int main()
{
    int choice = 0;
    BT *root = NULL;
    BT obj;
    cout << "MENU:\n1]Create\n2]Display Inorder traversal\n3]Count the Leaf nodes using Inorder traversal\n4]Display Mirror Image\n5]Height of the tree\n0]Exit\n";

    do
    {
        cout << "\nEnter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            obj.create(root);
            break;
        case 2:
            cout << "\nInorder traversal: ";
            if (root != NULL)
                root->inorder();
            else
                cout << "Tree is empty!";
            break;
        case 3:
            cout << "\nLeaf nodes: ";
            if (root != NULL)
                root->leafnode();
            else
                cout << "Tree is empty!";
            break;
        case 4:
            cout << "\nThe mirror image of BST: ";
            if (root != NULL)
            {
                root->mirror();
                root->inorder();
            }
            else
                cout << "Tree is empty!";
            break;
        case 5:
            cout << "\n";
            if (root != NULL)
                root->height();
            else
                cout << "Tree is empty!";
            break;
        case 0:
            cout << "\nExiting...";
            break;
        default:
            cout << "\nInvalid choice! Please try again.";
        }
    } while (choice != 0);

    return 0;
}
