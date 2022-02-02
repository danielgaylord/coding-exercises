#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    vector<int> nums;
    int size, single_del, first_range_del, last_range_del;
    cin >> size;
    for (int x = 0; x < size; x++) {
        int num;
        cin >> num;
        nums.push_back(num);
    }
    
    cin >> single_del;
    cin >> first_range_del >> last_range_del;
    
    nums.erase(nums.begin() + (single_del - 1));
    nums.erase(nums.begin() + (first_range_del - 1), nums.begin() + (last_range_del - 1));
    
    cout << nums.size() << endl;
    for (int x = 0; x < nums.size(); x++) {
        cout << nums[x] << " ";
    }
    return 0;
}
