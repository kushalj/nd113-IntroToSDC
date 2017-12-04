#include <iostream>
#include <vector>
using namespace std;

// need a solution for this:
static const int array1[3] = {5, 10, 27};
vector<int> v1 (array1, array1 + sizeof(array1) / sizeof(array1[0]));

// print
// int
void printVector(vector<int> vector) {
  for (int i=0; i < vector.size(); i++) {
    cout << vector[i] << " ";
  }
  cout << endl;
}

// float
void printVector(vector<float> vector) {
  for (int i=0; i < vector.size(); i++) {
    cout << vector[i] << " ";
  }
  cout << endl;
}


int sumVector(vector<int> vectorA) {
  int sum = 0;
  for (auto& n : vectorA)
    sum += n;

  return sum;
}

float sumVector(vector<float> vectorA) {
  float sum = 0;
  for (auto& n : vectorA)
    sum += n;

  return sum;
}


// add
// int
vector<int> addVectors(vector<int> vectorA, vector<int> vectorB) {
  vector<int> vector_sum (vectorA.size());
  for (int i = 0; i < vectorA.size(); i++) {
    vector_sum[i] = vectorA[i] + vectorB[i];
  }

  return vector_sum;
}

// float
vector<float> addVectors(vector<float> vectorA, vector<float> vectorB) {
  vector<float> vector_sum (vectorA.size());
  for (int i = 0; i < vectorA.size(); i++) {
    vector_sum[i] = vectorA[i] + vectorB[i];
  }

  return vector_sum;
}


// A - B (take vectorB from vectorA)
// int
vector<int> subVectors(vector<int> vectorA, vector<int> vectorB) {
  vector<int> vector_result (vectorA.size());
  for (int i = 0; i < vectorA.size(); i++) {
    vector_result[i] = vectorA[i] - vectorB[i];
  }

  return vector_result;
}

// float
vector<float> subVectors(vector<float> vectorA, vector<float> vectorB) {
  vector<float> vector_result (vectorA.size());
  for (int i = 0; i < vectorA.size(); i++) {
    vector_result[i] = vectorA[i] - vectorB[i];
  }

  return vector_result;
}


// diffVectors
// int
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

// float
vector<float> diffVectors(vector<float> vectorA, vector<float> vectorB) {
  vector<float> vector_result (vectorA.size());
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


// multiply
// int
vector<int> mulVectors(vector<int> vectorA, vector<int> vectorB) {
  vector<int> vector_result (vectorA.size());
  for (int i = 0; i < vectorA.size(); i++) {
    vector_result[i] = vectorA[i] * vectorB[i];
  }

  return vector_result;
}

// float
vector<float> mulVectors(vector<float> vectorA, vector<float> vectorB) {
  vector<float> vector_result (vectorA.size());
  for (int i = 0; i < vectorA.size(); i++) {
    vector_result[i] = vectorA[i] * vectorB[i];
  }

  return vector_result;
}
