#include <iostream>
#include <vector>
// #include "vector_lib.cpp"
using namespace std;

//TODO: Use this as a playground to practice with vectors


//TODO:
// Fill out your program's header. The header should contain any necessary
// include statements and also function declarations


//TODO:
// Write your main program. Remember that all C++ programs need
// a main function. The most important part of your program goes
// inside the main function.


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


// A - B (take vectorB from vectorA)
vector<int> subVectors(vector<int> vectorA, vector<int> vectorB) {
  vector<int> vector_result (vectorA.size());
  for (int i = 0; i < vectorA.size(); i++) {
    vector_result[i] = vectorA[i] - vectorB[i];
  }

  return vector_result;
}



vector<int> diffVectors(vector<int> vectorA, vector<int> vectorB) {
  vector<int> vector_result (vectorA.size());
  for (int i = 0; i < vectorA.size(); i++) {
    if (vectorA[i] > vectorB[i]) {
      vector_result[i] = vectorA[i] - vectorB[i];
    } else {
      // vectorB[i] is great than or equal to vectorA[i]
      vector_result[i] = vectorB[i] - vectorA[i];
    }

  }

  return vector_result;
}


vector<int> mulVectors(vector<int> vectorA, vector<int> vectorB) {
  vector<int> vector_result (vectorA.size());
  for (int i = 0; i < vectorA.size(); i++) {
    vector_result[i] = vectorA[i] * vectorB[i];
  }

  return vector_result;
}


int main() {
  static const int array1[3] = {5, 10, 27};
  static const int array2[3] = {3, 17, 12};
  vector<int> v1 (array1, array1 + sizeof(array1) / sizeof(array1[0]));
  vector<int> v2 (array2, array2 + sizeof(array2) / sizeof(array2[0]));

  printVector(v1);
  printVector(v2);

  printVector(addVectors(v1, v2));
  printVector(subVectors(v1, v2));
  printVector(subVectors(v2, v1));
  printVector(diffVectors(v2, v1));

  static const int array3[5] = {17, 10, 31, 5, 7};
  static const int array4[5] = {3, 1, 6, 19, 8};
  vector<int> v3 (array3, array3 + sizeof(array3) / sizeof(array3[0]));
  vector<int> v4 (array4, array4 + sizeof(array4) / sizeof(array4[0]));

  printVector(mulVectors(v3, v3));
}
