#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person {
    public:
        string name;
        int age;
        
    public:   
        virtual void getdata() {
            cin >> name >> age;
        }
        
        virtual void putdata() {
            cout << name << " " << age << "\n";
        }
};

class Professor: public Person {
    private:
        int publications;
        int cur_id;
        static int total_id;
    
    public:
        Professor() {
            cur_id = ++total_id;
        };
    
        void getdata() {
            cin >> name >> age >> publications;
        }
            
        void putdata() {
            cout << name << " " << age << " " << publications << " " << cur_id << "\n";
        }  
};

class Student: public Person {
    private:
        int marks[6];
        int cur_id;
        static int total_id;

    public:
        Student() {
            cur_id = ++total_id;
        };
        
        void getdata() {
            int size = sizeof(marks)/sizeof(marks[0]);
        
            cin >> name >> age;
            for (int x = 0; x < size; x++) {
                cin >> marks[x];
            }
        }
            
        void putdata() {
            int sum = 0;
            int size = sizeof(marks)/sizeof(marks[0]);
            
            for (int x = 0; x < size; x++) {
                sum += marks[x];
            }
            cout << name << " " << age << " " << sum << " " << cur_id << "\n";
        }  
};

int Professor::total_id = 0;
int Student::total_id = 0;

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
