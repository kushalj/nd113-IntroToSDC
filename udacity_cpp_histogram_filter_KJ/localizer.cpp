/**
	localizer.cpp

	Purpose: implements a 2-dimensional histogram filter
	for a robot living on a colored cyclical grid by
	correctly implementing the "initialize_beliefs",
	"sense", and "move" functions.

	This file is incomplete! Your job is to make these
	functions work. Feel free to look at localizer.py
	for working implementations which are written in python.
*/

#include "helpers.cpp"
#include <stdlib.h>
#include "debugging_helpers.cpp"
using namespace std;

// define our types for clearer code
// a vector of chars
typedef vector <char> vectorChar;

// a grid of chars
typedef vector <vectorChar> gridChar;

// a vector of floats
typedef vector <float> vectorFloat;

// a grid of floats
typedef vector <vectorFloat> gridFloat;

// might not need this
// typedef vector <char>::size_type vectorChar;


/**
	TODO - implement this function

    Initializes a grid of beliefs to a uniform distribution.

    @param grid - a two dimensional grid map (vector of vectors
    	   of chars) representing the robot's world. For example:

    	   g g g
    	   g r g
    	   g g g

		   would be a 3x3 world where every cell is green except
		   for the center, which is red.

    @return - a normalized two dimensional grid of floats. For
           a 2x2 grid, for example, this would be:

           0.25 0.25
           0.25 0.25
*/
gridFloat initialize_beliefs(gridChar grid) {
	gridFloat beliefGrid;

	// your code here
	int height = grid.size();
	int width = grid[0].size();
	int area = float(height) * float(width);
	float belief_per_cell = 1.0/float(area);

	vectorFloat newRow;
	for (int row=0; row < height; row++) {
			newRow.clear();
			for (int col=0; col < width; col++) {
				newRow.push_back(belief_per_cell);
			}
			// append new row of beliefs
			beliefGrid.push_back(newRow);
	}

	return beliefGrid;
}

/**
	TODO - implement this function

    Implements robot sensing by updating beliefs based on the
    color of a sensor measurement

	@param color - the color the robot has sensed at its location

	@param grid - the current map of the world, stored as a grid
		   (vector of vectors of chars) where each char represents a
		   color. For example:

		   g g g
    	   g r g
    	   g g g

   	@param beliefs - a two dimensional grid of floats representing
   		   the robot's beliefs for each cell before sensing. For
   		   example, a robot which has almost certainly localized
   		   itself in a 2D world might have the following beliefs:

   		   0.01 0.98
   		   0.00 0.01

    @param p_hit - the RELATIVE probability that any "sense" is
    	   correct. The ratio of p_hit / p_miss indicates how many
    	   times MORE likely it is to have a correct "sense" than
    	   an incorrect one.

   	@param p_miss - the RELATIVE probability that any "sense" is
    	   incorrect. The ratio of p_hit / p_miss indicates how many
    	   times MORE likely it is to have a correct "sense" than
    	   an incorrect one.

    @return - a normalized two dimensional grid of floats
    	   representing the updated beliefs for the robot.
*/
gridFloat sense(char color,
	gridChar grid,
	gridFloat beliefs,
	float p_hit,
	float p_miss)
{
	gridFloat newGrid;
	// cout << newGrid[0].size() << ", "  << endl;
	// your code here
	int height = grid.size();
	int width = grid[0].size();

	vectorFloat newRow;
	char cell;
	float new_belief;
	for (int row=0; row < height; row++) {
			newRow.clear();
			for (int col=0; col < width; col++) {
				cell = beliefs[row][col];
				// compare color with world given
				bool hit = (color == grid[row][col]);

				// calc new belief
				new_belief = cell * (float(hit) * p_hit + (1-float(hit)) * p_miss);

				newRow.push_back(new_belief);
			}
			// append new row of beliefs
			newGrid.push_back(newRow);
	}

	return normalize(newGrid);
}


/**
	TODO - implement this function

    Implements robot motion by updating beliefs based on the
    intended dx and dy of the robot.

    For example, if a localized robot with the following beliefs

    0.00  0.00  0.00
    0.00  1.00  0.00
    0.00  0.00  0.00

    and dx and dy are both 1 and blurring is 0 (noiseless motion),
    than after calling this function the returned beliefs would be

    0.00  0.00  0.00
    0.00  0.00  0.00
    0.00  0.00  1.00

	@param dy - the intended change in y position of the robot

	@param dx - the intended change in x position of the robot

   	@param beliefs - a two dimensional grid of floats representing
   		   the robot's beliefs for each cell before sensing. For
   		   example, a robot which has almost certainly localized
   		   itself in a 2D world might have the following beliefs:

   		   0.01 0.98
   		   0.00 0.01

    @param blurring - A number representing how noisy robot motion
           is. If blurring = 0.0 then motion is noiseless.

    @return - a normalized two dimensional grid of floats
    	   representing the updated beliefs for the robot.
*/
gridFloat move(int dy, int dx,
	gridFloat beliefs,
	float blurring)
{

	gridFloat newGrid;

	// your code here
	int height = beliefs.size();
	int width = beliefs[0].size();

	// zero the new grid
	newGrid = gridFloat (height, vectorFloat (width, 0));
	int newRowPos;
	int newColPos;
	float cell;
	for (int row=0; row < height; row++) {
			for (int col=0; col < width; col++) {
				cell = beliefs[row][col];
				newRowPos = ((row + dy) % height + height) % height;
				newColPos = ((col + dx) % width + width) % width;
				newGrid[newRowPos][newColPos] = cell;
			}
	}

	return blur(newGrid, blurring);
}
