#pragma once
#include "Airplane.h"
class Boing777 : public Airplane
{
public:
	Boing777(std::string bortNumber);
	bool startEngine() override;
	bool release—hassis() override;
	bool startAuxiliarySystems() override;
};

