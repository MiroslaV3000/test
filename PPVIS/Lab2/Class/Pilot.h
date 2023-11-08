#pragma once
#include "Worker.h"
class Pilot : public Worker
{
public:

	 bool work() override;
	 Pilot(std::string name, std::string salary, std::string age, std::string  personalNumber);
};

