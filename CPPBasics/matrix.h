#ifndef MATRIX_H
#define MATRIX_H

#include <vector>
#include <iostream>
#include <stdexcept>

typedef std::vector < std::vector <float> > gridFloat;
typedef std::vector <float> vectorFloat;
typedef std::vector <float>::size_type vectorSize;

class Matrix
{

        private:

            std::vector< std::vector<float> > grid;
            std::vector<float>::size_type rows;
            std::vector<float>::size_type cols;

        public:

        /*
        ** TODO: Declare  constructor functions
        ** For the matrix class, you will need two constructor functions.
        ** 1. An empty constructor function
        ** 2. A constructor function that accepts a 2-dimensional vector
        */

        Matrix();
        Matrix(gridFloat);

        /*
        ** TODO: Declare set and get functions for the three private variables.
        ** You will need 1 set function and 3 get functions.
        ** The names of these functions should be setGrid, getGrid, getRows,
        ** and getCols.
        **
        ** The setGrid does not return anything and has a 2-D vector input
        ** getGrid returns a 2-D vector and has no input
        ** getRows returns a size_type and has no input
        ** get Cols returns a size_type and has no input
        */

        // called with a grid sets the grid
        void setGrid(gridFloat);

        // called without a grid gets the current grid
        gridFloat getGrid();

        // get rows
        vectorSize getRows();

        // get cols
        vectorSize getCols();

        /*
        ** TODO: Declare the matrix functions. In a following exercise, you
        ** will program matrix_transpose, matrix_addition and matrix_print
        ** functions. So you will need to declare these two functions.
        **
        ** matrix_transpose has no input and outputs a 2D vector
        ** matrix_addition receives a Matrix and outputs a 2D vector
        ** matrix_print has no inputs and no outputs
        */

        Matrix matrix_transpose();
        Matrix matrix_addition(Matrix);

        void matrix_print();



};

#endif /* MATRIX */
