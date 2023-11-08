#include "Pilot.h"

bool Pilot::work()
{
    return true;
}

Pilot::Pilot(std::string name, std::string salary, std::string age, std::string personalNumber)
{
	this->name = name;
	this->salary = salary;
	this->age = age;
	this->personalNumber = personalNumber;
}
