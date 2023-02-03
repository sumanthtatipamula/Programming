//{ Driver Code Starts
import java.util.Scanner;
import java.util.*;
import java.io.*;

class Node
{
	int data;
	Node next;
	Node bottom;
	
	Node(int d)
	{
		data = d;
		next = null;
		bottom = null;
	}
}


class Flatttening_A_LinkedList
{	
    Node head;
	
	void printList(Node node)
    {
        //Node temp = head;
        while (node != null)
        {
            System.out.print(node.data + " ");
            node =node.bottom;
        }
        System.out.println();
    }
	public  static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		Flatttening_A_LinkedList list = new Flatttening_A_LinkedList();
		while(t>0)
		{
			int N = sc.nextInt();
			int arr[] = new int[N];
			for(int i=0;i<N;i++)
				arr[i] = sc.nextInt();
			
			Node temp = null;
			Node tempB = null;
			Node pre = null;
			Node preB = null;	
			int flag=1;
			int flag1=1;
			for(int i=0; i<N;i++)
			{
				int m = arr[i];
				m--;
				int a1 = sc.nextInt();
				temp = new Node(a1);
				if(flag == 1)
				{
					list.head = temp;
					pre = temp;
					flag = 0;
					flag1 = 1;
				}
				else
				{
					pre.next = temp;
					pre = temp;
					flag1 = 1;
				}
				
				for(int j=0;j<m;j++)
				{
					int a = sc.nextInt();
					tempB = new Node(a);
					if(flag1 == 1)
					{
						temp.bottom = tempB;
						preB = tempB;
						flag1 = 0;
					}
					else
					{
						preB.bottom = tempB;
						preB = tempB;
					}
				}
				
			}
			//list.printList();
			GfG g = new GfG();
			Node root = g.flatten(list.head);
			list.printList(root);
		
		t--;
		}
	}	
}
// } Driver Code Ends


/*Node class  used in the program
class Node
{
	int data;
	Node next;
	Node bottom;
	
	Node(int d)
	{
		data = d;
		next = null;
		bottom = null;
	}
}
*/
/*  Function which returns the  root of 
    the flattened linked list. */
class GfG
{
    Node flatten(Node root)
    {
	    Node sentinal = new Node(-1);
	    int len = findLength(root);
	    sentinal.next = root;
	    root = root.next;
	    for(int i = 1; i < len; i++){
	        Node next = root.next;
	        sentinal.next = merge(sentinal.next, root);
	        root = next;
	    }
	    return sentinal.next;
    }
    Node merge(Node list1, Node list2){
        Node sentinal = new Node(-1);
        Node p = sentinal;
        while(list1 != null && list2 != null){
            if(list1.data > list2.data){
                p.bottom = list2;
                list2 = list2.bottom;
            }
            else{
                p.bottom = list1;
                list1 = list1.bottom;
            }
            p = p.bottom;
        }
        while(list1 != null){
            p.bottom = list1;
            list1 = list1.bottom;
            p = p.bottom;
        }
        while(list2 != null){
            p.bottom = list2;
            list2 = list2.bottom;
            p = p.bottom;
        }
        p.bottom = null;
        return sentinal.bottom;
    }
    int findLength(Node root){
        int count = 0;
        while(root != null){
            count++;
            root = root.next;
        }
        return count;
    }
}