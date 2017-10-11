#include <iostream>
#include <iomanip>
#include <math.h>
#include "mymath.cpp" // Tau not pi


float getDiameter(float distBeforeTurn, float distAfterTurn)
{
  float circumference = distAfterTurn - distBeforeTurn;
  float diameter = 2 * (circumference / TAU);
  return diameter;
}

int main()
{
  std::cout << std::fixed;
  std::cout << "Diameter: ";
  std::cout << std::setprecision(16) << getDiameter(1.0, 6.0) << "\n";
}
