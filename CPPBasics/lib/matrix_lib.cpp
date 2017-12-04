#include <iostream>
#include <vector>
#include "./vector_lib.h"
using namespace std;

// 2D vector typedef
typedef vector< vector<int> > gridInt;
typedef vector< vector<float> > gridFloat;


// print 2D
// [ [ int ] ]
void print2DVector(gridInt twoDVector) {
  for (int row=0; row < twoDVector.size(); row++) {
    printVector(twoDVector[row]);
  }
}

// [ [ float ] ]
void print2DVector(gridFloat twoDVector) {
  for (int row=0; row < twoDVector.size(); row++) {
    printVector(twoDVector[row]);
  }
}


// add 2D
// [ [ int ] ]
gridInt add2DVectors(gridInt twoDV_A, gridInt twoDV_B) {
  gridInt new_grid;
  for (int row = 0; row < twoDV_A.size(); row++) {
    vector<int> new_row = addVectors(twoDV_A[row], twoDV_B[row]);
    new_grid.push_back(new_row);
  }
  return new_grid;
}

// [ [ float ] ]
gridFloat add2DVectors(gridFloat twoDV_A, gridFloat twoDV_B) {
  gridFloat new_grid;
  for (int row = 0; row < twoDV_A.size(); row++) {
    vector<float> new_row = addVectors(twoDV_A[row], twoDV_B[row]);
    new_grid.push_back(new_row);
  }
  return new_grid;
}


gridInt transpose(gridInt grid) {
  int height = grid.size();
  int width = grid[0].size();
  int new_height = width;
  int new_width = height;
  gridInt new_grid;
  // build the new grid, row by row
  for (int row = 0; row < new_height; row++) {
    vector<int> new_row;
    for (int col = 0; col < new_width; col++) {
      // access original with reversed coords to transpose
      new_row.push_back(grid[col][row]);
    }
    new_grid.push_back(new_row);
  }

  return new_grid;
}

gridFloat transpose(gridFloat grid) {
  float height = grid.size();
  float width = grid[0].size();
  float new_height = width;
  float new_width = height;
  gridFloat new_grid;
  // build the new grid, row by row
  for (int row = 0; row < new_height; row++) {
    vector<float> new_row;
    for (int col = 0; col < new_width; col++) {
      // access original with reversed coords to transpose
      new_row.push_back(grid[col][row]);
    }
    new_grid.push_back(new_row);
  }

  return new_grid;
}


// multiply 2D
gridInt mul2DVectors(gridInt twoDV_A, gridInt twoDV_B) {
  // A = m X n, B = w X z. n must = w. out must be m X z
  int m = twoDV_A.size();
  int n = twoDV_A[0].size();
  int w = twoDV_B.size();
  int z = twoDV_B[0].size();

  if (n != w)
    throw std::invalid_argument( "Matrices cannot be multiplied." );

  gridInt B_T = transpose(twoDV_B);
  gridInt new_grid;
  for (int rowA = 0; rowA < twoDV_A.size(); rowA++) {
    vector<int> new_row;
    for (int rowB = 0; rowB < B_T.size(); rowB++) {
      vector<int> vector_product = mulVectors(twoDV_A[rowA], B_T[rowB]);
      // sum the new vector
      int vector_sum = sumVector(vector_product);
      // write the vector to the row
      new_row.push_back(vector_sum);
    }
    // write the new row to the new grid
    new_grid.push_back(new_row);
  }
  return new_grid;
}


// multiply 2D
gridFloat mul2DVectors(gridFloat twoDV_A, gridFloat twoDV_B) {
  // A = m X n, B = w X z. n must = w. out must be m X z
  float m = twoDV_A.size();
  float n = twoDV_A[0].size();
  float w = twoDV_B.size();
  float z = twoDV_B[0].size();

  if (n != w)
    throw std::invalid_argument( "Matrices cannot be multiplied." );

  gridFloat B_T = transpose(twoDV_B);
  gridFloat new_grid;
  for (int rowA = 0; rowA < twoDV_A.size(); rowA++) {
    vector<float> new_row;
    for (int rowB = 0; rowB < B_T.size(); rowB++) {
      vector<float> vector_product = mulVectors(twoDV_A[rowA], B_T[rowB]);
      // sum the new vector
      float vector_sum = sumVector(vector_product);
      // write the vector to the row
      new_row.push_back(vector_sum);
    }
    // write the new row to the new grid
    new_grid.push_back(new_row);
  }
  return new_grid;
}
