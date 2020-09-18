/* ARRAYS

Given a sorted array of positive integers with an empty spot (zero) at the end, insert an element in sorted order. */
Approach: Shift from back, then insert
The first approach is to shift all the elements over and then insert the value x.
boolean insert(int[] array, int x) 
if (array[array.length - 1] != 0 || x <= 0) 
  return false;
// Start from last non-blank element, moving left and copying elements one by one. Stop when we've found the right spot for x. 
int index = array.length - 2; //start from 2nd to last
while (index >= 0 && array[index] > x)
array[index + 1] = array[index]; //shift over by one
index = index - 1; //move to next element
// insert element wherever the above loop stopped
array[index + 1] = x;
return true;

/* Reverse the order of elements in an array (without creating a new array). */
void reverse(int[] array)
  int midpoint = array.length / 2;
  for (int i = 0; i < midpoint; i++)
    //Get corresponding index on right side
    int otherside = array.length - 1 - i;
    // swap left and right values
    int temp = array[otherside];
    array[otherside] = array[i];
    array[i] = temp;
    
/* HASHTABLES - allows you to map a key to a value

Given two lists (A and B) of unique strings, write a program to determine if A is a subset of B. */
boolean isSubsetBruteForce(String[] bigger, String[] smaller)
  for (String s : smaller)
    boolean found = false;
    for (String b : bigger)
      if (s.equals(b)) //found element
        found = true;
        break;
      if (!found) //s wasn't found -> not subset
        return false;
    return true; //all elements found
    
/* Given a 2D Array of sales data where the first column is a product ID and the second column is the quantity, write a function to take this list of data
and return a 2D Array with the total sales for each product. */
>>> Input:
211, 4
262, 3
211, 5
>>> Output:
211, 9
262, 3
int [][] totalSales(int[][] data)
  Hashtable<Integer, Integer> hash =
    new Hashtable<Integer, Integer>();
  for (int i = 0; i < data.length; i++)
    int productId = data[i][0];
    int quantity = data[i][1];
    if (hash.containsKey(productId))
      quantity = quantity + hash.get(productId);
    hash.put(productId, quantity);
  //convert hashtable back to array
  int[][] totals = new int[hash.keySet().size()][2];
  int index = 0;
  for (int key : hash.keySet())
    totals[index][0] = key;
    totals[index][1] = hash.get(key);
    index = index + 1;
  return totals;

----
// Topics I will update later because it's not a priority for me right now:
// Trees
// Linked List
// Stack - data structure which defines a precise order for how elements must be inserted/removed
// Queue - FIFO instead of LIFO
// Algorithms - Merge Sort, Quick Sort, Insertion Sort, Bubble Sort
// Binary Search
// Graph Search
// Big O Notation
// Recursion

