#include "Boing737.h"

Boing737::Boing737(std::string bortNumber)
{
	this->bortNumber = bortNumber;
}

bool Boing737::startEngine()
{
	return true;
}

bool Boing737::releaseChassis()
{
	return true;
}

bool Boing737::startAuxiliarySystems()
{
	return true;
}


