//***************************************************
// Name			: Nicholas Warner
// Date			: 12 April 2016
// Subject		: CSCE 452
// Assignment	: Project 4
// Updated		: 12 April 2016
// Description	: Light Source class definition for
//				  Braintberg Vehicle Project
//***************************************************

#include <iostream>
#include <string>
#include <vector>

#include <GL/glut.h>

using namespace std;

class lightSource
{
private:
	int id;
	double x;
	double y;
	double intensity;

public:
	lightSource( int ident, double xco, double yco, double power )
				: id(ident), x(xco), y(yco), intensity(power) {};

	void printLight();
	int getLightID() { return id; };
	double getLightX() { return x; };
	double getLightY() { return y; };
	void drawLightSource();
};

void lightSource::printLight()
{
	cout << "Light: " << id << ", (" << x << "," << y << "),\t" << intensity << " Lumens.";
}

