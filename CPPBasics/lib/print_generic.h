#include <vector>
using namespace std;

// 2D vector typedef
typedef vector< vector<int> > gridInt;
typedef vector< vector<float> > gridFloat;

void print(int val);
void print(float val);
void print(double val);
void print(char val);
void print(bool val);

// vector of ints
void print(vector<int> vector);
// vector of floats
void print(vector<float> vector);

// print 2D matrix
// [ [ int ] ]
void print(gridInt twoDVector);

// [ [ float ] ]
void print(gridFloat twoDVector);
