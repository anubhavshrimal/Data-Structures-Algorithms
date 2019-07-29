# Data Structures and Algorithms

My implementation of some popular data structures and algorithms and interview questions relating to them in Python 3 and C++

## Index:

- [Data Structures and Algorithms](#Data-Structures-and-Algorithms)
  - [Index:](#Index)
  - [Content:](#Content)
    - [Bit Manipulation](#Bit-Manipulation)
    - [Dynamic Programming](#Dynamic-Programming)
    - [Graph](#Graph)
    - [Heaps](#Heaps)
    - [Linked List](#Linked-List)
        - [Singly Linked List](#Singly-Linked-List)
    - [Mathematics](#Mathematics)
    - [Matrix](#Matrix)
    - [Misc](#Misc)
    - [String or Array](#String-or-Array)
      - [Searching](#Searching)
      - [Sorting](#Sorting)
    - [Tree](#Tree)
        - [Binary Search Tree](#Binary-Search-Tree)
        - [Binary Tree](#Binary-Tree)
        - [Trie](#Trie)

------------------------------------------------------------------------------
## Content:

### Bit Manipulation

Contains some popular questions based on *bit manipulations*.

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|Check whether a given number n is a power of 2 or 0                            |[py](Bit_Manipulation/Check_Pow_2.py)         |[cpp](Bit_Manipulation/Check_Pow_2.cpp)|
|Count number of bits needed to be flipped to convert A to B                    |[py](Bit_Manipulation/Count_Bits_Flip_A_B.py) |[cpp](Bit_Manipulation/Count_Bits_Flip_A_B.cpp)|
|Find the two non-repeating elements in an array of repeating elements          |[py](Bit_Manipulation/Find_Non_Repeating.py)  |[cpp](Bit_Manipulation/Find_Non_Repeating.cpp)|
|Find the next greater and next smaller number with same number of set bits     |[py](Bit_Manipulation/Next_Number.py)         |[cpp](Bit_Manipulation/Next_Number.cpp)|

------------------------------------------------------------------------------
### Dynamic Programming

Contains some popular questions based on *dynamic programming approach*. 

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|	0-1 Knapsack Problem			                                                                                    |[py](DynamicProgramming/01_KnapsackProblem.py)| [-](DynamicProgramming/01_KnapsackProblem.cpp)|
|Cutting Rod problem                                                                                                    |[py](DynamicProgramming/CuttingRod.py)| [-](DynamicProgramming/CuttingRod.cpp)|
| minimum number of edits (operations) required to convert ‘str1’ into ‘str2’                                           |[py](DynamicProgramming/EditDistance.py)|[-](DynamicProgramming/EditDistance.cpp)|
| Given a 2-D matrix of 0s and 1s, find the Largest Square which contains all 1s in itself                              |[py](DynamicProgramming/LargestSquareInMatrix.py)|[-](DynamicProgramming/LargestSquareInMatrix.cpp)|
|Given two sequences, print the longest subsequence present in both of them.                                            |[py](DynamicProgramming/LongestCommonSubsequence.py)|[-](DynamicProgramming/LongestCommonSubsequence.cpp)|
|Length of the longest subsequence in an array such that all elements of the subsequence are sorted in increasing order |[py](DynamicProgramming/LongestIncreasingSubsequence.py)|[-](DynamicProgramming/LongestIncreasingSubsequence.cpp)|
|Find minimum cost path in a matrix from (0,0) to given point (m,n)                                                     |[py](DynamicProgramming/MinCostPath.py)| [-](DynamicProgramming/MinCostPath.cpp)|
|Partition a set into two subsets such that the difference of subset sums is minimum                                    |[py](DynamicProgramming/MinimumPartition.py)|[-](DynamicProgramming/MinimumPartition.cpp)|
|Minimum number of umbrellas of m different sizes required to accomodate N people                                       |[py](DynamicProgramming/MinUmbrellaNeeded.py)|[cpp](DynamicProgramming/MinUmbrellaNeeded.cpp)|
|Determine if there is a subset of the given set with sum equal to given sum                                            |[py](DynamicProgramming/SubsetSum.py)|[-](DynamicProgramming/SubsetSum.cpp)|
|	Maximum Subarray Problem		                                                                                    |[py](DynamicProgramming/TheMaximumSubarray.py)|[-](DynamicProgramming/TheMaximumSubarray.cpp)|
|Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps                         |[py](DynamicProgramming/WaysToCoverDistance.py)|[-](DynamicProgramming/WaysToCoverDistance.cpp)|

------------------------------------------------------------------------------
### Graph

Contains implementation of Graph data structure and some common questions and algorithms related to it.

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|Find all possible words in a board of characters                                               |[py](Graph/Boggle.py)|[-](Graph/Boggle.cpp)|
|	Breadth First Search Traversal                                                              |[py](Graph/BreadthFirstTraversal.py)|[-](Graph/BreadthFirstTraversal.cpp)|
|	Depth First Search Traversal                                                                |[py](Graph/DepthFirstTraversal.py)|[-](Graph/DepthFirstTraversal.cpp)|
|	Detect Cycle in directed graph                                                              |[py](Graph/DetectCycleDirected.py)|[-](Graph/DetectCycleDirected.cpp)|
|Detect cycle in undirected graph                                                               |[py](Graph/DetectCycleUndirected.py)|[-](Graph/DetectCycleUndirected.cpp)|
|Dijkstra’s Shortest Path Algorithm                                                             |[py](Graph/DijkstraShortestPath.py)|[-](Graph/DijkstraShortestPath.cpp)|
|Find shortest distances between each pair of vertices in a given edge weighted directed Graph  |[py](Graph/FloydWarshall_AllPairsShortestPath.py)|[-](Graph/FloydWarshall_AllPairsShortestPath.cpp)|
|	Graph implementation			                                                            |[py](Graph/Graph.py)|[-](Graph/Graph.cpp)|
|	Kruskal's Algorithm for Minimum Spanning Tree                                               |[py](Graph/KruskalMST.py)|[-](Graph/KruskalMST.cpp)|
|	Topological Sort                                                                            |[py](Graph/TopologicalSort.py)|[-](Graph/TopologicalSort.cpp)|

------------------------------------------------------------------------------
### Heaps

Contains implementation of Heap data structure and some common questions and algorithms related to it.

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|	Heap Sort algorithm                                                                         |[py](Heaps/HeapSort.py)|[-](Heaps/HeapSort.cpp)|
|   Max Heap implementation                                                                     |[py](Heaps/MaxHeap.py)|[-](Heaps/MaxHeap.cpp)|
|   Min Heap implementation                                                                     |[py](Heaps/MinHeap.py)|[-](Heaps/MinHeap.cpp)|
|Find the median for an incoming stream of numbers after each insertion in the list of numbers  |[py](Heaps/RunningMedian.py)|[-](Heaps/RunningMedian.cpp)|

------------------------------------------------------------------------------
### Linked List

Contains implementation of Linked List data structure and some common questions and algorithms related to it.

##### Singly Linked List

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|Clone a linked list with next and random pointer                                               |[py](LinkedList/CloneRandomPointerList.py)|[-](LinkedList/CloneRandomPointerList.cpp)|
|Given a linked list of line segments, remove middle points if any                              |[py](LinkedList/LineRemoveMiddlePoints.py)|[-](LinkedList/LineRemoveMiddlePoints.cpp)|
|Construct a Maximum Sum Linked List out of two Sorted Linked Lists having some Common nodes.   |[py](LinkedList/MaxSumLinkedList.py)|[-](LinkedList/MaxSumLinkedList.cpp)|
|Merge a linked list into another linked list at alternate positions                            |[py](LinkedList/MergeAlt.py)|[-](LinkedList/MergeAlt.cpp)|
|	Perform Merge Sort                                                                          |[py](LinkedList/MergeSort.py)|[-](LinkedList/MergeSort.cpp)|
|	Find Middle Node                                                                            |[py](LinkedList/MiddleNode.py)|[cpp](LinkedList/MiddleNode.cpp)|
|Point to next higher value node in a linked list with an arbitrary pointer                     |[py](LinkedList/NextHigerValueNode.py)|[-](LinkedList/NextHigerValueNode.cpp)|
|	Find if linked list contains any cycle			                                            |[py](LinkedList/NullOrCycle.py)|[-](LinkedList/NullOrCycle.cpp)|
|To select a random node in a singly linked list                                                |[py](LinkedList/Random_Node.py)|[-](LinkedList/Random_Node.cpp)|
|	Find and remove cycle if any                                                                |[py](LinkedList/RemoveCycle.py)|[cpp](LinkedList/RemoveCycle.cpp)|
|	Reverse sub list of K nodes each                                                            |[py](LinkedList/ReverseKNodes.py)|[cpp](LinkedList/ReverseKNodes.cpp)|
|	Reverse alternate sub list of K nodes each                                                  |[py](LinkedList/Reverse_Alt_K_Nodes.py)|[cpp](LinkedList/Reverse_Alt_K_Nodes.cpp)|
|	Reverse a linked list			                                                            |[py](LinkedList/ReverseSLL.py)|[cpp](LinkedList/ReverseSLL.cpp)|
|	Bring even valued nodes to the front                                                        |[py](LinkedList/SegregateEvenOdd.py)|[-](LinkedList/SegregateEvenOdd.cpp)|
|	Implementation of Singly Linked List                                                        |[py](LinkedList/SinglyLinkedList.py)|[cpp](LinkedList/SinglyLinkedList.cpp)|
|Skip M nodes and then delete N nodes alternately                                               |[py](LinkedList/SkipMDeleteN.py)|[cpp](LinkedList/SkipMDeleteN.cpp)|

------------------------------------------------------------------------------
### Mathematics

Contains implementation of some common questions and algorithms related to Mathematics.

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|Fine the number of trailing zeros in factorial of a number         |[py](Mathematics/Factorial_Trailing_Zeros.py)|[cpp](Mathematics/Factorial_Trailing_Zeros.cpp)|
|Find the greatest common divisor of 2 numbers                      |[py](Mathematics/GCD.py)|[-](Mathematics/GCD.cpp)|
|	print all prime factors of a given number                       |[py](Mathematics/Prime_factors.py)|[-](Mathematics/Prime_factors.cpp)|
|	Sieve of Eratosthenes (find prime numbers up to n efficiently)  |[py](Mathematics/Sieve_of_Eratosthenes.py)|[-](Mathematics/Sieve_of_Eratosthenes.cpp)|

------------------------------------------------------------------------------
### Matrix

Contains some common algorithms and questions based on *Matrix*.

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|Given the Coordinates of King and Queen on a chessboard, check if queen threatens the king |[py](Matrix/CheckQueenThreatsKing.py)|[-](Matrix/CheckQueenThreatsKing.cpp)|
|Search in a row wise and column wise sorted matrix                                         |[py](Matrix/SearchRowColumnSorted.py)|[-](Matrix/SearchRowColumnSorted.cpp)|
|Given a 2D array, print it in spiral form                                                  |[py](Matrix/SpiralPrint.py)|[-](Matrix/SpiralPrint.cpp)|

------------------------------------------------------------------------------
### Misc

Contains some miscellaneous questions and algorithms.

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|Given a dictionary, write a function to flatten it                             |[py](Misc/Flatten_Dictionary.py)|[-](Misc/Flatten_Dictionary.cpp)|

------------------------------------------------------------------------------
### String or Array

Contains some common questions and algorithms related to strings or 1-d arrays.

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|Find the longest substring with k unique characters in a given string              |[py](String_or_Array/K_Unique_Substring.py)|[-](String_or_Array/K_Unique_Substring.cpp)|
|Find a pattern in a string using KMP search algorithm                              |[py](String_or_Array/KMP_StringMatching.py)|[-](String_or_Array/KMP_StringMatching.cpp)|
|Find the Kth smallest element in the array                                         |[py](String_or_Array/Kth_Smallest.py)|[-](String_or_Array/Kth_Smallest.cpp)|
|Find a pair in an array with sum x                                                 |[py](String_or_Array/PairSum_is_X.py)|[-](String_or_Array/PairSum_is_X.cpp)|
|Print all valid (properly opened and closed) combinations of n pairs of parentheses|[py](String_or_Array/ParenthesesCombinations.py)|[-](String_or_Array/ParenthesesCombinations.cpp)|
|reverse the order of the words in the array                                        |[py](String_or_Array/Sentence_Reverse.py)|[-](String_or_Array/Sentence_Reverse.cpp)|
|Find index of given number in a sorted array shifted by an unknown offset          |[py](String_or_Array/Shifted_Array_Search.py)|[-](String_or_Array/Shifted_Array_Search.cpp)|
|Print all permutations of a given string                                           |[py](String_or_Array/StringPermutations.py)|[-](String_or_Array/StringPermutations.cpp)|

#### Searching

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|Linear Search in an array          |[py](String_or_Array/Searching/Linear_Search.py)|[-](String_or_Array/Searching/Linear_Search.cpp)|
|Binary Search in an array          |[py](String_or_Array/Searching/Binary_Search.py)|[-](String_or_Array/Searching/Binary_Search.cpp)|
|Interpolation Search in an array   |[py](String_or_Array/Searching/Interpolation_Search.py)|[-](String_or_Array/Searching/Interpolation_Search.cpp)|

#### Sorting

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|Bubble sort Algorithm                                                              |[py](String_or_Array/Sorting/Bubble_Sort.py)|[-](String_or_Array/Sorting/Bubble_Sort.cpp)|
|Counting sort Algorithm (non-comparision based sorting)                            |[py](String_or_Array/Sorting/Counting_Sort.py)|[-](String_or_Array/Sorting/Counting_Sort.cpp)|
|Insertion sort Algorithm                                                           |[py](String_or_Array/Sorting/Insertion_Sort.py)|[-](String_or_Array/Sorting/Insertion_Sort.cpp)|
|Sort an array where each element is at most k places away from its sorted position |[py](String_or_Array/Sorting/K_Messed_Sort.py)|[-](String_or_Array/Sorting/K_Messed_Sort.cpp)|
|Merge Sort Algorithm                                                               |[py](String_or_Array/Sorting/Merge_Sort.py)|[-](String_or_Array/Sorting/Merge_Sort.cpp)|
|Quick Sort Algorithm using last element as pivot                                   |[py](String_or_Array/Sorting/Quick_Sort.py)|[-](String_or_Array/Sorting/Quick_Sort.cpp)|
|Selection sort Algorithm                                                           |[py](String_or_Array/Sorting/Selection_Sort.py)|[-](String_or_Array/Sorting/Selection_Sort.cpp)|

------------------------------------------------------------------------------
### Tree

Contains implementation of Tree data structure and some common questions and algorithms related to it.

##### Binary Search Tree

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|	Binary Search Tree implementation			                                |[py](Tree/BinarySearchTree/BST.py)|[-](Tree/BinarySearchTree/BST.cpp)|
|Check if a given array can represent Preorder Traversal of Binary Search Tree  |[py](Tree/BinarySearchTree/Check_Correct_Preorder.py)|[-](Tree/BinarySearchTree/Check_Correct_Preorder.cpp)|
|Find the in-order ancestor of a given node in BST                              |[py](Tree/BinarySearchTree/InOrder_Ancestor.py)|[-](Tree/BinarySearchTree/InOrder_Ancestor.cpp)|
|Find the Lowest Common Ancestor                                                |[py](Tree/BinarySearchTree/Lowest_Common_Ancestor.py)|[-](Tree/BinarySearchTree/Lowest_Common_Ancestor.cpp)|
|Given a sorted array, create a BST with minimal height                         |[py](Tree/BinarySearchTree/Minimal_Tree.py)|[-](Tree/BinarySearchTree/Minimal_Tree.cpp)|

##### Binary Tree

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|Print Nodes in Bottom View of Binary Tree                                      |[py](Tree/BinaryTree/Bottom_View.py)|[-](Tree/BinaryTree/Bottom_View.cpp)|
|Check if a binary tree is height balanced                                      |[py](Tree/BinaryTree/Check_Balanced.py)|[-](Tree/BinaryTree/Check_Balanced.cpp)|
|Check whether a binary tree is a full binary tree or not                       |[py](Tree/BinaryTree/Check_Full_BinaryTree.py)|[-](Tree/BinaryTree/Check_Full_BinaryTree.cpp)|
|Given two binary trees, check if the first tree is subtree of the second one   |[py](Tree/BinaryTree/Is_SubTree.py)|[-](Tree/BinaryTree/Is_SubTree.cpp)|
|Find the Lowest Common Ancestor in a Binary Tree                               |[py](Tree/BinaryTree/Lowest_Common_Ancestor.py)|[-](Tree/BinaryTree/Lowest_Common_Ancestor.cpp)|
|Create a list of all nodes at each depth                                       |[py](Tree/BinaryTree/List_Of_Depths.py)|[-](Tree/BinaryTree/List_Of_Depths.cpp)|
|Find the maximum path sum i.e. max sum of a path in a binary tree              |[py](Tree/BinaryTree/Max_Path_Sum.py)|[-](Tree/BinaryTree/Max_Path_Sum.cpp)|
|	Find minimum depth of a binary tree                                         |[py](Tree/BinaryTree/Minimum_height.py)|[-](Tree/BinaryTree/Minimum_height.cpp)|
|Remove nodes on root to leaf paths of length < K                               |[py](Tree/BinaryTree/Remove_Path_Less_Than_K.py)|[-](Tree/BinaryTree/Remove_Path_Less_Than_K.cpp)|
|Given a Perfect Binary Tree, reverse the alternate level nodes of the tree     |[py](Tree/BinaryTree/Reverse_Alternate_Levels_PBT.py)|[-](Tree/BinaryTree/Reverse_Alternate_Levels_PBT.cpp)|
|Print Nodes in Top View of Binary Tree                                         |[py](Tree/BinaryTree/Top_View.py)|[-](Tree/BinaryTree/Top_View.cpp)|

##### Trie

| 			Topic/Question			                                            |	Code in Python                              | Code in C++ |
|-----------------------------------|:------------------:|:-----------------:|
|Implementation of Trie data structure                                          |[py](Tree/Trie/Trie.py)|[-](Tree/Trie/Trie.cpp)|

------------------------------------------------------------------------------
