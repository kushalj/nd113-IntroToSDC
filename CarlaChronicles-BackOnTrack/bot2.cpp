#include <iostream>
#include <iomanip>
#include <math.h>
#include "mymath.cpp" // Tau not pi


static float getDiameter(float distBeforeTurn, float distAfterTurn)
{
  float circumference = distAfterTurn - distBeforeTurn;
  float diameter = 2.0f * (circumference / TAU);
  return diameter;
}

int main()
{
  std::cout << std::fixed;
  std::cout << "Diameter: ";
  std::cout << std::setprecision(16) << getDiameter(1.0f, 6.0f) << "\n";
}
