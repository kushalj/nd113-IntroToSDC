#include <iostream>
#include <vector>
using namespace std;

// 2D vector typedef
typedef vector< vector<int> > gridInt;
typedef vector< vector<float> > gridFloat;

void print(int val) {
  cout << val << endl;
}

void print(float val) {
  cout << val << endl;
}

void print(double val) {
  cout << val << endl;
}

void print(char val) {
  cout << val << endl;
}

void print(bool val) {
  cout << val << endl;
}

// vector of ints
void print(vector<int> vector) {
  for (int i=0; i < vector.size(); i++) {
    cout << vector[i] << " ";
  }
  cout << endl;
}

// vector of floats
void print(vector<float> vector) {
  for (int i=0; i < vector.size(); i++) {
    cout << vector[i] << " ";
  }
  cout << endl;
}

// print 2D matrix
// [ [ int ] ]
void print(gridInt twoDVector) {
  for (int row=0; row < twoDVector.size(); row++) {
    print(twoDVector[row]);
  }
}

// [ [ float ] ]
void print(gridFloat twoDVector) {
  for (int row=0; row < twoDVector.size(); row++) {
    print(twoDVector[row]);
  }
}
