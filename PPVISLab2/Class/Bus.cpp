#include "Bus.h"

bool Bus::startWork()
{
	return true;
}

Bus::Bus(std::string seriaNumber)
{
	this->seriaNumber = seriaNumber;
}

