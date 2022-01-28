#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int length;
    cin >> length;
    int arr[length];
    for (int x = length - 1; x >= 0; x--) {
        cin >> arr[x];
    }
    
    for (int x = 0; x < length; x++) {
        cout << arr[x] << " ";
    }
    return 0;
}
