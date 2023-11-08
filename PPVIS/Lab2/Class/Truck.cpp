#include "Truck.h"

bool Truck::startWork()
{
    return true;
}

Truck::Truck(std::string seriaNumber)
{
    this->seriaNumber = seriaNumber;
}
