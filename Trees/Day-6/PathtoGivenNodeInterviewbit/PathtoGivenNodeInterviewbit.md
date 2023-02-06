**Problem Description**  

Given a Binary Tree **A** containing **N** nodes.

You need to find the path from **Root** to a given node **B**.

**NOTE:**

-   No two nodes in the tree have same data values.
-   You can assume that **B** is present in the tree **A** and a path always exists.

**Problem Constraints**

1 <= N <= 10<sup>5</sup>

1 <= Data Values of Each Node <= N

1 <= B <= N

**Input Format**

First Argument represents pointer to the root of binary tree **A**.

Second Argument is an integer **B** denoting the node number.

**Output Format**

Return an one-dimensional array denoting the path from **Root** to the node **B** in order.

**Example Input**

Input 1:

```
 A =
           1
         /   \
        2     3
       / \   / \
      4   5 6   7 

B = 5

```

Input 2:

```
 A = 
            1
          /   \
         2     3
        / \ .   \
       4   5 .   6

B = 1

```

**Example Output**

Output 1:

```
 [1, 2, 5]

```

Output 2:

```
 [1]

```

**Example Explanation**

Explanation 1:

```
 We need to find the path from root node to node with data value 5.
 So the path is 1 -> 2 -> 5 so we will return [1, 2, 5]

```

Explanation 2:

```
 We need to find the path from root node to node with data value 1.
 As node with data value 1 is the root so there is only one node in the path.
 So we will return [1]

```

Note:You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a question? Checkout [Sample Codes](https://www.interviewbit.com/pages/sample_codes/) for more details.

![submission-count](https://assets.interviewbit.com/packs/images/smiley.a20a61.svg)

23722successful submissions.

See Expected Output

See Expected Output

Enter your input as per the following guideline:

There are 2 lines in the input Line 1 ( Corresponds to arg 1 ) : Serialized representation of tree. The serialization of a binary tree follows a level order description of left and right child of nodes, where -1 signifies a NULL child. For example, 1 / \\ 2 3 / 4 \\ 5 will have representation as {1 2 3 -1 -1 4 -1 -1 5 -1 -1} The first integer on the line indicates the number of integers to follow in the serialized representation of the tree. Line 2 ( Corresponds to arg 2 ) : A single integer

Enter your input here: