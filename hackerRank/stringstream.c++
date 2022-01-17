#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    vector<int> integers;
    stringstream strings(str);
    int temp;
    char ch;
    
    if (strings.str().empty()) {
        return integers;
    }
    while (strings >> temp) {
        integers.push_back(temp);
        strings >> ch;
    }
    
    return integers;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}