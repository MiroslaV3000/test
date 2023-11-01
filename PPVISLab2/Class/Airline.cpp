#include "Airline.h"

Airline::Airline(std::string name)
{
	this->name = name;
}

void Airline::renameAirline(std::string name)
{
	this->name = name;
	
}

std::vector<Airplane*> Airline::getAirplanes()
{
	return airplanes;
}

std::vector<Worker*> Airline::getWorkers()
{
	return workers;
}

std::vector<GroundTransport*> Airline::getGroundTransports()
{
	return groundTransports;
}

void Airline::addAirpalne(Airplane* airplane)
{
	airplanes.push_back(airplane);
	
}

void Airline::addWorker(Worker* human)
{
	workers.push_back(human);
	
}

void Airline::addGroundTransport(GroundTransport* groundTransport)
{
	groundTransports.push_back(groundTransport);
	
}

void Airline::deleteAirplane(std::string bortNumber)
{
	int countAirplanes = airplanes.size();
	for (int i = 0; i < countAirplanes; i++)
	{
		if (airplanes[i]->getBortNumber() == bortNumber)
		{
			airplanes.erase(airplanes.begin() + i);
		}
	}
}

void Airline::deleteWorker(std::string personalNumber)
{
	int countHumans = workers.size();
	for (int i = 0; i < countHumans; i++)
	{
		if (workers[i]->getPersonalNumber() == personalNumber)
		{
			workers.erase(workers.begin() + i);
		}
	}
}

void Airline::deleteGroundTransport(std::string seriaNumber)
{
	int countGroundTransports = groundTransports.size();
	for (int i = 0; i < countGroundTransports; i++)
	{
		if (groundTransports[i]->getSeriaNumber() == seriaNumber)
		{
			groundTransports.erase(groundTransports.begin() + i);
		}
	}
}

std::string Airline::getName()
{
	return name;
}
