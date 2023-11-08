#include "Vector.h"
#include <math.h>

Vector::Vector(float x0, float y0, float z0, float x, float y, float z)
{
	this->x0 = x0;
	this->x = x;
	this->y0 = y0;
	this->y = y;
	this->z0 = z0;
	this->z = z;
}

void Vector::setEndToVars(float& x, float& y, float& z)
{
	x =this->x;
	y = this->y;
	z = this->z;
}

void Vector::setHomeToVars(float& x0, float& y0, float& z0)
{
	x0 = this->x0;
	y0 = this->y0;
	z0 = this->z0;
}

float Vector::size()
{

	return sqrt(pow((x-x0), 2) + pow((y-y0), 2) + pow((z-z0), 2));
}


bool Vector::operator <( Vector& other)
{
	return this->size() < other.size();
}

bool Vector::operator>(Vector& other)
{
	return this->size() > other.size();
}

bool Vector::operator<=(Vector& other)
{
	return this->size() <= other.size();
}

bool Vector::operator>=(Vector& other)
{
	return this->size() >= other.size();
}

Vector Vector::operator+(Vector& other)
{
	Vector result(this->x0 + other.x0, this->y0 + other.y0, this->z0 + other.z0, this->x + other.x, this->y + other.y, this->z + other.z);
	return result;
}

void Vector::operator+=(Vector& other)
{
	this->x0 += other.x0;
	this->y0 += other.y0;
	this->z0 += other.z0;
	this->x += other.x;
	this->y += other.y;
	this->z += other.z;
}

Vector Vector::operator-(Vector& other)
{
	Vector result(this->x0-other.x0 , this->y0 - other.y0, this->z0 - other.z0, this->x - other.x, this->y- other.y, this->z - other.z);
	return result;
}

void Vector::operator-=(Vector& other)
{
	this->x0 -= other.x0;
	this->y0 -= other.y0;
	this->z0 -= other.z0;
	this->x -= other.x;
	this->y -= other.y;
	this->z -= other.z;
}

float Vector::operator*(Vector& other)
{
	return ((this->x - this->x0) * (other.x - other.x0) + (this->y - this->y0) * (other.y - other.y0) + (this->z - this->z) * (other.z - other.z0));
}

Vector Vector::operator*(float other)
{
	Vector result(this->x0, this->y0 , this->z0, this->x * other, this->y*other, this->z * other);
	return result;
}

void Vector::operator*=(float other)
{
	
	this->x *= other;
	this->y *= other;
	this->z *= other;
}

float Vector::operator^(Vector& other)
{
	return ((this->x - this->x0) * (other.x - other.x0) + (this->y - this->y0) * (other.y - other.y0) + (this->z - this->z) * (other.z - other.z0)) / (this->size() * other.size());
}


