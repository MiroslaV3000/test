#include "Security.h"

bool Security::work()
{
    return true;
}

Security::Security(std::string name, std::string salary, std::string age, std::string personalNumber)
{
	this->name = name;
	this->salary = salary;
	this->age = age;
	this->personalNumber = personalNumber;
}
