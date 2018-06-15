#importing the numpy library
import numpy as np

try:
    matrix=[]                                           #empty list.
    w=int(input("Enter the width of the Matrix: "))     #asking input for the width of the matrix.
    h=int(input("Enter the height of the Matrix: "))    #asking input for the height of the matrix.

    for i in range(h):
        rows=[]
        print("row {}\n".format(i+1))
        for j in range(w):
            rows.append(int(input("")))                 #inputting the matrix values here.
        print("\r")
        matrix.append(rows)
    m=np.asarray(matrix)                                #list is converted to a numpy array.
    print(m)                                            #printing the matrix.
    print("\n")

    #here the size of the square matrix is asked to enter
    size_of_square_matrix=int(input("Enter maximum width of square submatrix (height and width must be same): "))

    #Calculating the total number of possible square submatrices can be formed from the given matrix and the output matrix.
    no_of_square_matrices = ((w-size_of_square_matrix)+1)*((h-size_of_square_matrix)+1)
    print("Total Number of Square Matrices will be:",no_of_square_matrices)
    print("\n")
    sosm=size_of_square_matrix
    row=(h-size_of_square_matrix)+1                     #It is the number of rows it will cover to find out the desired output.
    column=(w-size_of_square_matrix)+1                  #It is the number of columns it will cover to find out the desired output.
    max_val=0                                           #maximum sum initialized as zero.
    for i in range(row):
        for j in range(column):
            sq = m[i:i+sosm,j:j+sosm]
            print(sq)
            sm=sq[1:sosm-1,1:sosm-1]
            if sosm < 3:
                    sum_of_boundary_elements = sq.sum()
            else:
                sum_of_boundary_elements = sq.sum()-sm.sum()

            if sum_of_boundary_elements > max_val:
                max_val = sum_of_boundary_elements
                output_matrix = sq
            print("\t")

    print("The Output Matrix will be: \n",output_matrix) #The output matrix will get printed on the screen.

except Exception as e:
    print("Invalid Input, Try again",str(e))
