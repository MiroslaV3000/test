#pragma once
#include "Airplane.h"
class Boing737 : public Airplane
{   
	public:
	 Boing737(std::string bortNumber);
	 bool startEngine() override ;
	 bool releaseChassis() override;
	 bool startAuxiliarySystems() override;
};

