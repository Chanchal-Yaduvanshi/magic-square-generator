def odd_magic_square(n) :
    
    magicSquare = []
    for i in range(n):
        l = [] #making an empty list to add elements of the matrix
        for j in range(n):
            l.append(0) #assigning all elements to zero
        magicSquare.append(l) #adding the list l elements to magicSquare list
    i = n//2
    j = n-1
    
    num = n*n
    count = 1
    
    while(count<=num):
        if(i==-1 and j==n): #condn 4
            j = n-2
            i = 0
        else:
            if(j==n): #column exceeding value
                j = 0 
            if(i<0): #row becoming -1
                i = n-1
        if(magicSquare[i][j]!=0):          #already contains a num
            j = j-2
            i = i+1
            continue
        else:
            magicSquare[i][j] = count
            count+=1
        i = i-1
        j = j+1         #condn 1
        
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()
    
    print("The sum of each row/column/diagonal is : " + str(n*(n*n+1)/2))


def even_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    num = 1
    
    # Start position for 1 is at the middle of the first row
    i, j = 0, n // 2
    
    for num in range(1, n*n + 1):
        magic_square[i][j] = num
        
        # Move up and right
        i -= 1
        j += 1
        
        # Check for out-of-bounds and wrap around
        if i < 0 and j >= n:
            i += 2
            j -= 1
        elif i < 0:
            i = n - 1
        elif j >= n:
            j = 0
        elif magic_square[i][j] != 0:  # If cell is already filled, move down one cell
            i += 2
            j -= 1
    
    return magic_square


n = int(input("Enter the order of the matrix: "))    
if n%2 == 0:
    magic_square_4x4 = even_magic_square(n)
    for row in magic_square_4x4:
       print(row)
    print("The sum of each row/column/diagonal is : " + str(n*(n*n+1)/2))
else :
    odd_magic_square(n)


