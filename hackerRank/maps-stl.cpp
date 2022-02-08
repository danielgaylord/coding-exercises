#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int queries, command, marks;
    string student;
    map<string, int> homework;
    
    cin >> queries;
    
    for (int x = 0; x < queries; x++) {
        cin >> command >> student;
        
        if (command == 1) {
            cin >> marks;
            if (homework.find(student) == homework.end()) {
                homework.insert(make_pair(student, marks));
            } else {
                homework[student] += marks;
            }
        } else if (command == 2) {
            if (homework.find(student) != homework.end()) {
                homework.erase(student);
            }
        } else if (command == 3) {
            if (homework.find(student) != homework.end()) {
                cout << homework[student] << endl;
            } else {
                cout << 0 << endl;
            }
        } else {
            cout << "Command not recognized" << endl;
        }
    }
     
    return 0;
}