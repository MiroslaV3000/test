#include "Engineer.h"

bool Engineer::work()
{
	return true;
}

Engineer::Engineer(std::string name, std::string salary, std::string age, std::string personalNumber)
{
	this->name = name;
	this->salary = salary;
	this->age = age;
	this->personalNumber = personalNumber;
}
