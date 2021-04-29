#include <iostream>
#include <fstream>
using namespace std;

class MyClass {       // The class
  public:             // Access specifier
    int myNum;        // Attribute (int variable)
    string myString;  // Attribute (string variable)
    void myMethod() {  // Method/function defined inside the class
    	cout << "Hello World!";
    }
};


class MyClass2 {        // The class
  public:              // Access specifier
    void myMethod();   // Method/function declaration
};

// Method/function definition outside the class
void MyClass2::myMethod() {
  cout << "Hello World!";
}


// Constructor
class MyClass {     // The class
  public:           // Access specifier
    MyClass() {     // Constructor
      cout << "Hello World!";
    }
};

// Constructor with parameters
class Car {        // The class
  public:          // Access specifier
    string brand;  // Attribute
    string model;  // Attribute
    int year;      // Attribute
    Car(string x, string y, int z) { // Constructor with parameters
      brand = x;
      model = y;
      year = z;
    }
};


class Car {        // The class
  public:          // Access specifier
    string brand;  // Attribute
    string model;  // Attribute
    int year;      // Attribute
    Car(string x, string y, int z); // Constructor declaration
};

// Constructor definition outside the class
Car::Car(string x, string y, int z) {
  brand = x;
  model = y;
  year = z;
}


class MyClass {
  public:    // Public access specifier
    int x;   // Public attribute
  private:   // Private access specifier
    int y;   // Private attribute
};


// Getters and setters
class Employee {
  private:
    // Private attribute
    int salary;

  public:
    // Setter
    void setSalary(int s) {
      salary = s;
    }
    // Getter
    int getSalary() {
      return salary;
    }
};


// Inheritance
// Base class
class Vehicle {
  public:
    string brand = "Ford";
    void honk() {
      cout << "Tuut, tuut! \n" ;
    }
};

// Derived class
class Car: public Vehicle {
  public:
    string model = "Mustang";
};


// Multiple inheritance
// Base class
class MyClass {
  public:
    void myFunction() {
      cout << "Some content in parent class." ;
    }
};

// Another base class
class MyOtherClass {
  public:
    void myOtherFunction() {
      cout << "Some content in another class." ;
    }
};

// Derived class
class MyChildClass: public MyClass, public MyOtherClass {
};


// Polimorphism
// Base class
class Animal {
  public:
    void animalSound() {
    cout << "The animal makes a sound \n" ;
  }
};

// Derived class
class Pig : public Animal {
  public:
    void animalSound() {
    cout << "The pig says: wee wee \n" ;
   }
};

// Derived class
class Dog : public Animal {
  public:
    void animalSound() {
    cout << "The dog says: bow wow \n" ;
  }
};




int main() {
	MyClass myObj;  // Create an object of MyClass

	// Access attributes and set values
  	myObj.myNum = 15; 
  	myObj.myString = "Some text";
  	myObj.myMethod();  // Call the method

  	// Print attribute values
  	cout << myObj.myNum << "\n";
  	cout << myObj.myString;

  	// Create Car objects and call the constructor with different values
  	Car carObj1("BMW", "X5", 1999);
  	Car carObj2("Ford", "Mustang", 1969);


  	// Files
  	// Create and open a text file
  	ofstream MyFile("filename.txt");

  	// Write to the file
  	MyFile << "Files can be tricky, but it is fun enough!";


  	// Create a text string, which is used to output the text file
	string myText;

	// Read from the text file
	ifstream MyReadFile("filename.txt");

	// Use a while loop together with the getline() function to read the file line by line
	while (getline (MyReadFile, myText)) {
  		// Output the text from the file
  		cout << myText;
	}

  	// Close the file
  	MyFile.close();

	return 0;
}