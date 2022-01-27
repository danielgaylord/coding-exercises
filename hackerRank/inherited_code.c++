#include <iostream>
#include <string>
#include <sstream>
#include <exception>
using namespace std;

/* Define the exception here */
struct BadLengthException : public exception {
    private:
        string error;

    public: 
        BadLengthException(int n) {
            stringstream tmp;
            tmp << n;
            error = tmp.str();
        }
        
        const char* what() const throw() {
            return error.c_str();
        }
};

