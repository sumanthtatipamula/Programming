# Convert A Given Binary Tree To Doubly Linked List

MEDIUM

## Problem Statement

Suggest Edit

#### Given a Binary Tree, convert this binary tree to a Doubly Linked List.

#### A Binary Tree (BT) is a data structure in which each node has at most two children.

#### A Doubly Linked List contains a previous pointer, along with the next pointer and data.

#### The order of nodes in Doubly Linked List must be the same as Inorder of the given Binary Tree.

#### The doubly linked list should be returned by taking the next pointer as right and the previous pointer as left.

#### You need to return the head of the Doubly Linked List.

#### For the given binary tree :

![alt txt](https://files.codingninjas.in/graph-6530.png)

```
You need to return the head to the doubly linked list.
The doubly linked list would be: 1 2 3 4 5 and can be represented as:
```

![alt txt](https://files.codingninjas.in/graph-1-6531.png)

Detailed explanation ( Input/output format, Notes, Constraints, Images )

![](https://files.codingninjas.in/expand_less-20914.svg)

##### Sample Input 1 :

```
2
3 1 5 -1 2 -1 -1 -1 -1
9 6 10 4 7 -1 11 -1 -1 -1 -1 -1 -1
```

##### Sample Output 1 :

```
1 2 3 5
4 6 7 9 10 11
```

##### Explanation of Input 1 :

```
Here we have 2 test cases; hence there are 2 binary trees.

Test Case 1 :
```

![alt txt](https://files.codingninjas.in/graph-2-6533.png)

```
We can see that the inorder traversal of the given tree is: 1 2 3 5.


Test Case 2 :
```

![alt txt](https://files.codingninjas.in/graph-3-6532.png)

```
We can see that the inorder traversal of the given tree is: 4 6 7 9 10 11.
```

##### Sample Input 2 :

```
2
4 6 -1 5 -2 -1 -1 -1 -1
1 2 3 4 4 -1 4 -1 -1 -1 -1 -1 -1
```

##### Sample Output 2 :

```
5 6 -2 4
4 2 4 1 3 4
```
