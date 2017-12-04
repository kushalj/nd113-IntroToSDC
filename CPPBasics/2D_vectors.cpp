#include <iostream>
#include <vector>
// #include "vector_lib.cpp"
using namespace std;

//TODO: Write a function that receives two integer matrices and outputs
// the sum of the two matrices. Then in your main() function, input a few
// examples to check your solution. Output the results of your function to
// cout. You could even write a separate function that prints an arbitrarily
// sized matric to cout.

// 2D vector typedef
typedef vector< vector<int> > gridInt;

void printVector(vector<int> vector) {
  for (int i=0; i < vector.size(); i++) {
    cout << vector[i] << " ";
  }
  cout << endl;
}


vector<int> addVectors(vector<int> vectorA, vector<int> vectorB) {
  vector<int> vector_sum (vectorA.size());
  for (int i = 0; i < vectorA.size(); i++) {
    vector_sum[i] = vectorA[i] + vectorB[i];
  }

  return vector_sum;
}



/* 2D functions from here */

void print2DVector(gridInt twoDVector) {
  for (int row=0; row < twoDVector.size(); row++) {
    printVector(twoDVector[row]);
  }
}


gridInt add2DVectors(gridInt twoDV_A, gridInt twoDV_B) {
  gridInt new_grid;
  for (int row = 0; row < twoDV_A.size(); row++) {
    vector<int> new_row = addVectors(twoDV_A[row], twoDV_B[row]);
    new_grid.push_back(new_row);
  }
  return new_grid;
}


int main() {
  gridInt twoDVector1 (5, vector<int> (3, 2));
  gridInt twoDVector2 (5, vector<int> (3, 2));
  gridInt sum2DVectors = add2DVectors(twoDVector1, twoDVector2);
  print2DVector(sum2DVectors);
}
