#pragma once
#include "GroundTransport.h"
class Bus : public GroundTransport
{
public:

	 bool startWork() override;
	 Bus(std::string seriaNumber);
	 
};

