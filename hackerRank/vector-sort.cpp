#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    vector<int> nums;
    int times, val;
    cin >> times;

    for (int x = 0; x < times; x++) {
        cin >> val;
        nums.push_back(val);
    }  
    
    sort(nums.begin(), nums.end());
    
    for (int x = 0; x < nums.size(); x ++) {
        cout << nums[x] << " ";
    }
    return 0;
}