// C++

typedef type newname;
typedef int feet;
// create a new name for existing type

enum enum-name {list of names} var-list;
enum color {red, green, blue} c;
c = blue;
// enumerated type. Variable c of type color and value "blue"
// red has value 0, green has value 1, blue has value 2
enum color { red, green = 5, blue };
// red has value 0, green has value 5, blue has value 6

extern int d = 3, f = 5;    // declaration of d and f. 
int d = 3, f = 5;           // definition and initializing d and f. 
// The declaration happens at the time of compilation

#define identifier value
#define LENGTH 10 
// #define preprocessor constant

const type variable = value;
const int  LENGTH = 10;
// declare constant


/* Modifier Types */
const
// Objects of type const cannot be changed by your program during execution.
volatile
// The modifier volatile tells the compiler that a variable's value may be changed in ways not explicitly specified by the program.
restrict
// A pointer qualified by restrict is initially the only means by which the object it points to can be accessed. Only C99 adds a new type qualifier called restrict.


/* Storage specifiers */
int mount;
auto int month;
// auto: default storage class for all local variables

register int  miles;
// register: local variables stored in a register instead of RAM. Limited size, can't have &, for quick access.

static int count = 10;
// static: local static variables mantain their value during the life-time of the program.
// global static variables have their scope restrict to the file in which they are declared.
// class data members have only one copy of that member shared by all objects.

extern int count;
extern void write_extern();
// extern: is used to give a reference of a global variable or function in another file.

mutable
// mutable: applies only to class objects. A mutable member can be modified by a const member function.


/* Casting Operators */
const_cast<type> (expr)
// The const_cast operator is used to explicitly override const and/or volatile in a cast. The target type must be the same as the source type except for the alteration of its const or volatile attributes. This type of casting manipulates the const attribute of the passed object, either to be set or removed.

dynamic_cast<type> (expr)
// The dynamic_cast performs a runtime cast that verifies the validity of the cast. If the cast cannot be made, the cast fails and the expression evaluates to null. A dynamic_cast performs casts on polymorphic types and can cast a A* pointer into a B* pointer only if the object being pointed to actually is a B object.

reinterpret_cast<type> (expr)
// The reinterpret_cast operator changes a pointer to any other type of pointer. It also allows casting from pointer to an integer type and vice versa.

static_cast<type> (expr)
// The static_cast operator performs a nonpolymorphic cast. For example, it can be used to cast a base class pointer into a derived class pointer.


/* Function Definition */
return_type function_name( parameter list ) {
   body of the function
}

// Function Declaration
return_type function_name( parameter list );
int max(int num1, int num2);
int max(int, int);


/* Arrays */
type arrayName [ arraySize ];
double balance[10];
double balance[5] = {1000.0, 2.0, 3.4, 17.0, 50.0};


/* Reference */
int i = 17;
int& r = i;


/* Structure */
struct [structure tag] {
   member definition;
   member definition;
   ...
   member definition;
} [one or more structure variables];  

struct Books {
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
} book;  

struct Books Book1;        // Declare Book1 of type Book

// book 1 specification
strcpy( Book1.title, "Learn C++ Programming");
strcpy( Book1.author, "Chand Miyan"); 
strcpy( Book1.subject, "C++ Programming");
Book1.book_id = 6495407;

typedef struct {
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
} Books;

Books Book1, Book2;


/* Class Definition */
class Box {
   public:
      double length;   // Length of a box
      double breadth;  // Breadth of a box
      double height;   // Height of a box
};

// Object Definition
Box Box1;          // Declare Box1 of type Box
Box Box2;          // Declare Box2 of type Box

// box 1 specification
Box1.height = 5.0; 
Box1.length = 6.0; 
Box1.breadth = 7.0;

/* Class Member Functions */
class Line {
	double length;			  // Member variables are private by default

   public:
      double getLength(void); // Returns box length
      void setLength( double len );
      Line();				  // This is the constructor declaration
      ~Line();  			  // This is the destructor: declaration
};

// Member functions definitions including constructor
Line::Line(void) {
   cout << "Object is being created" << endl;
}
Line::~Line(void) {
   cout << "Object is being deleted" << endl;
}
double Line::getLength(void) {
   return length;
}

void Line::setLength( double len ) {
   length = len;
}

Line line;
line.setLength(6.0); 

// Initialization Lists in Constructor
Line::Line( double len): length(len) {				// length = len;
   cout << "Object is being created, length = " << len << endl;
}

C::C( double a, double b, double c): X(a), Y(b), Z(c) {			// Multiple variables
   ....
}

/* Copy constructor */
classname (const classname &obj) {
   // body of constructor
}

class Line {

   public:
      int getLength( void );
      Line( int len );             // simple constructor
      Line( const Line &obj);  // copy constructor
      ~Line();                     // destructor

   private:
      int *ptr;
};

// Member functions definitions including constructor
Line::Line(int len) {
   cout << "Normal constructor allocating ptr" << endl;
   
   // allocate memory for the pointer;
   ptr = new int;
   *ptr = len;
}

Line::Line(const Line &obj) {
   cout << "Copy constructor allocating ptr." << endl;
   ptr = new int;
   *ptr = *obj.ptr; // copy the value
}

Line::~Line(void) {
   cout << "Freeing memory!" << endl;
   delete ptr;
}

int Line::getLength( void ) {
   return *ptr;
}

/* Friend Functions */
class Box {
   double width;
   
   public:
      friend void printWidth( Box box );
      void setWidth( double wid );
};

friend class ClassTwo;

// Member function definition
void Box::setWidth( double wid ) {
   width = wid;
}

// Note: printWidth() is not a member function of any class.
void printWidth( Box box ) {
   /* Because printWidth() is a friend of Box, it can
   directly access any member of this class */
   cout << "Width of box : " << box.width <<endl;
}

/* Inline Functions */
inline int Max(int x, int y) {
   return (x > y)? x : y;
}

/* This Pointer */
class Box {
   public:
      // Constructor definition
      Box(double l = 2.0, double b = 2.0, double h = 2.0) {
         cout <<"Constructor called." << endl;
         length = l;
         breadth = b;
         height = h;
      }
      double Volume() {
         return length * breadth * height;
      }
      int compare(Box box) {
         return this->Volume() > box.Volume();
      }
      
   private:
      double length;     // Length of a box
      double breadth;    // Breadth of a box
      double height;     // Height of a box
};


/* Inheritance */
/* Base and Derived Classes */
class derived-class: access-specifier base-class

// Base class
class Shape {
   public:
      void setWidth(int w) {
         width = w;
      }
      void setHeight(int h) {
         height = h;
      }
      
   protected:
      int width;
      int height;
};

// Derived class
class Rectangle: public Shape {
   public:
      int getArea() { 
         return (width * height); 
      }
};

/* Multiple inheritance */
class derived-class: access baseA, access baseB...

// Base class Shape
class Shape {
   public:
      void setWidth(int w) {
         width = w;
      }
      void setHeight(int h) {
         height = h;
      }
      
   protected:
      int width;
      int height;
};

// Base class PaintCost
class PaintCost {
   public:
      int getCost(int area) {
         return area * 70;
      }
};

// Derived class
class Rectangle: public Shape, public PaintCost {
   public:
      int getArea() {
         return (width * height); 
      }
};


/* Overload */
class printData {
   public:
      void print(int i) {
        cout << "Printing int: " << i << endl;
      }
      void print(double  f) {
        cout << "Printing float: " << f << endl;
      }
      void print(char* c) {
        cout << "Printing character: " << c << endl;
      }
};

// Operator Overload
Box operator+(const Box&);

// Overload + operator to add two Box objects.
Box operator+(const Box& b) {
    Box box;
    box.length = this->length + b.length;
    box.breadth = this->breadth + b.breadth;
    box.height = this->height + b.height;
    return box;
}


/* Polymorphism */
class Shape {
   protected:
      int width, height;
      
   public:
      Shape( int a = 0, int b = 0) {
         width = a;
         height = b;
      }
      virtual int area() {
         cout << "Parent class area :" <<endl;
         return 0;
      }
};

class Rectangle: public Shape {
   public:
      Rectangle( int a = 0, int b = 0):Shape(a, b) { }
      
      int area () { 
         cout << "Rectangle class area :" <<endl;
         return (width * height); 
      }
};

class Triangle: public Shape {
   public:
      Triangle( int a = 0, int b = 0):Shape(a, b) { }
      
      int area () { 
         cout << "Triangle class area :" <<endl;
         return (width * height / 2); 
      }
};

// main()
Shape *shape;
Rectangle rec(10,7);
Triangle  tri(10,5);

// store the address of Rectangle
shape = &rec;
   
// call rectangle area.
shape->area();

// store the address of Triangle
shape = &tri;
   
// call triangle area.
shape->area();


/* Interfaces */

class Box {
   public:
      // pure virtual function
      virtual double getVolume() = 0;
      
   private:
      double length;      // Length of a box
      double breadth;     // Breadth of a box
      double height;      // Height of a box
};


/* Files and Streams */
void open(const char *filename, ios::openmode mode);

// write mode and truncate
ofstream outfile;
outfile.open("file.dat", ios::out | ios::trunc );

// read and write mode
fstream  afile;
afile.open("file.dat", ios::out | ios::in );


/* Exception Handling */
try {
   // protected code
} catch( ExceptionName e ) {
  // code to handle ExceptionName exception
}

try {
   // protected code
} catch(...) {
  // code to handle any exception
}


/* Dynamic Memory */
new data-type;

double* pvalue  = NULL; // Pointer initialized with null
pvalue  = new double;   // Request memory for the variable

delete pvalue;        // Release memory pointed to by pvalue

// Array
char* pvalue  = NULL;         // Pointer initialized with null
pvalue  = new char[20];       // Request memory for the variable

delete [] pvalue;             // Delete array pointed to by pvalue

double** pvalue  = NULL;      // Pointer initialized with null 
pvalue  = new double [3][4];  // Allocate memory for a 3x4 array 

delete [] pvalue;            // Delete array pointed to by pvalue


/* Namespace */
namespace namespace_name {
   // code declarations
}

name::code;  // code could be variable or function.

// first name space
namespace first_space {
   void func() {
      cout << "Inside first_space" << endl;
   }
}

// second name space
namespace second_space {
   void func() {
      cout << "Inside second_space" << endl;
   }
}

// Calls function from first name space.
first_space::func();
   
// Calls function from second name space.
second_space::func(); 

// OR
using namespace first_space;
int main () {
   // This calls function from first name space.
   func();
   
   return 0;
}


/* Template */
// Function Template
template <class type> ret-type func-name(parameter list) {
   // body of function
} 

template <typename T>
inline T const& Max (T const& a, T const& b) { 
   return a < b ? b:a; 
}

// Class Template
template <class type> class class-name {
   .
   .
   .
}

template <class T>
class Stack { 
   private: 
      vector<T> elems;    // elements 

   public: 
      void push(T const&);  // push element 
      void pop();               // pop element 
      T top() const;            // return top element 
      
      bool empty() const {      // return true if empty.
         return elems.empty(); 
      } 
}; 


/* Preprocessor */
#define macro-name replacement-text 
#define PI 3.14159
#define MIN(a,b) (((a)<(b)) ? a : b)

#ifndef NULL
   #define NULL 0
#endif

#ifdef DEBUG
   cerr <<"Variable x = " << x << endl;
#endif

#if 0
   code prevented from compiling
#endif

#define MKSTR( x ) #x
MKSTR(HELLO C++)
// = "HELLO C++"

#define concat(a, b) a ## b
concat(x, y)
// = xy


/* Macros */
__LINE__: current line number
__FILE__: current file name
__DATE__: month/day/year
__TIME__: hour:minute:second








https://www.tutorialspoint.com/cplusplus/cpp_web_programming.htm