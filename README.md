# Data Structures and Algorithms in Python 3

My implementation of some popular data structures and algorithms and interview questions relating to them in Python 3

## Index:

* [Bit Manipulation](#bit-manipulation)
* [Dynamic Programming](#dynamic-programming)
* [Graph](#graph)
* [Heaps](#heaps)
* [Linked List](#linked-list)
    * [Singly Linked List](#singly-linked-list)
* [Mathematics](#mathematics)
* [Matrix](#matrix)
* [String or Array](#string-or-array)
    * [Searching](#searching)
    * [Sorting](#sorting)
* [Tree](#tree)
    * [Binary Search Tree](#binary-search-tree)
    * [Binary Tree](#binary-tree)
    * [Trie](#trie)

------------------------------------------------------------------------------
## Content:

### Bit Manipulation

Contains some popular questions based on *bit manipulations*.

| 			Topic/Question			|	Code File Name |
|-----------------------------------|------------------|
|Check whether a given number n is a power of 2 or 0|Check_Pow_2.py|
|Count number of bits needed to be flipped to convert A to B|Count_Bits_Flip_A_B.py|
|Find the two non-repeating elements in an array of repeating elements|Find_Non_Repeating.py|
|Find the next greater and next smaller number with same number of set bits|Next_Number.py|

------------------------------------------------------------------------------
### Dynamic Programming

Contains some popular questions based on *dynamic programming approach*. 

| 			Topic/Question			|	Code File Name |
|-----------------------------------|------------------|
|	0-1 Knapsack Problem			| 01_KnapsackProblem.py|
|Cutting Rod problem| CuttingRod.py|
| minimum number of edits (operations) required to convert ‘str1’ into ‘str2’|EditDistance.py|
|Given two sequences, print the longest subsequence present in both of them.|LongestCommonSubsequence.py|
|Find minimum cost path in a matrix from (0,0) to given point (m,n)| MinCostPath.py|
|Partition a set into two subsets such that the difference of subset sums is minimum|MinimumPartition.py|
|	Maximum Subarray Problem		|TheMaximumSubarray.py|
|Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps|WaysToCoverDistance.py|

------------------------------------------------------------------------------
### Matrix

Contains some common algorithms and questions based on *Matrix*.

| 			Topic/Question			|	Code File Name |
|-----------------------------------|------------------|
|Search in a row wise and column wise sorted matrix| SearchRowColumnSorted.py|
|Given a 2D array, print it in spiral form|SpiralPrint.py|

------------------------------------------------------------------------------
### Graph

Contains implementation of Graph data structure and some common questions and algorithms related to it.

| 			Topic/Question          |	Code File Name |
|-----------------------------------|------------------|
|Find all possible words in a board of characters| Boggle.py|
|	Breadth First Search Traversal  | BreadthFirstTraversal.py|
|	Depth First Search Traversal  | DepthFirstTraversal.py|
|	Detect Cycle in directed graph  | DetectCycleDirected.py|
|Detect cycle in undirected graph   |DetectCycleUndirected.py|
|Dijkstra’s Shortest Path Algorithm| DijkstraShortestPath.py|
|Find shortest distances between each pair of vertices in a given edge weighted directed Graph|FloydWarshall_AllPairsShortestPath.py|
|	Graph implementation			| Graph.py|
|	Kruskal's Algorithm for Minimum Spanning Tree| KruskalMST.py|
|	Topological Sort                 | TopologicalSort.py|

------------------------------------------------------------------------------
### Heaps

Contains implementation of Heap data structure and some common questions and algorithms related to it.

| 			Topic/Question          |	Code File Name |
|-----------------------------------|------------------|
|	Heap Sort algorithm             | HeapSort.py|
|   Max Heap implementation         | MaxHeap.py|
|   Min Heap implementation         | MinHeap.py|
|Find the median for an incoming stream of numbers after each insertion in the list of numbers|RunningMedian.py|

------------------------------------------------------------------------------
### Linked List

Contains implementation of Linked List data structure and some common questions and algorithms related to it.

##### Singly Linked List

| 			Topic/Question			|	Code File Name |
|-----------------------------------|------------------|
|Clone a linked list with next and random pointer|CloneRandomPointerList.py|
|Given a linked list of line segments, remove middle points if any|LineRemoveMiddlePoints.py|
|Construct a Maximum Sum Linked List out of two Sorted Linked Lists having some Common nodes.|MaxSumLinkedList.py|
|Merge a linked list into another linked list at alternate positions|MergeAlt.py|
|	Perform Merge Sort              | MergeSort.py|
|	Find Middle Node                | MiddleNode.py|
|Point to next higher value node in a linked list with an arbitrary pointer|NextHigerValueNode.py|
|	Find if linked list contains any cycle			| NullOrCycle.py|
|To select a random node in a singly linked list|Random_Node.py|
|	Find and remove cycle if any    | RemoveCycle.py|
|	Reverse sub list of K nodes each| ReverseKNodes.py|
|	Reverse alternate sub list of K nodes each | Reverse\_Alt\_K_Nodes.py|
|	Reverse a linked list			| ReverseSLL.py|
|	Bring even valued nodes to the front | SegregateEvenOdd.py|
|	Implementation of Singly Linked List | SinglyLinkedList.py|
|Skip M nodes and then delete N nodes alternately |SkipMDeleteN.py|

------------------------------------------------------------------------------
### Mathematics

Contains implementation of some common questions and algorithms related to Mathematics.

| 			Topic/Question          |	Code File Name |
|-----------------------------------|------------------|
|Find the greatest common divisor of 2 numbers|GCD.py|
|	print all prime factors of a given number | Prime_factors.py|
|	Sieve of Eratosthenes (find prime numbers up to n efficiently)| Sieve_of_Eratosthenes.py|

------------------------------------------------------------------------------
### Misc

Contains some miscellaneous questions and algorithms.

| 			Topic/Question			|	Code File Name |
|-----------------------------------|------------------|
|Given a dictionary, write a function to flatten it| Flatten_Dictionary.py|

------------------------------------------------------------------------------
### String or Array

Contains some common questions and algorithms related to strings or 1-d arrays.

| 			Topic/Question			|	Code File Name |
|-----------------------------------|------------------|
|Find the longest substring with k unique characters in a given string|K_Unique_Substring.py|
|Find a pattern in a string using KMP search algorithm|KMP_StringMatching.py|
|Find the Kth smallest element in the array |Kth_Smallest.py|
|Find a pair in an array with sum x|PairSum_is_X.py|
|reverse the order of the words in the array|Sentence_Reverse.py|
|Find index of given number in a sorted array shifted by an unknown offset|Shifted_Array_Search.py|
|Print all permutations of a given string| StringPermutations.py|

#### Searching

| 			Topic/Question			|	Code File Name |
|-----------------------------------|------------------|
|Linear Search in an array|Linear_Search.py|
|Binary Search in an array|Binary_Search.py|
|Interpolation Search in an array|Interpolation_Search.py|

#### Sorting

| 			Topic/Question			|	Code File Name |
|-----------------------------------|------------------|
|Bubble sort Algorithm|Bubble_Sort.py|
|Counting sort Algorithm (non-comparision based sorting)|Counting_Sort.py|
|Insertion sort Algorithm|Insertion_Sort.py|
|Sort an array where each element is at most k places away from its sorted position|K_Messed_Sort.py|
|Merge Sort Algorithm|Merge_Sort.py|
|Quick Sort Algorithm using last element as pivot|Quick_Sort.py|
|Selection sort Algorithm|Selection_Sort.py|

------------------------------------------------------------------------------
### Tree

Contains implementation of Tree data structure and some common questions and algorithms related to it.

##### Binary Search Tree

| 			Topic/Question			|	Code File Name |
|-----------------------------------|------------------|
|	Binary Search Tree implementation			| BST.py|
|Check if a given array can represent Preorder Traversal of Binary Search Tree|Check_Correct_Preorder.py|
|Find the in-order ancestor of a given node in BST|InOrder_Ancestor.py|
|Find the Lowest Common Ancestor|Lowest_Common_Ancestor.py|
|Given a sorted array, create a BST with minimal height|Minimal_Tree.py|

##### Binary Tree

| 			Topic/Question			|	Code File Name |
|-----------------------------------|------------------|
|Print Nodes in Bottom View of Binary Tree|Bottom_View.py|
|Check if a binary tree is height balanced|Check_Balanced.py|
|Check whether a binary tree is a full binary tree or not|Check_Full_BinaryTree.py|
|Given two binary trees, check if the first tree is subtree of the second one|Is_SubTree.py|
|Find the Lowest Common Ancestor in a Binary Tree|Lowest_Common_Ancestor.py|
|Create a list of all nodes at each depth|List_Of_Depths.py|
|Find the maximum path sum i.e. max sum of a path in a binary tree|Max_Path_Sum.py|
|	Find minimum depth of a binary tree | Minimum_height.py|
|Remove nodes on root to leaf paths of length < K|Remove_Path_Less_Than_K.py|
|Given a Perfect Binary Tree, reverse the alternate level nodes of the tree|Reverse_Alternate_Levels_PBT.py|
|Print Nodes in Top View of Binary Tree|Top_View.py|

##### Trie

| 			Topic/Question			|	Code File Name |
|-----------------------------------|------------------|
|Implementation of Trie data structure|Trie.py|

------------------------------------------------------------------------------