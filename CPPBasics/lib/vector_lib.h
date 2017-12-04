#include <iostream>
#include <vector>
using namespace std;

// need a solution for this:
// static const int array1[3] = {5, 10, 27};
// vector<int> v1 (array1, array1 + sizeof(array1) / sizeof(array1[0]));

// print
// int
void printVector(vector<int> vector);
// float
void printVector(vector<float> vector);

int sumVector(vector<int> vectorA);
float sumVector(vector<float> vectorA);

// add
// int
vector<int> addVectors(vector<int> vectorA, vector<int> vectorB);
// float
vector<float> addVectors(vector<float> vectorA, vector<float> vectorB);
// A - B (take vectorB from vectorA)
// int
vector<int> subVectors(vector<int> vectorA, vector<int> vectorB);

// float
vector<float> subVectors(vector<float> vectorA, vector<float> vectorB);


// diffVectors
// int
vector<int> diffVectors(vector<int> vectorA, vector<int> vectorB);

// float
vector<float> diffVectors(vector<float> vectorA, vector<float> vectorB);


// multiply
// int
vector<int> mulVectors(vector<int> vectorA, vector<int> vectorB);
// float
vector<float> mulVectors(vector<float> vectorA, vector<float> vectorB);
