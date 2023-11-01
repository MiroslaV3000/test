#pragma once
#include "Worker.h"
class Security : public Worker
{
public:

	 bool work() override;
	 Security(std::string name, std::string salary, std::string age, std::string  personalNumber);
};

