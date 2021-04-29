import java.util.Scanner;

public class Main {
  // Static method
  static void myStaticMethod() {
    System.out.println("Static methods can be called without creating objects");
  }

  // Public method
  public void myPublicMethod() {
    System.out.println("Public methods must be called by creating objects");
  }

  int x;  // Create a class attribute

  // Create a class constructor for the Main class
  public Main() {
    x = 5;  // Set the initial value for the class attribute x
  }

	public static void main(String[] args) {
		// Variables
		byte myByte = 100;
		short myShort = 5000;
		int myInt = 100000;
		long myLong = 15000000000L;
		float myFloat = 5.75f;
		double myDouble = 19.99d;
		boolean myBoolean = true;
		char myChar = 'a';
		String txt = "Hello World";
		final int myNum = 15; // constant

		System.out.println(txt.length()); // length
		System.out.println(txt.toUpperCase());   // Outputs "HELLO WORLD"
		System.out.println(txt.toLowerCase());   // Outputs "hello world"
		System.out.println(txt.indexOf("o")); // Outputs 4
		System.out.println(txt.concat("!!!")); // Concatenate

		// Math
		Math.max(5, 10);
		Math.min(5, 10);
		Math.sqrt(64);
		Math.abs(-4.7);
		Math.random();

		// if
		for (int i = 0; i <= 10; i = i + 2) {
			System.out.println(i);
		}

		String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
		for (String i : cars) {
			System.out.println(i);
		}

		// Arrays
		String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
		int[] myNum = {10, 20, 30, 40};
		System.out.println(cars.length); // length
		int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };

		myMethod(); // Method

		// Class
		myStaticMethod(); // Call the static method

		Main myObj = new Main(); // Create an object of Main
		myObj.myPublicMethod(); // Call the public method on the object
	    
	    System.out.println(myObj.x); // Print the value of x

	    Scanner myRead = new Scanner(System.in);
	    System.out.println("Enter username");

    	String userName = myRead.nextLine();
    	System.out.println("Username is: " + userName);


    	// ArrayList
    	import java.util.ArrayList; // import the ArrayList class
    	ArrayList<String> cars = new ArrayList<String>(); // Create an ArrayList object
    	cars.add("Volvo");
    	cars.get(0);
    	cars.set(0, "Opel");
    	cars.remove(0);
    	cars.clear();
    	cars.size();

    	import java.util.Collections;  // Import the Collections class
    	Collections.sort(cars);  // Sort cars

    	// LinkedList
    	import java.util.LinkedList; // Import the LinkedList class
    	LinkedList<String> cars = new LinkedList<String>();
    	cars.addFirst("Volvo");
    	cars.addLast("Opel");
    	cars.removeFirst();
    	cars.removeLast();
    	cars.getFirst();
    	cars.getLast();

    	// HashMap
    	import java.util.HashMap; // import the HashMap class
    	HashMap<String, String> capitalCities = new HashMap<String, String>();
    	capitalCities.put("England", "London");
    	capitalCities.get("England");
    	capitalCities.remove("England");
    	capitalCities.clear();
    	capitalCities.size();

    	// Print keys
    	for (String i : capitalCities.keySet()) {
    		System.out.println(i);
    	}

    	// Print values
		for (String i : capitalCities.values()) {
  			System.out.println(i);
		}

		// HashSet
		import java.util.HashSet; // Import the HashSet class
		HashSet<String> cars = new HashSet<String>();
		cars.add("Volvo");
		cars.contains("Mazda");
		cars.remove("Volvo");
		cars.clear();
		cars.size();

		// Iterator
		import java.util.Iterator;
		// Get the iterator
    	Iterator<String> it = cars.iterator();
    	// Print the first item
    	System.out.println(it.next());

    	while(it.hasNext()) {
  			System.out.println(it.next());
		}


		// Try Catch
		try {
			//  Block of code to try
		}
		catch(Exception e) {
			//  Block of code to handle errors
		}


	}
}


// Inheritance
class Vehicle {
  protected String brand = "Ford";        // Vehicle attribute
  public void honk() {                    // Vehicle method
    System.out.println("Tuut, tuut!");
  }
}

class Car extends Vehicle {
  private String modelName = "Mustang";    // Car attribute
  public static void main(String[] args) {

    // Create a myCar object
    Car myCar = new Car();

    // Call the honk() method (from the Vehicle class) on the myCar object
    myCar.honk();

    // Display the value of the brand attribute (from the Vehicle class) and the value of the modelName from the Car class
    System.out.println(myCar.brand + " " + myCar.modelName);
  }
}


// Inner Class
class OuterClass {
  int x = 10;

  class InnerClass {
    int y = 5;
  }
}

public class Main {
  public static void main(String[] args) {
    OuterClass myOuter = new OuterClass();
    OuterClass.InnerClass myInner = myOuter.new InnerClass();
    System.out.println(myInner.y + myOuter.x);
  }
}
// Outputs 15 (5 + 10)


// Interface
interface Animal {
  public void animalSound(); // interface method (does not have a body)
  public void sleep(); // interface method (does not have a body)
}

// Pig "implements" the Animal interface
class Pig implements Animal {
  public void animalSound() {
    // The body of animalSound() is provided here
    System.out.println("The pig says: wee wee");
  }
  public void sleep() {
    // The body of sleep() is provided here
    System.out.println("Zzz");
  }
}

class Main {
  public static void main(String[] args) {
    Pig myPig = new Pig();  // Create a Pig object
    myPig.animalSound();
    myPig.sleep();
  }
}


// Enums
enum Level {
  LOW,
  MEDIUM,
  HIGH
}

for (Level myVar : Level.values()) {
  System.out.println(myVar);
}


// Thread
public class Main extends Thread {
  	public static void main(String[] args) {
	    Main thread = new Main();
    	thread.start();
    	System.out.println("This code is outside of the thread");
  	}
  	public void run() {
    	System.out.println("This code is running in a thread");
  	}
}

public class Main implements Runnable {
  	public static void main(String[] args) {
	    Main obj = new Main();
	    Thread thread = new Thread(obj);
	    thread.start();
	    System.out.println("This code is outside of the thread");
  	}
  	public void run() {
	    System.out.println("This code is running in a thread");
  	}
}