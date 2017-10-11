#include <iostream>
#include <math.h>

float TAU = M_PI*2;

int main()
{
  float d = 100;
  float r = d/2;
  float circumference = TAU * r;
  std::cout << "Circumference: " << circumference << "\n";
}
