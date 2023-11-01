#pragma once
#include <string>
#include <iostream>

class Airplane
{
public:
	
	virtual bool startEngine() = 0;
	virtual bool release—hassis() = 0;
	virtual bool startAuxiliarySystems() = 0;
	std::string getBortNumber();
	void setBortNumber(std::string & bortNumber);
protected:
	std::string bortNumber;
};

