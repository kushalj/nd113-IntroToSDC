#include <iostream>

int main() {

  // TODO: write a program that outputs whether a vehicle is a motorcycle,
  // 2-door coupe, 4-door car or a 5-door mini-van.
  // You should create a variable that holds the number of doors in the vehicle
  // A motorcycle would have doors = 0 for example.
  // Then use a switch statement to output to the terminal the kind of vehicle
  // you have

  char doors = 0;

  switch(doors) {
    case 0:
        std::cout << "motorbike" << std::endl;
        break;
    case 2:
        std::cout << "coupe" << std::endl;
        break;
    case 4:
        std::cout << "car" << std::endl;
        break;
    case 5:
        std::cout << "minivan" << std::endl;
  }

  return 0;
}
