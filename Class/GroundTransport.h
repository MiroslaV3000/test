#pragma once
#include <string>
#include <iostream>
class GroundTransport
{
public:
	virtual bool startWork() = 0;
	std::string getSeriaNumber();
	void setSeriaNumber(std::string seriaNumber);
protected:
	std::string seriaNumber;
	
	
};

