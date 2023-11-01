#pragma once
#include <string>
#include <vector>
#include <iostream>
#include "GroundTransport.h"
#include "Airplane.h"
#include "Worker.h"

class Airline
{

public:
	Airline(std::string name);
	void renameAirline(std::string name);
	std::vector<Airplane*> getAirplanes();
	std::vector<Worker*> getWorkers();
	std::vector<GroundTransport*> getGroundTransports();
	void addAirpalne(Airplane * airplane);
	void addWorker(Worker * worker);
	void addGroundTransport(GroundTransport * groundTransport);
	void deleteAirplane(std::string bortNumber);
	void deleteWorker(std::string personalNumber);
	void deleteGroundTransport(std::string seriaNumber); 
	std::string getName();

private:
	std::vector<GroundTransport*> groundTransports;
	std::vector<Airplane*> airplanes;
	std::vector<Worker*> workers;
	std::string name;
};

