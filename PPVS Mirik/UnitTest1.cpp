



#include "pch.h"
#include "CppUnitTest.h"
#include "..\ppvis1\Vector.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
	TEST_CLASS(UnitTest1)
	{
	public:
		
		TEST_METHOD(Constructortest)
		{
			Vector f(1,2,3,4,5,6);
			float x0, y0, z0, x, y, z;
			f.getHome(x0, y0, z0);
			f.getEnd(x, y, z);
			Assert::IsTrue(x0==1);
			Assert::IsTrue(y0 == 2);
			Assert::IsTrue(z0 == 3);
			Assert::IsTrue(x == 4);
			Assert::IsTrue(y == 5);
			Assert::IsTrue(z == 6);
		}
		TEST_METHOD(Size)
		{
			Vector f(2, 3, 5, 4, 5, 6);
			
			Assert::IsTrue(f.size() == 3 );
			
		}
		TEST_METHOD(opperator1)
		{
			Vector f(2, 3, 5, 4, 5, 6);
			Vector g(1, 1, 1, 4, 5, 6);

			Assert::IsTrue(f<g);

		}
		TEST_METHOD(opperator2)
		{
			Vector f(2, 3, 5, 4, 5, 6);
			Vector g(1, 1, 1, 4, 5, 6);

			Assert::IsTrue(g>f);

		}
		TEST_METHOD(opperator3)
		{
			Vector f(2, 3, 5, 4, 5, 6);
			Vector g(1, 1, 1, 4, 5, 6);
			Vector c(1, 1, 1, 4, 5, 6);
			Assert::IsTrue(f <= g);
			Assert::IsTrue(c <= g);

		}
		TEST_METHOD(opperator4)
		{
			Vector f(2, 3, 5, 4, 5, 6);
			Vector g(1, 1, 1, 4, 5, 6);
			Vector c(1, 1, 1, 4, 5, 6);

			Assert::IsTrue(g > f);
			Assert::IsTrue(g >= f);

		}
		TEST_METHOD(opperator5)
		{
			Vector f(2, 3, 5, 4, 5, 6);
			Vector g(1, 1, 1, 4, 5, 6);
			Vector c = f + g;
			float x0, y0, z0, x, y, z;
			c.getHome(x0, y0, z0);
			c.getEnd(x, y, z);
			Assert::IsTrue(x0 == 3);
			Assert::IsTrue(y0 == 4);
			Assert::IsTrue(z0 == 6);
			Assert::IsTrue(x == 8);
			Assert::IsTrue(y == 10);
			Assert::IsTrue(z == 12);

		}
		TEST_METHOD(opperator6)
		{
			Vector f(2, 3, 5, 4, 5, 6);
			Vector g(1, 1, 1, 4, 5, 6);
			f += g;
			float x0, y0, z0, x, y, z;
			f.getHome(x0, y0, z0);
			f.getEnd(x, y, z);
			Assert::IsTrue(x0 == 3);
			Assert::IsTrue(y0 == 4);
			Assert::IsTrue(z0 == 6);
			Assert::IsTrue(x == 8);
			Assert::IsTrue(y == 10);
			Assert::IsTrue(z == 12);

		}
		TEST_METHOD(opperator7)
		{
			Vector f(2, 3, 5, 4, 5, 6);
			Vector g(1, 1, 1, 4, 5, 6);
			Vector c = f - g;
			float x0, y0, z0, x, y, z;
			c.getHome(x0, y0, z0);
			c.getEnd(x, y, z);
			Assert::IsTrue(x0 == 1);
			Assert::IsTrue(y0 == 2);
			Assert::IsTrue(z0 == 4);
			Assert::IsTrue(x == 0);
			Assert::IsTrue(y == 0);
			Assert::IsTrue(z == 0);
		}
		TEST_METHOD(opperator8)
		{
			Vector f(2, 3, 5, 4, 5, 6);
			Vector g(1, 1, 1, 4, 5, 6);
			float c;
			c = f * g;
			c = 19;
		}
		TEST_METHOD(opperator9)
		{
			Vector f(2, 3, 5, 4, 5, 6);
			Vector c = f * 5;
			float x0, y0, z0, x, y, z;
			c.getHome(x0, y0, z0);
			c.getEnd(x, y, z);
			Assert::IsTrue(x0 == 2);
			Assert::IsTrue(y0 == 3);
			Assert::IsTrue(z0 == 5);
			Assert::IsTrue(x == 4*5);
			Assert::IsTrue(y == 5*5);
			Assert::IsTrue(z == 6*5);
			
		}
		TEST_METHOD(opperator10)
		{
			Vector f(2, 3, 5, 4, 5, 6);
			f *= 5;
			float x0, y0, z0, x, y, z;
			f.getHome(x0, y0, z0);
			f.getEnd(x, y, z);
			Assert::IsTrue(x0 == 2);
			Assert::IsTrue(y0 == 3);
			Assert::IsTrue(z0 == 5);
			Assert::IsTrue(x == 4 * 5);
			Assert::IsTrue(y == 5 * 5);
			Assert::IsTrue(z == 6 * 5);

		}
		TEST_METHOD(opperator11)
		{
			Vector f(0, 0, 0, 0, 0, 1);
			Vector g(0, 0, 0, 1, 1, 0);
			float c = f ^ g;
			
			Assert::IsTrue(c == 0);

		}
		
	};
}
