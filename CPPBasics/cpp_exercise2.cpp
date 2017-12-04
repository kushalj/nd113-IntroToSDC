#include <iostream>
#include <vector>
#include "./lib/matrix_lib.h"
#include "./lib/print_generic.h"
using namespace std;


// // 2D vector typedef
// typedef vector< vector<int> > gridInt;
// typedef vector< vector<float> > gridFloat;



int main() {
  gridInt twoDVector1 (5, vector<int> (3, 2));
  gridInt twoDVector2 (5, vector<int> (3, 2));

  print(add2DVectors(twoDVector1, twoDVector2));
  print(transpose(twoDVector1));
  print(mul2DVectors( twoDVector1, transpose(twoDVector2)) );

  gridFloat twoDVector3 (5, vector<float> (3, 2));
  gridFloat twoDVector4 (5, vector<float> (3, 2));

  print(add2DVectors(twoDVector3, twoDVector4));
  print(transpose(twoDVector3));
  print(mul2DVectors( twoDVector3, transpose(twoDVector4)) );


}
