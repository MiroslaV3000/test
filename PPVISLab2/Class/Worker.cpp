#include "Worker.h"

std::string Worker::getName()
{
    return name;
}

void Worker::setName(std::string name)
{
    this->name = name;
}

std::string Worker::getSalary()
{
    return salary;
}

void Worker::setSalary(std::string salary)
{
    this->salary = salary;
}

std::string Worker::getAge()
{
    return age;
}

void Worker::setAge(std::string age)
{
    this->age = age;
}

std::string Worker::getPersonalNumber()
{
    return personalNumber;
}

void Worker::setPersonalNumber(std::string personalNumber)
{
    this->personalNumber = personalNumber;
}
