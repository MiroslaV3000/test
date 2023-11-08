#include "pch.h"
#include "CppUnitTest.h"
#include "../Lab2Piovis/Airline.h"
#include "../Lab2Piovis/Airplane.h"
#include "../Lab2Piovis/Boing737.h"
#include "../Lab2Piovis/Boing777.h"
#include "../Lab2Piovis/Bus.h"
#include "../Lab2Piovis/Engineer.h"
#include "../Lab2Piovis/GroundTransport.h"
#include "../Lab2Piovis/Pilot.h"
#include "../Lab2Piovis/Security.h"
#include "../Lab2Piovis/Truck.h"
#include "../Lab2Piovis/Worker.h"
#include <iostream>
#include <string>


using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace AirlineTests
{
	TEST_CLASS(AirlineTests)
	{
	public:
		
		TEST_METHOD(constructor)
		{
			Airline myCompany("BelAir");
			std::string rightAnswer = "BelAir";
			Assert::AreEqual(rightAnswer, myCompany.getName());
			

		}
		TEST_METHOD(renameAirline)
		{
			Airline myCompany("Air");
			myCompany.renameAirline("BelAir");
			std::string rightAnswer = "BelAir";
			Assert::AreEqual(rightAnswer, myCompany.getName());

		}
		TEST_METHOD(addAirpalne)
		{
			Airline myCompany("Air");
			Boing737 myBoing("123");
			myCompany.addAirpalne(&myBoing);
			size_t rightAnswer = 1;
			Assert::AreEqual(rightAnswer, myCompany.getAirplanes().size());

		}
		TEST_METHOD(addGroundTransport)
		{
			Airline myCompany("Air");
			Truck myTruck("123");
			myCompany.addGroundTransport(&myTruck);
			size_t rightAnswer = 1;
			Assert::AreEqual(rightAnswer, myCompany.getGroundTransports().size());

		}
		TEST_METHOD(addWorker)
		{
			Airline myCompany("Air");
			Pilot myPilot("123","e","d","d");
			myCompany.addWorker(&myPilot);
			size_t rightAnswer = 1;
			Assert::AreEqual(rightAnswer, myCompany.getWorkers().size());
		

		}
		TEST_METHOD(deleteWorker)
		{
			Airline myCompany("Air");
			Pilot myPilot("123", "e", "d", "d");
			myCompany.addWorker(&myPilot);
			myCompany.deleteWorker("d"); 
			size_t rightAnswer = 0;
			Assert::AreEqual(rightAnswer, myCompany.getWorkers().size());


		}
		TEST_METHOD(deleteAirplane)
		{
			Airline myCompany("Air");
			Boing777 myBoing("123");
			myCompany.addAirpalne(&myBoing);
			myCompany.deleteAirplane("123");
			size_t rightAnswer = 0;
			Assert::AreEqual(rightAnswer, myCompany.getWorkers().size());


		}
		TEST_METHOD(deleteGroundTransport)
		{
			Airline myCompany("Air");
			Bus myBus("123");
			myCompany.addGroundTransport(&myBus);
			myCompany.deleteGroundTransport("123");
			size_t rightAnswer = 0;
			Assert::AreEqual(rightAnswer, myCompany.getWorkers().size());


		}
	};
	TEST_CLASS(Boing737Testss)
	{
	public:

		TEST_METHOD(startAllSystems)
		{
			Boing737 myBoing("123");
			Assert::IsTrue(myBoing.startEngine());
			Assert::IsTrue(myBoing.startAuxiliarySystems());
			Assert::IsTrue(myBoing.releaseChassis());
		}
	};
	TEST_CLASS(Boing777Tests)
	{
	public:

		TEST_METHOD(startAllSystems)
		{
			Boing777 myBoing("123");
			Assert::IsTrue(myBoing.startEngine());
			Assert::IsTrue(myBoing.startAuxiliarySystems());
			Assert::IsTrue(myBoing.releaseChassis());
		}
	};
	TEST_CLASS(BusTests)
	{
	public:

		TEST_METHOD(startWork)
		{
			Bus myBus("123");
			Assert::IsTrue(myBus.startWork());
		}
	};
	TEST_CLASS(EngineerTests)
	{
	public:

		TEST_METHOD(work)
		{
			Engineer myEngineer("123", "e", "d", "d");
			Assert::IsTrue(myEngineer.work());
		}
	};
	TEST_CLASS(GroundTransportTests)
	{
	public:

		TEST_METHOD(setSeriaNumber)
		{
			Airline myCompany("Air");
			Bus myBus("123");
			myBus.setSeriaNumber("222");
			std::string rightAnswer = { "222" };
			Assert::AreEqual(rightAnswer, myBus.getSeriaNumber());

		}
	};
	TEST_CLASS(WorkerTests)
	{
	public:

		TEST_METHOD(AllSetters)
		{
			Engineer myEngineer("123", "e", "d", "d");
			myEngineer.setAge("22");
			myEngineer.setSalary("2123");
			myEngineer.setName("Grisha");
			myEngineer.setPersonalNumber("3");
			std::string rightAnswer = { "22" };
			Assert::AreEqual(rightAnswer, myEngineer.getAge());
			rightAnswer = { "2123" };
			Assert::AreEqual(rightAnswer, myEngineer.getSalary());
			rightAnswer = { "Grisha" };
			Assert::AreEqual(rightAnswer, myEngineer.getName());
			rightAnswer = { "3" };
			Assert::AreEqual(rightAnswer, myEngineer.getPersonalNumber());

		}
	};
	TEST_CLASS(PilotTests)
	{
	public:

		TEST_METHOD(work)
		{
			Pilot myPilot("123", "e", "d", "d");
			Assert::IsTrue(myPilot.work());
		}
	};
	TEST_CLASS(SecurityTests)
	{
	public:

		TEST_METHOD(work)
		{
			Security mySecurity("123", "e", "d", "d");
			Assert::IsTrue(mySecurity.work());
		}
	};
	TEST_CLASS(TruckTests)
	{
	public:

		TEST_METHOD(startWork)
		{
			Truck myTruck("123");
			Assert::IsTrue(myTruck.startWork());
		}
	};
	
}
