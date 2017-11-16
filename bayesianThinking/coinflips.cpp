#include <iostream>
//#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <math.h>
//#include <vector>
// #include "mymath.cpp" // Tau not pi

int main()
{

  int numTrials = 100000;
	int heads = 0;
	int tails = 0;
	float pHeads = 0.5;

  std::srand(std::time(0));
	for (int i = 1; i <= numTrials; i++) {
		float randomNumber = std::rand()/( static_cast< float >( RAND_MAX ) + 1.f );
		if (randomNumber < pHeads) {
			heads++;
		} else {
			tails++;
		}
	}
	std::cout << "In " << numTrials << " trials there were " << heads << " heads and " << tails << " tails\n";
	std::cout << "ERCENT HEADS: " <<
    100.f * static_cast< float >(heads) / static_cast< float >(numTrials) << " percent";

}
