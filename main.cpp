//***************************************************
// Name			: Nicholas Warner
// Date			: 10 April 2016
// Subject		: CSCE 452
// Assignment	: Project 4
// Updated		: 12 April 2016
// Description	: Linear Algebra behind Braitenberg
//				  Vehicles
//***************************************************

// compile with: g++ -std=c++11 main.cpp -o out

#include <iostream>
#include <string>
#include <vector>
#include "lightSource.h"
#include "BraitenbergVehicle.h"

using namespace std;

int main( int argc, char const *argv[] )
{
	int numberVehicles;
	int numberLights;

	vector<double> wheel = {1,1};
	vector<double> sensor = {10,10};
	vector<vector<double> > body = {{1,1}, {1,2}, {2,1}, {2,2}};
	vector<BraitenbergVehicle*> vehicles;
	vector<lightSource*> lights;


	cout << "# vehicles: ";
	cin >> numberVehicles;
	cout << "# lights: ";
	cin >> numberLights;

	for ( int i = 0; i < numberVehicles; ++i )
		vehicles.push_back( new BraitenbergVehicle( i, 2, {i*1.0,i*2.0}, {4.0*i,5.0*i}, {{1.0*i,1.0*i}, {1.0*i,2.0*i}, {2.0*i,1.0*i}, {2.0*i,2.0*i}} ) );

	for (int j = 0; j < numberLights; ++j)
		lights.push_back( new lightSource( j, j*2.5, j*3, j*8) );

	for (int k = 0; k < vehicles.size(); ++k)
	{
		vehicles[k]->printVehicle();
		cout << "\n";
	}

	for (int l = 0; l < lights.size(); ++l)
	{
		lights[l]->printLight();
		cout << "\n";
	}

	// BraitenbergVehicle bob( 1, 2, wheel, sensor, body );

	// bob.printBody();
	// bob.move1();
	// cout << "\n\n";
	// bob.printBody();

	return 0;
}
