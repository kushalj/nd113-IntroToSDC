#include <iostream>
#include <vector>
using namespace std;

// 2D vector typedef
typedef vector< vector<int> > gridInt;
typedef vector< vector<float> > gridFloat;


// print 2D
// [ [ int ] ]
void print2DVector(gridInt twoDVector);

// [ [ float ] ]
void print2DVector(gridFloat twoDVector);


// add 2D
// [ [ int ] ]
gridInt add2DVectors(gridInt twoDV_A, gridInt twoDV_B);

// [ [ float ] ]
gridFloat add2DVectors(gridFloat twoDV_A, gridFloat twoDV_B);


gridInt transpose(gridInt grid);
gridFloat transpose(gridFloat grid);


// multiply 2D
gridInt mul2DVectors(gridInt twoDV_A, gridInt twoDV_B);
gridFloat mul2DVectors(gridFloat twoDV_A, gridFloat twoDV_B);
