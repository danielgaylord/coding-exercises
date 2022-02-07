#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int queries, command, val;
    set<int> nums;
    cin >> queries;
    
    for (int x = 0; x < queries; x++) {
        cin >> command >> val;
        if (command == 1) {
            nums.insert(val);
        } else if (command == 2) {
            if (nums.end() != nums.find(val)) {
                nums.erase(val);
            }
        } else if (command == 3) {
            if (nums.end() != nums.find(val)) {
                cout << "Yes" << endl;
            } else {
                cout << "No" << endl;
            }
        } else {
            cout << "Command not recognized" << endl;
        }
    }
    return 0;
}



