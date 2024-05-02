# magic-square-generator
This Python script generates a magic square of order n and displays it along with the sum of each row, column, and diagonal.

**What is a Magic Square?**
A magic square is a square grid filled with distinct positive integers in the range 1,2,3,....,n^2 , where the sum of numbers in each row, column, and diagonal is the same.

**How it Computes:**
Initializes an empty square grid to store the magic square matrix.
Constructs a square grid of size n×n and fills it with zeros.
Iterates through each cell, by handlling conditions.
Prints the constructed magic square matrix.
Calculates and prints the sum of each row, column, and diagonal, ensuring they are equal in a magic square

Magic number = n(n^2 +1)/2

**Magic Square Specified Rules:**
1. In any magic square, 1 is located at position (n/2 , n-1) say(p,q)
2. Next number which is 2 located at (p-1, q+1) 
   If calculated row position becomes -1 then make it n-1 and if column position becomes n then make it 0.
3. If calculated position already contains a number then decrement the column by 2 and increment the row by 1.
4. If anytime row position becomes -1 and column becomes n, switch it to (0,n-2)

Example - 
Magic square of size 3
2 7 6
9 5 1
4 3 8

The sum of each row/column/diagonal is: 15.0

Enjoy generating and exploring magic squares of different orders!
