#include<bits/stdc++.h>

using namespace std;
//Implement the class Box  
//l,b,h are integers representing the dimensions of the box

// The class should have the following functions : 

// Constructors: 
// Box();
// Box(int,int,int);
// Box(Box);


// int getLength(); // Return box's length
// int getBreadth (); // Return box's breadth
// int getHeight ();  //Return box's height
// long long CalculateVolume(); // Return the volume of the box

//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)

class Box {
    private:
        int l, b, h;
    
    public:
        Box(int l, int b, int h) {
            this->l = l;
            this->h = h;
            this->b = b;
        }
        
        Box() {
            l = h = b = 0;;
        }
        
        Box(const Box &B) {
            l = B.l;
            b = B.b;
            h = B.h;
        }
        
        int getLength() {
            return l;
        }
        
        int getBreadth() {
            return b;
        }
        
        int getHeight() {
            return h;
        }
        
        long long CalculateVolume() {
            return ((long long) l*b*h);
        }
        
        friend bool operator<(Box& A, Box& B) {
            return  ((A.l < B.l) || (A.l == B.l && A.b < B.b) || (A.l == B.l && A.b == B.b && A.h < B.h));
        }
        
        friend ostream& operator<<(ostream& out, Box& b) {
            return out << b.l << " " << b.b << " " << b.h;
        }
};

