#pragma once
#include <string>
#include <iostream>
class Worker
{
public:
	
	virtual bool work() = 0;
	std::string getName(); 
	void setName(std::string name);
	std::string getSalary();
	void setSalary(std::string salary);
	std::string getAge();
	void setAge(std::string age);
	std::string getPersonalNumber();
	void setPersonalNumber(std::string personalNumber);
protected:

	std::string name;
	std::string salary;
	std::string age;
	std::string personalNumber;
	  
};

