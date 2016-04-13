//***************************************************
// Name			: Nicholas Warner
// Date			: 10 April 2016
// Subject		: CSCE 452
// Assignment	: Project 4
// Updated		: 12 April 2016
// Description	: Vehicle class definition for
//				  Braintberg Vehicle Project
//***************************************************

#include <iostream>
#include <string>
#include <vector>

#include <GL/glut.h>

using namespace std;

//**************************************
//
//	(0,0) = (x = 0, y = 0)
//
//			|-  -|
// wheels = | w1 |
//			| w2 |
//			|-  -|
//
//			 |-  -|
// sensors = | s1 |
//			 | s2 |
//			 |-  -|
//
//			|--	   --|
// body = 	| k1, k2 |
//			| k3, k4 |
//			|--	   --|
//
//***************************************

class BraitenbergVehicle
{
private:
	int vehicle;
	int size;
	int x;
	int y;
	vector<double> w;			// wheels: w1, w2 -> (0,0), (0,0)
	vector<double> s;			// sensors: s1, s2 -> (0,0), (0,0)
	vector<int> k;		// body: k1, k2, k3, k4 -> ((0,0), (0,0), (0,0), (0,0))
						/*       k1---k2
						         |     |    k1.x = x1, k1.y = 1, k3.x = x2, k3.y = y2
						         k4---k3 */
									

							

public:
	BraitenbergVehicle( int id = 0, int s = 2,
						vector<double> wheel = {0,0}, vector<double> sensor = {0,0},
						vector<int> body = {0,0,0,0},
						int startX = 100, int startY = 100)
						: vehicle(id), size(s), w(wheel), s(sensor), k(body), x(startX), y(startY) {};


	void printBody();
	void printVehicle();
	vector<double> getWheels() { return w; };
	vector<double> getSensors() { return s; };
	int getVehicleID() { return vehicle; };
	void findW();
	void scaleW();
	void updateK();
	void updateWfromS(double s1, double s2 );
	void drawVehicle();

	//Setting variables post declaration
	void setID(int i){vehicle = i;}
	void setSize(int s){size = s;}
	void setX(int ex){x=ex;}
	void setY(int why){y=why;}
	void setWheelSpeed(int which, double speed){w[which] = speed;} //can pic which wheel and set speed for that wheel
	void setSensorInput(int which, double input){s[which] = input;}
	void setKMatrix(int k1, int value){ 
		if(value == 1 || value == 0){
			k[k1] = value;
		}
		else{
			cout << "Error in: k[" << k1 << "] = " <<  value << " This value is not binary\n";
			k[k1] = 0;
		}
	}

	int getX(){return x;}
	int getY(){return y;}
};


void BraitenbergVehicle::printVehicle()
{
	cout << "ID: " << vehicle << ", size: " << size << "\n";
	cout << "S1: " << s[0] << ", S2: " << s[1] << "\n";
	printBody();
}

void BraitenbergVehicle::printBody()
{
	for ( int i = 0; i < 4; ++i )
	{
		cout << k[i] << " ";
	}
	cout << endl;
}
/*
void BraitenbergVehicle::findW()
{
	// update body position k
	// wheel and sensor positions can be updated from this matrix point
	// multiply K by S for W
	double temp = 0.0;
	for ( int i = 0; i < 4; ++i )
	{
		for ( int j = 0; j < 2; ++j )
		{
			temp = k[i][j];
			if ( i < 2 )
				k[i][j] = temp * s[0];
			else
				k[i][j] = temp * s[1];
		}
	}
}*/

void BraitenbergVehicle::scaleW()
{
	w[0] = w[0] * s[0];
	w[1] = w[1] * s[1];
}

void BraitenbergVehicle::updateK()
{
	/* This is where the final pieace of magic happens.
		Figure this out, and we've got a moving bot we
		can just plot every refresh. 
	*/
}

void BraitenbergVehicle::updateWfromS( double s1, double s2 )
{
	s[0] = s1;
	s[1] = s2;
	scaleW();
}



void drawVehicle(){
	//Start with body
	glPushMatrix();
	//glRectd(k[0][0], k[0][1], k[2][0], k[2][1])
	glPopMatrix();
}






