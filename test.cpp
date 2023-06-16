#include <iostream>
using namespace std;
class BT
{
public:
    int data;
    BT *LC, *RC;
    void create();
    void insert(BT *root, BT *next);
    void height();
    void leafnode(BT *root);
    void mirror(BT *root);
    void inorder(BT *root);
} *root, *st[10];
int cnt = 0, cntl, cntr;
void BT ::create()
{
    int ch;
    BT *next;
    root = new BT;
    root->LC = NULL;
    root->RC = NULL;
    cout << "enter the root data";
    cin >> root->data;
    cnt++;
    cnt = cntl = cntr;
    do
    {
        cout << "do you want to enter more data(if yes press 1)";
        cin >> ch;
        if (ch == 1)
        {
            // BT *next;
            next = new BT;
            next->LC = NULL;
            next->RC = NULL;
            cout << "enter new data";
            cin >> next->data;
            insert(root, next);
            if (cntl > cnt)
            {
                cnt = cntl;
            }
            else
            {
                cnt = cntr;
            }
        }
    } while (ch == 1);
}
void BT ::height()
{
    cout << "height of the tree is" << cnt;
}
void BT ::insert(BT *root, BT *next)
{
    cout << "root data is" << root->data;
    // BT *temp;

    if (root != NULL)
    {
        if (root->data > next->data)
        {
            if (root->LC == NULL)
            {
                root->LC = next;
                cntl++;
            }
            else
            {
                insert(root->LC, next);
            }
            if (root->data < next->data)
            {
                if (root->RC == NULL)
                {
                    root->RC = next;
                    cntr++;
                }
                else
                {
                    insert(root->RC, next);
                }
            }
        }
    }
}

void BT ::inorder(BT *root)
{
    int top = -1;
    BT *temp;
    temp = root;
    if (root != NULL)
    {
        do
        {
            while (temp != NULL)
            {
                top++;
                temp = st[top];
                temp = temp->LC;
                if (top != -1)
                {
                    st[top] = temp;
                    cout << temp->data << "\t";
                    temp = temp->RC;
                    top--;
                }
            }
        } while (temp != NULL || top != -1);
    }
}
void BT::leafnode(BT *root)
{
    int top = -1;
    BT *temp;
    temp = root;
    int lcount = 0;
    if (root != NULL)
    {
        cout << "leafnodes are";
        do
        {
            while (temp != NULL)
            {
                top++;
                temp = st[top];
                temp = temp->LC;
            }
            if (top != -1)
            {
                st[top] = temp;
                if (root->LC == NULL && root->RC == NULL)
                {
                    cout << temp->data << "\t";
                    lcount++;
                }
                temp = temp->RC;
                top--;
            }
        } while (temp != NULL || top != -1);
    }
    cout << "total no of leafnode " << lcount;
}
void BT ::mirror(BT *root)
{
    int top = -1;
    BT *temp;
    temp = new BT;
    if (root != NULL)
    {
        mirror(root->LC);
        mirror(root->RC);
        temp = root->LC;
        root->LC = root->RC;
        root->RC = temp;
    }
    else
    {
        temp = root;
        if (root != NULL)
        {
            do
            {
                while (temp != NULL)
                {
                    top++;
                    temp = st[top];
                    temp = temp->LC;
                }
                if (top != -1)
                {
                    st[top] = temp;
                    cout << temp->data << "\t";
                    temp = temp->RC;
                    top--;
                }

            } while (temp != NULL || top != -1);
        }
    }
}

int main()
{
    int choice = 0;
    BT obj;
    cout << "\nMENU:\n1]Create\n2]Display Inorder traversal\n3] Count the Leaf nodes using Inorder traversal\n4]Display Mirror Image\n5]Height of the tree";
    do
    {
        cout << "\n\nEnter your choice:";
        cin >> choice;
        switch (choice)
        {
        case 1:
            obj.create();
            break;
        case 2:
            cout << "\nInorder traversal \n: ";
            obj.inorder(root);
            break;
        case 3:
            obj.leafnode(root);
            break;
        case 4:
            cout << "\nThe mirror image of BST is \n: ";
            obj.mirror(root);
            obj.inorder(root);
            break;
        case 5:
            obj.height();
            break;
        }
    } while (choice != 0);
    return 0;
}