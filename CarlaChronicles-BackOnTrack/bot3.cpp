#include <iostream>
#include <iomanip>
#include <math.h>
#include <vector>
// #include "mymath.cpp" // Tau not pi


static float a_lat(float v, float r)
{
  return pow(v,2.0f) / r;
}

int main()
{
  float v = 30;
  std::vector<float> radii = {50, 31.4f, 75, 16};
  for (auto r : radii) {
    std::cout << "a_lat for radius " << r << ": ";
    std::cout << a_lat(v, r) << "\n";
  }
}
