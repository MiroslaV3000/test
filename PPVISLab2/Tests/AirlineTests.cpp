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


using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace AirlineTests
{
	TEST_CLASS(AirlineTests)
	{
	public:
		
		TEST_METHOD(constructor)
		{
			Airline myCompany("BelAir");
			Assert::IsTrue(myCompany.getName() == "BelAir");

		}
		TEST_METHOD(renameAirline)
		{
			Airline myCompany("Air");
			myCompany.renameAirline("BelAir");
			Assert::IsTrue(myCompany.getName() == "BelAir");

		}
		TEST_METHOD(addAirpalne)
		{
			Airline myCompany("Air");
			Boing737 myBoing("123");
			myCompany.addAirpalne(&myBoing);
			Assert::IsTrue(myCompany.getAirplanes().size()==1);

		}
		TEST_METHOD(addGroundTransport)
		{
			Airline myCompany("Air");
			Truck myTruck("123");
			myCompany.addGroundTransport(&myTruck);
			Assert::IsTrue(myCompany.getGroundTransports().size() == 1);

		}
		TEST_METHOD(addWorker)
		{
			Airline myCompany("Air");
			Pilot myPilot("123","e","d","d");
			myCompany.addWorker(&myPilot);
			Assert::IsTrue(myCompany.getWorkers().size() == 1);
		

		}
		TEST_METHOD(deleteWorker)
		{
			Airline myCompany("Air");
			Pilot myPilot("123", "e", "d", "d");
			myCompany.addWorker(&myPilot);
			myCompany.deleteWorker("d");
			Assert::IsTrue(myCompany.getWorkers().size() == 0);


		}
		TEST_METHOD(deleteAirplane)
		{
			Airline myCompany("Air");
			Boing777 myBoing("123");
			myCompany.addAirpalne(&myBoing);
			myCompany.deleteAirplane("123");
			Assert::IsTrue(myCompany.getWorkers().size() == 0);


		}
		TEST_METHOD(deleteGroundTransport)
		{
			Airline myCompany("Air");
			Bus myBus("123");
			myCompany.addGroundTransport(&myBus);
			myCompany.deleteGroundTransport("123");
			Assert::IsTrue(myCompany.getWorkers().size() == 0);


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
			Assert::IsTrue(myBoing.release—hassis());
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
			Assert::IsTrue(myBoing.release—hassis());
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
			Assert::IsTrue(myBus.getSeriaNumber()=="222");

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

			Assert::IsTrue(myEngineer.getAge()=="22");
			Assert::IsTrue(myEngineer.getSalary() == "2123");
			Assert::IsTrue(myEngineer.getName() == "Grisha");
			Assert::IsTrue(myEngineer.getPersonalNumber() == "3");

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
