#pragma once
class Vector
{private:
	float x0;
	float y0;
	float z0;
	float x;
	float y;
	float z;
public:
	Vector(float x0 , float y0, float z0, float x , float y , float z );
	
	
	void getEnd(float& x,float& y,float& z);
	void getHome(float& x0, float& y0, float& z0);
	float size();
	bool operator <(Vector& other);
	bool operator >(Vector& other);
	bool operator <=(Vector& other);
	bool operator >=(Vector& other);
	Vector operator +(Vector& other);
	void operator +=(Vector& other);
	Vector operator -(Vector& other);
	void operator -=(Vector& other);
	float operator *(Vector& other);
	Vector operator *(float b);
	void operator *=(float b);
	float operator ^(Vector& other);
};

