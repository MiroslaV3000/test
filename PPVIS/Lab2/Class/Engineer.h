#pragma once
#include "Worker.h"
class Engineer : public Worker
{
public:
	 bool work() override;
	 Engineer(std::string name, std::string salary, std::string age, std::string  personalNumber);
};

