# Generic Matrices - Donna Bui - 4/14/2023 - Professor Henry Estrada's COMSC 078
# This program will add and multiply matrices and implement abstract methods into concrete subclasses for operations on specific types of matrices (Integer and Rational). 
# I modified the docstring comments under some of the methods based on how I interpreted the instructions on Canvas.

# For this program, I will assume that the following rules apply:
# 1. Only matrices with the same dimensions can be added.
#    E.g. A 3x2 matrix cannot add with a 2x3 matrix. A 3x3 matrix can add with a 3x3 matrix.

# 2. Matrices with differing dimensions can be multiplied as long as they meet the column/row equality requirement. They do not have to be equal in size/dimension.
#    E.g. A 3x2 matrix can multiply with a 2x3 matrix. Other functional combinations that will be tested in this program (in addition to the ones provided on Canvas) include 3x2 and 2x4, 3x3 and 3x2.
#    Using a*b and c*d to represent the dimensions of matrix 1 and matrix 2 respectively (in terms of row * column), the following conditions must be true:
#    b = c and a*d will equal the size of the result matrix after multiplying.

# 3. Only matrices of the same type will be added/multiplied with each other, 
#    E.g. An integer matrix will not be added/multiplied by a rational matrix

# 4. Matrices will only contain its designated type of number.
#    E.g. An integer matrix will not contain any rational numbers and vice versa.

from fractions import Fraction

class GenericMatrix(object):

    def __add__(self):
        """Returns a matrix object containing the resulting values after adding two matrices using __addMatrix__"""
        # This abstract method returns nothing as it will be overriden in a concrete subclass    

    def __mul__ (self):
        """Returns a matrix object containing the resulting values after multiplying two matrices using __multiplyMatrix__"""
        # This abstract method returns nothing as it will be overriden in a concrete subclass

    def __zero__(self):
        """Abstract method for defining the zero element for the type of matrix."""
        # The abstract method returns nothing as it will be overriden in the concrete subclass
    
    def __addMatrix__ (self, matrix2):
        """Adds two matrices with the same types of elements and returns a 2D list containing the resulting values."""
        # If the conditions are not met, it will print the problem and return nothing.
        if self.rows == matrix2.rows and self.columns == matrix2.columns: # If the two matrices have the exact same dimensions,
            if type(self) == type(matrix2): # And if both matrices are the same type,
            # We can also use type() on the elements themselves (assuming that rule #4 applies), for example: if type(self[0][0]) == type(matrix2[0][0]). However, just type(self) == type(matrix2) will suffice.
                result = [[self.__zero__()] * self.columns for r in range(self.rows)] # Create an empty matrix with the same dimensions.
                for r in range(self.rows):
                    for c in range(self.columns):
                        result[r][c] = self.values[r][c] + matrix2.values[r][c]
                        # Since all 3 matrices (result, self, and matrix2) have the same dimensions, we can just add the values together and assign them to the exact same index in the resulting matrix.
                return result
            
            else: print("Matrices are not compatible types.")
        else: print("The number of columns in matrix 1 is not equal to the number of rows in matrix 2.")
               
    def __multiplyMatrix__(self, matrix2):
        """Multiplies two matrices with the same types of elements and returns a 2D list containing the resulting values"""
        # If the conditions are not met, it will print the problem and return nothing.
        if self.columns == matrix2.rows: # If the two matrices meet the column/row equality requirement, 
            if type(self) == type(matrix2): # And if both matrices are the same type
            
                result = [[self.__zero__()] * matrix2.columns for r in range(self.rows)] # Create an empty matrix.
               # No matter what, the size of the resulting matrix will always be the number of rows in matrix1 times the number of columns in matrix2.
              
               # For multiplication part, use the given formula on Canvas: cij = ain × bnj 
               # result[i][j] += MatrixA[i][n] * MatrixB[n][j]
               # i = rows in MatrixA, j = columns in MatrixB, and n = columns in MatrixA = rows in MatrixB
               # I changed i and j to r and c in my code below but they still represent the same thing
                for r in range(self.rows): # For every row in matrix 1 - Gives us the index i of the row in matrix1
                    for c in range(matrix2.columns): # And for every corresponding column in matrix 2 - Gives us the index j of the column in matrix2
                        for rc in range(self.columns): # Gives us the index n of the column in matrix1 and/or row in matrix2.
                        # Alternatively, we can also use matrix2.rows as the range because of the column/row equality rule; both should be equal.
                            result[r][c] += self.values[r][rc] * matrix2.values[rc][c]
                return result # Since this method will be called by the __mul__ method, the concrete subclasses will handle which type of matrix to return
            # In this assignment, we have only Integer and Rational matrices, but this code can also work for other types of matrices,
            # such as irrational matrices or complex matrices, as long as their __mul__ method calls this __multiplyMatrix__ method and Python supports the multiplication operation for that number type.
            
            else: print("Matrices are not compatible types.")
        else: print("The number of columns in matrix 1 is not equal to the number of rows in matrix 2.")
        
    def __str__ (self):
        """Returns the string representation of a matrix"""
      # Instructions on Canvas said to return the string representation of the result, but the result is supposed to be a matrix itself, so this method also applies to all matrices.
        matrixValues = ""
        for r in range(self.rows):
            for c in range(self.columns):
                matrixValues += str(self.values[r][c]) + "\t"
            matrixValues += "\n"
        return "\n" + matrixValues
      
class IntegerMatrix(GenericMatrix): # Allows you to add and multiply the elements in an IntegerMatrix

    def __init__ (self, values): # Constructor
        self.values = values
        self.rows = len(values)
        self.columns = len(values[0])
        
    def __add__ (self, matrix2): 
        """Adds two integer matrices using the inherited __addMatrix__ method from GenericMatrices and returns an IntegerMatrix object containing the sum"""
        return IntegerMatrix(self.__addMatrix__(matrix2))
    
    def __mul__ (self, matrix2):
        """Multplies two integers using the inherited __multiplyMatrix__ method from GenericMatrices and returns an IntegerMatrix object containing the product"""
        return IntegerMatrix(self.__multiplyMatrix__(matrix2))  

    def __zero__(self):
        """Returns 0 for an integer matrix"""
        return 0

      

class RationalMatrix(GenericMatrix): # Allows you to add and multiply two elements in a RationalMatrix

    def __init__ (self, values): # Constructor [self.__zero__() * matrix2.columns for val in range(self.rows)] # Create an empty matrix.
        self.values = [[Fraction(element).limit_denominator() for element in row] for row in values] # This uses list comprehension to iterate through each element in the values list and turn it into a fraction. 
        self.rows = len(values)
        self.columns = len(values[0])

    def __add__(self, matrix2):
        """Add two Rational matrices using the inherited __addMatrix method__ and returns a RationalMatrix containing the sum"""
        return RationalMatrix(self.__addMatrix__(matrix2)) 

    def __mul__ (self, matrix2):
        """Multiply two Rational matrices using the inherited __multiplyMatrix__ method and returns a RationalMatrix containing the product"""
        return RationalMatrix(self.__multiplyMatrix__(matrix2))

    def __zero__(self):
        """Returns the zero for rational numbers (0/1)."""
        return Fraction(0/1)
      
      
      
def main(): # Driver method

    """m1 and m2 are the examples provided on Canvas"""
   
    m1_int = IntegerMatrix([[1, 2, 3],
                            [4, 5, 6],
                            [1, 1, 1,]])
    
    m2_int = IntegerMatrix([[1, 1, 1],
                            [2, 2, 2],
                            [0, 0, 0]])
    
    m1_rat = RationalMatrix([[1/5, 1/6, 1/7],
                             [2/5, 1/3, 2/7],
                             [3/5, 1/2, 3/7]])
    
    m2_rat = RationalMatrix([[1/6, 1/7, 1/8],
                             [1/3, 2/7, 1/4],
                             [1/2, 3/7, 3/8]])
    
    print("Adding IntegerMatrixes 1 and 2", m1_int + m2_int) # Python automatically calls self.__add__(matrix2) when using the + operator.
    print("Multiplying IntegerMatrix 1 and 2:", m1_int * m2_int) # It also automatically calls self.__mul__(matrix2) when using the * operator.
    print("Adding RationalMatrix 1 and 2:", m1_rat + m2_rat)
    print("Multiplying RationalMatrix 1 and 2:", m1_rat * m2_rat)
    
    
    """Adding will not be tested for the following matrices because they are not the same dimensions."""
    
    # m3 and m4 will be testing 3x2 and 2x4 matrix multiplication.
    # The values and expected output for m3_int and m4_int can be found here: https://www.basic-mathematics.com/multiply-matrices.html
    m3_int = IntegerMatrix([[1, 4],
                            [0, 1],
                            [-1, 0]])
    
    m4_int = IntegerMatrix([[4, 1, 2, 1],
                            [0, 1, -1, 3]])
    
    m3_rat = RationalMatrix([[1/5, 1/6],
                             [2/5, 1/3],
                             [3/5, 1/2]])
    
    m4_rat = RationalMatrix([[1/6, 1/7, 1/8, 1/2],
                             [1/3, 2/7, 1/4, 3/7]])
    
    # m5 and m6 will be testing 3x3 and 3x2 matrix multiplication.
    # The values and expected output for m5_int and m6_int can be found here: https://www.statology.org/matrix-multiplication-3x3-by-3x2/
    m5_int = IntegerMatrix([[-3, 5, 4],
                            [1, 2, 3],
                            [-1, 0, 2]])
    
    m6_int = IntegerMatrix([[2, 1],
                            [5, 1],
                            [0, -1]])
    
    # m5_rat and m6_rat use the values from Canvas, with one column being ommitted from m5_rat to make it 3x2. 
    # The output should be the same as m1_rat and m2_rat, except that the rightmost column is ommitted.  
    m5_rat = RationalMatrix([[1/5, 1/6, 1/7],
                             [2/5, 1/3, 2/7],
                             [3/5, 1/2, 3/7]])
    
    m6_rat = RationalMatrix([[1/6, 1/7],
                             [1/3, 2/7],
                             [1/2, 3/7]])
    
    print("Multiplying IntegerMatrix 3 and 4:", m3_int * m4_int)
    print("Multiplying RationalMatrix 3 and 4:", m3_rat * m4_rat)
    print("Multiplying IntegerMatrix 5 and 6:", m5_int * m6_int)
    print("Multiplying RationalMatrix 5 and 6:", m5_rat * m6_rat)
    
main()

'''
*Note that some IDEs may format \t (tab) differently.
**I use Thonny, and for my __str__ method, I used "\t" instead of space because it looks neater for me.
Expected Output:

Adding IntegerMatrixes 1 and 2 
2 3 4 
6 7 8 
1 1 1 

Multiplying IntegerMatrix 1 and 2: 
5 5 5 
14 14 14 
3 3 3 

Adding RationalMatrix 1 and 2: 
11/30 13/42 15/56 
11/15 13/21 15/28 
11/10 13/14 45/56 

Multiplying RationalMatrix 1 and 2: 
101/630 101/735 101/840 
101/315 202/735 101/420 
101/210 101/245 101/280 

Multiplying IntegerMatrix 3 and 4: 
 4   5 -2  13 
 0   1 -1  3 
-4  -1 -2 -1 

Multiplying RationalMatrix 3 and 4: 
4/45 8/105 1/15 6/35 
8/45 16/105 2/15 12/35 
4/15 8/35 1/5 18/35 

Multiplying IntegerMatrix 5 and 6: 
19 -2 
12 0 
-2 -3 

Multiplying RationalMatrix 5 and 6: 
101/630 101/735 
101/315 202/735 
101/210 101/245
'''