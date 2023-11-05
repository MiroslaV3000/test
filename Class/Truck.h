#pragma once
#include "GroundTransport.h"
class Truck : public GroundTransport
{
public:

	 bool startWork() override;
	 Truck(std::string seriaNumber);
};

