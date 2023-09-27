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
	
	
	void setEndToVars(float& x,float& y,float& z);
	void setHomeToVars(float& x0, float& y0, float& z0);
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
	Vector operator *(float other);
	void operator *=(float other);
	float operator ^(Vector& other);
};

