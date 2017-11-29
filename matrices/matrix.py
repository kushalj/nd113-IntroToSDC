import math
from math import sqrt
import numbers
# import pdb


def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)


def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################


    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")

        determinant = 0
        # TODO - your code here
        if self.h == 1:
            determinant = abs(self.g[0][0])

        elif self.h ==2:
            #[a b]^-1
            #[c d]

            #=

            #1/(ad-bc) *
            #[d -b]
            #[-c a]

            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]

            determinant = (a*d - b*c)

        return determinant


    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        t = 0
        for i in range(self.h):
            t += self.g[i][i]

        return t


    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")


        # TODO - your code here
        inverse = []
        inverse_determinant = 1/self.determinant()

        if self.h == 1:
            inverse.append([inverse_determinant])

        # 2x2: A^−1 = 1/det(A) * [(tr A)I−A]
        elif self.h ==2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            traceAI_minusA = [ [d, -b],
                               [-c, a] ]


            # iterate over traceAI_minusA and multiply inverse determinant
            for i in range(len(traceAI_minusA)):
                row = []
                for j in range(len(traceAI_minusA[i])):
                    row.append(inverse_determinant * traceAI_minusA[i][j])
                inverse.append(row)

        return Matrix(inverse)


    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        new_matrix = [[ self.g[j][i] for j in range(self.h) ] for i in range(self.w) ]

        return Matrix(new_matrix)


    def is_square(self):
        return self.h == self.w


    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
        #
        # TODO - your code here
        #
        m = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] + other.g[i][j])

            m.append(row)

        return Matrix(m)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #
        # TODO - your code here
        #
        g = [[-self.g[i][j] for i in range(self.h)] for j in range(self.w)]

        return Matrix(g)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #
        # TODO - your code here
        #
        m = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
#                 pdb.set_trace()
                row.append(self.g[i][j] - other.g[i][j])

            m.append(row)

        return Matrix(m)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #
        # TODO - your code here
        #


        product = []
        other_T = other.T()
        for i in range(self.h):
            row = []
            for j in range(other_T.h):
                vector_product = [self.g[i][k]*other_T.g[j][k] for k in range(self.w)]
                dp = sum(vector_product)
                row.append(dp)
            product.append(row)

        return Matrix(product)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        m = []
        if isinstance(other, numbers.Number):
            pass
            #
            # TODO - your code here
            #
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(self.g[i][j] * other)

                m.append(row)

        return Matrix(m)
