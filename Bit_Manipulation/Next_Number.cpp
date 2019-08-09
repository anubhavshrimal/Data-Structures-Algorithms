/*
Find the next greater and next smaller number with same number of set bits
 */
#include<iostream>

using namespace std;

// Ex. num = 6 bin = 110
int next_greater(int num) {
    
    int res = num;
    
    // at least one set bit
    if (num != 0) {
        // Find the right most 1 pos
        // Ex. right_one = 2 bin = 10
        int right_one = num & -num;

        int left_pattern = num + right_one;

        int right_pattern = (num ^ left_pattern) >> (right_one + 1);

        res = left_pattern | right_pattern;
    }

    return res;
}

int previous_smaller(int num) {
    return ~next_greater(~num);
}
int main() {

    cout << next_greater(6) << endl;
    cout << previous_smaller(6) << endl;

    return 0;
}