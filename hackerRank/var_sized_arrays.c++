#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int length, queries, size, element, at, ind;
    cin >> length >> queries;
    
    vector<int> arr[length];
    
    for (int x = 0; x < length; x++) {
        cin >> size;
        
        for (int y = 0; y < size; y++) {
            cin >> element;
            arr[x].push_back(element);
        }
    }

    for (int x = 0; x < queries; x++) {
        cin >> at >> ind;
        cout << arr[at][ind] << "\n";
    }
       
    return 0;
}