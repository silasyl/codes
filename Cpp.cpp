// C++

#include <iostream> //header file library
#include <string> // Include the string library
#include <cmath> // Include the cmath library

using namespace std; //names from standard library

// Create a function
// Function declaration
void myFunction();

// default parameter
void myFunction2(string country = "Norway") {
  cout << country << "\n";
}

// Function overload
int plusFunc(int x, int y) {
  return x + y;
}

double plusFunc(double x, double y) {
  return x + y;
}


int main() {
	// Variables
	const int constNum = 1; // readable only
	int numInteger;
	double numDouble = 1.1;
	char varCharacter = 'a';
	string varString = "AAA";
	bool boolean = true;

	cout << "Hello World!" << constNum << " Other text";
	cout << "Type a number: ";
	cint >> numInteger;

	// Strings:
	string varString2 = varString + "BBB";
	varString2 = varString.append("CCC"); // append() is faster
	varString.length(); // return length
	varString.size(); // same as length
	getline(cin, varString2); // accept space as input

	// Omitting Namespace
	std::string varString3 = "a";
	std::cout << varString3;

	// C++ Math
	cout << max(5, 10); // return max value
	cout << min(5, 10); // return min value
	
	// <cmath> Header
	cout << sqrt(64); // square root
	cout << round(2.6); // round
	cout << log(2); // natural logarithm
	cout << abs(1); // absolute value

	// if
	int time = 22;
	if (time < 10) {
		cout << "Good morning.";
	} else if (time < 20) {
		cout << "Good day.";
	} else {
		cout << "Good evening.";
	}
	string result = (time < 18) ? "Good day." : "Good evening."; // ternary operator

	// switch
	int day = 1;
	switch (day) {
		case 1:
			cout << "Monday";
			break;
		case 2:
			cout << "Tuesday";
			break;
		default:
    	cout << "Sunday";
	}

	// while
	int i = 0;
	while (i < 5) {
		cout << i << "\n";
		i++;
	}

	// for
	for (int i = 0; i < 5; i++) {
		cout << i << "\n";
	}

	// array
	string cars[] = {"Volvo", "BMW", "Ford"}; // will have only 3 spaces
	string cars[4];
	string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};
	int myNum[3] = {10, 20, 30};

	// reference
	string food = "Pizza";  // food variable
	string &meal = food;    // reference to food
	cout << &food; // Outputs memory address 0x6dfed4

	// Pointer
	string food = "Pizza";  // A food variable of type string
	string* ptr = &food;    // A pointer variable, with the name ptr, that stores the address of food

	// Reference: Output the memory address of food with the pointer (0x6dfed4)
	cout << ptr << "\n";
	// Dereference: Output the value of food with the pointer (Pizza)
	cout << *ptr << "\n";

	// Function
	myFunction(); // call the function

  return 0;
}

// Function definition
void myFunction() {
  cout << "I just got executed!";
}