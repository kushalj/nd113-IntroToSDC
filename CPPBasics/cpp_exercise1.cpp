#include <iostream>
#include <vector>
#include "./lib/print_generic.cpp"
#include "./lib/matrix_lib.cpp"
using namespace std;

// p = [0.2, 0.2, 0.2, 0.2, 0.2]
static const float p1[5] = {0.2, 0.2, 0.2, 0.2, 0.2};
vector<float> p (p1, p1 + sizeof(p1) / sizeof(p1[0]));

// world = ['green', 'red', 'red', 'green', 'green']
static const char world1[5] = {'g', 'r', 'r', 'g', 'g'};
vector<char> world (world1, world1 + sizeof(world1) / sizeof(world1[0]));

// measurements = ['red', 'green']
static const char m1[2] = {'r', 'g'};
vector<char> measurements (m1, m1 + sizeof(m1) / sizeof(m1[0]));

// motions = [1,1]
static const float motions1[2] = {1, 1};
vector<float> motions (motions1, motions1 + sizeof(motions1) / sizeof(motions1[0]));

// pHit = 0.6
float pHit = 0.6;

// pMiss = 0.2
float pMiss = 0.2;

// pExact = 0.8
float pExact = 0.8;

// pOvershoot = 0.1
float pOvershoot = 0.1;

// pUndershoot = 0.1
float pUndershoot = 0.1;

// 2D vector typedef
typedef vector< vector<int> > gridInt;
typedef vector< vector<float> > gridFloat;

// Z is sensed value ('r' or 'g')
vector<float> sense(vector<float> p, char Z);

// U is 'moves'
vector<float> move(vector<float> p, int U);


int main() {
  char Z = 'r';
  // p = sense(p, 'r');
  // printVector(p);
  // p = move(p, 1);
  // printVector(p);
  //
  for (int k = 0; k < measurements.size(); k++) {
    p = sense(p, measurements[k]);
    p = move(p, motions[k]);
  }

  printVector(p);
}

// Z is sensed value ('r' or 'g')
vector<float> sense(vector<float> p, char Z) {
  vector<float> q;
  for (int i = 0; i < p.size(); i++) {
    bool hit = (Z == world[i]);
    q.push_back(p[i] * (float(hit) * pHit + (1-float(hit)) * pMiss));
  }

  // normalise
  float sum = 0;
  for (auto& n : q)
    sum += n;

  for (int i = 0; i < q.size(); i++) {
    q[i] = q[i]/sum;
  }

  return q;
}



// U is 'moves'
vector<float> move(vector<float> p, int U) {
  vector<float> q;
  for (int i = 0; i < p.size(); i++) {
    int len = p.size();
    float s = pExact * p[(i-U) % len];
    s = s + pOvershoot * p[(i-U-1) % len];
    s = s + pUndershoot * p[(i-U+1) % len];
    q.push_back(s);
  }

  return q;
}
