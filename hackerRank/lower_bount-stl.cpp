#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vector<int> nums;
    int size, queries, val;
    vector<int>::iterator low;
    
    cin >> size;
    for (int x = 0; x < size; x++) {
        cin >> val;
        nums.push_back(val);
    }
    cin >> queries;
    for (int x = 0; x < queries; x++) {
        cin >> val;
        low = lower_bound(nums.begin(), nums.end(), val);
        if (*low == val) {
           cout << "Yes ";
        } else {
            cout << "No ";
        }
        cout << low - nums.begin() + 1 << endl;
    }
    return 0;
}